#!/usr/bin/env python3
"""Expand B1 Units 1-4 with more Quebec French content."""

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
    # UNIT 1: PLUS-QUE-PARFAIT
    # =========================================================================
    marker_1_end = '<h2 id="h-b1-u2">'
    new_1 = """
<p><strong>Quebec Context: Sharing Anecdotes (🍁):</strong></p>
<p>The plus-que-parfait is heavily used when recounting historical anecdotes or personal stories from the past. When discussing the Quiet Revolution (Révolution tranquille), for example:</p>
<ul>
<li><strong>Avant 1960, l'Église catholique avait contrôlé presque toutes les écoles et les hôpitaux du Québec.</strong> (Before 1960, the Catholic Church had controlled almost all schools and hospitals in Quebec.)</li>
<li><strong>Maurice Duplessis avait dirigé la province pendant l'époque qu'on appelle "la Grande Noirceur".</strong> (Maurice Duplessis had led the province during the era known as "The Great Darkness".)</li>
<li><strong>Le gouvernement provincial n'avait jamais créé de ministère de l'Éducation avant la Révolution tranquille.</strong> (The provincial government had never created a Ministry of Education prior to the Quiet Revolution.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Family Story:</strong></p>
<p><em>Un grand-père québécois raconte sa jeunesse à ses petits-enfants.</em></p>
<p>"Vous savez, les enfants, quand j'ai rencontré votre grand-mère en 1970, elle <strong>avait déjà fini</strong> ses études d'infirmière. Moi, par contre, je <strong>n'avais pas encore commencé</strong> à travailler sérieusement. J'<strong>avais voyagé</strong> un peu partout en Amérique du Nord sur le pouce (hitchhiking)."<br>"Et comment vous vous êtes rencontrés?"<br>"On s'est croisés à un spectacle de Robert Charlebois sur les plaines d'Abraham. J'<strong>avais réussi</strong> à me faufiler en avant, et elle, elle <strong>avait perdu</strong> ses amies dans la foule. Le reste, c'est de l'histoire!"</p>

"""
    html = insert_before(html, marker_1_end, new_1)

    # =========================================================================
    # UNIT 2: CONDITIONNEL PRÉSENT
    # =========================================================================
    marker_2_end = '<h2 id="h-b1-u3">'
    new_2 = """
<p><strong>Conditionnel in Quebec Social Issues (🍁):</strong></p>
<p>The conditional is used extensively when discussing hypotheses regarding politics, economy, and social services.</p>
<table>
<thead><tr><th>Scenario</th><th>English Translation</th></tr></thead>
<tbody>
<tr><td><strong>Si le gouvernement investissait plus en santé, il y aurait moins d'attente à l'urgence.</strong></td><td>If the government invested more in healthcare, there would be less waiting in the ER.</td></tr>
<tr><td><strong>Avec un meilleur réseau de transport en commun, les Montréalais prendraient moins leur char.</strong></td><td>With a better public transit network, Montrealers would take their cars less.</td></tr>
<tr><td><strong>Une nouvelle loi sur la laïcité provoquerait probablement des manifestations.</strong></td><td>A new law on secularism would probably provoke protests.</td></tr>
<tr><td><strong>Selon Radio-Canada, la grève des profs pourrait s'étirer jusqu'en janvier.</strong></td><td>According to Radio-Canada, the teachers' strike could stretch until January.</td></tr>
</tbody>
</table>

<p><strong>Expressing Politeness in Customer Service:</strong></p>
<ul>
<li><strong>Pourriez-vous m'accommoder?</strong> (Could you accommodate me?)</li>
<li><strong>J'aimerais parler au gérant, s'il vous plaît.</strong> (I would like to speak to the manager, please.)</li>
<li><strong>Serait-il possible de reporter mon rendez-vous à la clinique?</strong> (Would it be possible to postpone my appointment at the clinic?)</li>
</ul>
<p><em>Note: In Quebec, even when using formal "vous" and the conditional, tone and body language remain relatively warm and less rigid than in France.</em></p>

"""
    html = insert_before(html, marker_2_end, new_2)

    # =========================================================================
    # UNIT 3: SUBJONCTIF PRÉSENT
    # =========================================================================
    marker_3_end = '<h2 id="h-b1-u4">'
    new_3 = """
<p><strong>Quebec Administrative Necessities (Subjonctif in Action) (🍁):</strong></p>
<p>When dealing with Immigration (MIFI), the Régie du logement (TAL), or the SAAQ, you will hear the subjunctive constantly to express obligations and necessities.</p>
<table>
<thead><tr><th>Context</th><th>French Phrase</th><th>English</th></tr></thead>
<tbody>
<tr><td><strong>Immigration</strong></td><td>Il faut que le candidat <strong>réussisse</strong> son test de valeurs québécoises.</td><td>The candidate must pass their Quebec values test.</td></tr>
<tr><td><strong>Housing (TAL)</strong></td><td>Il est primordial que le locataire <strong>paie</strong> son loyer le 1er du mois.</td><td>It is primordial that the tenant pay their rent on the 1st of the month.</td></tr>
<tr><td><strong>Driving (SAAQ)</strong></td><td>La SAAQ exige que vous <strong>fassiez</strong> inspecter votre véhicule.</td><td>The SAAQ demands that you have your vehicle inspected.</td></tr>
<tr><td><strong>Taxes (Revenu QC)</strong></td><td>Afin que nous <strong>puissions</strong> traiter votre dossier, envoyez le formulaire T4.</td><td>So that we may process your file, send the T4 form.</td></tr>
<tr><td><strong>Healthcare (RAMQ)</strong></td><td>Il vaut mieux que tu <strong>ailles</strong> dans une clinique sans rendez-vous.</td><td>It's better that you go to a walk-in clinic.</td></tr>
</tbody>
</table>

<p><strong>Common Subjunctive "Trigger" Verbs & Expressions for B1:</strong></p>
<ul>
<li><strong>Douter que:</strong> Je doute que les Nordiques reviennent à Québec à court terme. (I doubt the Nordiques will return to Quebec City in the short term.)</li>
<li><strong>Craindre que:</strong> Les écologistes craignent que le projet de pipeline ne <strong>détruise</strong> la faune locale. (Environmentalists fear that the pipeline project will destroy local wildlife.)</li>
<li><strong>Bien que / Quoique:</strong> Bien que l'hiver <strong>soit</strong> long, c'est une saison magnifique. (Although winter is long, it's a beautiful season.)</li>
</ul>

"""
    html = insert_before(html, marker_3_end, new_3)

    # =========================================================================
    # UNIT 4: FUTUR ANTÉRIEUR
    # =========================================================================
    marker_4_end = '<h1 id="h-b1-part-ii">'
    new_4 = """
<p><strong>4.1 Introduction (Continued)</strong></p>
<p>The <strong>futur antérieur</strong> translates to "will have [done]" in English. It establishes a timeline in the future, marking an action that will be completed <em>before</em> another future action.</p>
<ul>
<li><strong>Quand tu arriveras (futur simple), j'aurai déjà préparé (futur antérieur) le souper.</strong> (When you arrive, I will have already prepared supper.)</li>
<li><strong>Dès qu'il aura obtenu sa citoyenneté, il votera.</strong> (As soon as he has obtained his citizenship, he will vote.)</li>
</ul>

<p><strong>4.2 Formation</strong></p>
<p>Futur antérieur = <strong>futur simple of avoir/être + past participle</strong>.</p>
<table>
<thead><tr><th>Pronoun</th><th>With Avoir (Finir)</th><th>With Être (Arriver)</th></tr></thead>
<tbody>
<tr><td>J' / Je</td><td>aurai fini</td><td>serai arrivé(e)</td></tr>
<tr><td>Tu</td><td>auras fini</td><td>seras arrivé(e)</td></tr>
<tr><td>Il/Elle/On</td><td>aura fini</td><td>sera arrivé(e)</td></tr>
<tr><td>Nous</td><td>aurons fini</td><td>serons arrivé(e)s</td></tr>
<tr><td>Vous</td><td>aurez fini</td><td>serez arrivé(e)(s)</td></tr>
<tr><td>Ils/Elles</td><td>auront fini</td><td>seront arrivé(e)s</td></tr>
</tbody>
</table>

<p><strong>4.3 Uses & Examples (Focus on Quebec Future Predictions 🍁)</strong></p>
<ul>
<li><strong>By a certain time:</strong> D'ici 2030, Hydro-Québec <strong>aura construit</strong> de nouveaux barrages pour répondre à la demande. (By 2030, Hydro-Québec will have built new dams to meet demand.)</li>
<li><strong>After conjunctions of time (quand, lorsque, dès que, aussitôt que):</strong> Aussitôt que la neige <strong>aura fondu</strong>, les nids-de-poule (potholes) apparaîtront sur les routes de Montréal. (As soon as the snow has melted, potholes will appear on Montreal roads.)</li>
<li><strong>Expressing probability regarding a past event:</strong> Elle n'est pas au bureau aujourd'hui. Elle <strong>aura sûrement pogné</strong> (QC) la grippe. (She's not at the office today. She must have caught the flu.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing the R.E.M. (Réseau express métropolitain):</strong></p>
<p>"Est-ce que l'extension du REM va être prête l'année prochaine?"<br>"Ils espèrent que oui. D'ici l'automne prochain, ils <strong>auront terminé</strong> les tests sur la nouvelle ligne vers l'aéroport."<br>"Tant mieux! Quand le projet complet <strong>aura été inauguré</strong>, le trafic sur l'autoroute 20 va sûrement diminuer."<br>"C'est l'objectif. Dès qu'on <strong>aura branché</strong> la Rive-Nord et la Rive-Sud directement au centre-ville, ça va changer la dynamique immobilière."</p>
<p><em>(Translation: "Will the REM extension be ready next year?" "They hope so. By next fall, they will have finished testing on the new line to the airport." "Good! When the entire project has been inaugurated, traffic on Highway 20 will surely decrease." "That's the goal. As soon as we have connected the North Shore and South Shore directly to downtown, it will change the real estate dynamics.")</em></p>

"""
    html = insert_before(html, marker_4_end, new_4)

    write_file(path, html)
    print("B1 Part 1 done: Units 1-4 expanded successfully!")

if __name__ == '__main__':
    main()
