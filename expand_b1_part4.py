#!/usr/bin/env python3
"""Expand B1 Units 13-16 with more Quebec French content."""

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
    # UNIT 13: STORYTELLING
    # =========================================================================
    marker_13_end = '<h2 id="h-b1-u14">'
    new_13 = """
<p><strong>Quebec Folklore and Storytelling (🍁):</strong></p>
<p>Quebec has a rich oral tradition of storytelling ("les contes"). Narrative tenses (Imparfait, Passé Composé, Plus-que-parfait) are heavily used here.</p>
<table>
<thead><tr><th>Quebec Folktale</th><th>Description for Storytelling</th></tr></thead>
<tbody>
<tr><td><strong>La Chasse-galerie</strong></td><td>A classic deal-with-the-devil story where lumberjacks (bûcherons) make a pact to fly a canoe through the air to visit their sweethearts on New Year's Eve, promising not to swear or touch crosses on church steeples.</td></tr>
<tr><td><strong>Le Bonhomme Sept Heures</strong></td><td>A bogeyman figure used to scare children into going to bed. He visits at 7 PM to capture kids who are still awake.</td></tr>
<tr><td><strong>La Corriveau</strong></td><td>Based on a real historical figure (Marie-Josephte Corriveau) executed in 1763 for murder, her ghost is said to haunt the region of Lévis.</td></tr>
<tr><td><strong>Le Diable à la Danse</strong></td><td>A handsome stranger (the Devil in disguise) arrives at a party and dances endlessly with a young woman, until a priest intervenes to save her soul.</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – Telling a Ghost Story:</strong></p>
<p>"Il était une fois, dans les années 1800, un vieil homme qui <strong>habitait (imparfait)</strong> seul près de la forêt. Un soir qu'il <strong>avait neigé (plus-que-parfait)</strong> toute la journée, il <strong>a entendu (passé composé)</strong> cogner à sa porte."<br>"C'était qui?"<br>"C'est ça l'affaire! Quand il <strong>a ouvert</strong> la porte, il n'y <strong>avait</strong> personne. Seulement des traces de pas dans la neige qui <strong>s'arrêtaient</strong> net au milieu de la cour."<br>"Ah, tu me donnes la chair de poule (goosebumps)!"</p>

"""
    html = insert_before(html, marker_13_end, new_13)

    # =========================================================================
    # UNIT 14: FEELINGS & EMOTIONS
    # =========================================================================
    marker_14_end = '<h2 id="h-b1-u15">'
    new_14 = """
<p><strong>Quebec Expressions for Strong Emotions (🍁):</strong></p>
<p>B1 students should move beyond basic "Je suis content" or "Je suis triste."</p>
<ul>
<li><strong>Capoter (QC):</strong> To freak out / go crazy (positively or negatively). <em>"J'ai capoté quand j'ai vu le prix!"</em></li>
<li><strong>Avoir son voyage (QC):</strong> To be completely exhausted/fed up. <em>"J'ai mon voyage de cette tempête de neige!"</em></li>
<li><strong>Être en maudit (QC):</strong> To be very angry (mildly vulgar). <em>"Il m'a coupé sur l'autoroute, j'étais en maudit."</em></li>
<li><strong>Être de bonne heure sur le piton (QC):</strong> To be up early and energetic.</li>
<li><strong>S'ennuyer de (QC/FR):</strong> To miss someone/something. <em>"Je m'ennuie de ma famille en France." (Quebec prefers "s'ennuyer", France often uses "manquer à").</em></li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Reacting to Bad News:</strong></p>
<p>"J'en reviens pas! On vient de m'annoncer que la compagnie ferme ses portes."<br>"Quoi?! Tu me niaises? (Are you kidding me?)"<br>"Non, je suis sérieux. Je suis complètement découragé. J'y travaille depuis cinq ans."<br>"Je suis tellement désolé pour toi. Qu'est-ce que tu vas faire?"<br>"Honnêtement, je panique un peu. C'est tellement frustrant de perdre sa job comme ça, sans avertissement."<br>"Lâche pas, on va regarder son CV ensemble en fin de semaine."</p>

"""
    html = insert_before(html, marker_14_end, new_14)

    # =========================================================================
    # UNIT 15: RELATIONSHIPS
    # =========================================================================
    marker_15_end = '<h2 id="h-b1-u16">'
    new_15 = """
<p><strong>Quebec Dating & Relationship Culture (🍁):</strong></p>
<p>Vocabulary around relationships is essential. "Chum" and "Blonde" are strictly used for serious romantic partners in Quebec (they can loosely mean friends for older generations, but not today).</p>
<ul>
<li><strong>Mon chum / Ma blonde:</strong> My boyfriend / My girlfriend.</li>
<li><strong>Frencher (QC):</strong> To French kiss.</li>
<li><strong>Cruiser (QC):</strong> To flirt / hit on someone.</li>
<li><strong>Sortir ensemble:</strong> To date (exclusively).</li>
<li><strong>Les chicanes de couple (QC):</strong> Couple's arguments.</li>
<li><strong>Le conjoint de fait:</strong> Common-law partner (a massive legal/cultural institution in Quebec where many couples never marry).</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing Relationship Drama:</strong></p>
<p>"Est-ce que ça va avec ton chum dernièrement?"<br>"Pas vraiment... on s'est pognés (we argued) hier soir pour une niaiserie (a stupid thing)."<br>"Ah oui? Est-ce qu'il pense toujours à son ex?"<br>"Non, c'est pas ça. Il ne veut jamais faire de compromis quand on planifie nos fins de semaine. J'ai de la misère à communiquer avec lui."<br>"Tu devrais peut-être en jaser sérieusement avec. La communication, c'est la base, tsé."</p>

"""
    html = insert_before(html, marker_15_end, new_15)

    # =========================================================================
    # UNIT 16: COMPLAINTS & APOLOGIES
    # =========================================================================
    marker_16_end = '<h1 id="h-b1-part-v">'
    new_16 = """
<p><strong>Consumer Protection in Quebec (OPC) (🍁):</strong></p>
<p>The <strong>Office de la protection du consommateur (OPC)</strong> is a powerful government body in Quebec. When complaining formally, refer to your rights.</p>
<ul>
<li><strong>La garantie légale:</strong> In Quebec, the law implies a warranty of reasonable durability for all products, even without an extended warranty.</li>
<li><strong>Porter plainte:</strong> To file a complaint.</li>
<li><strong>Rembourser:</strong> To refund.</li>
<li><strong>Dédommager:</strong> To compensate.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Formal Complaint to Customer Service:</strong></p>
<p>"Bonjour, j'aimerais parler au responsable. J'ai acheté ce lave-vaisselle il y a à peine quatorze mois et le moteur a déjà sauté."<br>"Je suis désolé, monsieur, mais la garantie du fabricant d'un an est expirée."<br>"Je comprends, cependant au Québec, la Loi sur la protection du consommateur prévoit une garantie légale. Un appareil de ce prix devrait durer plus que quatorze mois."<br>"Je vais vérifier votre dossier avec mon superviseur. Vraiment désolé pour l'inconvénient."<br>"Merci, j'attends. S'il n'y a rien à faire de votre côté, je me verrai dans l'obligation de déposer une plainte à l'OPC."<br>"Un instant s'il vous plaît, je suis certain qu'on peut trouver un arrangement."</p>

"""
    html = insert_before(html, marker_16_end, new_16)

    write_file(path, html)
    print("B1 Part 4 done: Units 13-16 expanded successfully!")

if __name__ == '__main__':
    main()
