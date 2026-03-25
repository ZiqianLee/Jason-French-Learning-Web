#!/usr/bin/env python3
"""Expand A2 Units 17-20 and Conclusion with more Quebec French content."""

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
    path = r'e:\MyProjects\Web\Jason-French-Learning-Web\a2.html'
    html = read_file(path)

    # =========================================================================
    # UNIT 17: TRAVEL PLANNING
    # =========================================================================

    marker_17_end = '<h2 id="h-unit-18-hotel-airport">'
    new_17 = """
<p><strong>Quebec & Canadian Travel Options (🍁):</strong></p>
<table>
<thead><tr><th>Mode</th><th>Service</th><th>Coverage</th><th>Vocabulary</th></tr></thead>
<tbody>
<tr><td>Train</td><td>VIA Rail</td><td>Montréal–Québec, Montréal–Ottawa, Montréal–Toronto</td><td>"Deux billets aller-retour Montréal-Québec, s'il vous plaît." (Two round-trip tickets.)</td></tr>
<tr><td>Inter-city Bus</td><td>Orléans Express / Limocar / Flixbus</td><td>Quebec's inter-city bus network</td><td>"L'autobus part à quelle heure?" (What time does the bus leave?)</td></tr>
<tr><td>Car</td><td>Road trip</td><td>Quebec's highway network (autoroutes)</td><td>"On prend l'autoroute 20 jusqu'à Québec." (We take Highway 20 to Quebec City.)</td></tr>
<tr><td>Ferry</td><td>Traversier</td><td>Québec–Lévis, Rivière-du-Loup–Saint-Siméon, Îles-de-la-Madeleine</td><td>"Le traversier, ça prend combien de temps?" (How long does the ferry take?)</td></tr>
<tr><td>Airplane</td><td>Air Canada, Porter, WestJet</td><td>Domestic and international flights</td><td>"Mon vol est à dix heures à YUL." (My flight is at ten at YUL.)</td></tr>
<tr><td>Carpooling</td><td>Amigo Express / Poparide</td><td>Between Quebec cities</td><td>"J'ai trouvé un lift sur Poparide." (I found a ride on Poparide.)</td></tr>
</tbody>
</table>
<p><strong>Quebec Road Trip Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>une halte routière</td><td>a rest stop</td><td>"Arrêtons à la prochaine halte routière." (Let's stop at the next rest stop.)</td></tr>
<tr><td>un relais routier</td><td>a truck stop / roadside restaurant</td><td>"On dîne au relais routier." (We'll eat lunch at the truck stop.)</td></tr>
<tr><td>un péage</td><td>a toll</td><td>"Y'a pas de péage sur les autoroutes au Québec!" (No tolls on Quebec highways! – mostly)</td></tr>
<tr><td>une carte routière / un GPS</td><td>a road map / GPS</td><td>"Le GPS dit de tourner à gauche."</td></tr>
<tr><td>le coffre</td><td>the trunk</td><td>"Mets les valises dans le coffre."</td></tr>
<tr><td>faire le plein</td><td>to fill up (gas)</td><td>"Faut faire le plein avant de partir."</td></tr>
<tr><td>un casse-croûte</td><td>a snack bar / chip stand (QC)</td><td>"On arrête au casse-croûte pour une poutine?" (Let's stop at the chip stand for a poutine?)</td></tr>
<tr><td>un belvédère / un point de vue</td><td>a lookout point</td><td>"Y'a un beau belvédère sur la route 132." (There's a nice lookout on Route 132.)</td></tr>
</tbody>
</table>
<p><strong>Top Quebec Road Trip Destinations:</strong></p>
<table>
<thead><tr><th>Destination</th><th>Region</th><th>Known For</th><th>Distance from Montreal</th></tr></thead>
<tbody>
<tr><td>Vieux-Québec</td><td>Capitale-Nationale</td><td>UNESCO World Heritage, Château Frontenac, European charm</td><td>~250 km (2.5 hrs)</td></tr>
<tr><td>Mont-Tremblant</td><td>Laurentides</td><td>Ski resort, nature, village piétonnier</td><td>~130 km (1.5 hrs)</td></tr>
<tr><td>Charlevoix</td><td>Charlevoix</td><td>Stunning landscapes, Baie-Saint-Paul, whale watching</td><td>~400 km (4 hrs)</td></tr>
<tr><td>Percé</td><td>Gaspésie</td><td>Rocher Percé, Île Bonaventure, fous de Bassan</td><td>~950 km (10 hrs)</td></tr>
<tr><td>Tadoussac</td><td>Côte-Nord</td><td>Whale watching capital of Quebec!</td><td>~475 km (5 hrs)</td></tr>
<tr><td>Îles-de-la-Madeleine</td><td>Golfe du Saint-Laurent</td><td>Beaches, red cliffs, seafood, wind</td><td>~1,400 km + ferry</td></tr>
<tr><td>Lac-Saint-Jean</td><td>Saguenay-Lac-Saint-Jean</td><td>Blueberries, swimming, tourtière du Lac</td><td>~500 km (5 hrs)</td></tr>
<tr><td>Parc de la Jacques-Cartier</td><td>Near Quebec City</td><td>Canyons, hiking, canoeing</td><td>~290 km (3 hrs)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Planning a Road Trip on the Route des Baleines:</strong></p>
<p><em>Vous planifiez un voyage sur la route des Baleines (Whale Route) sur la Côte-Nord.</em></p>
<p>"Cet été, on devrait faire la route des Baleines sur la Côte-Nord!"<br>"Ah oui! J'ai toujours voulu voir les baleines à Tadoussac!"<br>"On pourrait partir de Québec, traverser à Lévis en traversier, pis prendre la route 132 Est vers Rivière-du-Loup."<br>"Combien de temps ça prend pour se rendre à Tadoussac?"<br>"Environ quatre heures et demie de Québec. On pourrait arrêter dîner en chemin."<br>"Pis est-ce qu'on peut voir les baleines depuis la côte?"<br>"Oui, mais c'est mieux en bateau. Y'a des croisières aux baleines qui partent du quai de Tadoussac. On peut voir des bélugas, des rorquals, pis même des baleines bleues!"<br>"C'est quoi le meilleur temps pour y aller?"<br>"La fin de juillet pis le mois d'août, c'est quand y'a le plus de baleines."<br>"Parfait! Je réserve un chalet sur Airbnb pis tu réserves la croisière?"<br>"Deal!"</p>
<p><em>(You're planning a trip on the Whale Route on the North Shore. "This summer, we should do the Whale Route on the North Shore!" "Oh yes! I've always wanted to see the whales in Tadoussac!" "We could leave from Quebec City, cross to Lévis by ferry, and take Route 132 East toward Rivière-du-Loup." "How long does it take to get to Tadoussac?" "About four and a half hours from Quebec City. We could stop for lunch on the way." "And can you see the whales from the shore?" "Yes, but it's better by boat. There are whale watching cruises from the Tadoussac wharf. You can see belugas, fin whales, and even blue whales!" "What's the best time to go?" "Late July and August is when there are the most whales." "Perfect! I'll book a cottage on Airbnb and you book the cruise?" "Deal!")</em></p>

"""
    html = insert_before(html, marker_17_end, new_17)

    # =========================================================================
    # UNIT 18: AT THE HOTEL & AIRPORT
    # =========================================================================

    marker_18_end = '<h2 id="h-unit-19-quebec-culture">'
    new_18 = """
<p><strong>Quebec Airport Codes & Information (🍁):</strong></p>
<table>
<thead><tr><th>Airport</th><th>Code</th><th>City</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Montréal-Trudeau</td><td>YUL</td><td>Montréal (Dorval)</td><td>Quebec's main international airport. "Aéroport Montréal-Trudeau"</td></tr>
<tr><td>Jean-Lesage</td><td>YQB</td><td>Québec City</td><td>"Aéroport international Jean-Lesage de Québec"</td></tr>
<tr><td>Mirabel</td><td>YMX</td><td>Mirabel</td><td>Cargo only now (former passenger airport)</td></tr>
</tbody>
</table>
<p><strong>Airport Vocabulary – Complete Guide:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>l'enregistrement</td><td>check-in</td><td>"L'enregistrement ouvre deux heures avant le vol." (Check-in opens two hours before the flight.)</td></tr>
<tr><td>la carte d'embarquement</td><td>boarding pass</td><td>"Voici ma carte d'embarquement." (Here's my boarding pass.)</td></tr>
<tr><td>la porte d'embarquement</td><td>boarding gate</td><td>"L'embarquement est à la porte C-22." (Boarding is at gate C-22.)</td></tr>
<tr><td>le contrôle de sécurité</td><td>security check</td><td>"Enlevez vos souliers au contrôle de sécurité." (Take off your shoes at security.)</td></tr>
<tr><td>les douanes</td><td>customs</td><td>"Déclaration de douanes, s'il vous plaît." (Customs declaration, please.)</td></tr>
<tr><td>les bagages à main</td><td>carry-on luggage</td><td>"Un bagage à main et un article personnel." (One carry-on and one personal item.)</td></tr>
<tr><td>les bagages enregistrés</td><td>checked luggage</td><td>"J'ai deux valises à enregistrer." (I have two bags to check.)</td></tr>
<tr><td>le carrousel à bagages</td><td>baggage carousel</td><td>"Les bagages arrivent au carrousel numéro trois." (Baggage arrives at carousel three.)</td></tr>
<tr><td>un vol direct</td><td>a direct flight</td><td>"Y'a-tu un vol direct Montréal-Paris?" (Is there a direct flight Montreal-Paris?)</td></tr>
<tr><td>une escale</td><td>a layover</td><td>"Mon vol a une escale à Toronto." (My flight has a layover in Toronto.)</td></tr>
<tr><td>un retard</td><td>a delay</td><td>"Mon vol a deux heures de retard." (My flight is two hours late.)</td></tr>
<tr><td>annulé</td><td>cancelled</td><td>"Mon vol est annulé à cause de la tempête!" (My flight is cancelled because of the storm!)</td></tr>
</tbody>
</table>
<p><strong>Hotel Vocabulary – Extended:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>J'ai une réservation au nom de...</td><td>I have a reservation under the name...</td><td>"J'ai une réservation au nom de Tremblay."</td></tr>
<tr><td>une chambre pour deux personnes</td><td>a room for two</td><td>"Vous avez-tu une chambre pour deux avec un grand lit?"</td></tr>
<tr><td>un lit simple / un lit double</td><td>a single bed / a double bed</td><td>"On voudrait deux lits simples."</td></tr>
<tr><td>le stationnement</td><td>parking</td><td>"Est-ce que le stationnement est inclus?"</td></tr>
<tr><td>le déjeuner inclus</td><td>breakfast included (QC)</td><td>"Est-ce que le déjeuner est inclus?" (Is breakfast included?)</td></tr>
<tr><td>le Wi-Fi</td><td>Wi-Fi</td><td>"C'est quoi le mot de passe du Wi-Fi?"</td></tr>
<tr><td>la climatisation</td><td>air conditioning</td><td>"La climatisation fonctionne pas." (The AC isn't working.)</td></tr>
<tr><td>le ménage / l'entretien</td><td>housekeeping</td><td>"On n'a pas besoin du ménage aujourd'hui."</td></tr>
<tr><td>libérer la chambre</td><td>to check out</td><td>"Il faut libérer la chambre avant onze heures." (Check-out is before 11.)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – A Flight Cancelled Due to a Winter Storm:</strong></p>
<p><em>Votre vol est annulé à l'aéroport Montréal-Trudeau à cause d'une tempête de neige.</em></p>
<p>"Votre attention s'il vous plaît. Le vol AC 401 à destination de Toronto est annulé en raison des conditions météorologiques."<br>"Ah non! C'est mon vol! Qu'est-ce que je fais?"<br>[Au comptoir d'Air Canada:]<br>"Bonjour, mon vol est annulé. Est-ce que vous pouvez me mettre sur un autre vol?"<br>"Je suis désolée, monsieur. Tous les vols pour Toronto sont annulés ce soir à cause de la tempête."<br>"Quand est le prochain vol disponible?"<br>"Demain matin à six heures trente. Je peux vous mettre sur la liste de confirmation."<br>"D'accord. Est-ce que la compagnie offre un hébergement?"<br>"Puisque l'annulation est causée par la météo, malheureusement, nous ne couvrons pas l'hébergement. Mais je vous donne un bon repas de vingt dollars pour l'aéroport."<br>"Merci. Je vais voir si y'a un hôtel proche avec des chambres disponibles."<br>"Y'a un Marriott juste à côté de l'aéroport avec une navette gratuite. Bonne chance!"</p>

"""
    html = insert_before(html, marker_18_end, new_18)

    # =========================================================================
    # UNIT 19: QUEBEC CULTURE & FESTIVALS
    # =========================================================================

    marker_19_end = '<h2 id="h-unit-20-review-b1">'
    new_19 = """
<p><strong>Quebec's Major Festivals – Complete Guide (🍁):</strong></p>
<table>
<thead><tr><th>Festival</th><th>When</th><th>Where</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Carnaval de Québec</td><td>Feb</td><td>Québec City</td><td>World's largest winter carnival since 1894! Bonhomme Carnaval mascot, ice sculptures, parade.</td></tr>
<tr><td>Festival de Jazz de Montréal</td><td>Late June – early July</td><td>Montréal</td><td>World's largest jazz festival! Hundreds of free outdoor concerts.</td></tr>
<tr><td>Festival Juste pour rire</td><td>July</td><td>Montréal</td><td>World's largest comedy festival. Bilingual shows.</td></tr>
<tr><td>Festival d'été de Québec (FEQ)</td><td>July</td><td>Québec City</td><td>Major music festival on the Plaines d'Abraham. International artists.</td></tr>
<tr><td>Fête nationale / Saint-Jean-Baptiste</td><td>June 24</td><td>Province-wide</td><td>Quebec's national holiday! Bonfires, concerts, parades. THE most important holiday.</td></tr>
<tr><td>Festival des Films du Monde</td><td>Aug – Sept</td><td>Montréal</td><td>Montreal World Film Festival.</td></tr>
<tr><td>Igloofest</td><td>Jan – Feb</td><td>Montréal (Old Port)</td><td>Outdoor electronic music festival IN WINTER! In the cold!</td></tr>
<tr><td>Osheaga</td><td>Aug</td><td>Montréal (Parc Jean-Drapeau)</td><td>Major music and arts festival. Indie, rock, electronic.</td></tr>
<tr><td>Festival de la Poutine</td><td>Aug</td><td>Drummondville</td><td>Celebrating Quebec's most famous dish – poutine!</td></tr>
<tr><td>Festival Western de St-Tite</td><td>Sept</td><td>Saint-Tite</td><td>Rodeo and Western festival, one of the biggest in Canada.</td></tr>
</tbody>
</table>
<p><strong>Quebec National Symbols & Identity (🍁):</strong></p>
<table>
<thead><tr><th>Symbol</th><th>French</th><th>Significance</th></tr></thead>
<tbody>
<tr><td>Flag</td><td>Le fleurdelisé</td><td>White cross on blue with four fleur-de-lis. Adopted in 1948.</td></tr>
<tr><td>Motto</td><td>"Je me souviens"</td><td>"I remember" – on all QC license plates.</td></tr>
<tr><td>National flower</td><td>L'iris versicolore</td><td>Blue flag iris, official flower since 1999.</td></tr>
<tr><td>National bird</td><td>Le harfang des neiges</td><td>The snowy owl – representing Quebec's harsh winters.</td></tr>
<tr><td>National tree</td><td>Le bouleau jaune</td><td>The yellow birch.</td></tr>
<tr><td>National dish</td><td>La poutine</td><td>Invented in rural Quebec in the 1950s.</td></tr>
<tr><td>Patron saint</td><td>Saint-Jean-Baptiste</td><td>National holiday, June 24th.</td></tr>
<tr><td>Language law</td><td>La Loi 101 (Charte de la langue française)</td><td>Establishes French as the official language of Quebec since 1977.</td></tr>
</tbody>
</table>
<p><strong>Quebec Regions – A Quick Guide:</strong></p>
<table>
<thead><tr><th>Region</th><th>Capital</th><th>Known For</th></tr></thead>
<tbody>
<tr><td>Montréal</td><td>Montréal</td><td>Quebec's largest city, festivals, restaurants, multiculturalism</td></tr>
<tr><td>Capitale-Nationale</td><td>Québec City</td><td>History, Château Frontenac, European atmosphere</td></tr>
<tr><td>Laurentides</td><td>Saint-Jérôme</td><td>Mountains, ski resorts, cottages</td></tr>
<tr><td>Estrie (Eastern Townships)</td><td>Sherbrooke</td><td>Wine, cheese, fall colours, bilingual culture</td></tr>
<tr><td>Gaspésie</td><td>Gaspé</td><td>Rocher Percé, dramatic coastline, nature</td></tr>
<tr><td>Saguenay–Lac-Saint-Jean</td><td>Saguenay</td><td>Fjord, blueberries, tourtière, outdoor adventure</td></tr>
<tr><td>Côte-Nord</td><td>Sept-Îles</td><td>Whale watching, vast wilderness, Indigenous culture</td></tr>
<tr><td>Outaouais</td><td>Gatineau</td><td>Federal government jobs, Musée canadien de l'histoire</td></tr>
<tr><td>Mauricie</td><td>Trois-Rivières</td><td>Parc national de la Mauricie, forestry history</td></tr>
<tr><td>Charlevoix</td><td>Baie-Saint-Paul</td><td>Art galleries, fine dining, dramatic landscapes, Massif ski resort</td></tr>
</tbody>
</table>
<p><strong>Popular Quebec Expressions About Culture (🍁):</strong></p>
<table>
<thead><tr><th>Expression</th><th>English</th><th>Context</th></tr></thead>
<tbody>
<tr><td>"Vive le Québec!"</td><td>"Long live Quebec!"</td><td>Expression of Quebec pride</td></tr>
<tr><td>"La Belle Province"</td><td>"The Beautiful Province"</td><td>Old nickname for Quebec</td></tr>
<tr><td>"Chez nous" (au Québec)</td><td>"At home" / "Our place"</td><td>"Chez nous, on fait les choses différemment." (At our place, we do things differently.)</td></tr>
<tr><td>"De souche"</td><td>"Old stock" / ancestral</td><td>"Québécois de souche" = Quebecers with roots going back to New France</td></tr>
<tr><td>"Un snowbird"</td><td>A retiree who winters in Florida</td><td>"Mes grands-parents sont des snowbirds, y passent l'hiver en Floride."</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Attending the Saint-Jean-Baptiste Celebrations:</strong></p>
<p><em>C'est le 24 juin, la Fête nationale du Québec! Vous allez aux célébrations.</em></p>
<p>"Bonne Saint-Jean! Viens, on va sur les Plaines d'Abraham pour le spectacle!"<br>"Oui! C'est qui les artistes cette année?"<br>"Les Cowboys Fringants, Cœur de Pirate, pis plein d'autres! Y va y avoir du monde en masse!"<br>"J'ai apporté un drapeau du Québec pis des cierges magiques!"<br>"Parfait! On va se trouver une belle place sur le gazon."<br>"Regarde, y'a déjà des milliers de personnes! Tout le monde porte du bleu et du blanc!"<br>"C'est normal, c'est notre fête nationale! Faut célébrer!"<br>"C'est quand le feu de joie?"<br>"Le feu de la Saint-Jean, c'est à minuit. Une tradition qui remonte à des centaines d'années."<br>"J'adore! Y'a rien de plus beau que la Fête nationale. Vive le Québec!"<br>"VIVE LE QUÉBEC!"</p>
<p><em>(It's June 24th, Quebec's national holiday! You're going to the celebrations. "Happy Saint-Jean! Come on, let's go to the Plains of Abraham for the concert!" "Yes! Who are the artists this year?" "Les Cowboys Fringants, Cœur de Pirate, and many others! There'll be tons of people!" "I brought a Quebec flag and sparklers!" "Perfect! Let's find a nice spot on the grass." "Look, there are already thousands of people! Everyone's wearing blue and white!" "It's normal, it's our national holiday! We have to celebrate!" "When's the bonfire?" "The Saint-Jean bonfire is at midnight. A tradition that goes back hundreds of years." "I love it! There's nothing more beautiful than the national holiday. Long live Quebec!" "LONG LIVE QUEBEC!")</em></p>

"""
    html = insert_before(html, marker_19_end, new_19)

    # =========================================================================
    # UNIT 20: REVIEW & B1 PREPARATION
    # =========================================================================

    marker_20_end = '<h1 id="h-a2-conclusion">'
    new_20 = """
<p><strong>A2 Grammar Summary – Quick Reference Table:</strong></p>
<table>
<thead><tr><th>Grammar Topic</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Passé composé (avoir)</td><td>Subject + avoir + past participle</td><td>"J'ai mangé de la poutine."</td></tr>
<tr><td>Passé composé (être)</td><td>Subject + être + past participle (agrees!)</td><td>"Elle est allée au parc."</td></tr>
<tr><td>Imparfait</td><td>Nous stem + imparfait endings</td><td>"Quand j'étais jeune, je jouais dehors."</td></tr>
<tr><td>Futur simple</td><td>Infinitive + future endings</td><td>"Demain, je parlerai français."</td></tr>
<tr><td>Futur proche</td><td>Aller + infinitive</td><td>"Je vais manger tantôt."</td></tr>
<tr><td>Passé récent</td><td>Venir de + infinitive</td><td>"Je viens de finir."</td></tr>
<tr><td>En train de</td><td>Être en train de + infinitive</td><td>"Je suis en train de travailler."</td></tr>
<tr><td>Impératif</td><td>Tu/Nous/Vous verb forms (no subject)</td><td>"Mange! Mangeons! Mangez!"</td></tr>
<tr><td>Comparatif</td><td>Plus/moins/aussi + adj + que</td><td>"Montréal est plus grande que Québec."</td></tr>
<tr><td>Superlatif</td><td>Le/la/les plus/moins + adj</td><td>"C'est la plus belle ville."</td></tr>
<tr><td>Negation</td><td>Ne... pas/jamais/plus/rien</td><td>"Je ne mange jamais de viande."</td></tr>
<tr><td>Pronouns (COD)</td><td>le/la/les before verb</td><td>"Je le connais." (I know him.)</td></tr>
<tr><td>Pronouns (COI)</td><td>me/te/lui/nous/vous/leur</td><td>"Je lui parle." (I speak to him/her.)</td></tr>
<tr><td>"Y" (location)</td><td>Replaces à + place</td><td>"J'y vais." (I'm going there.)</td></tr>
<tr><td>"En" (quantity)</td><td>Replaces de + noun</td><td>"J'en veux." (I want some.)</td></tr>
</tbody>
</table>
<p><strong>What to Expect at B1 Level – Preview:</strong></p>
<table>
<thead><tr><th>B1 Topic</th><th>What You'll Learn</th><th>Why It Matters</th></tr></thead>
<tbody>
<tr><td>Le conditionnel</td><td>Would + verb: "Je voudrais, j'aimerais"</td><td>Polite requests, hypothetical situations</td></tr>
<tr><td>Le subjonctif</td><td>After "il faut que", "je veux que"</td><td>Expressing necessity, desire, doubt</td></tr>
<tr><td>Les pronoms relatifs</td><td>Qui, que, dont, où</td><td>Making complex sentences</td></tr>
<tr><td>Le plus-que-parfait</td><td>Had done: "J'avais déjà mangé"</td><td>Talking about events before other past events</td></tr>
<tr><td>Le discours indirect</td><td>He said that...: "Il a dit que..."</td><td>Reporting speech</td></tr>
<tr><td>Les expressions de cause/conséquence</td><td>Because, therefore, so that</td><td>Building arguments</td></tr>
<tr><td>L'expression d'opinion</td><td>"Je pense que, à mon avis"</td><td>Expressing opinions and debating</td></tr>
</tbody>
</table>
<p><strong>Quebec French Checklist – What You Should Know at the End of A2 (🍁):</strong></p>
<ul>
<li>✅ Understand "tu" vs "vous" social rules in Quebec (use "tu" widely)</li>
<li>✅ Recognize and use Quebec contractions: "chu" (je suis), "y" (il), "a" (elle), "pis" (puis)</li>
<li>✅ Know the "-tu" question particle: "C'est-tu bon?" (Is it good?)</li>
<li>✅ Understand "tantôt" (earlier/later today) and "asteure" (now)</li>
<li>✅ Know Quebec meal names: déjeuner, dîner, souper</li>
<li>✅ Navigate Québec shopping: dépanneur, centre d'achats, spécial, aubaines</li>
<li>✅ Understand Quebec housing: 3½, 4½, triplex, July 1st moving day</li>
<li>✅ Talk about weather with Quebec expressions: "Y fait frette!" "Y mouille."</li>
<li>✅ Know basic Quebec healthcare vocabulary: RAMQ, CLSC, 811</li>
<li>✅ Recognize common fillers: "tsé", "faque", "ben", "genre", "mettons"</li>
<li>✅ Know key cultural references: Saint-Jean-Baptiste, cabane à sucre, hockey</li>
<li>✅ Understand negative without "ne": "J'sais pas" instead of "Je ne sais pas"</li>
</ul>
<p><strong>A2 to B1 Study Tips:</strong></p>
<ul>
<li><strong>Watch Quebec TV:</strong> Start with "Tout le monde en parle" (talk show) and "Les Parent" (sitcom) to improve listening comprehension.</li>
<li><strong>Read Quebec news:</strong> La Presse (lapresse.ca) has free articles at a good A2-B1 level. Start with the "Actualités" section.</li>
<li><strong>Listen to Quebec music:</strong> Les Cowboys Fringants, Cœur de Pirate, and Lisa LeBlanc are great for learning vocabulary and pronunciation.</li>
<li><strong>Practice with Quebecers:</strong> Join conversation groups at your local library or community centre. Many offer free "cafés-conversations" in French.</li>
<li><strong>Use Quebec podcasts:</strong> "Aujourd'hui l'histoire" (history) and "Radio-Canada Première" are excellent for A2-B1 learners.</li>
<li><strong>Take francisation courses:</strong> If you're an immigrant, free full-time or part-time French courses are available through the MIFI.</li>
<li><strong>Keep a vocabulary journal:</strong> Write down 5 new Quebec words every day with example sentences.</li>
<li><strong>Don't be afraid to make mistakes:</strong> Quebecers are known for being patient and encouraging with French learners. "Lâche pas!" (Don't give up!)</li>
</ul>

"""
    html = insert_before(html, marker_20_end, new_20)

    # =========================================================================
    # CONCLUSION – Add learning resources
    # =========================================================================

    # Find the end of the conclusion section
    # We'll add content just after the conclusion heading
    conclusion_marker = '<h1 id="h-a2-conclusion">'
    conclusion_idx = html.find(conclusion_marker)
    if conclusion_idx != -1:
        # Find the end of the h1 tag
        end_tag = html.find('</h1>', conclusion_idx)
        if end_tag != -1:
            insert_point = end_tag + len('</h1>')
            new_conclusion = """
<p><strong>Congratulations on completing A2!</strong> You now have a solid foundation in Quebec French. You can handle everyday situations, express yourself in the past, present, and future, and navigate Quebec's unique culture and vocabulary.</p>
<p><strong>Key A2 Resources for Continuing Your Learning:</strong></p>
<ul>
<li><strong>Online:</strong> ICI Radio-Canada (radio-canada.ca) for news and video content in Quebec French.</li>
<li><strong>Apps:</strong> Mauril (CBC/Radio-Canada's free bilingual learning app), Duolingo (for general French basics).</li>
<li><strong>Books:</strong> "Le Petit Robert" dictionary (the standard French dictionary, covers Quebec vocabulary too).</li>
<li><strong>In-person:</strong> Libraries across Quebec offer free French conversation circles ("cercles de conversation").</li>
<li><strong>Movies:</strong> "Bon Cop, Bad Cop" (2006), "C.R.A.Z.Y." (2005), "Starbuck" (2011), "Mommy" (2014) by Xavier Dolan.</li>
</ul>
<p><em>"Lâche pas la patate!"</em> – Don't give up! (A classic Quebec encouragement meaning "Don't let go of the potato!" 🥔)</p>

"""
            html = html[:insert_point] + new_conclusion + html[insert_point:]

    write_file(path, html)
    print("A2 Part 4 done: Units 17-20 and Conclusion expanded successfully!")

if __name__ == '__main__':
    main()
