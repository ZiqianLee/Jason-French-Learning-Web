#!/usr/bin/env python3
"""Expand B1 Units 5-8 with more Quebec French content."""

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
    # UNIT 5: EXPRESSING OPINIONS
    # =========================================================================
    marker_5_end = '<h2 id="h-b1-u6">'
    new_5 = """
<p><strong>Quebec Talk Radio Vocabulary (Lignes Ouvertes) (🍁):</strong></p>
<p>Talk radio ("les lignes ouvertes") is a massive part of Quebec media culture. To participate or understand the debates, you need specific phrasing:</p>
<table>
<thead><tr><th>French Phrase</th><th>English Context</th></tr></thead>
<tbody>
<tr><td><strong>"Je veux réagir à ce qui vient d'être dit."</strong></td><td>I want to react to what was just said. (Classic caller intro)</td></tr>
<tr><td><strong>"Ça n'a pas de bon sens!"</strong></td><td>That doesn't make any sense! (Very common expression of indignation)</td></tr>
<tr><td><strong>"Je suis entièrement d'accord avec l'animateur."</strong></td><td>I completely agree with the host.</td></tr>
<tr><td><strong>"Il faut prendre les choses avec un grain de sel."</strong></td><td>You have to take things with a grain of salt.</td></tr>
<tr><td><strong>"Je suis tanné(e) d'entendre parler de ça."</strong></td><td>I'm tired/sick of hearing about this.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – Debating the "Loi 96" on the Radio:</strong></p>
<p><em>Un auditeur appelle à une émission de radio pour donner son opinion sur la loi sur le français.</em></p>
<p>"Bonjour Mario. Écoute, moi je trouve que le gouvernement va trop loin avec cette nouvelle loi. <strong>À mon avis</strong>, on devrait encourager le français au lieu de punir les entreprises anglophones."<br>"Mais Paul, <strong>tu ne trouves pas que</strong> le français est menacé à Montréal?"<br>"<strong>Je reconnais que</strong> la situation est fragile, mais <strong>je suis persuadé que</strong> la coercition n'est pas la bonne solution. <strong>Il me semble que</strong> l'incitatif fonctionne mieux."<br>"C'est un point de vue qui se défend. Merci pour ton appel!"</p>

"""
    html = insert_before(html, marker_5_end, new_5)

    # =========================================================================
    # UNIT 6: CAUSE & CONSEQUENCE
    # =========================================================================
    marker_6_end = '<h2 id="h-b1-u7">'
    new_6 = """
<p><strong>Describing Quebec Infrastructure Issues (🍁):</strong></p>
<p>Cause and consequence vocabulary is perfect for discussing Montreal's perennial construction (les fameux "cônes oranges").</p>
<ul>
<li><strong>À cause de</strong> l'échangeur Turcot (Because of the Turcot interchange): <em>À cause des travaux sur l'échangeur, le trafic est paralysé.</em></li>
<li><strong>En raison de</strong> (Due to - more formal): <em>Le pont a été fermé en raison de vents violents.</em></li>
<li><strong>C'est pourquoi</strong> (That is why): <em>Nos infrastructures vieillissent, c'est pourquoi il y a tant de nids-de-poule et de cônes oranges.</em></li>
<li><strong>Par conséquent</strong> (Consequently): <em>Le REM en est encore à la phase de test. Par conséquent, les usagers de la Rive-Sud doivent être patients.</em></li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing the Cost of Living:</strong></p>
<p>"As-tu vu le prix des maisons dernièrement? C'est fou!"<br>"Oui, <strong>à cause de</strong> l'inflation et de la hausse des taux d'intérêt, les jeunes de notre génération ne peuvent plus acheter."<br>"<strong>Puisque</strong> l'offre est très faible et la demande est forte, les prix explosent."<br>"<strong>C'est pour ça que</strong> je regarde pour m'acheter un condo à Longueuil au lieu de Montréal. <strong>Ainsi</strong>, j'aurai une hypothèque qui a de l'allure (that makes sense)."</p>

"""
    html = insert_before(html, marker_6_end, new_6)

    # =========================================================================
    # UNIT 7: HYPOTHESES & CONDITIONS
    # =========================================================================
    marker_7_end = '<h2 id="h-b1-u8">'
    new_7 = """
<p><strong>Quebec Scenarios: "Si" Clauses in Action (🍁):</strong></p>
<table>
<thead><tr><th>Scenario Type</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td><strong>Possible (Present + Future)</strong></td><td>Si + Présent -> Futur Simple</td><td>"Si la CAQ gagne les prochaines élections, elle <strong>continuera</strong> ses réformes." (If the CAQ wins the next election, they will continue their reforms.)</td></tr>
<tr><td><strong>Unlikely (Imparfait + Cond. Présent)</strong></td><td>Si + Imparfait -> Cond. Présent</td><td>"Si je gagnais le salaire d'un joueur du Canadien, je <strong>m'achèterais</strong> une grosse cabane (mansion)." (If I earned a Habs player's salary, I would buy a mansion.)</td></tr>
<tr><td><strong>Impossible (Plus-que-parfait + Cond. Passé)*</strong></td><td>Si + Pluperfect -> Cond. Past</td><td>"Si les Nordiques n'étaient pas partis en 1995, le hockey à Québec <strong>aurait été</strong> différent." (If the Nordiques hadn't left in 1995...) <em>*Cond. Passé is B2 level, but good to recognize!</em></td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – Planning for Winter in a Chalet:</strong></p>
<p>"Si on louait un chalet dans Charlevoix pour Noël, ça serait magique!"<br>"Oui, mais si on a une grosse tempête de neige, on pourrait rester coincés."<br>"C'est vrai. Mais si le chalet a un bon poêle à bois, on n'aura pas froid, même s'il y a une panne d'électricité d'Hydro-Québec!"<br>"Bon point. Si le prix est raisonnable sur Airbnb, je vais le réserver."</p>

"""
    html = insert_before(html, marker_7_end, new_7)

    # =========================================================================
    # UNIT 8: REPORTED SPEECH
    # =========================================================================
    marker_8_end = '<h1 id="h-b1-part-iii">'
    new_8 = """
<p><strong>Analyzing Quebec News Reports (TVA, Radio-Canada) (🍁):</strong></p>
<p>Journalists use reported speech constantly. Notice how the verb tenses shift when reporting what a politician said:</p>
<ul>
<li><em>Direct:</em> Le Premier ministre: "Nous baisserons les impôts l'année prochaine." <strong>(Futur)</strong></li>
<li><em>Reported:</em> TVA Nouvelles a rapporté que le Premier ministre <strong>baisserait (Conditionnel)</strong> les impôts l'année <strong>suivante</strong>.</li>
</ul>
<ul>
<li><em>Direct:</em> Le maire de Montréal: "La piste cyclable est un énorme succès." <strong>(Présent)</strong></li>
<li><em>Reported:</em> Radio-Canada a souligné que le maire trouvait que la piste cyclable <strong>était (Imparfait)</strong> un énorme succès.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Spreading Gossip at the Office:</strong></p>
<p>"Hey, as-tu entendu ce que la boss a dit ce matin?"<br>"Non, qu'est-ce qu'elle a dit?"<br>"Elle a annoncé qu'elle <strong>allait (imparfait)</strong> prendre sa retraite bientôt."<br>"Vraiment? Et est-ce qu'elle a mentionné qui <strong>la remplacerait (conditionnel)</strong>?"<br>"Non, mais elle a demandé si nous <strong>voulions (imparfait)</strong> organiser un 5 à 7 pour son départ le mois <strong>suivant</strong>."</p>
<p><em>(Translation: "Hey, did you hear what the boss said this morning?" "No, what did she say?" "She announced that she was going to retire soon." "Really? And did she mention who would replace her?" "No, but she asked if we wanted to organize a 5 à 7 for her departure the following month.")</em></p>

"""
    html = insert_before(html, marker_8_end, new_8)

    write_file(path, html)
    print("B1 Part 2 done: Units 5-8 expanded successfully!")

if __name__ == '__main__':
    main()
