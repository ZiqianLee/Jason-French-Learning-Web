const TABLE_HEADERS = new Set([
  "\u6cd5\u8bed\u539f\u6587",
  "\u4e2d\u6587\u91ca\u4e49",
  "\u4f7f\u7528\u573a\u666f",
  "\u573a\u666f",
  "\u9633\u6027\u5f62\u5f0f",
  "\u9634\u6027\u5f62\u5f0f",
  "\u590d\u6570\u5f62\u5f0f",
  "\u56fd\u5bb6\u540d\u79f0",
  "\u7ffb\u8bd1"
]);

const LABEL_LINES = new Set([
  "\u7ffb\u8bd1\uff1a",
  "\u8bed\u6cd5\u8be6\u89e3\uff1a",
  "\u4ec0\u4e48\u65f6\u5019\u7528\uff1f",
  "\u548c\u4e00\u822c\u73b0\u5728\u65f6\u7684\u533a\u522b\uff1f",
  "\u9b41\u5317\u514b\u7684\u53e3\u8bed\u7528\u6cd5",
  "\u975e\u6b63\u5f0f\u573a\u5408\uff1a",
  "\u6b63\u5f0f\u573a\u5408\uff1a"
]);

const selectors = {
  hero: document.querySelector("#hero"),
  overviewGrid: document.querySelector("#overviewGrid"),
  lessonList: document.querySelector("#lessonList"),
  sidebarLinks: document.querySelector("#sidebarLinks"),
  sidebarNote: document.querySelector("#sidebarNote"),
  searchInput: document.querySelector("#searchInput"),
  menuButton: document.querySelector("#menuButton"),
  sidebar: document.querySelector("#sidebar"),
  overlay: document.querySelector("#overlay")
};

let searchIndex = new Map();

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

async function loadData() {
  const response = await fetch("./course-data.json.gz.b64");
  if (!response.ok) throw new Error("Could not load course data");
  const base64 = (await response.text()).trim();
  const binary = atob(base64);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i += 1) bytes[i] = binary.charCodeAt(i);

  if (!("DecompressionStream" in window)) {
    throw new Error("This browser does not support gzip decompression.");
  }

  const decompressed = new Blob([bytes]).stream().pipeThrough(new DecompressionStream("gzip"));
  const jsonText = await new Response(decompressed).text();
  return JSON.parse(jsonText);
}

function endsWithFullWidthColon(line) {
  return line.length > 0 && line.charCodeAt(line.length - 1) === 0xff1a;
}

function looksLikeLabel(line) {
  return endsWithFullWidthColon(line) || LABEL_LINES.has(line);
}

function getHeaderCount(lines, startIndex) {
  let count = 0;
  for (let index = startIndex; index < lines.length; index += 1) {
    if (!TABLE_HEADERS.has(lines[index])) break;
    count += 1;
  }
  return count;
}

function segmentBlockLines(lines) {
  const segments = [];
  let index = 0;

  while (index < lines.length) {
    const line = lines[index];

    if (looksLikeLabel(line)) {
      segments.push({ type: "label", text: line });
      index += 1;
      continue;
    }

    const headerCount = getHeaderCount(lines, index);
    if (headerCount >= 2) {
      const headers = lines.slice(index, index + headerCount);
      index += headerCount;
      const rows = [];

      while (index + headerCount - 1 < lines.length) {
        if (getHeaderCount(lines, index) >= 2) break;
        if (looksLikeLabel(lines[index]) && getHeaderCount(lines, index + 1) >= 2) break;
        rows.push(lines.slice(index, index + headerCount));
        index += headerCount;
      }

      if (rows.length > 0) {
        segments.push({ type: "table", headers, rows });
      } else {
        segments.push({ type: "lines", lines: headers });
      }
      continue;
    }

    const paragraphLines = [];
    while (index < lines.length && !looksLikeLabel(lines[index]) && getHeaderCount(lines, index) < 2) {
      paragraphLines.push(lines[index]);
      index += 1;
    }

    if (paragraphLines.length > 0) {
      segments.push({ type: "lines", lines: paragraphLines });
    }
  }

  return segments;
}

