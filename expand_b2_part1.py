#!/usr/bin/env python3
"""Expand B2 Units 1-4 with more Quebec French content."""

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
    # UNIT 1: SUBJONCTIF PASSÉ
    # =========================================================================
    marker_1_end = '<h2 id="h-b2-u2">'
    new_1 = """
<p><strong>Applying Subjonctif Passé in Quebec Social Contexts (🍁):</strong></p>
<p>At the B2 level, expressing regret or doubt regarding past political/social events is a key competency. The <em>Subjonctif passé</em> elevates your argument.</p>
<ul>
<li><strong>Bien que la Charte de la langue française ait été adoptée en 1977, le débat linguistique persiste.</strong> (Although the Charter of the French Language was adopted in 1977, the linguistic debate persists.)</li>
<li><strong>Je doute fort que le gouvernement précédent ait prévu cette crise du logement.</strong> (I highly doubt the previous government foresaw this housing crisis.)</li>
<li><strong>Il est déplorable que tant d'entreprises locales aient fait faillite pendant la pandémie.</strong> (It is deplorable that so many local businesses went bankrupt during the pandemic.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing Urban Development:</strong></p>
<p><em>Un panel de discussion à la radio sur le développement immobilier à Montréal.</em></p>
<p>"Je suis vraiment fâchée que les promoteurs <strong>aient détruit</strong> ces bâtiments patrimoniaux dans Griffintown."<br>"C'est vrai que c'est triste. Il aurait fallu que la Ville <strong>soit intervenue</strong> plus tôt pour les protéger."<br>"Absolument. Jusqu'à ce que les citoyens <strong>se soient mobilisés</strong>, personne n'en parlait. Il est impensable qu'on <strong>ait laissé</strong> cela se produire dans une ville avec une telle histoire."</p>

"""
    html = insert_before(html, marker_1_end, new_1)

    # =========================================================================
    # UNIT 2: THE PASSIVE VOICE
    # =========================================================================
    marker_2_end = '<h2 id="h-b2-u3">'
    new_2 = """
<p><strong>Bureaucratic & Police French in Quebec (🍁):</strong></p>
<p>The passive voice is extremely common in official communications (police press releases, government bulletins) to remain objective.</p>
<table>
<thead><tr><th>Active (Informal / Spoken)</th><th>Passive (Official / Written)</th></tr></thead>
<tbody>
<tr><td>La police a arrêté deux suspects à Longueuil.</td><td>Deux suspects <strong>ont été appréhendés</strong> par le SPVAL (Service de police de l'agglomération de Longueuil).</td></tr>
<tr><td>La Sûreté du Québec (SQ) va bloquer la route 132.</td><td>La route 132 <strong>sera entravée</strong> (blocked/obstructed) par la SQ.</td></tr>
<tr><td>Le conseil municipal a rejeté la proposition.</td><td>La proposition <strong>a été rejetée</strong> par le conseil municipal.</td></tr>
<tr><td>On a octroyé (granted) un contrat de 5 millions.</td><td>Un contrat de 5 millions <strong>a été octroyé</strong>.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – Reading a Hydro-Québec Notice:</strong></p>
<p><em>Avis d'interruption de service</em></p>
<p>« Chers clients, veuillez noter que l'alimentation électrique <strong>sera interrompue</strong> le 15 mai entre 8h et 16h en raison de travaux d'entretien. Votre compteur intelligent <strong>sera remplacé</strong> par un de nos techniciens. Vous <strong>serez avisés</strong> par courriel lorsque le service <strong>aura été rétabli</strong> (futur antérieur passif). Merci de votre compréhension. »</p>

"""
    html = insert_before(html, marker_2_end, new_2)

    # =========================================================================
    # UNIT 3: DISCOURSE MARKERS
    # =========================================================================
    marker_3_end = '<h2 id="h-b2-u4">'
    new_3 = """
<p><strong>Advanced Structuring of Arguments (🍁):</strong></p>
<p>To pass the B2 DELF or TEFAQ speaking exams, you must link your ideas elegantly, especially when discussing "pour ou contre" (pros and cons) issues like secularism (laïcité) or healthcare privatization.</p>
<ul>
<li><strong>Concession:</strong> <em>Il est vrai que</em> le système privé est plus rapide. <em>Or</em> (However), il crée une médecine à deux vitesses.</li>
<li><strong>Addition:</strong> <em>Outre</em> (Besides) le manque de personnel, <em>il s'ajoute le fait que</em> nos infrastructures sont vétustes (outdated).</li>
<li><strong>Opposition:</strong> Les régions éloignées perdent leur population, <em>tandis que</em> Montréal souffre de surpopulation urbaine.</li>
<li><strong>Synthesis:</strong> <em>Dans l'ensemble</em> (Overall), <em>tout compte fait</em> (all things considered), nous devons réformer le système.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – An Opinion Piece (Une lettre d'opinion) in Le Devoir:</strong></p>
<p>« <strong>Certes</strong>, l'intégration de nouvelles technologies dans les écoles québécoises est inévitable et souhaitable. <strong>Toutefois</strong>, il convient de s'interroger sur l'impact des écrans sur la concentration des élèves. <strong>En effet</strong>, plusieurs études démontrent une baisse de l'attention. <strong>Ainsi</strong>, <strong>bien que</strong> nous devions moderniser nos méthodes éducatives, <strong>il n'en demeure pas moins que</strong> la modération est de mise. »</p>
<p><em>(Translation: "Admittedly, the integration of new technologies in Quebec schools is inevitable and desirable. However, it is necessary to question the impact of screens on students' concentration. Indeed, several studies show a drop in attention. Thus, although we must modernize our educational methods, the fact remains that moderation is required.")</em></p>

"""
    html = insert_before(html, marker_3_end, new_3)

    # =========================================================================
    # UNIT 4: NUANCED OPINIONS
    # =========================================================================
    marker_4_end = '<h1 id="h-b2-part-ii">'
    new_4 = """
<p><strong>High-Level Debate Vocabulary in Quebec (🍁):</strong></p>
<p>When participating in university seminars, board meetings, or political debates, expressing polite but firm disagreement is essential.</p>
<ul>
<li><strong>Je m'inscris en faux contre cette affirmation.</strong> (I strongly disagree with that statement - Highly formal).</li>
<li><strong>Permettez-moi d'en douter.</strong> (Allow me to doubt that.)</li>
<li><strong>Il y a un bémol à apporter.</strong> (A caveat must be added.)</li>
<li><strong>C'est un couteau à double tranchant.</strong> (It's a double-edged sword.)</li>
<li><strong>C'est tirer par les cheveux.</strong> (That's far-fetched / stretching the truth.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Heated Television Debate on "Tout le monde en parle":</strong></p>
<p><em>Guy A. Lepage (animateur) interroge deux invités sur la protection de l'environnement.</em></p>
<p>"Vous prétendez que la taxe carbone va détruire nos petites entreprises, mais <strong>n'est-il pas vrai que</strong> l'inaction coûtera encore plus cher?"<br>"<strong>Je comprends votre point de vue, mais on doit nuancer.</strong> Les fermiers en région n'ont pas d'alternative pour leurs tracteurs. <strong>C'est utopique de penser que</strong> tout le monde peut passer à l'électrique du jour au lendemain."<br>"<strong>Je vous arrête tout de suite. La réalité est bien différente.</strong> Les subventions gouvernementales sont là pour aider la transition. <strong>Il est aberrant que</strong> nous continuions à protéger les énergies fossiles."</p>

"""
    html = insert_before(html, marker_4_end, new_4)

    write_file(path, html)
    print("B2 Part 1 done: Units 1-4 expanded successfully!")

if __name__ == '__main__':
    main()
