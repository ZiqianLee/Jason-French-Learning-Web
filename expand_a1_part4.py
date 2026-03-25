#!/usr/bin/env python3
"""Expand A1 Units 15-20 and Conclusion with more Quebec French content."""

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
    path = r'e:\MyProjects\Web\Jason-French-Learning-Web\a1.html'
    html = read_file(path)

    # =========================================================================
    # UNIT 15: PREPOSITIONS & LOCATIONS
    # =========================================================================

    marker_15_end = '<h2 id="h-unit-16-asking-questions">'
    new_15 = """
<p><strong>Quebec-Specific Location Vocabulary (🍁):</strong></p>
<p>Quebec has many unique place-related terms that differ from France French. Knowing these is essential for daily life in Quebec:</p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th><th>Description</th></tr></thead>
<tbody>
<tr><td>le dépanneur</td><td>l'épicerie de quartier</td><td>convenience store</td><td>Found on every corner in Quebec! Sells beer, snacks, basics.</td></tr>
<tr><td>le CLSC</td><td>le centre de santé</td><td>community health clinic</td><td>"Centre local de services communautaires" – first stop for healthcare.</td></tr>
<tr><td>la SAQ</td><td>le magasin de vin</td><td>liquor store</td><td>"Société des alcools du Québec" – government-run, only place to buy wine/spirits.</td></tr>
<tr><td>le cégep</td><td>le lycée/l'université</td><td>college (pre-university)</td><td>"Collège d'enseignement général et professionnel" – unique to Quebec education system.</td></tr>
<tr><td>la polyvalente</td><td>le lycée</td><td>high school</td><td>Quebec high school (secondary 1-5, ages 12-17).</td></tr>
<tr><td>le centre d'achats</td><td>le centre commercial</td><td>shopping centre/mall</td><td>Quebec prefers "centre d'achats" over "centre commercial."</td></tr>
<tr><td>la caisse populaire</td><td>la banque coopérative</td><td>credit union (Desjardins)</td><td>A cooperative financial institution, very popular in QC. "Caisse Desjardins."</td></tr>
<tr><td>le parc provincial</td><td>le parc régional</td><td>provincial park</td><td>Quebec has many beautiful "parcs nationaux du Québec" (not federal parks).</td></tr>
<tr><td>le stationnement</td><td>le parking</td><td>parking lot</td><td>"Où est le stationnement?" (Where's the parking lot?)</td></tr>
<tr><td>la buanderie</td><td>la laverie</td><td>laundromat</td><td>"Je vais faire mon lavage à la buanderie." (I'm going to do laundry at the laundromat.)</td></tr>
<tr><td>le métro</td><td>le métro</td><td>subway/metro</td><td>Montreal has a 4-line metro system.</td></tr>
<tr><td>l'autoroute</td><td>l'autoroute</td><td>highway</td><td>"L'autoroute 20" / "l'autoroute Transcanadienne"</td></tr>
<tr><td>le rang</td><td>la route de campagne</td><td>rural road/concession</td><td>"Mon chalet est sur le rang Saint-Joseph." (My cottage is on Saint-Joseph range road.)</td></tr>
</tbody>
</table>
<p><strong>Montreal Neighbourhoods – Essential Geography:</strong></p>
<p>If you live in or visit Montreal, knowing the main neighbourhoods is crucial:</p>
<table>
<thead><tr><th>Neighbourhood</th><th>Pronunciation</th><th>Known For</th></tr></thead>
<tbody>
<tr><td>Le Plateau Mont-Royal</td><td>"le Plah-toe"</td><td>Trendy, artistic, famous outdoor staircases, restaurants</td></tr>
<tr><td>Le Vieux-Montréal</td><td>"le Vyeuh Mon-ray-al"</td><td>Historic old port, cobblestone streets, tourist area</td></tr>
<tr><td>Rosemont–La Petite-Patrie</td><td>"Roze-mon"</td><td>Family-friendly, Marché Jean-Talon, Little Italy</td></tr>
<tr><td>Hochelaga-Maisonneuve</td><td>"Osh-lah-gah"</td><td>Working class, up-and-coming, Olympic Stadium</td></tr>
<tr><td>Outremont</td><td>"Oo-truh-mon"</td><td>Upscale, francophone, Université de Montréal nearby</td></tr>
<tr><td>Verdun</td><td>"Vair-duhn"</td><td>Increasingly popular, riverfront, affordable</td></tr>
<tr><td>NDG (Notre-Dame-de-Grâce)</td><td>"en-dee-zhee"</td><td>Anglophone neighbourhood, Concordia area</td></tr>
<tr><td>Côte-des-Neiges</td><td>"Coat-day-nezh"</td><td>Very diverse, many immigrants, Université de Montréal</td></tr>
</tbody>
</table>
<p><strong>Quebec Direction Vocabulary Extensions:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Tournez à droite au coin</td><td>Turn right at the corner</td><td>"Tournez à droite au prochain coin de rue."</td></tr>
<tr><td>C'est au bout de la rue</td><td>It's at the end of the street</td><td>"Le dépanneur est au bout de la rue, à gauche."</td></tr>
<tr><td>Montez la côte</td><td>Go up the hill</td><td>"Montez la côte et c'est à gauche." (Common in Quebec City!)</td></tr>
<tr><td>Descendez la côte</td><td>Go down the hill</td><td>"Descendez la côte vers le fleuve."</td></tr>
<tr><td>C'est en face de</td><td>It's across from</td><td>"Le restaurant est en face de la pharmacie."</td></tr>
<tr><td>Passez le pont</td><td>Cross the bridge</td><td>"Passez le pont Jacques-Cartier pour aller à Longueuil."</td></tr>
<tr><td>C'est dans le sous-sol</td><td>It's in the basement</td><td>"Le stationnement est dans le sous-sol."</td></tr>
<tr><td>À l'étage</td><td>Upstairs / on the floor</td><td>"Les bureaux sont au troisième étage."</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Getting Lost in Montreal's Underground City:</strong></p>
<p><em>Vous cherchez un magasin dans le Montréal souterrain.</em></p>
<p>"Excusez-moi, je cherche la pharmacie. C'est par où?"<br>"La pharmacie? Vous êtes au niveau de la Place Ville-Marie. Marchez tout droit dans le corridor jusqu'au prochain embranchement."<br>"Okay, pis après?"<br>"Tournez à gauche, passez devant les restaurants, et la pharmacie est juste après, sur votre droite."<br>"C'est loin d'ici?"<br>"Non, c'est à environ cinq minutes de marche. Le Montréal souterrain est immense, mais c'est bien indiqué."<br>"Merci! C'est incroyable, toute cette ville en dessous de la ville!"<br>"Oui, c'est le plus grand réseau souterrain au monde! Trente-deux kilomètres de tunnels. En hiver, c'est ben pratique!"</p>
<p><em>(You're looking for a store in Montreal's underground city. "Excuse me, I'm looking for the pharmacy. Which way is it?" "The pharmacy? You're at the Place Ville-Marie level. Walk straight in the corridor to the next junction." "Okay, then what?" "Turn left, pass the restaurants, and the pharmacy is just after, on your right." "Is it far from here?" "No, it's about a five-minute walk. The underground city is huge, but it's well signed." "Thanks! It's incredible, this whole city underneath the city!" "Yes, it's the largest underground network in the world! Thirty-two kilometres of tunnels. In winter, it's really convenient!")</em></p>

"""
    html = insert_before(html, marker_15_end, new_15)

    # =========================================================================
    # UNIT 16: ASKING QUESTIONS
    # =========================================================================

    marker_16_end = '<h1 id="h-part-v-important-structures">'
    new_16 = """
<p><strong>Quebec Question Patterns – How Quebecers Really Ask Questions (🍁):</strong></p>
<p>Quebec French has some distinctive question-asking patterns that differ from standard French:</p>
<table>
<thead><tr><th>Standard French</th><th>Quebec French</th><th>English</th><th>Type</th></tr></thead>
<tbody>
<tr><td>Est-ce que tu viens?</td><td>Tu viens-tu?</td><td>Are you coming?</td><td>The "-tu" particle (most QC!)</td></tr>
<tr><td>Qu'est-ce que tu fais?</td><td>Tu fais quoi? / Qu'oss tu fais?</td><td>What are you doing?</td><td>Word order change</td></tr>
<tr><td>Qu'est-ce qu'il y a?</td><td>Kessé qu'y a? / Qu'ossa donne?</td><td>What's going on? / What's the point?</td><td>Contracted forms</td></tr>
<tr><td>Où est-ce que tu vas?</td><td>Tu vas où? / Oùsque tu vas?</td><td>Where are you going?</td><td>"Oùsque" = informal "où"</td></tr>
<tr><td>Comment est-ce que tu fais?</td><td>Comment tu fais?</td><td>How do you do it?</td><td>Drop "est-ce que"</td></tr>
<tr><td>Pourquoi est-ce que tu pleures?</td><td>Pourquoi tu brailles?</td><td>Why are you crying?</td><td>"Brailler" = QC for "pleurer"</td></tr>
<tr><td>Combien est-ce que ça coûte?</td><td>Combien ça coûte? / C'est combien?</td><td>How much does it cost?</td><td>Simplified form</td></tr>
<tr><td>Qu'est-ce que tu veux?</td><td>Tu veux quoi?</td><td>What do you want?</td><td>Question word at end</td></tr>
</tbody>
</table>
<p><strong>The Quebec "-tu" Question Particle – Comprehensive Guide (🍁):</strong></p>
<p>The interrogative "-tu" is the most distinctive grammatical feature of Quebec French. It can be added after ANY conjugated verb to make a yes/no question:</p>
<table>
<thead><tr><th>Statement</th><th>Question with -tu</th><th>English</th></tr></thead>
<tbody>
<tr><td>Tu travailles.</td><td>Tu travailles-tu?</td><td>Are you working?</td></tr>
<tr><td>Il fait beau.</td><td>Y fait-tu beau?</td><td>Is it nice out?</td></tr>
<tr><td>C'est bon.</td><td>C'est-tu bon?</td><td>Is it good?</td></tr>
<tr><td>On peut y aller.</td><td>On peut-tu y aller?</td><td>Can we go?</td></tr>
<tr><td>Tu veux venir.</td><td>Tu veux-tu venir?</td><td>Do you want to come?</td></tr>
<tr><td>Il y a du café.</td><td>Y'a-tu du café?</td><td>Is there any coffee?</td></tr>
<tr><td>On va au cinéma.</td><td>On va-tu au cinéma?</td><td>Are we going to the movies?</td></tr>
<tr><td>C'est correct.</td><td>C'est-tu correct?</td><td>Is it okay?</td></tr>
</tbody>
</table>
<p><strong>Important:</strong> This "-tu" is NOT the pronoun "tu" (you). It's a question particle that comes from Old French "ti" and is unique to Laurentian French (Quebec, Ontario, New Brunswick). Never use it in formal writing!</p>
<p><strong>Common Quebec Question Expressions:</strong></p>
<table>
<thead><tr><th>Quebec Question</th><th>Standard French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Coudonc, qu'est-ce qui se passe?</td><td>Mais enfin, qu'est-ce qui se passe?</td><td>So, what's going on?</td></tr>
<tr><td>Comment ça se fait?</td><td>Comment cela se fait-il?</td><td>How come? / How's that possible?</td></tr>
<tr><td>C'est qui ça?</td><td>Qui est-ce?</td><td>Who is that?</td></tr>
<tr><td>Ça te tente-tu?</td><td>Ça te dit?</td><td>Do you feel like it?</td></tr>
<tr><td>T'as-tu besoin d'aide?</td><td>As-tu besoin d'aide?</td><td>Do you need help?</td></tr>
<tr><td>C'est quoi ton nom?</td><td>Quel est ton nom?</td><td>What's your name?</td></tr>
<tr><td>T'habites où?</td><td>Où habites-tu?</td><td>Where do you live?</td></tr>
<tr><td>Tu fais quoi dans la vie?</td><td>Qu'est-ce que tu fais comme travail?</td><td>What do you do for a living?</td></tr>
</tbody>
</table>
<p><strong>Responding to Questions – Quebec Style:</strong></p>
<table>
<thead><tr><th>Quebec Response</th><th>Standard French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Ben oui!</td><td>Bien sûr!</td><td>Of course! / Yeah!</td></tr>
<tr><td>Pantoute!</td><td>Pas du tout!</td><td>Not at all!</td></tr>
<tr><td>Ché pas</td><td>Je ne sais pas</td><td>I dunno</td></tr>
<tr><td>Mettons...</td><td>Disons...</td><td>Let's say... / I guess...</td></tr>
<tr><td>C'est ça!</td><td>C'est exact!</td><td>That's right!</td></tr>
<tr><td>Mets-en!</td><td>Absolument!</td><td>You bet! / Totally!</td></tr>
<tr><td>En effet</td><td>En effet</td><td>Indeed (same, more formal)</td></tr>
<tr><td>Pas vraiment</td><td>Pas vraiment</td><td>Not really</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Asking Questions at Société de l'assurance automobile du Québec (SAAQ):</strong></p>
<p><em>Vous êtes à la SAAQ pour obtenir votre permis de conduire québécois.</em></p>
<p>"Bonjour! C'est pour quoi?"<br>"Je voudrais obtenir un permis de conduire québécois. J'ai un permis de mon pays d'origine."<br>"D'accord. De quel pays venez-vous?"<br>"Du Brésil."<br>"Est-ce que le Brésil a une entente avec le Québec pour l'échange de permis?"<br>"Je ne suis pas sûr. Comment est-ce que je peux vérifier?"<br>"On va vérifier tout de suite. Quel type de permis avez-vous?"<br>"Un permis pour automobile."<br>"Combien de temps avez-vous conduit dans votre pays?"<br>"J'ai conduit pendant huit ans."<br>"D'accord. Malheureusement, y'a pas d'entente avec le Brésil, donc vous devez passer l'examen théorique et pratique."<br>"C'est-tu possible de passer l'examen en français?"<br>"Ben oui! En français ou en anglais, c'est votre choix."<br>"Je vais le faire en français! C'est bon pour ma pratique!"</p>

"""
    html = insert_before(html, marker_16_end, new_16)

    # =========================================================================
    # UNIT 17: NEGATION
    # =========================================================================

    marker_17_end = '<h2 id="h-unit-18-the-pass-compos-compound-past">'
    new_17 = """
<p><strong>Negation in Quebec Spoken French – The Dropped "Ne" (🍁):</strong></p>
<p>The most important thing to know about negation in Quebec French is that <strong>the "ne" is almost always dropped in spoken language</strong>. This is not "bad French" – it's standard spoken Quebec French:</p>
<table>
<thead><tr><th>Written/Formal French</th><th>Quebec Spoken French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Je ne sais pas.</td><td>Je sais pas. / Ché pas.</td><td>I don't know.</td></tr>
<tr><td>Je ne comprends pas.</td><td>J'comprends pas.</td><td>I don't understand.</td></tr>
<tr><td>Il n'y a pas de...</td><td>Y'a pas de...</td><td>There isn't any...</td></tr>
<tr><td>Ce n'est pas vrai.</td><td>C'est pas vrai.</td><td>It's not true.</td></tr>
<tr><td>Nous ne voulons rien.</td><td>On veut rien.</td><td>We don't want anything.</td></tr>
<tr><td>Je n'ai jamais vu ça.</td><td>J'ai jamais vu ça.</td><td>I've never seen that.</td></tr>
<tr><td>Il ne mange plus.</td><td>Y mange plus.</td><td>He doesn't eat anymore.</td></tr>
<tr><td>Elle ne connaît personne.</td><td>A connaît personne.</td><td>She doesn't know anyone.</td></tr>
</tbody>
</table>
<p><strong>Quebec-Specific Negative Expressions (🍁):</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Standard French</th><th>English</th><th>Usage</th></tr></thead>
<tbody>
<tr><td>Pantoute!</td><td>Pas du tout!</td><td>Not at all!</td><td>"T'es-tu fâché? – Pantoute!" (Are you angry? – Not at all!)</td></tr>
<tr><td>Même pas!</td><td>Même pas!</td><td>Not even!</td><td>"Y a même pas dit merci!" (He didn't even say thank you!)</td></tr>
<tr><td>Pas une miette!</td><td>Pas du tout!</td><td>Not one bit!</td><td>"J'ai pas peur, pas une miette!" (I'm not scared, not one bit!)</td></tr>
<tr><td>Plus pantoute!</td><td>Plus du tout!</td><td>Not at all anymore!</td><td>"J'ai plus pantoute envie d'y aller." (I don't feel like going there at all anymore.)</td></tr>
<tr><td>Jamais de la vie!</td><td>Jamais de la vie!</td><td>Never in my life!</td><td>"Tu ferais ça? – Jamais de la vie!" (Would you do that? – Never!)</td></tr>
</tbody>
</table>
<p><strong>Negation with "Là" – A Quebec Filler (🍁):</strong></p>
<p>Quebecers frequently add "là" (there) at the end of sentences for emphasis, especially with negatives:</p>
<ul>
<li><strong>"Je sais pas, là."</strong> = I really don't know. (the "là" adds emphasis or mild frustration)</li>
<li><strong>"C'est pas correct, là."</strong> = This isn't right, you know.</li>
<li><strong>"Fais pas ça, là!"</strong> = Don't do that, come on!</li>
<li><strong>"Y'a rien qui marche, là."</strong> = Nothing works, seriously.</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – Complaining About the Weather (A Quebec Classic!):</strong></p>
<p><em>Deux Québécois se plaignent de la météo.</em></p>
<p>"Ayoye! Y fait pas beau pantoute aujourd'hui!"<br>"Met-en! Ça fait trois jours qu'y arrête pas de pleuvoir."<br>"Pis y'a même pas de soleil en vue. J'ai vérifié la météo tantôt."<br>"Moi, j'en peux plus, là. Je veux plus voir de pluie!"<br>"Oh, dis pas ça. Au Québec, on sait jamais. Demain y peut faire trente!"<br>"C'est vrai. Mais là, le terrain est pas drainé pantoute pis mon sous-sol a commencé à couler."<br>"Ah non! T'as-tu appelé un plombier?"<br>"Oui, mais y peut pas venir avant jeudi. Y'a personne de disponible avant ça."<br>"C'est pas l'fun, ça. Ça m'est jamais arrivé, mais je sais que c'est pas rare au Québec."<br>"En tout cas, je m'en remettrai. Y'a rien là! C'est la vie au Québec!"</p>
<p><em>(Two Quebecers complaining about the weather. "Ow! The weather isn't nice at all today!" "You can say that again! It hasn't stopped raining for three days." "And there isn't even any sun in sight. I checked the weather earlier." "I can't take it anymore. I don't want to see any more rain!" "Oh, don't say that. In Quebec, you never know. Tomorrow it could be thirty!" "True. But right now, the ground isn't drained at all and my basement started leaking." "Oh no! Did you call a plumber?" "Yes, but he can't come before Thursday. Nobody's available before that." "That's no fun. It's never happened to me, but I know it's not rare in Quebec." "Anyway, I'll get over it. No biggie! That's life in Quebec!")</em></p>

"""
    html = insert_before(html, marker_17_end, new_17)

    # =========================================================================
    # UNIT 18: PASSÉ COMPOSÉ
    # =========================================================================

    marker_18_end = '<h2 id="h-unit-19-near-future-aller-infinitive">'
    new_18 = """
<p><strong>Passé Composé in Quebec Spoken French (🍁):</strong></p>
<p>While the passé composé rules are the same everywhere, Quebec spoken French has some patterns to be aware of:</p>
<table>
<thead><tr><th>Feature</th><th>Standard French</th><th>Quebec Spoken French</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Subject pronouns</td><td>Full pronouns used</td><td>Contracted pronouns</td><td>"J'ai fini" → "Ga fini" / "Y'a fini" / "A'a fini"</td></tr>
<tr><td>Negation</td><td>"ne...pas" around auxiliary</td><td>"pas" only, "ne" dropped</td><td>"J'ai pas compris" (I didn't understand)</td></tr>
<tr><td>Questions</td><td>"Est-ce que tu as..."</td><td>"T'as-tu...?"</td><td>"T'as-tu mangé?" (Did you eat?)</td></tr>
<tr><td>"On" instead of "nous"</td><td>"Nous sommes allés"</td><td>"On est allés"</td><td>"On est allés à Québec." (We went to Quebec City.)</td></tr>
</tbody>
</table>
<p><strong>Common Quebec Activities in the Past Tense:</strong></p>
<table>
<thead><tr><th>French (Passé Composé)</th><th>English</th><th>Context</th></tr></thead>
<tbody>
<tr><td>J'ai pelleté toute la matinée.</td><td>I shoveled all morning.</td><td>Winter activity</td></tr>
<tr><td>On est allés aux glissades d'eau.</td><td>We went to the water slides.</td><td>Summer fun</td></tr>
<tr><td>J'ai fait du ski à Tremblant.</td><td>I went skiing at Tremblant.</td><td>Winter sports</td></tr>
<tr><td>On a visité le Vieux-Québec.</td><td>We visited Old Quebec.</td><td>Tourism</td></tr>
<tr><td>J'ai vu un show de Céline Dion!</td><td>I saw a Celine Dion show!</td><td>Entertainment</td></tr>
<tr><td>On a fait une cabane à sucre.</td><td>We went to a sugar shack.</td><td>Spring tradition</td></tr>
<tr><td>J'ai passé l'Halloween.</td><td>I did trick-or-treating.</td><td>Halloween (QC says "passer l'Halloween")</td></tr>
<tr><td>On a déménagé le premier juillet.</td><td>We moved on July 1st.</td><td>Quebec moving day!</td></tr>
<tr><td>J'ai pris le traversier pour Lévis.</td><td>I took the ferry to Lévis.</td><td>Quebec City area</td></tr>
<tr><td>On a cueilli des bleuets au Lac-Saint-Jean.</td><td>We picked blueberries in Lac-Saint-Jean.</td><td>Summer activity</td></tr>
</tbody>
</table>
<p><strong>Using the Passé Composé to Talk About Quebec History:</strong></p>
<p>Here's some basic Quebec history using the passé composé – great for practice and cultural knowledge:</p>
<ul>
<li>"Jacques Cartier a exploré le fleuve Saint-Laurent en 1534." (Jacques Cartier explored the St. Lawrence River in 1534.)</li>
<li>"Samuel de Champlain a fondé Québec en 1608." (Samuel de Champlain founded Quebec City in 1608.)</li>
<li>"Les Français ont colonisé la Nouvelle-France pendant plus de 150 ans." (The French colonized New France for over 150 years.)</li>
<li>"Les Anglais ont conquis la Nouvelle-France en 1760." (The English conquered New France in 1760.)</li>
<li>"Le Québec a eu la Révolution tranquille dans les années 1960." (Quebec had the Quiet Revolution in the 1960s.)</li>
<li>"Le Québec a voté deux fois dans des référendums sur la souveraineté (1980 et 1995)." (Quebec voted twice in sovereignty referendums.)</li>
<li>"Le métro de Montréal a ouvert en 1966." (The Montreal metro opened in 1966.)</li>
<li>"Montréal a accueilli les Jeux olympiques en 1976." (Montreal hosted the Olympics in 1976.)</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – Telling Your Friends About Your Trip to Quebec City:</strong></p>
<p><em>Vous racontez votre voyage à Québec à vos amis.</em></p>
<p>"On a passé une fin de semaine incroyable à Québec!"<br>"Ah oui? Qu'est-ce que vous avez fait?"<br>"Vendredi soir, on est arrivés à l'hôtel dans le Vieux-Québec. On a marché sur le Château Frontenac et on a soupé dans un restaurant sur la rue Saint-Jean."<br>"C'était-tu bon?"<br>"Écœurant! On a mangé de la poutine au canard confit. J'ai jamais mangé quelque chose d'aussi bon!"<br>"Pis samedi?"<br>"On a visité le Musée de la civilisation, on a fait les boutiques du Quartier Petit Champlain, pis on a pris le traversier pour aller à Lévis."<br>"Le traversier, c'est-tu beau la vue?"<br>"Mets-en! On a vu tout le panorama de Québec depuis le fleuve. J'ai pris plein de photos."<br>"Pis dimanche?"<br>"On est allés aux chutes Montmorency. On a même monté la téléphérique. Après, on est rentrés à Montréal, fatigués mais contents!"</p>

"""
    html = insert_before(html, marker_18_end, new_18)

    # =========================================================================
    # UNIT 19: NEAR FUTURE
    # =========================================================================

    marker_19_end = '<h2 id="h-unit-20-hobbies-preferences-abilities">'
    new_19 = """
<p><strong>Using the Near Future for Quebec Life Planning (🍁):</strong></p>
<p>The near future tense (aller + infinitive) is extremely useful for talking about plans in Quebec. Here are typical conversations:</p>
<p><strong>Quebec Seasonal Activities – Future Plans:</strong></p>
<table>
<thead><tr><th>Season</th><th>Near Future Plan</th><th>English</th></tr></thead>
<tbody>
<tr><td>Winter</td><td>On va aller skier à Mont-Tremblant.</td><td>We're going to go skiing at Mont-Tremblant.</td></tr>
<tr><td>Winter</td><td>Je vais faire du patin sur le canal.</td><td>I'm going to go skating on the canal.</td></tr>
<tr><td>Winter</td><td>On va aller au Carnaval de Québec.</td><td>We're going to go to the Quebec Carnival.</td></tr>
<tr><td>Spring</td><td>On va aller à la cabane à sucre.</td><td>We're going to go to the sugar shack.</td></tr>
<tr><td>Spring</td><td>Je vais commencer mon jardin.</td><td>I'm going to start my garden.</td></tr>
<tr><td>Summer</td><td>On va aller camper en Gaspésie.</td><td>We're going to go camping in the Gaspé.</td></tr>
<tr><td>Summer</td><td>Je vais aller au Festival de Jazz.</td><td>I'm going to go to the Jazz Festival.</td></tr>
<tr><td>Summer</td><td>On va se baigner au lac.</td><td>We're going to go swimming at the lake.</td></tr>
<tr><td>Fall</td><td>On va aller aux pommes.</td><td>We're going to go apple picking.</td></tr>
<tr><td>Fall</td><td>Je vais passer l'Halloween.</td><td>I'm going to go trick-or-treating.</td></tr>
</tbody>
</table>
<p><strong>Quebec Cultural Activities – Making Plans:</strong></p>
<ul>
<li>"On va aller au Festival Juste pour rire cet été." (We're going to go to the Just for Laughs Festival this summer.)</li>
<li>"Je vais m'inscrire à un cours de francisation." (I'm going to sign up for a French language course.)</li>
<li>"On va aller voir les Canadiens jouer au Centre Bell." (We're going to go see the Canadiens play at the Bell Centre.)</li>
<li>"Je vais déménager le premier juillet." (I'm going to move on July 1st. – A Quebec tradition!)</li>
<li>"On va aller cueillir des bleuets au Lac-Saint-Jean cet été." (We're going to go pick blueberries in Lac-Saint-Jean this summer.)</li>
<li>"Je vais commencer à prendre le métro pour aller travailler." (I'm going to start taking the metro to go to work.)</li>
</ul>
<p><strong>Near Future with Quebec Expressions:</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>English</th><th>Context</th></tr></thead>
<tbody>
<tr><td>Ça va être l'fun!</td><td>It's going to be fun!</td><td>Expressing enthusiasm about plans</td></tr>
<tr><td>Ça va être plate.</td><td>It's going to be boring.</td><td>Dreading something</td></tr>
<tr><td>Ça va ben aller!</td><td>It's going to be okay!</td><td>Encouragement (became a QC motto during COVID!)</td></tr>
<tr><td>On va s'en sortir.</td><td>We're going to get through it.</td><td>Resilience</td></tr>
<tr><td>Je vais m'arranger.</td><td>I'll manage / figure it out.</td><td>Self-reliance</td></tr>
</tbody>
</table>
<p><strong>Note:</strong> "Ça va bien aller" (It's going to be alright) became a famous Quebec motto during the COVID-19 pandemic, with rainbow drawings in windows across the province.</p>
<p><strong>🇫🇷 Real-Life Scene – Planning a Quebec Road Trip:</strong></p>
<p><em>Vous planifiez un voyage en auto à travers le Québec.</em></p>
<p>"Bon, on va partir de Montréal vendredi matin de bonne heure."<br>"On va prendre l'autoroute 20 jusqu'à Rivière-du-Loup?"<br>"Oui! Ça va nous prendre environ quatre heures. On va s'arrêter à Drummondville pour dîner."<br>"Qu'est-ce qu'on va faire à Rivière-du-Loup?"<br>"On va prendre le traversier pour aller aux Trois-Pistoles. Pis on va continuer vers Rimouski."<br>"Combien de temps on va rester?"<br>"On va passer deux nuits à Rimouski. On va visiter le Parc national du Bic."<br>"Ça va être magnifique! Pis après?"<br>"Après, on va continuer vers Percé. On va voir le Rocher Percé et l'Île Bonaventure."<br>"J'ai tellement hâte! Ça va être le plus beau voyage de notre vie!"<br>"Ben oui! La Gaspésie, c'est la plus belle région du Québec. Tu vas capoter!"</p>
<p><em>(You're planning a road trip across Quebec. "Okay, we're going to leave Montreal early Friday morning." "We're going to take Highway 20 to Rivière-du-Loup?" "Yes! It'll take us about four hours. We'll stop in Drummondville for lunch." "What are we going to do in Rivière-du-Loup?" "We're going to take the ferry to Trois-Pistoles. Then continue toward Rimouski." "How long are we going to stay?" "We'll spend two nights in Rimouski. We'll visit Bic National Park." "That's going to be beautiful! And after?" "Then we'll continue to Percé. We'll see Percé Rock and Bonaventure Island." "I'm so excited! It's going to be the best trip of our lives!" "Of course! The Gaspé is the most beautiful region of Quebec. You're going to be blown away!")</em></p>

"""
    html = insert_before(html, marker_19_end, new_19)

    # =========================================================================
    # UNIT 20: HOBBIES & PREFERENCES
    # =========================================================================

    marker_20_end = '<h1 id="h-conclusion-study-tips">'
    new_20 = """
<p><strong>Quebec Hobbies and Cultural Activities (🍁):</strong></p>
<p>Quebec has a rich cultural life with many activities unique to the province:</p>
<table>
<thead><tr><th>Category</th><th>Activity (French)</th><th>English</th><th>Quebec Context</th></tr></thead>
<tbody>
<tr><td>Winter Sports</td><td>le hockey sur glace</td><td>ice hockey</td><td>THE national sport. "Les Canadiens de Montréal" (the Habs!) – everyone follows them!</td></tr>
<tr><td>Winter Sports</td><td>le ski alpin</td><td>downhill skiing</td><td>Mont-Tremblant, Mont-Sainte-Anne, Le Massif – world-class ski resorts</td></tr>
<tr><td>Winter Sports</td><td>le ski de fond</td><td>cross-country skiing</td><td>Popular in parks and nature reserves across Quebec</td></tr>
<tr><td>Winter Sports</td><td>la motoneige</td><td>snowmobiling</td><td>Quebec has the largest network of snowmobile trails in the world!</td></tr>
<tr><td>Winter Sports</td><td>la raquette</td><td>snowshoeing</td><td>Traditional activity, great exercise in winter forests</td></tr>
<tr><td>Winter Sports</td><td>la glissade</td><td>tobogganing/sledding</td><td>Families go "glisser" at parks with hills</td></tr>
<tr><td>Summer</td><td>le canot / le kayak</td><td>canoeing / kayaking</td><td>Thousands of lakes and rivers to explore</td></tr>
<tr><td>Summer</td><td>la pêche</td><td>fishing</td><td>"Aller à la pêche" – hugely popular, especially in rural Quebec</td></tr>
<tr><td>Summer</td><td>le vélo</td><td>cycling</td><td>"La Route Verte" – 5,300 km cycling network across Quebec!</td></tr>
<tr><td>Summer</td><td>le camping</td><td>camping</td><td>SEPAQ parks are very popular for camping: Tremblant, Jacques-Cartier, etc.</td></tr>
<tr><td>Year-round</td><td>les quilles</td><td>bowling</td><td>QC uses "quilles" not "bowling"</td></tr>
<tr><td>Cultural</td><td>aller aux festivals</td><td>going to festivals</td><td>Montreal has more festivals per capita than any city in North America!</td></tr>
<tr><td>Cultural</td><td>écouter de la musique québécoise</td><td>listening to Quebec music</td><td>Rich music scene: Les Cowboys Fringants, Jean Leloup, Cœur de Pirate, etc.</td></tr>
</tbody>
</table>
<p><strong>Quebec Music – Artists Every Learner Should Know:</strong></p>
<table>
<thead><tr><th>Artist/Band</th><th>Genre</th><th>Why They Matter</th></tr></thead>
<tbody>
<tr><td>Céline Dion</td><td>Pop</td><td>The most famous Quebecer in the world. From Charlemagne, QC.</td></tr>
<tr><td>Les Cowboys Fringants</td><td>Folk-rock</td><td>Hugely popular band singing about Quebec life and identity.</td></tr>
<tr><td>Jean Leloup</td><td>Rock/Pop</td><td>Iconic Quebec singer-songwriter.</td></tr>
<tr><td>Cœur de Pirate</td><td>Pop/Indie</td><td>Béatrice Martin – bilingual artist from Montreal.</td></tr>
<tr><td>Harmonium</td><td>Progressive rock</td><td>Legendary 70s Quebec band. Their music is timeless.</td></tr>
<tr><td>Mes Aïeux</td><td>Folk</td><td>Traditional Quebec folk with modern twist. Great for learning QC culture.</td></tr>
<tr><td>Ariane Moffatt</td><td>Pop/Electronic</td><td>Award-winning Quebec artist.</td></tr>
<tr><td>Félix Leclerc</td><td>Chansonnier</td><td>Father of Quebec chanson. Essential cultural figure.</td></tr>
<tr><td>Gilles Vigneault</td><td>Chansonnier</td><td>"Mon pays, ce n'est pas un pays, c'est l'hiver" – iconic Quebec song.</td></tr>
<tr><td>Robert Charlebois</td><td>Rock/Pop</td><td>Pioneer of Quebec rock music in the 1960s-70s.</td></tr>
</tbody>
</table>
<p><strong>Quebec TV Shows for Language Learners:</strong></p>
<ul>
<li><strong>"Tout le monde en parle"</strong> – Quebec's most popular talk show. Great for hearing natural Quebec French.</li>
<li><strong>"District 31"</strong> – Popular police drama. Everyday Quebec French.</li>
<li><strong>"Les Parent"</strong> – Family sitcom. Perfect for learning family vocabulary.</li>
<li><strong>"La Petite Vie"</strong> – Classic Quebec comedy. The most-watched show in Quebec history!</li>
<li><strong>"Unité 9"</strong> – Drama series. More complex vocabulary.</li>
<li><strong>"Bon Cop, Bad Cop"</strong> – Movie. Bilingual comedy about Quebec-Ontario culture clash.</li>
<li><strong>"C.R.A.Z.Y."</strong> – Movie by Jean-Marc Vallée. Growing up in 1960s-70s Quebec.</li>
</ul>
<p><strong>The "Jouer" Patterns – Important for Hobbies:</strong></p>
<table>
<thead><tr><th>Pattern</th><th>Usage</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Jouer <strong>au</strong> + sport</td><td>For team/ball sports</td><td>"Jouer au hockey" / "Jouer au soccer" / "Jouer au football"</td></tr>
<tr><td>Jouer <strong>de</strong> + instrument</td><td>For musical instruments</td><td>"Jouer de la guitare" / "Jouer du piano" / "Jouer du violon"</td></tr>
<tr><td>Jouer <strong>à</strong> + game</td><td>For games</td><td>"Jouer aux cartes" / "Jouer aux jeux vidéo" / "Jouer aux quilles"</td></tr>
<tr><td>Faire <strong>du/de la</strong> + activity</td><td>For general activities</td><td>"Faire du ski" / "Faire de la natation" / "Faire du vélo"</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – At a Quebec Hockey Game:</strong></p>
<p><em>Vous assistez à un match de hockey des Canadiens de Montréal au Centre Bell.</em></p>
<p>"On est au Centre Bell! C'est mon premier match des Canadiens!"<br>"Tu vas voir, l'ambiance est malade! Vingt mille personnes qui crient pour les Habs!"<br>"C'est quoi, les 'Habs'?"<br>"C'est le surnom des Canadiens. Ça vient de 'Les Habitants'. Tout le monde dit 'Go Habs Go!'"<br>"Go Habs Go! C'est qui le numéro trente-et-un?"<br>"C'est le gardien de but. Y est vraiment bon!"<br>"Wow, c'est rapide! La rondelle va tellement vite!"<br>"La rondelle, oui! En anglais, c'est 'the puck'. Pis regarde, y'a une mise en jeu!"<br>"C'est quoi une mise en jeu?"<br>"C'est quand l'arbitre laisse tomber la rondelle entre deux joueurs. En anglais, c'est 'face-off'."<br>[L'équipe marque un but]<br>"BUUUUUT! Les Canadiens ont compté!"<br>"Au Québec, on dit 'compter un but'. En France, y disent 'marquer un but'. Mais ici, c'est 'compter'!"<br>"Compter un but! J'adore! Le hockey, c'est l'fun en titi!"</p>
<p><em>(You're at a Montreal Canadiens hockey game at the Bell Centre. "We're at the Bell Centre! It's my first Canadiens game!" "You'll see, the atmosphere is insane! Twenty thousand people cheering for the Habs!" "What are 'the Habs'?" "It's the Canadiens' nickname. It comes from 'Les Habitants.' Everyone says 'Go Habs Go!'" ...The team scores a goal... "GOOOAL! The Canadiens scored!" "In Quebec, we say 'compter un but' [to count a goal]. In France, they say 'marquer un but' [to score a goal]. But here, it's 'compter'!" "Score a goal! I love it! Hockey is so much fun!")</em></p>

"""
    html = insert_before(html, marker_20_end, new_20)

    # =========================================================================
    # CONCLUSION: Expand study tips and resources
    # =========================================================================

    marker_conclusion = '<h3 id="h-final-notes">'
    new_conclusion = """
<p><strong>Quebec French Learning Resources – Comprehensive Guide:</strong></p>
<p><strong>Television and Streaming:</strong></p>
<ul>
<li><strong>Radio-Canada (ICI Tou.tv)</strong> – Quebec's public broadcaster. Free streaming of many shows. Start with news (slower speech) and work up to dramas.</li>
<li><strong>Télé-Québec</strong> – Educational and cultural programming.</li>
<li><strong>Club illico</strong> – Quebec streaming service with original content.</li>
<li><strong>Crave</strong> – Canadian streaming with many Quebec shows.</li>
<li><strong>Netflix</strong> – Has Quebec films and shows like "Plan B" and "Lupin" (French from France, but good practice).</li>
</ul>
<p><strong>Radio and Podcasts:</strong></p>
<ul>
<li><strong>Radio-Canada Première</strong> – Talk radio, great for listening comprehension.</li>
<li><strong>CHOI Radio X</strong> (Quebec City) – Popular radio station.</li>
<li><strong>"Aujourd'hui l'histoire"</strong> – Podcast about Quebec and Canadian history.</li>
<li><strong>"La soirée est (encore) jeune"</strong> – Fun Quebec culture podcast.</li>
<li><strong>"Raccourcis"</strong> – ICI Radio-Canada podcast for general culture.</li>
</ul>
<p><strong>Quebec Music Playlists:</strong></p>
<ul>
<li>Search "musique québécoise" on Spotify or Apple Music for curated playlists.</li>
<li>Start with: Les Cowboys Fringants, Cœur de Pirate, Jean Leloup, Ariane Moffatt.</li>
<li>Classic chanson: Félix Leclerc, Gilles Vigneault, Robert Charlebois.</li>
</ul>
<p><strong>Free French Courses in Quebec:</strong></p>
<ul>
<li><strong>Francisation courses (MIFI)</strong> – Free French classes for immigrants, full-time or part-time.</li>
<li><strong>Community organizations</strong> – Many offer free conversation groups and French practice.</li>
<li><strong>Libraries (Bibliothèques)</strong> – Offer free French conversation circles and language resources.</li>
<li><strong>Université Laval / UQAM / McGill</strong> – Offer French courses for non-francophones.</li>
</ul>
<p><strong>Quebec Newspapers and Magazines:</strong></p>
<ul>
<li><strong>La Presse (lapresse.ca)</strong> – Major Montreal daily, free online. Great reading practice.</li>
<li><strong>Le Journal de Montréal</strong> – Tabloid-style, easier language, more colloquial.</li>
<li><strong>Le Devoir</strong> – Intellectual newspaper, more complex vocabulary.</li>
<li><strong>L'actualité</strong> – Quebec news magazine, like Canada's equivalent of Time.</li>
<li><strong>Protégez-vous</strong> – Consumer magazine, practical everyday vocabulary.</li>
</ul>
<p><strong>Quebec Cultural Experiences for Language Practice:</strong></p>
<ul>
<li><strong>Visit a cabane à sucre</strong> in March/April – full French immersion in Quebec tradition!</li>
<li><strong>Join a community hockey league</strong> – you'll learn Quebec's most passionate vocabulary!</li>
<li><strong>Attend local festivals</strong> – Saint-Jean-Baptiste (June 24), Carnaval de Québec (February), Festival d'été de Québec (July).</li>
<li><strong>Volunteer</strong> with Quebec organizations – great way to practice and meet people.</li>
<li><strong>Take a cooking class</strong> for Quebec cuisine – learn food vocabulary while making tourtière!</li>
</ul>

"""
    html = insert_before(html, marker_conclusion, new_conclusion)

    write_file(path, html)
    print("Part 4 done: Units 15-20 and Conclusion expanded successfully!")

if __name__ == '__main__':
    main()