function renderSegment(segment) {
  if (segment.type === "label") {
    return `<p class="content-label">${escapeHtml(segment.text)}</p>`;
  }

  if (segment.type === "table") {
    return `
      <div class="table-wrap">
        <table>
          <thead>
            <tr>${segment.headers.map((header) => `<th>${escapeHtml(header)}</th>`).join("")}</tr>
          </thead>
          <tbody>
            ${segment.rows
              .map((row) => `<tr>${row.map((cell) => `<td>${escapeHtml(cell)}</td>`).join("")}</tr>`)
              .join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  return segment.lines
    .map((line) => {
      const cls = line.includes("\uff1a") && !looksLikeLabel(line) ? "content-subline" : "content-line";
      return `<p class="${cls}">${escapeHtml(line)}</p>`;
    })
    .join("");
}

function renderBlock(block) {
  const contentSegments = segmentBlockLines(block.lines);
  return `
    <section class="block">
      ${block.title ? `<h5 class="block__title">${escapeHtml(block.title)}</h5>` : ""}
      <div class="content-stack">
        ${contentSegments.map(renderSegment).join("")}
      </div>
    </section>
  `;
}

function createPracticeCard(episode) {
  return `
    <section class="practice-card" aria-label="Guided practice">
      <h4>Guided Practice</h4>
      <div class="practice-card__grid">
        <div>
          <p class="content-label">Review Goal</p>
          <p class="content-line">Retell the main ideas from Episode ${episode.number} in your own words, then read one dialogue aloud twice.</p>
          <p class="content-label">Output Prompt</p>
          <p class="content-line">Use this episode's vocabulary and grammar to make 5 to 8 new sentences about your own life.</p>
        </div>
        <div>
          <p class="content-label">Checklist</p>
          <ul class="check-list">
            <li>Review the core vocabulary.</li>
            <li>Notice the main grammar pattern.</li>
            <li>Read the example lines aloud.</li>
            <li>Write your own short mini dialogue.</li>
          </ul>
        </div>
        <div>
          <p class="content-label">Mini Dialogue Prompt</p>
          <div class="dialogue">
            <p class="dialogue__line">A: Let's review Episode ${episode.number} together.</p>
            <p class="dialogue__line">B: Good idea. I will use the new expressions from ${escapeHtml(episode.title)}.</p>
          </div>
        </div>
      </div>
    </section>
  `;
}

function renderEpisodeCard(episode) {
  const sectionMarkup = episode.sections
    .map(
      (section) => `
        <article class="section-card">
          <h4>${escapeHtml(section.title)}</h4>
          ${section.blocks.map((block) => renderBlock(block)).join("")}
        </article>
      `
    )
    .join("");

  const summaryTags = episode.sections
    .map((section) => `<span class="chip">${escapeHtml(section.title)}</span>`)
    .join("");

  return `
    <article class="episode-card" id="${episode.slug}">
      <div class="episode-header">
        <div>
          <p class="episode-index">Episode ${episode.number}</p>
          <h3>${escapeHtml(episode.title)}</h3>
          <p>${escapeHtml(episode.description || "Episode content organized into vocabulary, grammar, examples, and dialogues.")}</p>
        </div>
        <div class="lesson-meta">${summaryTags}</div>
      </div>

      <div class="section-grid">
        ${sectionMarkup}
      </div>

      ${createPracticeCard(episode)}
    </article>
  `;
}

function renderHero(meta) {
  const missingNote =
    meta.missingEpisodeNumbers.length > 0
      ? `<p class="hero__note">The source document skips Episode ${meta.missingEpisodeNumbers.join(", ")}. The site keeps the original numbering and covers every episode present in the material.</p>`
      : "";

  selectors.hero.innerHTML = `
    <div>
      <p class="eyebrow">Structured From Your Course Material</p>
      <h1 class="hero__title">Par ici A1 Quebec French Learning Site</h1>
      <p class="hero__lede">${escapeHtml(meta.introduction)}</p>
      <div class="hero__chips">
        <span class="chip">${meta.episodeCount} episodes</span>
        <span class="chip">Vocabulary + Grammar + Dialogues</span>
        <span class="chip chip--accent">Mobile and orientation friendly</span>
      </div>
      ${missingNote}
    </div>
    <div class="hero__panel">
      <h3>How To Study</h3>
      <ul>
        <li>Start with the episode summary, then review vocabulary and grammar.</li>
        <li>Read French first, then check the Chinese explanation.</li>
        <li>Use the guided practice card to turn passive review into output.</li>
      </ul>
    </div>
  `;
}

function renderOverview(meta, episodes) {
  const firstUnit = episodes[0]?.fullTitle ?? "";
  const lastUnit = episodes[episodes.length - 1]?.fullTitle ?? "";

  selectors.overviewGrid.innerHTML = `
    <article class="overview-card">
      <p class="eyebrow">Coverage</p>
      <h3>Scope</h3>
      <p>Identity, dates, time, daily activities, descriptions, restaurants, health, directions, past actions, housing, weather, clothes, food, and the near future are all covered in episode order.</p>
    </article>
    <article class="overview-card">
      <p class="eyebrow">Range</p>
      <h3>Episode Span</h3>
      <p>First episode: ${escapeHtml(firstUnit)}</p>
      <p>Last episode: ${escapeHtml(lastUnit)}</p>
    </article>
    <article class="overview-card">
      <p class="eyebrow">Reading</p>
      <h3>Responsive Design</h3>
      <p>Long tables scroll safely on smaller screens, lines wrap cleanly, and the navigation drawer stays stable during resizing and orientation changes.</p>
    </article>
  `;
}

function renderSidebar(episodes, meta) {
  selectors.sidebarLinks.innerHTML = episodes
    .map(
      (episode) => `
        <a class="sidebar__link" href="#${episode.slug}" data-target="${episode.slug}">
          <strong>Episode ${episode.number}</strong><br />
          <span>${escapeHtml(episode.title)}</span>
        </a>
      `
    )
    .join("");

  selectors.sidebarNote.textContent =
    meta.missingEpisodeNumbers.length > 0
      ? `Note: the source file does not include Episode ${meta.missingEpisodeNumbers.join(", ")}.`
      : "Note: this site covers every episode present in the source file.";
}

function buildSearchText(episode) {
  const lines = episode.sections.flatMap((section) => [
    section.title,
    ...section.blocks.flatMap((block) => [block.title, ...block.lines])
  ]);

  return [episode.fullTitle, episode.description, ...lines].join(" ").toLowerCase();
}

function bindUi(episodes) {
  selectors.searchInput.addEventListener("input", (event) => {
    const query = event.target.value.trim().toLowerCase();
    const cards = document.querySelectorAll(".episode-card");
    const links = document.querySelectorAll(".sidebar__link[data-target]");

    cards.forEach((card) => {
      const haystack = searchIndex.get(card.id) || "";
      const matches = !query || haystack.includes(query);
      card.classList.toggle("is-hidden", !matches);
    });

    links.forEach((link) => {
      const haystack = searchIndex.get(link.dataset.target) || "";
      const matches = !query || haystack.includes(query);
      link.classList.toggle("is-hidden", !matches);
    });
  });

  selectors.menuButton.addEventListener("click", () => {
    const isOpen = selectors.sidebar.classList.toggle("is-open");
    selectors.menuButton.setAttribute("aria-expanded", String(isOpen));
    selectors.overlay.hidden = !isOpen;
  });

  selectors.overlay.addEventListener("click", closeSidebar);

  document.querySelectorAll(".sidebar__link").forEach((link) => {
    link.addEventListener("click", () => {
      if (window.innerWidth <= 980) closeSidebar();
    });
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 980) closeSidebar();
  });
}

function closeSidebar() {
  selectors.sidebar.classList.remove("is-open");
  selectors.menuButton.setAttribute("aria-expanded", "false");
  selectors.overlay.hidden = true;
}

function activateScrollSpy() {
  const links = Array.from(document.querySelectorAll(".sidebar__link[data-target]"));
  const sections = links.map((link) => document.getElementById(link.dataset.target)).filter(Boolean);

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((link) => {
          link.classList.toggle("is-active", link.dataset.target === entry.target.id);
        });
      });
    },
    {
      rootMargin: "-25% 0px -60% 0px",
      threshold: [0.1, 0.4, 0.7]
    }
  );

  sections.forEach((section) => observer.observe(section));
}

async function init() {
  try {
    const data = await loadData();
    searchIndex = new Map(data.episodes.map((episode) => [episode.slug, buildSearchText(episode)]));
    renderHero(data.meta);
    renderOverview(data.meta, data.episodes);
    renderSidebar(data.episodes, data.meta);
    selectors.lessonList.innerHTML = data.episodes.map((episode) => renderEpisodeCard(episode)).join("");
    bindUi(data.episodes);
    activateScrollSpy();
  } catch (error) {
    console.error(error);
    selectors.hero.innerHTML = `
      <div class="notice-card">
        <p class="eyebrow">Load Error</p>
        <h3>The course data could not be loaded.</h3>
        <p>Please refresh the page or try again in a browser that supports modern gzip decompression.</p>
      </div>
    `;
  }
}

init();
