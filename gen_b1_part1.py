#!/usr/bin/env python3
"""Generate B1 HTML - Part 1: Template + TOC + Units 1-4"""
import os
DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(DIR, "b1.html")
A1 = os.path.join(DIR, "a1.html")

with open(A1, 'r', encoding='utf-8') as f:
    a1 = f.read()
css = a1[a1.index('<style>')+7:a1.index('</style>')]

toc = """
<li><a href="#h-b1-textbook" class="nav-link depth-1">Canadian French B1 Level</a></li>
<li><a href="#h-b1-guide" class="nav-link depth-2">A Comprehensive Guide</a></li>
<li><a href="#h-b1-toc" class="nav-link depth-2">TABLE OF CONTENTS</a></li>
<li><a href="#h-b1-part-i" class="nav-link depth-1">PART I: ADVANCED TENSES</a></li>
<li><a href="#h-b1-u1" class="nav-link depth-2">UNIT 1: PLUS-QUE-PARFAIT</a></li>
<li><a href="#h-b1-1-1" class="nav-link depth-3">1.1 Introduction</a></li>
<li><a href="#h-b1-1-2" class="nav-link depth-3">1.2 Formation</a></li>
<li><a href="#h-b1-1-3" class="nav-link depth-3">1.3 Uses &amp; Examples</a></li>
<li><a href="#h-b1-1-4" class="nav-link depth-3">1.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u2" class="nav-link depth-2">UNIT 2: CONDITIONNEL PRÉSENT</a></li>
<li><a href="#h-b1-2-1" class="nav-link depth-3">2.1 Introduction</a></li>
<li><a href="#h-b1-2-2" class="nav-link depth-3">2.2 Formation</a></li>
<li><a href="#h-b1-2-3" class="nav-link depth-3">2.3 Uses &amp; Si Clauses</a></li>
<li><a href="#h-b1-2-4" class="nav-link depth-3">2.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u3" class="nav-link depth-2">UNIT 3: SUBJONCTIF PRÉSENT</a></li>
<li><a href="#h-b1-3-1" class="nav-link depth-3">3.1 Introduction</a></li>
<li><a href="#h-b1-3-2" class="nav-link depth-3">3.2 Formation</a></li>
<li><a href="#h-b1-3-3" class="nav-link depth-3">3.3 When to Use the Subjonctif</a></li>
<li><a href="#h-b1-3-4" class="nav-link depth-3">3.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u4" class="nav-link depth-2">UNIT 4: FUTUR ANTÉRIEUR</a></li>
<li><a href="#h-b1-4-1" class="nav-link depth-3">4.1 Introduction</a></li>
<li><a href="#h-b1-4-2" class="nav-link depth-3">4.2 Formation</a></li>
<li><a href="#h-b1-4-3" class="nav-link depth-3">4.3 Uses &amp; Examples</a></li>
<li><a href="#h-b1-4-4" class="nav-link depth-3">4.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-part-ii" class="nav-link depth-1">PART II: COMPLEX EXPRESSION</a></li>
<li><a href="#h-b1-u5" class="nav-link depth-2">UNIT 5: EXPRESSING OPINIONS</a></li>
<li><a href="#h-b1-5-1" class="nav-link depth-3">5.1 Giving Opinions</a></li>
<li><a href="#h-b1-5-2" class="nav-link depth-3">5.2 Agreeing &amp; Disagreeing</a></li>
<li><a href="#h-b1-5-3" class="nav-link depth-3">5.3 Debating a Topic</a></li>
<li><a href="#h-b1-5-4" class="nav-link depth-3">5.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u6" class="nav-link depth-2">UNIT 6: CAUSE &amp; CONSEQUENCE</a></li>
<li><a href="#h-b1-6-1" class="nav-link depth-3">6.1 Expressing Cause</a></li>
<li><a href="#h-b1-6-2" class="nav-link depth-3">6.2 Expressing Consequence</a></li>
<li><a href="#h-b1-6-3" class="nav-link depth-3">6.3 Practice &amp; Examples</a></li>
<li><a href="#h-b1-6-4" class="nav-link depth-3">6.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u7" class="nav-link depth-2">UNIT 7: HYPOTHESES &amp; CONDITIONS</a></li>
<li><a href="#h-b1-7-1" class="nav-link depth-3">7.1 Si Clauses Overview</a></li>
<li><a href="#h-b1-7-2" class="nav-link depth-3">7.2 Real Conditions (Present)</a></li>
<li><a href="#h-b1-7-3" class="nav-link depth-3">7.3 Unreal Conditions (Imparfait)</a></li>
<li><a href="#h-b1-7-4" class="nav-link depth-3">7.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u8" class="nav-link depth-2">UNIT 8: REPORTED SPEECH</a></li>
<li><a href="#h-b1-8-1" class="nav-link depth-3">8.1 Direct vs. Indirect Speech</a></li>
<li><a href="#h-b1-8-2" class="nav-link depth-3">8.2 Tense Changes</a></li>
<li><a href="#h-b1-8-3" class="nav-link depth-3">8.3 Practice &amp; Examples</a></li>
<li><a href="#h-b1-8-4" class="nav-link depth-3">8.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-part-iii" class="nav-link depth-1">PART III: SOCIETY &amp; MEDIA</a></li>
<li><a href="#h-b1-u9" class="nav-link depth-2">UNIT 9: MEDIA &amp; NEWS</a></li>
<li><a href="#h-b1-9-1" class="nav-link depth-3">9.1 Media Vocabulary</a></li>
<li><a href="#h-b1-9-2" class="nav-link depth-3">9.2 Understanding News</a></li>
<li><a href="#h-b1-9-3" class="nav-link depth-3">9.3 Discussing Current Events</a></li>
<li><a href="#h-b1-9-4" class="nav-link depth-3">9.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u10" class="nav-link depth-2">UNIT 10: ENVIRONMENT</a></li>
<li><a href="#h-b1-10-1" class="nav-link depth-3">10.1 Environment Vocabulary</a></li>
<li><a href="#h-b1-10-2" class="nav-link depth-3">10.2 Talking About Climate</a></li>
<li><a href="#h-b1-10-3" class="nav-link depth-3">10.3 Green Living</a></li>
<li><a href="#h-b1-10-4" class="nav-link depth-3">10.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u11" class="nav-link depth-2">UNIT 11: WORK &amp; CAREER</a></li>
<li><a href="#h-b1-11-1" class="nav-link depth-3">11.1 Job Search Vocabulary</a></li>
<li><a href="#h-b1-11-2" class="nav-link depth-3">11.2 Writing a CV &amp; Cover Letter</a></li>
<li><a href="#h-b1-11-3" class="nav-link depth-3">11.3 Job Interviews</a></li>
<li><a href="#h-b1-11-4" class="nav-link depth-3">11.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u12" class="nav-link depth-2">UNIT 12: EDUCATION</a></li>
<li><a href="#h-b1-12-1" class="nav-link depth-3">12.1 Education System in Quebec</a></li>
<li><a href="#h-b1-12-2" class="nav-link depth-3">12.2 Academic Vocabulary</a></li>
<li><a href="#h-b1-12-3" class="nav-link depth-3">12.3 University Life</a></li>
<li><a href="#h-b1-12-4" class="nav-link depth-3">12.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-part-iv" class="nav-link depth-1">PART IV: NARRATIVE &amp; EMOTION</a></li>
<li><a href="#h-b1-u13" class="nav-link depth-2">UNIT 13: STORYTELLING</a></li>
<li><a href="#h-b1-13-1" class="nav-link depth-3">13.1 Narrative Tenses</a></li>
<li><a href="#h-b1-13-2" class="nav-link depth-3">13.2 Story Structure</a></li>
<li><a href="#h-b1-13-3" class="nav-link depth-3">13.3 Connectors for Narratives</a></li>
<li><a href="#h-b1-13-4" class="nav-link depth-3">13.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u14" class="nav-link depth-2">UNIT 14: FEELINGS &amp; EMOTIONS</a></li>
<li><a href="#h-b1-14-1" class="nav-link depth-3">14.1 Emotion Vocabulary</a></li>
<li><a href="#h-b1-14-2" class="nav-link depth-3">14.2 Expressing Feelings</a></li>
<li><a href="#h-b1-14-3" class="nav-link depth-3">14.3 Reacting to Situations</a></li>
<li><a href="#h-b1-14-4" class="nav-link depth-3">14.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u15" class="nav-link depth-2">UNIT 15: RELATIONSHIPS</a></li>
<li><a href="#h-b1-15-1" class="nav-link depth-3">15.1 Relationship Vocabulary</a></li>
<li><a href="#h-b1-15-2" class="nav-link depth-3">15.2 Describing Relationships</a></li>
<li><a href="#h-b1-15-3" class="nav-link depth-3">15.3 Conflict &amp; Resolution</a></li>
<li><a href="#h-b1-15-4" class="nav-link depth-3">15.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u16" class="nav-link depth-2">UNIT 16: COMPLAINTS &amp; APOLOGIES</a></li>
<li><a href="#h-b1-16-1" class="nav-link depth-3">16.1 Making Complaints</a></li>
<li><a href="#h-b1-16-2" class="nav-link depth-3">16.2 Apologizing</a></li>
<li><a href="#h-b1-16-3" class="nav-link depth-3">16.3 Finding Solutions</a></li>
<li><a href="#h-b1-16-4" class="nav-link depth-3">16.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-part-v" class="nav-link depth-1">PART V: QUEBEC CULTURE</a></li>
<li><a href="#h-b1-u17" class="nav-link depth-2">UNIT 17: QUEBEC HISTORY</a></li>
<li><a href="#h-b1-17-1" class="nav-link depth-3">17.1 Key Historical Events</a></li>
<li><a href="#h-b1-17-2" class="nav-link depth-3">17.2 Historical Vocabulary</a></li>
<li><a href="#h-b1-17-3" class="nav-link depth-3">17.3 Discussing History</a></li>
<li><a href="#h-b1-17-4" class="nav-link depth-3">17.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u18" class="nav-link depth-2">UNIT 18: ARTS &amp; MUSIC</a></li>
<li><a href="#h-b1-18-1" class="nav-link depth-3">18.1 Quebec Music Scene</a></li>
<li><a href="#h-b1-18-2" class="nav-link depth-3">18.2 Literature &amp; Cinema</a></li>
<li><a href="#h-b1-18-3" class="nav-link depth-3">18.3 Expressing Artistic Opinions</a></li>
<li><a href="#h-b1-18-4" class="nav-link depth-3">18.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u19" class="nav-link depth-2">UNIT 19: POLITICS &amp; SOCIETY</a></li>
<li><a href="#h-b1-19-1" class="nav-link depth-3">19.1 Political Vocabulary</a></li>
<li><a href="#h-b1-19-2" class="nav-link depth-3">19.2 Quebec Political System</a></li>
<li><a href="#h-b1-19-3" class="nav-link depth-3">19.3 Discussing Social Issues</a></li>
<li><a href="#h-b1-19-4" class="nav-link depth-3">19.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b1-u20" class="nav-link depth-2">UNIT 20: REVIEW &amp; B2 PREP</a></li>
<li><a href="#h-b1-20-1" class="nav-link depth-3">20.1 Grammar Summary</a></li>
<li><a href="#h-b1-20-2" class="nav-link depth-3">20.2 Vocabulary Summary</a></li>
<li><a href="#h-b1-20-3" class="nav-link depth-3">20.3 What to Expect at B2</a></li>
<li><a href="#h-b1-20-4" class="nav-link depth-3">20.4 Study Tips</a></li>
<li><a href="#h-b1-conclusion" class="nav-link depth-1">CONCLUSION</a></li>
"""

header = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canadian French B1 Level Complete Textbook</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
{css}
    </style>
</head>
<body>
    <button class="sidebar-toggle" id="sidebarToggle" title="Toggle Menu">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
    </button>
    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <div class="app-container">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h2>📚 French Journey</h2>
            </div>
            <a href="index.html" class="home-btn">
                <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Return to Home
            </a>
            <nav class="toc">
                <ul>{toc}</ul>
            </nav>
        </aside>
        <main class="content-area">
            <div class="content-wrapper">

<h1 id="h-b1-textbook">Canadian French B1 Level Complete Textbook</h1>
<h2 id="h-b1-guide">A Comprehensive Guide for English Speakers</h2>
<hr>
<h2 id="h-b1-toc">TABLE OF CONTENTS</h2>
<p><strong>PART I: ADVANCED TENSES</strong> – Plus-que-parfait, Conditionnel, Subjonctif, Futur Antérieur</p>
<p><strong>PART II: COMPLEX EXPRESSION</strong> – Opinions, Cause &amp; Consequence, Hypotheses, Reported Speech</p>
<p><strong>PART III: SOCIETY &amp; MEDIA</strong> – Media, Environment, Work, Education</p>
<p><strong>PART IV: NARRATIVE &amp; EMOTION</strong> – Storytelling, Feelings, Relationships, Complaints</p>
<p><strong>PART V: QUEBEC CULTURE</strong> – History, Arts, Politics, Review</p>
<hr>

