#!/usr/bin/env python3
"""Expand B2 Units 9-12 with more Quebec French content."""

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
    # UNIT 9: LITERATURE
    # =========================================================================
    marker_9_end = '<h2 id="h-b2-u10">'
    new_9 = """
<p><strong>The Evolution of Quebec Literature (🍁):</strong></p>
<p>Quebec literature reflects the province's transition from an agrarian, religious society to a modern, secular one.</p>
<ul>
<li><strong>Le terroir (Pre-1960s):</strong> Literature focusing on the land, the farm, and submission to divine will (e.g., <em>Un homme et son péché</em> by Claude-Henri Grignon).</li>
<li><strong>La rupture & l'utilisation du Joual (1960s+):</strong> Michel Tremblay revolutionized Quebec theater with <em>Les Belles-Sœurs</em> (1968), using raw, working-class Montreal dialect (Joual) on a formal stage for the first time.</li>
<li><strong>Modern Voices:</strong> Authors like Kim Thúy (<em>Ru</em>) explore the immigrant experience, integrating Vietnamese origins into Quebec culture.</li>
<li><strong>The Passé Simple:</strong> Unlike everyday speech, French literature exclusively relates narratives using the Passé Simple (e.g., "Il <em>frappa</em> à la porte" instead of "Il a frappé..."). You must recognize it, though you rarely need to write it or speak it.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Book Club Meeting (Club de lecture):</strong></p>
<p>"Qu'avez-vous pensé du roman qu'on devait lire ce mois-ci?"<br>"<strong>De prime abord</strong>, l'intrigue m'a semblé prévisible. Par contre, j'ai été fasciné par le développement psychologique de la protagoniste. L'auteur a su capter l'angoisse de la solitude urbaine avec beaucoup de justesse."<br>"<strong>Je partage ton analyse.</strong> L'utilisation du discours indirect libre donne une profondeur inouïe au récit. Ce qui est remarquable, c'est la façon dont le langage évolue au fil de l'histoire, passant d'un registre très soutenu à des éclats de familiarité."</p>

"""
    html = insert_before(html, marker_9_end, new_9)

    # =========================================================================
    # UNIT 10: CINEMA & MEDIA
    # =========================================================================
    marker_10_end = '<h2 id="h-b2-u11">'
    new_10 = """
<p><strong>Analyzing Media Bias and Francophone Cinema (🍁):</strong></p>
<p>At the B2 level, critical consumption of media is essential. Quebec cinema, heavily subsidized via Telefilm Canada and SODEC, holds a mirror to society.</p>
<ul>
<li><strong>L'objectivité journalistique:</strong> Objectivity in journalism vs. "les faits alternatifs" and "la désinformation" (fake news).</li>
<li><strong>Le parti pris:</strong> Bias / Preconceived stance. <em>"Cet éditorialiste a un parti pris évident."</em></li>
<li><strong>La mise en scène:</strong> The directing/staging of a film.</li>
<li><strong>Un plan-séquence:</strong> A long take (filming technique).</li>
<li><strong>Le jeu d'acteur / Le scénario:</strong> Acting / The script.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing Media Ethics:</strong></p>
<p>"Est-ce que tu as vu le reportage choc de l'émission 'Enquête' hier soir à Radio-Canada?"<br>"Oui, c'était troublant. Le journalisme d'investigation qu'ils font est d'une grande rigueur. Ils ont complètement exposé le stratagème de corruption."<br>"Absolument. Contrairement aux chaînes d'information en continu, qui privilégient souvent le sensationnalisme, ce type de magazine prend le temps d'approfondir les dossiers. C'est essentiel pour la vitalité démocratique."</p>

"""
    html = insert_before(html, marker_10_end, new_10)

    # =========================================================================
    # UNIT 11: SOCIAL DEBATES
    # =========================================================================
    marker_11_end = '<h2 id="h-b2-u12">'
    new_11 = """
<p><strong>Major Societal Challenges in Quebec (🍁):</strong></p>
<p>To pass a B2 oral exam, you must be able to debate current social issues using formal structures and statistics.</p>
<table>
<thead><tr><th>Societal Issue</th><th>Key Vocabulary</th></tr></thead>
<tbody>
<tr><td><strong>Laïcité (Secularism / Loi 21)</strong></td><td>Les signes ostentatoires (conspicuous symbols), la neutralité de l'État, un accommodement raisonnable, la liberté de conscience.</td></tr>
<tr><td><strong>Immigration (MIFI)</strong></td><td>La pénurie de main-d'œuvre (labor shortage), la francisation (teaching French), la reconnaissance des acquis (recognizing foreign degrees).</td></tr>
<tr><td><strong>Crise du logement (Housing)</strong></td><td>La spéculation immobilière, les rénovictions (evicting to renovate), l'abordabilité (affordability), l'étalement urbain (urban sprawl).</td></tr>
<tr><td><strong>Crise de la santé (Healthcare)</strong></td><td>Le temps d'attente aux urgences, l'exode des infirmières (nursing exodus), le vieillissement de la population.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – Debating Urban Sprawl at a City Council:</strong></p>
<p>"Il faut agir contre l'étalement urbain. Les nouvelles banlieues détruisent nos terres agricoles de la vallée du Saint-Laurent."<br>"C'est facile à dire, mais avec la crise du logement, les jeunes familles ne peuvent plus se loger sur l'île de Montréal. L'abordabilité est quasi nulle."<br>"<strong>Toutefois,</strong> construire toujours plus d'autoroutes ne règlera pas le problème. Il faut densifier les quartiers existants près des stations de métro et du REM."<br>"<strong>Je suis d'accord sur le principe, mais</strong> les municipalités doivent agir de concert avec Québec pour adapter le zonage."</p>

"""
    html = insert_before(html, marker_11_end, new_11)

    # =========================================================================
    # UNIT 12: QUEBEC IDENTITY
    # =========================================================================
    marker_12_end = '<h1 id="h-b2-part-iv">'
    new_12 = """
<p><strong>The Linguistic and National Question (Loi 101) (🍁):</strong></p>
<p>The core of Quebec political life revolves around the protection of the French language in a sea of English North America.</p>
<ul>
<li><strong>L'affichage public:</strong> The law dictates that commercial signage must have French distinctly predominant. The OQLF (Office québécois de la langue française) enforces this.</li>
<li><strong>L'assimilation:</strong> The fear of francophones adopting English as their primary language, leading to demographic decline (le déclin du français).</li>
<li><strong>Le multiculturalisme vs. l'interculturalisme:</strong> Canada promotes multiculturalism (a mosaic of cultures). Quebec favors <em>interculturalism</em> (immigrants integrate into a common public culture, centered on the French language, while maintaining their roots).</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing the Future of the Language:</strong></p>
<p>"As-tu lu l'étude démographique de Statistique Canada ce matin? Le taux de francophones à la maison a encore baissé."<br>"Oui, c'est très préoccupant. <strong>C'est pour pallier cette situation que</strong> le gouvernement a renforcé la loi 101 avec le projet de loi 96."<br>"<strong>Penses-tu vraiment que</strong> légiférer soit suffisant? <strong>Il me semble que</strong> nous devrions plutôt miser sur la promotion de l'attrait de notre culture."<br>"Les deux sont nécessaires. On ne peut pas être naïf ; face à l'hégémonie anglo-saxonne, des mesures de protection strictes sont primordiales."</p>

"""
    html = insert_before(html, marker_12_end, new_12)

    write_file(path, html)
    print("B2 Part 3 done: Units 9-12 expanded successfully!")

if __name__ == '__main__':
    main()
