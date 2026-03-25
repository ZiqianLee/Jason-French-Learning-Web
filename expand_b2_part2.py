#!/usr/bin/env python3
"""Expand B2 Units 5-8 with more Quebec French content."""

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
    path = r'e:\MyProjects\Web\Jason-French-Learning-Web\b2.html'
    html = read_file(path)

    # =========================================================================
    # UNIT 5: BUSINESS FRENCH
    # =========================================================================
    marker_5_end = '<h2 id="h-b2-u6">'
    new_5 = """
<p><strong>Corporate Quebec & Formal Emails (Courriels) (🍁):</strong></p>
<p>The business culture in Quebec (especially Montreal) is a unique blend of North American pragmatism and French linguistic formality. Note the vocabulary differences:</p>
<table>
<thead><tr><th>English</th><th>France French</th><th>Quebec French</th></tr></thead>
<tbody>
<tr><td>Email</td><td>Un e-mail / Un mail</td><td><strong>Un courriel</strong></td></tr>
<tr><td>Meeting</td><td>Une réunion / Un meeting</td><td><strong>Une rencontre / Une réunion</strong></td></tr>
<tr><td>Weekend</td><td>Le week-end</td><td><strong>La fin de semaine</strong></td></tr>
<tr><td>Feedback</td><td>Un feedback / Un retour</td><td><strong>Une rétroaction</strong></td></tr>
<tr><td>To sponsor</td><td>Sponsoriser</td><td><strong>Commanditer</strong></td></tr>
</tbody>
</table>

<p><strong>Key Acronyms:</strong> PDG (Président-directeur général - CEO), CA (Conseil d'administration - Board), RH (Ressources humaines - HR), OBNL (Organisme à but non lucratif - Non-profit).</p>

<p><strong>🇫🇷 Real-Life Scene – A Formal Email Exchange (Courriel formel):</strong></p>
<p><strong>Objet :</strong> Suivi concernant la rencontre du conseil d'administration</p>
<p><em>Bonjour madame Tremblay,</em></p>
<p><em>Faisant suite à notre discussion de ce matin, veuillez trouver ci-joint l'ordre du jour (agenda) pour le comité de direction de la semaine prochaine. <strong>Comme il a été convenu</strong>, nous aborderons en priorité la question de la pénurie de main-d'œuvre. <strong>Je vous saurais gré de bien vouloir</strong> me faire parvenir vos commentaires quant aux solutions proposées d'ici vendredi, fin de journée (COB).</em></p>
<p><em>Cordialement,</em></p>
<p><em>Mathieu Gagnon<br>Vice-président, Finances</em></p>

"""
    html = insert_before(html, marker_5_end, new_5)

    # =========================================================================
    # UNIT 6: LAW & RIGHTS
    # =========================================================================
    marker_6_end = '<h2 id="h-b2-u7">'
    new_6 = """
<p><strong>The Legal System in Quebec (Le Droit Civil) (🍁):</strong></p>
<p>Unlike the rest of Canada (which uses English Common Law), Quebec private law operates under the <strong>Code civil du Québec</strong>. This has massive implications for contracts, property, and family law.</p>
<ul>
<li><strong>La Charte des droits et libertés de la personne:</strong> Quebec's human rights charter, which is quasi-constitutional and prevails over ordinary laws.</li>
<li><strong>Un constat d'infraction:</strong> A ticket/fine (e.g., for speeding).</li>
<li><strong>Poursuivre quelqu'un:</strong> To sue someone. <em>"Il l'a poursuivi aux petites créances." (He sued him in small claims court).</em></li>
<li><strong>Un huissier de justice:</strong> A bailiff (who seizes property or serves documents).</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Small Claims Court (Les petites créances):</strong></p>
<p>"Je n'en reviens pas. L'entrepreneur qui a refait ma toiture a fait un travail bâclé, et maintenant il refuse de réparer les dégâts causés par les infiltrations d'eau."<br>"As-tu signé un contrat en bonne et due forme?"<br>"Oui, tout est écrit noir sur blanc. Je lui ai envoyé une <strong>mise en demeure</strong> (formal notice/demand letter) par courrier recommandé la semaine dernière."<br>"S'il ne répond pas dans le délai prescrit, tu n'auras pas d'autre choix que d'ouvrir un dossier à la <strong>Division des petites créances de la Cour du Québec</strong>. Tu vas te représenter toi-même, c'est fait pour ça."</p>

"""
    html = insert_before(html, marker_6_end, new_6)

    # =========================================================================
    # UNIT 7: SCIENCE & TECH
    # =========================================================================
    marker_7_end = '<h2 id="h-b2-u8">'
    new_7 = """
<p><strong>Quebec as a Tech Hub (🍁):</strong></p>
<p>Montreal is a global center for Artificial Intelligence (Mila institute), Video Games (Ubisoft, EA, Warner Bros), and Aerospace (Bombardier, CAE, CSA). OQLF works hard to francize tech terms.</p>
<table>
<thead><tr><th>Tech Field</th><th>French Terminology</th></tr></thead>
<tbody>
<tr><td><strong>AI / Machine Learning</strong></td><td>L'intelligence artificielle (IA), l'apprentissage automatique, un algorithme, les données (data).</td></tr>
<tr><td><strong>Video Games</strong></td><td>Un logiciel ludique, la jouabilité (gameplay), un développeur de jeux vidéo, la réalité virtuelle (RV).</td></tr>
<tr><td><strong>Aerospace</strong></td><td>L'aérospatiale, un simulateur de vol, l'ingénierie aéronautique.</td></tr>
<tr><td><strong>Cybersecurity</strong></td><td>La cybersécurité, le piratage informatique, l'hameçonnage (phishing), la protection des renseignements personnels.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – A Tech Startup Pitch:</strong></p>
<p>"Notre jeune pousse (startup) a développé une plateforme d'apprentissage profond (deep learning) qui permet de réduire les pertes énergétiques dans les usines de 15 %."<br>"C'est très impressionnant. Est-ce que votre solution nécessite une connexion infonuagique (cloud connection) constante?"<br>"Oui, toutes les données sont chiffrées (encrypted) de bout en bout et hébergées sur des serveurs locaux au Québec, pour respecter la Loi 25 sur la protection des données personnelles."<br>"Excellent. Nous aimerions organiser une réunion avec notre CTO pour voir comment on pourrait intégrer ça à notre pipeline (chaîne de production)."</p>

"""
    html = insert_before(html, marker_7_end, new_7)

    # =========================================================================
    # UNIT 8: HIGHER EDUCATION
    # =========================================================================
    marker_8_end = '<h1 id="h-b2-part-iii">'
    new_8 = """
<p><strong>Academic Research Terminology in Quebec (🍁):</strong></p>
<p>University language requires formal precision. Whether at UdeM, Laval, or UQAM, thesis writing follows strict protocols.</p>
<ul>
<li><strong>Le premier cycle / deuxième cycle / troisième cycle:</strong> Undergraduate (Bacc) / Graduate (Maîtrise) / Postgraduate (Doctorat).</li>
<li><strong>Un directeur de recherche / Une directrice de thèse:</strong> A thesis advisor.</li>
<li><strong>Une bourse de recherche (FRQSC, CRSNG):</strong> A research grant/fellowship.</li>
<li><strong>La soutenance de thèse:</strong> The thesis defense. (Not to be confused with "défense" which is an anglicism in this context).</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing a Master's Thesis:</strong></p>
<p>"Où en es-tu avec ta rédaction de mémoire (Master's thesis)?"<br>"J'avance tranquillement. J'ai terminé ma recension des écrits (literature review) le mois passé. Actuellement, je compile la méthodologie."<br>"Et ton directeur de recherche est satisfait du cadre théorique (theoretical framework)?"<br>"Oui, il a approuvé mon approche épistémologique. <strong>Toutefois</strong>, il m'a suggéré de raffiner ma problématique pour qu'elle soit plus arrimée (aligned) à la réalité sociologique du Québec rural."<br>"Bon courage! La rédaction, c'est toujours un travail de moine (a meticulous/painstaking job)."</p>

"""
    html = insert_before(html, marker_8_end, new_8)

    write_file(path, html)
    print("B2 Part 2 done: Units 5-8 expanded successfully!")

if __name__ == '__main__':
    main()