<h1 id="h-b1-part-i">PART I: ADVANCED TENSES</h1>

<h2 id="h-b1-u1">UNIT 1: LE PLUS-QUE-PARFAIT (PLUPERFECT)</h2>

<h3 id="h-b1-1-1">1.1 Introduction</h3>
<p>The <strong>plus-que-parfait</strong> describes an action that happened <strong>before</strong> another past action. In English, it corresponds to &quot;had done&quot; something.</p>
<ul>
<li><strong>Quand je suis arrivé à la gare, le train était déjà parti.</strong> (When I arrived at the station, the train had already left.)</li>
<li><strong>Elle m&#39;a dit qu&#39;elle avait visité le Vieux-Montréal la veille.</strong> (She told me that she had visited Old Montreal the day before.)</li>
</ul>

<h3 id="h-b1-1-2">1.2 Formation</h3>
<p>The plus-que-parfait = <strong>imparfait of avoir/être + past participle</strong>.</p>
<table>
<thead><tr><th>Pronoun</th><th>With Avoir (parler)</th><th>With Être (aller)</th></tr></thead>
<tbody>
<tr><td>J&#39;</td><td>avais parlé</td><td>étais allé(e)</td></tr>
<tr><td>Tu</td><td>avais parlé</td><td>étais allé(e)</td></tr>
<tr><td>Il/Elle/On</td><td>avait parlé</td><td>était allé(e)</td></tr>
<tr><td>Nous</td><td>avions parlé</td><td>étions allé(e)s</td></tr>
<tr><td>Vous</td><td>aviez parlé</td><td>étiez allé(e)(s)</td></tr>
<tr><td>Ils/Elles</td><td>avaient parlé</td><td>étaient allé(e)s</td></tr>
</tbody></table>
<p><strong>Remember:</strong> The same verbs that take <strong>être</strong> in the passé composé also take être in the plus-que-parfait (DR MRS VANDERTRAMP verbs + reflexive verbs).</p>

