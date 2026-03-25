#!/usr/bin/env python3
"""Expand B2 Units 13-16 with more Quebec French content."""

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
    # UNIT 13: HUMOUR & SARCASM
    # =========================================================================
    marker_13_end = '<h2 id="h-b2-u14">'
    new_13 = """
<p><strong>Quebec Humour & Stand-up Comedy (🍁):</strong></p>
<p>Comedy is a massive industry in Quebec. Understanding local humour is the ultimate test of cultural integration. It relies heavily on self-deprecation (l'autodérision), social observation, and navigating the line between formal French and thick <em>Joual</em> for comedic effect.</p>
<ul>
<li><strong>Le deuxième degré:</strong> Irony/sarcasm. Taking something seriously when it's meant as a joke. <em>"Faut le prendre au deuxième degré."</em></li>
<li><strong>Une blague plate:</strong> A dad joke, a flat/lame joke.</li>
<li><strong>Le festival Juste pour rire (Just For Laughs):</strong> The largest international comedy festival in the world, held every July in Montreal. Includes "Les Galas" hosted by major comedians.</li>
<li><strong>Le cynisme:</strong> Often used when discussing politics or winter.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing a Comedy Show:</strong></p>
<p>"Es-tu allé voir le nouveau spectacle de Martin Matte?"<br>"Oui, hier soir. J'ai ri aux larmes! Son autodérision est incomparable. Il a passé vingt minutes à rire de son propre ego."<br>"C'est sa marque de commerce. L'humour québécois, c'est souvent très grinçant (biting/dark), mais ça fait du bien de ne pas se prendre au sérieux."<br>"Totalement. Par contre, il y avait deux Français derrière moi qui n'ont rien compris aux références sur la politique municipale de Montréal!"</p>

"""
    html = insert_before(html, marker_13_end, new_13)

    # =========================================================================
    # UNIT 14: IDIOMS & SLANG (ADVANCED JOUAL)
    # =========================================================================
    marker_14_end = '<h2 id="h-b2-u15">'
    new_14 = """
<p><strong>Deep Joual & Sacres (Advanced Slang) (🍁):</strong></p>
<p>At B2, you should be able to comprehend heavy working-class Quebec slang ("le joual") in movies and informal settings, even if you speak standard French yourself. <em>Warning: "Sacres" (swears) are deeply offensive to older generations but common among peers.</em></p>
<table>
<thead><tr><th>Quebec Slang / Idiom</th><th>Equivalent / Meaning</th></tr></thead>
<tbody>
<tr><td><strong>Être pâmé sur quelqu'un</strong></td><td>To swoon over someone / be deeply infatuated.</td></tr>
<tr><td><strong>Se péter les bretelles</strong></td><td>To brag / boast (literally: snapping one's suspenders).</td></tr>
<tr><td><strong>Avoir la chienne</strong></td><td>To be terrified / scared to death.</td></tr>
<tr><td><strong>Les sacres (Tabarnak, Câlice, Osti)</strong></td><td>Catholic-derived swears. They act as adjectives, adverbs, and punctuation. DO NOT use them in professional settings.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – A Passionate Hockey Argument (Heavy Accent context):</strong></p>
<p>"C'est quoi c'te (cette) passe-là! Y'a (il a) même pas r'gardé (regardé) avant d'tirer!"<br>"Ben voyons donc, l'arbitre a rien vu pantoute! C'est de l'aveuglement volontaire rendu là."<br>"J't'le (Je te le) dis, s'ils (s'y) perdent c'te game-là, j'déchire (je déchire) ma carte de membre. Ça a pas de maudit bon sens de jouer demême (de même / like that)."</p>

"""
    html = insert_before(html, marker_14_end, new_14)

    # =========================================================================
    # UNIT 15: FORMAL WRITING (BUREAUCRACY)
    # =========================================================================
    marker_15_end = '<h2 id="h-b2-u16">'
    new_15 = """
<p><strong>Writing Formal Syntheses & Bureaucratic French (🍁):</strong></p>
<p>If working in the Quebec government (fonction publique) or academia, you must master the "note de service" (memo) and "compte-rendu" (minutes/report). Sentences are highly structured.</p>
<ul>
<li><strong>Par la présente:</strong> By this letter/memo...</li>
<li><strong>Dans l'éventualité où:</strong> In the event that...</li>
<li><strong>Veuillez agréer, Madame, Monsieur, l'expression de mes sentiments distingués:</strong> Formal closing (used mainly with Europe/France). Quebec often prefers the simpler: <em>"Veuillez agréer mes salutations distinguées."</em></li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Writing an Administrative Memo:</strong></p>
<p><em>Mémo interne du Ministère des Transports du Québec (MTQ)</em></p>
<p>« <strong>Par la présente</strong>, nous vous informons que le déploiement de la nouvelle signalisation débutera le 1er septembre. <strong>Dans l'éventualité où</strong> des conditions météorologiques défavorables entraveraient le processus, un plan de contingence sera mis en œuvre. <strong>Quiconque</strong> remarquera une anomalie sur le réseau routier est prié de le signaler au coordonnateur régional. »</p>

"""
    html = insert_before(html, marker_15_end, new_15)

    # =========================================================================
    # UNIT 16: PRONUNCIATION (ADVANCED PHONETICS)
    # =========================================================================
    marker_16_end = '<h1 id="h-b2-part-v">'
    new_16 = """
<p><strong>Advanced Quebec Phonetics (🍁):</strong></p>
<p>To truly understand native speakers, you must recognize linguistic shifts unique to Quebec:</p>
<ul>
<li><strong>L'affrication (Ts / Dz):</strong> The letters 'T' and 'D' become 'Ts' and 'Dz' when followed by 'U' or 'I'. Example: <em>Poutine</em> sounds like Pout<strong>s</strong>ine. <em>Mardi</em> sounds like Mar<strong>dz</strong>i.</li>
<li><strong>Les diphtongues:</strong> Long vowels stretch into two sounds. <em>Fête</em> sounds like f<strong>ai-i</strong>te. <em>Père</em> sounds like p<strong>a-e</strong>r.</li>
<li><strong>Relâchement vocalique:</strong> Vowels 'i', 'u', 'ou' become lax in closed syllables. Example: <em>Minute</em> sounds like min<strong>u</strong>t (almost an 'uh' sound), not the tight French 'u'.</li>
<li><strong>La suppression du "il":</strong> "Il pleut" becomes "Y pleut". "Il y a" becomes "Y'a".</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Understanding Fast Native Speech:</strong></p>
<p><em>Standard French (Written):</em> "Il faut que tu dises la vérité sur l'histoire du bout du monde."<br><em>Quebec Spoken Reality:</em> "Faut qu'tu <strong>dz</strong>ises la véri<strong>ts</strong>é sur l'histoi-è-re du bout <strong>dz</strong>u monde."</p>

"""
    html = insert_before(html, marker_16_end, new_16)

    write_file(path, html)
    print("B2 Part 4 done: Units 13-16 expanded successfully!")

if __name__ == '__main__':
    main()
