#!/usr/bin/env python3
"""Expand B1 Units 17-20 with more Quebec French content."""

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_before(html, marker, new_content):
    idx = html.find(marker)
    if idx == -1:
        print(f"WARNING: marker not found: {marker[:80]}...")
        return html
    return html[:idx] + new_content + html[idx:]

def main():
    path = r'e:\MyProjects\Web\Jason-French-Learning-Web\b1.html'
    html = read_file(path)

    # =========================================================================
    # UNIT 17: QUEBEC HISTORY
    # =========================================================================
    marker_17_end = '<h2 id="h-b1-u18">'
    new_17 = """
<p><strong>Key Moments in Quebec History (🍁):</strong></p>
<p>Understanding these historical events is crucial for understanding modern Quebec identity.</p>
<table>
<thead><tr><th>Event</th><th>Date</th><th>Significance</th></tr></thead>
<tbody>
<tr><td><strong>La Nouvelle-France</strong></td><td>1534 - 1763</td><td>Jacques Cartier's arrival; the foundation of French roots in North America until the British conquest.</td></tr>
<tr><td><strong>La Révolution Tranquille</strong></td><td>1960s</td><td>The "Quiet Revolution" - rapid modernization, secularization of society, creation of the welfare state (Hydro-Québec nationalization, hospital/school public control). "Maîtres chez nous".</td></tr>
<tr><td><strong>La Crise d'Octobre</strong></td><td>1970</td><td>The FLQ terrorist crisis in Montreal, resulting in the kidnapping/murder of a minister and the invocation of the War Measures Act by PM Pierre Elliott Trudeau.</td></tr>
<tr><td><strong>La Loi 101</strong></td><td>1977</td><td>The Charter of the French Language, establishing French as the sole official language of Quebec and requiring children of immigrants to attend French schools.</td></tr>
<tr><td><strong>Les Référendums</strong></td><td>1980, 1995</td><td>Two referendums on Quebec independence/sovereignty. The 1995 "Non" vote won by a razor-thin 50.58%.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – Discussing History in a Café:</strong></p>
<p>"Est-ce que tu penses qu'il va y avoir un troisième référendum sur la souveraineté dans notre vie?"<br>"J'en doute fort. La génération de nos parents était beaucoup plus militante à cause de la Révolution tranquille. Nous avons d'autres enjeux maintenant."<br>"C'est vrai, mais la question de l'identité et de la protection du français avec la Loi 101 reste au cœur des débats politiques."<br>"Absolument. 'Je me souviens' n'est pas juste une devise sur nos plaques d'immatriculation, c'est notre devoir de mémoire vis-à-vis de l'histoire du Québec."</p>

"""
    html = insert_before(html, marker_17_end, new_17)

    # =========================================================================
    # UNIT 18: ARTS & MUSIC
    # =========================================================================
    marker_18_end = '<h2 id="h-b1-u19">'
    new_18 = """
<p><strong>Quebec Music and Cinema Culture (🍁):</strong></p>
<p>Integrating into Quebec means knowing the artistic references (which are celebrated heavily at the ADISQ and Iris galas).</p>
<ul>
<li><strong>La chanson québécoise:</strong> Artists like Les Cowboys Fringants, Jean Leloup, Charlotte Cardin, Cœur de Pirate, and FouKi dominate airwaves. Many mix French with English slang (Franglais).</li>
<li><strong>Le cinéma québécois:</strong> Internationally acclaimed directors include Denis Villeneuve (Dune, Arrival), Xavier Dolan (Mommy), and Jean-Marc Vallée (C.R.A.Z.Y.). Films often use thick "Joual" to portray realism.</li>
<li><strong>Les humoristes:</strong> Comedians (Louis-José Houde, Martin Matte) are arguably the biggest stars in Quebec. Stand-up comedy is an art form here, celebrated at the Just For Laughs (Juste pour rire) festival.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing a Quebec Film:</strong></p>
<p>"As-tu finalement vu 'Incendies' de Denis Villeneuve?"<br>"Oui! Quel film puissant! La fin m'a complètement bouleversé. Les acteurs étaient exceptionnels."<br>"Je te l'avais dit! C'est un chef-d'œuvre. Si tu as aimé, tu devrais écouter 'C.R.A.Z.Y.'. C'est un grand classique du cinéma québécois."<br>"C'est sur ma liste. J'apprécie vraiment le fait que les films québécois n'ont pas peur de montrer la réalité crue, avec notre vrai accent et nos expressions."</p>

"""
    html = insert_before(html, marker_18_end, new_18)

    # =========================================================================
    # UNIT 19: POLITICS & SOCIETY
    # =========================================================================
    marker_19_end = '<h2 id="h-b1-u20">'
    new_19 = """
<p><strong>The Quebec Political System (🍁):</strong></p>
<p>Quebec operates under a parliamentary system (L'Assemblée nationale du Québec in Quebec City). B1 level learners should know the major political parties:</p>
<table>
<thead><tr><th>Party</th><th>Stance / Ideology</th></tr></thead>
<tbody>
<tr><td><strong>CAQ (Coalition Avenir Québec)</strong></td><td>Center-right, nationalist (autonomist), currently the dominant governing party. Focus on economy and protecting Quebec identity/language.</td></tr>
<tr><td><strong>PLQ (Parti libéral du Québec)</strong></td><td>Center, federalist (pro-Canada). Traditionally supported by the anglophone and immigrant communities.</td></tr>
<tr><td><strong>PQ (Parti Québécois)</strong></td><td>Center-left, sovereignist (pro-independence), nationalist.</td></tr>
<tr><td><strong>QS (Québec Solidaire)</strong></td><td>Left-wing, sovereignist, progressive, environmentalist.</td></tr>
</tbody>
</table>

<p><strong>Political Vocabulary:</strong></p>
<ul>
<li><strong>Un député:</strong> A Member of the National Assembly (MNA).</li>
<li><strong>Le scrutin:</strong> The election / ballot.</li>
<li><strong>L'Hôtel du Parlement:</strong> Where the provincial government sits in Quebec City.</li>
<li><strong>La laïcité:</strong> Secularism (separation of church and state, a major topic via Loi 21).</li>
</ul>

"""
    html = insert_before(html, marker_19_end, new_19)

    # =========================================================================
    # UNIT 20: REVIEW & B2 PREP
    # =========================================================================
    marker_20_end = '<h1 id="h-b1-conclusion">'
    new_20 = """
<p><strong>Advanced Grammar Review Checklist (End of B1):</strong></p>
<ul>
<li>✅ You can tell complex stories using the Imparfait (setting the scene), Passé Composé (actions), and Plus-que-parfait (prior actions).</li>
<li>✅ You confidently use "Si" clauses to make hypotheses (Si j'avais de l'argent, j'achèterais...).</li>
<li>✅ You correctly apply the Subjonctif in obligations and emotions (Il faut que je fasse ça).</li>
<li>✅ You can structure an argument with connectors (Cependant, En revanche, Par conséquent).</li>
<li>✅ You can express nuanced opinions and participate in debates without just saying "C'est bon" or "C'est mauvais".</li>
</ul>

<p><strong>Preview of B2 Level:</strong></p>
<p>In B2, you will learn to navigate the <em>bureaucracy</em> and the <em>intellectual sphere</em>:</p>
<ul>
<li><strong>Subjonctif Passé:</strong> Expressing doubt/emotion about past events (Je suis ravi que tu sois venu).</li>
<li><strong>Passive Voice Mastery:</strong> Used heavily in news and official documents.</li>
<li><strong>Nuanced Register:</strong> Switching seamlessly between formal business French ("soutenu") and intense Quebec slang ("Joual/familier").</li>
<li><strong>Complex Texts:</strong> Writing formal syntheses, professional cover letters, and university-level essays.</li>
</ul>

<p><strong>B1-B2 Transition Study Tips for Quebec:</strong></p>
<ul>
<li><strong>Read Le Devoir or La Presse daily:</strong> Move beyond the headlines and read the "Opinions" or "Chroniques" sections to absorb complex sentence structures and debate vocabulary.</li>
<li><strong>Listen to Radio-Canada Première:</strong> Talk radio is the best way to hear educated, fast-paced Quebec French.</li>
<li><strong>Watch Quebec political debates:</strong> (E.g., "Midi info" or "Les Coulisses du pouvoir") to understand the socio-political climate.</li>
</ul>

"""
    html = insert_before(html, marker_20_end, new_20)

    # =========================================================================
    # CONCLUSION
    # =========================================================================
    conclusion_marker = '<h1 id="h-b1-conclusion">'
    conclusion_idx = html.find(conclusion_marker)
    if conclusion_idx != -1:
        end_tag = html.find('</h1>', conclusion_idx)
        if end_tag != -1:
            insert_point = end_tag + len('</h1>')
            new_conclusion = """
<p><strong>Félicitations pour avoir complété le niveau B1 !</strong> You have now moved from basic survival to true independance. You can understand the news, express your opinions, handle complex social situations, and appreciate the nuances of Quebec's distinct history, politics, and culture.</p>
<p>At this stage, you possess the required level to operate confidently in most Quebec workplaces and participate in the vibrant social life of the province. <em>La prochaine étape : L'aisance totale au niveau B2 !</em> (Next step: Total fluency at the B2 level!)</p>
"""
            html = html[:insert_point] + new_conclusion + html[insert_point:]

    write_file(path, html)
    print("B1 Part 5 done: Units 17-20 and Conclusion expanded successfully!")

if __name__ == '__main__':
    main()