<h3 id="h-b1-1-3">1.3 Uses &amp; Examples</h3>
<ul>
<li><strong>Action before another past action:</strong> Il avait déjà mangé quand sa femme est rentrée du travail. (He had already eaten when his wife came home from work.)</li>
<li><strong>Explaining a past situation:</strong> Nous étions fatigués parce que nous avions marché pendant cinq heures dans le parc de la Jacques-Cartier. (We were tired because we had walked for five hours in Jacques-Cartier Park.)</li>
<li><strong>Regrets with &quot;si seulement&quot;:</strong> Si seulement j&#39;avais étudié plus, j&#39;aurais réussi mon examen au cégep. (If only I had studied more, I would have passed my exam at CEGEP.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Missed Opportunity:</strong></p>
<p><em>Vous racontez une journée malchanceuse à votre colocataire.</em></p>
<p>&quot;Tu ne devineras jamais ce qui m&#39;est arrivé aujourd&#39;hui!&quot;<br>&quot;Quoi?&quot;<br>&quot;J&#39;avais oublié mon portefeuille à la maison. Quand je suis arrivé au restaurant pour mon entrevue, je n&#39;avais pas mes pièces d&#39;identité.&quot;<br>&quot;Oh non! Et qu&#39;est-ce que tu as fait?&quot;<br>&quot;J&#39;avais déjà appelé pour confirmer le matin, alors ils m&#39;ont quand même reçu. Mais en plus, j&#39;avais pris le mauvais autobus et je suis arrivé vingt minutes en retard!&quot;<br>&quot;Ça, c&#39;est une journée de même! Au moins, tu y es allé. C&#39;est l&#39;important.&quot;</p>
<p><em>(You are telling your roommate about an unlucky day. &quot;You&#39;ll never guess what happened to me today!&quot; &quot;What?&quot; &quot;I had forgotten my wallet at home. When I arrived at the restaurant for my interview, I didn&#39;t have my ID.&quot; &quot;Oh no! And what did you do?&quot; &quot;I had already called to confirm in the morning, so they still saw me. But on top of that, I had taken the wrong bus and I arrived twenty minutes late!&quot; &quot;That&#39;s one of those days! At least you went. That&#39;s what matters.&quot;)</em></p>

<h3 id="h-b1-1-4">1.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In spoken Quebec French, the plus-que-parfait is used naturally: <strong>&quot;J&#39;avais-tu oublié ça, moi!&quot;</strong> (Had I ever forgotten that!) – The &quot;-tu&quot; here is used as an emphasis marker, not a question.</li>
<li><strong>&quot;De même&quot;</strong> is a typical Québécois expression meaning &quot;like that&quot;: <strong>&quot;Une journée de même&quot;</strong> = a day like that.</li>
</ul>
<hr>

<h2 id="h-b1-u2">UNIT 2: LE CONDITIONNEL PRÉSENT</h2>

<h3 id="h-b1-2-1">2.1 Introduction</h3>
<p>The <strong>conditionnel présent</strong> expresses what &quot;would&quot; happen. It is used for polite requests, wishes, hypothetical situations, and giving advice.</p>

<h3 id="h-b1-2-2">2.2 Formation</h3>
<p>Conditionnel = <strong>futur simple stem + imparfait endings</strong> (-ais, -ais, -ait, -ions, -iez, -aient).</p>
<table>
<thead><tr><th>Pronoun</th><th>Parler</th><th>Avoir</th><th>Être</th><th>Pouvoir</th></tr></thead>
<tbody>
<tr><td>Je</td><td>parlerais</td><td>aurais</td><td>serais</td><td>pourrais</td></tr>
<tr><td>Tu</td><td>parlerais</td><td>aurais</td><td>serais</td><td>pourrais</td></tr>
<tr><td>Il/Elle/On</td><td>parlerait</td><td>aurait</td><td>serait</td><td>pourrait</td></tr>
<tr><td>Nous</td><td>parlerions</td><td>aurions</td><td>serions</td><td>pourrions</td></tr>
<tr><td>Vous</td><td>parleriez</td><td>auriez</td><td>seriez</td><td>pourriez</td></tr>
<tr><td>Ils/Elles</td><td>parleraient</td><td>auraient</td><td>seraient</td><td>pourraient</td></tr>
</tbody></table>

<h3 id="h-b1-2-3">2.3 Uses &amp; Si Clauses</h3>
<p><strong>1. Polite requests:</strong></p>
<ul>
<li><strong>Est-ce que vous pourriez m&#39;indiquer le chemin pour aller au Musée des beaux-arts, s&#39;il vous plaît?</strong> (Could you show me the way to the Museum of Fine Arts, please?)</li>
<li><strong>Je voudrais un café au lait et un croissant aux amandes, s&#39;il vous plaît.</strong> (I would like a café au lait and an almond croissant, please.)</li>
</ul>
<p><strong>2. Wishes and desires:</strong></p>
<ul>
<li><strong>J&#39;aimerais tellement visiter la Gaspésie cet été pour voir le rocher Percé.</strong> (I would love so much to visit the Gaspé Peninsula this summer to see Percé Rock.)</li>
</ul>
<p><strong>3. Si + imparfait → conditionnel (unreal conditions):</strong></p>
<ul>
<li><strong>Si j&#39;avais plus de temps libre, je prendrais des cours de peinture au centre communautaire.</strong> (If I had more free time, I would take painting classes at the community centre.)</li>
<li><strong>Si nous habitions à Montréal, nous irions au Festival de jazz chaque année.</strong> (If we lived in Montreal, we would go to the Jazz Festival every year.)</li>
</ul>
<p><strong>4. Giving advice:</strong></p>
<ul>
<li><strong>À ta place, je demanderais une augmentation de salaire à mon patron.</strong> (If I were you, I would ask my boss for a raise.)</li>
<li><strong>Tu devrais essayer la poutine au canard confit chez ce restaurant, elle est incroyable.</strong> (You should try the duck confit poutine at that restaurant, it&#39;s incredible.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Dreaming About Winning the Lottery:</strong></p>
<p><em>Vous discutez avec vos amis de ce que vous feriez si vous gagniez à la loterie.</em></p>
<p>&quot;Si je gagnais dix millions à la Loto-Québec, j&#39;achèterais un chalet au bord du lac Massawippi!&quot;<br>&quot;Moi, je voyagerais partout dans le monde. J&#39;irais en France, au Japon et en Australie.&quot;<br>&quot;Moi, je quitterais ma job et j&#39;ouvrirais une microbrasserie dans les Laurentides.&quot;<br>&quot;Et toi, Julie?&quot;<br>&quot;Je donnerais une partie à des organismes de charité et j&#39;investirais le reste. Je ne changerais pas trop ma vie, mais je serais plus tranquille.&quot;</p>
<p><em>(You are discussing with your friends what you would do if you won the lottery. &quot;If I won ten million from Loto-Québec, I would buy a cottage on the shores of Lake Massawippi!&quot; &quot;Me, I would travel all over the world. I would go to France, Japan, and Australia.&quot; &quot;Me, I would quit my job and I would open a microbrewery in the Laurentians.&quot; &quot;And you, Julie?&quot; &quot;I would give part to charities and invest the rest. I wouldn&#39;t change my life too much, but I would be more at peace.&quot;)</em></p>

<h3 id="h-b1-2-4">2.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>Loto-Québec</strong> is the provincial lottery corporation. <strong>&quot;Le 6/49&quot;</strong> and <strong>&quot;Lotto Max&quot;</strong> are popular lottery games.</li>
<li>In Quebec, <strong>&quot;une microbrasserie&quot;</strong> (microbrewery) is a cultural phenomenon. Quebec has over 250 microbreweries, and craft beer is very popular.</li>
<li>The expression <strong>&quot;lâcher sa job&quot;</strong> is informal Québécois for &quot;quitting one&#39;s job.&quot;</li>
</ul>
<hr>

<h2 id="h-b1-u3">UNIT 3: LE SUBJONCTIF PRÉSENT</h2>

<h3 id="h-b1-3-1">3.1 Introduction</h3>
<p>The <strong>subjonctif</strong> is a mood (not a tense) used to express subjectivity: wishes, doubts, emotions, necessity, and opinions. It appears after specific trigger expressions, always preceded by <strong>que</strong>.</p>

<h3 id="h-b1-3-2">3.2 Formation</h3>
<p>Take the <strong>ils/elles</strong> form of the present tense, remove <strong>-ent</strong>, and add subjonctif endings:</p>
<table>
<thead><tr><th>Pronoun</th><th>Ending</th><th>Parler (parl-)</th><th>Finir (finiss-)</th></tr></thead>
<tbody>
<tr><td>que je</td><td>-e</td><td>parle</td><td>finisse</td></tr>
<tr><td>que tu</td><td>-es</td><td>parles</td><td>finisses</td></tr>
<tr><td>qu&#39;il/elle</td><td>-e</td><td>parle</td><td>finisse</td></tr>
<tr><td>que nous</td><td>-ions</td><td>parlions</td><td>finissions</td></tr>
<tr><td>que vous</td><td>-iez</td><td>parliez</td><td>finissiez</td></tr>
<tr><td>qu&#39;ils/elles</td><td>-ent</td><td>parlent</td><td>finissent</td></tr>
</tbody></table>

<p><strong>Common irregular subjonctif forms:</strong></p>
<table>
<thead><tr><th>Verb</th><th>que je</th><th>que nous</th></tr></thead>
<tbody>
<tr><td>être</td><td>sois</td><td>soyons</td></tr>
<tr><td>avoir</td><td>aie</td><td>ayons</td></tr>
<tr><td>aller</td><td>aille</td><td>allions</td></tr>
<tr><td>faire</td><td>fasse</td><td>fassions</td></tr>
<tr><td>pouvoir</td><td>puisse</td><td>puissions</td></tr>
<tr><td>savoir</td><td>sache</td><td>sachions</td></tr>
<tr><td>vouloir</td><td>veuille</td><td>voulions</td></tr>
</tbody></table>

<h3 id="h-b1-3-3">3.3 When to Use the Subjonctif</h3>
<p><strong>1. After expressions of necessity:</strong></p>
<ul>
<li><strong>Il faut que tu apprennes le français si tu veux vivre au Québec.</strong> (You must learn French if you want to live in Quebec.)</li>
<li><strong>Il est nécessaire que nous fassions des efforts pour protéger l&#39;environnement.</strong> (It is necessary that we make efforts to protect the environment.)</li>
</ul>
<p><strong>2. After expressions of emotion:</strong></p>
<ul>
<li><strong>Je suis content que tu puisses venir à ma fête de graduation.</strong> (I am happy that you can come to my graduation party.)</li>
<li><strong>C&#39;est dommage qu&#39;il faille attendre si longtemps à l&#39;urgence de l&#39;hôpital.</strong> (It&#39;s a shame that one has to wait so long at the hospital emergency room.)</li>
</ul>
<p><strong>3. After expressions of doubt:</strong></p>
<ul>
<li><strong>Je doute qu&#39;il fasse beau demain. La météo annonce de la pluie verglaçante.</strong> (I doubt it will be nice tomorrow. The forecast calls for freezing rain.)</li>
</ul>
<p><strong>4. After expressions of desire/wish:</strong></p>
<ul>
<li><strong>Je veux que mes enfants aillent dans une école francophone au Québec.</strong> (I want my children to go to a French-language school in Quebec.)</li>
</ul>
<p><strong>5. After certain conjunctions:</strong> bien que (although), pour que (so that), avant que (before), à moins que (unless):</p>
<ul>
<li><strong>Bien que Montréal soit une grande ville, on peut y trouver des quartiers très calmes.</strong> (Although Montreal is a big city, you can find very quiet neighbourhoods there.)</li>
<li><strong>Je t&#39;envoie l&#39;adresse pour que tu puisses me retrouver facilement.</strong> (I&#39;m sending you the address so that you can find me easily.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Planning a Move to Quebec:</strong></p>
<p><em>Un immigrant discute avec un conseiller en immigration.</em></p>
<p>&quot;Pour que votre demande soit acceptée, il faut que vous passiez un test de français.&quot;<br>&quot;D&#39;accord. Est-ce qu&#39;il est nécessaire que j&#39;aie un niveau B2?&quot;<br>&quot;Il est préférable que vous ayez au moins un B1 oral. Le gouvernement veut que les immigrants puissent s&#39;intégrer rapidement.&quot;<br>&quot;Je comprends. J&#39;étudie le français depuis un an. J&#39;espère que mon niveau soit suffisant.&quot;<br>&quot;Je suis sûr que vous réussirez! Il est important que vous continuiez à pratiquer, surtout l&#39;écoute et la conversation.&quot;</p>
<p><em>(An immigrant is talking with an immigration advisor. &quot;For your application to be accepted, you must pass a French test.&quot; &quot;Okay. Is it necessary that I have a B2 level?&quot; &quot;It is preferable that you have at least an oral B1. The government wants immigrants to be able to integrate quickly.&quot; &quot;I understand. I&#39;ve been studying French for a year. I hope my level is sufficient.&quot; &quot;I&#39;m sure you will succeed! It is important that you continue to practice, especially listening and conversation.&quot;)</em></p>

<h3 id="h-b1-3-4">3.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In spoken Quebec French, the subjonctif is sometimes avoided in casual speech, replaced with the indicatif: <strong>&quot;Faut que je vais&quot;</strong> (informal) instead of <strong>&quot;Il faut que j&#39;aille&quot;</strong> (correct). Be aware of this but learn the correct form!</li>
<li>Quebec immigrants often take <strong>&quot;cours de francisation&quot;</strong> (French classes for immigrants), offered free by the government through the MIFI (Ministère de l&#39;Immigration, de la Francisation et de l&#39;Intégration).</li>
</ul>
<hr>

<h2 id="h-b1-u4">UNIT 4: LE FUTUR ANTÉRIEUR</h2>

<h3 id="h-b1-4-1">4.1 Introduction</h3>
<p>The <strong>futur antérieur</strong> expresses an action that &quot;will have been completed&quot; before another future action. It is the future equivalent of the plus-que-parfait.</p>

<h3 id="h-b1-4-2">4.2 Formation</h3>
<p>Futur antérieur = <strong>futur simple of avoir/être + past participle</strong>.</p>
<table>
<thead><tr><th>Pronoun</th><th>With Avoir (finir)</th><th>With Être (partir)</th></tr></thead>
<tbody>
<tr><td>J&#39;</td><td>aurai fini</td><td>serai parti(e)</td></tr>
<tr><td>Tu</td><td>auras fini</td><td>seras parti(e)</td></tr>
<tr><td>Il/Elle/On</td><td>aura fini</td><td>sera parti(e)</td></tr>
<tr><td>Nous</td><td>aurons fini</td><td>serons parti(e)s</td></tr>
<tr><td>Vous</td><td>aurez fini</td><td>serez parti(e)(s)</td></tr>
<tr><td>Ils/Elles</td><td>auront fini</td><td>seront parti(e)s</td></tr>
</tbody></table>

<h3 id="h-b1-4-3">4.3 Uses &amp; Examples</h3>
<ul>
<li><strong>Before another future action:</strong> Quand tu arriveras, j&#39;aurai déjà préparé le souper. (When you arrive, I will have already prepared dinner.)</li>
<li><strong>Assumption about the past:</strong> Il n&#39;est pas encore arrivé. Il aura pris le mauvais autobus. (He hasn&#39;t arrived yet. He will have taken the wrong bus. [i.e., He must have taken the wrong bus.])</li>
<li><strong>Deadline:</strong> D&#39;ici la fin du mois, nous aurons terminé tous les travaux de rénovation de la cuisine. (By the end of the month, we will have finished all the kitchen renovation work.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – End of Semester:</strong></p>
<p><em>Deux étudiants au cégep discutent avant les examens finaux.</em></p>
<p>&quot;Quand est-ce que tu auras fini tes examens?&quot;<br>&quot;J&#39;aurai tout terminé vendredi prochain. Et toi?&quot;<br>&quot;Moi, j&#39;aurai fini mercredi. Mon dernier examen, c&#39;est philo.&quot;<br>&quot;La philo, c&#39;est tough! Quand tu auras réussi, on fêtera ça en allant au 5 à 7!&quot;<br>&quot;Bonne idée! D&#39;ici là, j&#39;aurai lu trois cents pages de Camus et j&#39;aurai écrit deux dissertations.&quot;</p>
<p><em>(Two CEGEP students are talking before final exams. &quot;When will you have finished your exams?&quot; &quot;I will have finished everything next Friday. And you?&quot; &quot;Me, I will have finished Wednesday. My last exam is philosophy.&quot; &quot;Philosophy is tough! When you pass, we&#39;ll celebrate by going to a happy hour!&quot; &quot;Good idea! By then, I will have read three hundred pages of Camus and I will have written two essays.&quot;)</em></p>

<h3 id="h-b1-4-4">4.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>The futur antérieur is mostly used in writing and formal speech in Quebec. In conversation, Quebecers prefer simpler structures.</li>
<li><strong>&quot;Philo&quot;</strong> refers to the mandatory philosophy courses at cégep. All Quebec students must take two philosophy courses and one ethics course.</li>
<li><strong>&quot;Tough&quot;</strong> (pronounced like the English word) is commonly used in Quebec French to mean &quot;difficult&quot;: <strong>&quot;C&#39;est tough!&quot;</strong></li>
</ul>
"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(header)

print(f"B1 Part 1 (Template + Units 1-4) done. File size: {os.path.getsize(OUTPUT)} bytes")
