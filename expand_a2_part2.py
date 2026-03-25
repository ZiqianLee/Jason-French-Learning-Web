#!/usr/bin/env python3
"""Expand A2 Units 6-10 with more Quebec French content."""

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
    # UNIT 6: HOUSING & HOME
    # =========================================================================

    marker_6_end = '<h2 id="h-unit-7-transport">'
    new_6 = """
<p><strong>Quebec Apartment System – Complete Guide (🍁):</strong></p>
<p>Quebec has a unique apartment naming system that every resident must understand:</p>
<table>
<thead><tr><th>Apartment Size</th><th>What It Means</th><th>Typical For</th><th>Average Price (Montreal 2024)</th></tr></thead>
<tbody>
<tr><td>1½</td><td>Studio: 1 room + bathroom</td><td>Student, single person</td><td>$800-1,200/month</td></tr>
<tr><td>2½</td><td>1 bedroom + kitchen-living + bathroom</td><td>Single person, couple</td><td>$900-1,400/month</td></tr>
<tr><td>3½</td><td>1 bedroom + living room + kitchen + bathroom</td><td>Single, couple</td><td>$1,000-1,600/month</td></tr>
<tr><td>4½</td><td>2 bedrooms + living room + kitchen + bathroom</td><td>Couple, small family</td><td>$1,200-1,800/month</td></tr>
<tr><td>5½</td><td>3 bedrooms + living room + kitchen + bathroom</td><td>Family</td><td>$1,400-2,200/month</td></tr>
<tr><td>6½</td><td>4 bedrooms + living room + kitchen + bathroom</td><td>Large family</td><td>$1,600-2,500/month</td></tr>
</tbody>
</table>
<p><strong>Note:</strong> The "½" always refers to the bathroom. So a "4½" has 4 rooms (2 bedrooms + living room + kitchen) plus 1 bathroom.</p>
<p><strong>Quebec Housing Types:</strong></p>
<table>
<thead><tr><th>Type</th><th>Description</th></tr></thead>
<tbody>
<tr><td>un appartement</td><td>An apartment (most common in Montreal)</td></tr>
<tr><td>un duplex</td><td>A building with 2 separate apartments (one on each floor)</td></tr>
<tr><td>un triplex</td><td>A building with 3 separate apartments (very common in Montreal!)</td></tr>
<tr><td>un condo</td><td>A condominium (owned, not rented)</td></tr>
<tr><td>une maison</td><td>A house (more common in suburbs and rural areas)</td></tr>
<tr><td>un chalet</td><td>A cottage/cabin (for vacation, very important in QC culture!)</td></tr>
<tr><td>une chambre meublée</td><td>A furnished room (for students)</td></tr>
<tr><td>un loft</td><td>A loft apartment (popular in converted industrial buildings)</td></tr>
</tbody>
</table>
<p><strong>July 1st – Quebec Moving Day (🍁):</strong></p>
<p>July 1st is not just Canada Day in Quebec – it's <strong>le jour du déménagement</strong> (moving day)! All leases traditionally end on June 30 and begin July 1st, making it the busiest moving day in North America:</p>
<ul>
<li><strong>"On déménage le premier juillet."</strong> (We're moving on July 1st.)</li>
<li><strong>"As-tu réservé un camion de déménagement?"</strong> (Did you book a moving truck?)</li>
<li><strong>"Faut que je fasse mes boîtes."</strong> (I have to pack my boxes.)</li>
<li><strong>"Mon nouveau loyer est plus cher que l'ancien."</strong> (My new rent is more expensive than the old one.)</li>
<li><strong>"Je cherche des boîtes en carton au dépanneur."</strong> (I'm looking for cardboard boxes at the corner store.)</li>
</ul>
<p><strong>Renting Vocabulary for Quebec:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>le bail</td><td>the lease</td><td>"Mon bail est d'un an." (My lease is one year.)</td></tr>
<tr><td>le loyer</td><td>the rent</td><td>"Mon loyer inclut le chauffage." (My rent includes heating.)</td></tr>
<tr><td>le propriétaire</td><td>the landlord</td><td>"Le propriétaire habite au premier étage." (The landlord lives on the first floor.)</td></tr>
<tr><td>le locataire</td><td>the tenant</td><td>"On est trois locataires dans le triplex." (There are three tenants in the triplex.)</td></tr>
<tr><td>la Régie du logement</td><td>the Rental Board (QC)</td><td>"Tu peux appeler la Régie si ton proprio augmente trop le loyer." (You can call the Rental Board if your landlord raises the rent too much.)</td></tr>
<tr><td>le chauffage inclus</td><td>heat included</td><td>"Cherche un appart avec chauffage inclus!" (Look for an apartment with heat included!)</td></tr>
<tr><td>l'eau chaude incluse</td><td>hot water included</td><td>"L'eau chaude est incluse dans le loyer." (Hot water is included in the rent.)</td></tr>
<tr><td>les électros / électroménagers</td><td>appliances</td><td>"L'appart vient avec les électros." (The apartment comes with appliances.)</td></tr>
<tr><td>un escalier extérieur</td><td>exterior staircase</td><td>"C'est typiquement montréalais, les escaliers extérieurs!" (Exterior staircases are typically Montreal!)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Visiting an Apartment in Montreal:</strong></p>
<p><em>Vous visitez un appartement avec le propriétaire.</em></p>
<p>"Bonjour! Bienvenue! C'est un beau quatre et demie sur le Plateau."<br>"C'est lumineux! Les fenêtres sont grandes."<br>"Oui, y'a beaucoup de lumière naturelle. Pis vous avez un grand balcon en arrière."<br>"Est-ce que le chauffage est inclus?"<br>"Non, le chauffage est à la charge du locataire, mais c'est électrique, faque c'est pas si cher."<br>"D'accord. Les électros sont fournis?"<br>"Oui, le poêle pis le frigo sont inclus. La laveuse et la sécheuse sont dans le sous-sol, partagées avec les autres locataires."<br>"C'est combien, le loyer?"<br>"Quatorze cents par mois. Le bail commence le premier juillet."<br>"Est-ce que je peux avoir un animal?"<br>"Oui, les chats c'est correct. Pour un chien, faudrait en discuter."<br>"Parfait! Je suis très intéressé. Comment je fais pour appliquer?"</p>
<p><em>(You're visiting an apartment with the landlord. "Hello! Welcome! It's a nice four-and-a-half on the Plateau." "It's bright! The windows are big." "Yes, there's a lot of natural light. And you have a big back balcony." "Is heating included?" "No, heating is the tenant's responsibility, but it's electric, so it's not that expensive." "Okay. Are appliances provided?" "Yes, the stove and fridge are included. The washer and dryer are in the basement, shared with other tenants." "How much is the rent?" "Fourteen hundred a month. The lease starts July 1st." "Can I have a pet?" "Yes, cats are fine. For a dog, we'd have to discuss." "Perfect! I'm very interested. How do I apply?")</em></p>

"""
    html = insert_before(html, marker_6_end, new_6)

    # =========================================================================
    # UNIT 7: TRANSPORTATION
    # =========================================================================

    marker_7_end = '<h2 id="h-unit-8-weather">'
    new_7 = """
<p><strong>Quebec Public Transit Systems (🍁):</strong></p>
<table>
<thead><tr><th>City</th><th>Transit System</th><th>Features</th></tr></thead>
<tbody>
<tr><td>Montréal</td><td>STM (Société de transport de Montréal)</td><td>4 metro lines (verte, orange, bleue, jaune) + bus network. Opus card for payment.</td></tr>
<tr><td>Québec City</td><td>RTC (Réseau de transport de la Capitale)</td><td>Bus network, Metrobus express routes. Opus card.</td></tr>
<tr><td>Gatineau</td><td>STO (Société de transport de l'Outaouais)</td><td>Bus network, connects to Ottawa's OC Transpo.</td></tr>
<tr><td>Laval</td><td>STL (Société de transport de Laval)</td><td>Bus network + 3 metro stations (orange line).</td></tr>
<tr><td>Longueuil</td><td>RTL (Réseau de transport de Longueuil)</td><td>Bus network + 1 metro station (jaune line).</td></tr>
</tbody>
</table>
<p><strong>Driving Vocabulary for Quebec (🍁):</strong></p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th></tr></thead>
<tbody>
<tr><td>chauffer / conduire</td><td>conduire</td><td>to drive</td></tr>
<tr><td>le char</td><td>la voiture</td><td>the car</td></tr>
<tr><td>le bazou</td><td>la vieille voiture</td><td>old beat-up car</td></tr>
<tr><td>le permis de conduire</td><td>le permis de conduire</td><td>driver's license</td></tr>
<tr><td>la SAAQ</td><td>(no equivalent)</td><td>Quebec auto insurance/licensing agency</td></tr>
<tr><td>le gaz / l'essence</td><td>l'essence</td><td>gas / fuel</td></tr>
<tr><td>le poste d'essence</td><td>la station-service</td><td>gas station</td></tr>
<tr><td>les pneus d'hiver</td><td>les pneus neige</td><td>winter tires (mandatory Dec 1 - Mar 15 in QC!)</td></tr>
<tr><td>la souffleuse</td><td>le chasse-neige</td><td>snowblower</td></tr>
<tr><td>la côte</td><td>la montée / la pente</td><td>hill (very common word in Quebec City!)</td></tr>
<tr><td>le boulevard / le chemin</td><td>le boulevard / la route</td><td>boulevard / road</td></tr>
<tr><td>la bretelle d'autoroute</td><td>la bretelle d'autoroute</td><td>highway on-ramp</td></tr>
<tr><td>l'heure de pointe</td><td>l'heure de pointe</td><td>rush hour</td></tr>
<tr><td>le trafic</td><td>la circulation</td><td>traffic</td></tr>
</tbody>
</table>
<p><strong>Winter Driving in Quebec – Essential Vocabulary:</strong></p>
<ul>
<li><strong>"Les routes sont glacées."</strong> (The roads are icy.)</li>
<li><strong>"Faut mettre les pneus d'hiver avant le premier décembre."</strong> (You have to put on winter tires before December 1st.)</li>
<li><strong>"Mon char part pas à matin, la batterie est morte."</strong> (My car won't start this morning, the battery is dead.)</li>
<li><strong>"J'ai besoin d'un boost."</strong> (I need a boost/jump start.) – "boost" is common in QC</li>
<li><strong>"Faut gratter le pare-brise."</strong> (Have to scrape the windshield.)</li>
<li><strong>"Le démarreur à distance, c'est la meilleure invention au Québec!"</strong> (Remote start is the best invention in Quebec!)</li>
</ul>
<p><strong>Giving Directions – Extended Phrases:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Allez tout droit pendant deux feux de circulation.</td><td>Go straight for two traffic lights.</td></tr>
<tr><td>Tournez à gauche au prochain stop.</td><td>Turn left at the next stop sign.</td></tr>
<tr><td>Prenez la première rue à droite après le dépanneur.</td><td>Take the first street right after the corner store.</td></tr>
<tr><td>C'est au coin de la rue, en face de la pharmacie.</td><td>It's on the corner, across from the pharmacy.</td></tr>
<tr><td>Montez la côte et c'est la troisième maison à gauche.</td><td>Go up the hill and it's the third house on the left.</td></tr>
<tr><td>Prenez l'autoroute 20 Est en direction de Québec.</td><td>Take Highway 20 East toward Quebec City.</td></tr>
<tr><td>Sortez à la sortie 138 et suivez les panneaux.</td><td>Exit at exit 138 and follow the signs.</td></tr>
<tr><td>C'est à cinq minutes d'ici en char.</td><td>It's five minutes from here by car.</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Getting a Boost on a Cold Morning:</strong></p>
<p><em>Votre char ne part pas un matin d'hiver.</em></p>
<p>"Ayoye, mon char part pas! La batterie est morte!"<br>"As-tu des câbles à batterie?"<br>"Oui, y sont dans le coffre. Peux-tu me donner un boost?"<br>"Ben oui! Approche ton char du mien, nez à nez."<br>"Correct. Rouge sur le positif, noir sur le négatif, hein?"<br>"Oui, c'est ça. Laisse-moi partir mon char en premier."<br>"Okay... Essaie de partir le tien asteure."<br>"Ça marche! Merci en maudit! Tu me sauves la vie!"<br>"De rien! Mais tu devrais faire vérifier ta batterie chez Canadian Tire."<br>"T'as raison. Je vais y aller à soir après l'ouvrage. Merci encore!"</p>
<p><em>(Your car won't start on a winter morning. "Ow, my car won't start! The battery is dead!" "Do you have jumper cables?" "Yes, they're in the trunk. Can you give me a boost?" "Of course! Pull your car up to mine, nose to nose." "Right. Red on positive, black on negative, right?" "Yes, that's it. Let me start mine first." "Okay... Try to start yours now." "It works! Thanks so much! You're saving my life!" "No problem! But you should have your battery checked at Canadian Tire." "You're right. I'll go tonight after work. Thanks again!")</em></p>

"""
    html = insert_before(html, marker_7_end, new_7)

    # =========================================================================
    # UNIT 8: WEATHER & CLIMATE
    # =========================================================================

    marker_8_end = '<h2 id="h-unit-9-invitations">'
    new_8 = """
<p><strong>Quebec Weather – Complete Vocabulary (🍁):</strong></p>
<p>Weather is the #1 small talk topic in Quebec. You MUST master this vocabulary:</p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th><th>Temperature Range</th></tr></thead>
<tbody>
<tr><td>Y fait frette!</td><td>Il fait froid!</td><td>It's freezing!</td><td>Below -15°C</td></tr>
<tr><td>Y fait frais.</td><td>Il fait frais.</td><td>It's cool.</td><td>0 to 10°C</td></tr>
<tr><td>Y fait doux.</td><td>Il fait doux.</td><td>It's mild.</td><td>10 to 20°C</td></tr>
<tr><td>Y fait chaud!</td><td>Il fait chaud!</td><td>It's hot!</td><td>25 to 30°C</td></tr>
<tr><td>Y fait chaud en titi!</td><td>Il fait très chaud!</td><td>It's really hot!</td><td>Above 30°C</td></tr>
<tr><td>Y mouille.</td><td>Il pleut.</td><td>It's raining.</td><td>—</td></tr>
<tr><td>Y neige.</td><td>Il neige.</td><td>It's snowing.</td><td>—</td></tr>
<tr><td>Y fait tempête.</td><td>Il y a une tempête.</td><td>There's a storm.</td><td>—</td></tr>
<tr><td>Y fait un temps de canard.</td><td>Il fait mauvais.</td><td>It's lousy weather.</td><td>—</td></tr>
<tr><td>Y fait beau!</td><td>Il fait beau!</td><td>It's nice out!</td><td>—</td></tr>
</tbody>
</table>
<p><strong>Winter Weather Specifics:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>le facteur vent / l'éolien</td><td>wind chill</td><td>"Avec le facteur vent, ça fait moins quarante." (With wind chill, it feels like minus forty.)</td></tr>
<tr><td>le verglas</td><td>freezing rain / ice storm</td><td>"Y'a du verglas sur les routes." (There's freezing rain on the roads.)</td></tr>
<tr><td>la poudrerie</td><td>blowing snow</td><td>"Y fait de la poudrerie, on voit rien!" (There's blowing snow, you can't see anything!)</td></tr>
<tr><td>une bordée de neige</td><td>a big snowfall</td><td>"On a reçu une bonne bordée de neige hier." (We got a big snowfall yesterday.)</td></tr>
<tr><td>la slush / la sloche</td><td>la neige fondue</td><td>"Y'a de la slush partout!" (There's slush everywhere!)</td></tr>
<tr><td>la glace noire</td><td>le verglas invisible</td><td>"Attention à la glace noire!" (Watch out for black ice!)</td></tr>
<tr><td>le banc de neige</td><td>le congère</td><td>"Y'a des bancs de neige de deux mètres!" (There are snowbanks two metres high!)</td></tr>
<tr><td>le dégel</td><td>le dégel</td><td>"Le dégel commence en mars." (The thaw starts in March.)</td></tr>
<tr><td>la canicule</td><td>la canicule</td><td>"On est en pleine canicule à Montréal." (We're in a heat wave in Montreal.)</td></tr>
<tr><td>les nids-de-poule</td><td>les nids-de-poule</td><td>"Au printemps, les rues sont pleines de nids-de-poule." (In spring, the streets are full of potholes.)</td></tr>
</tbody>
</table>
<p><strong>Quebec Climate by Season – What to Expect:</strong></p>
<table>
<thead><tr><th>Season</th><th>Months</th><th>Typical Temperatures</th><th>Key Events</th></tr></thead>
<tbody>
<tr><td>Hiver</td><td>Déc – Mars</td><td>-25°C to -5°C</td><td>Carnaval de Québec, hockey, ski, motoneige</td></tr>
<tr><td>Printemps</td><td>Avril – Mai</td><td>0°C to 15°C</td><td>Temps des sucres, dégel, nids-de-poule!</td></tr>
<tr><td>Été</td><td>Juin – Août</td><td>20°C to 35°C</td><td>Festivals, camping, Saint-Jean-Baptiste, canicules</td></tr>
<tr><td>Automne</td><td>Sept – Nov</td><td>0°C to 15°C</td><td>Couleurs d'automne, cueillette de pommes, Halloween</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Watching the Weather Report:</strong></p>
<p><em>Vous écoutez la météo à la télé un soir d'hiver.</em></p>
<p>"Bonsoir! Voici la météo pour demain. Attention, un avertissement de tempête de neige est en vigueur pour la grande région de Montréal."<br>"On prévoit entre vingt-cinq et trente centimètres de neige accompagnés de vents violents. Le facteur éolien fera descendre la température ressentie à moins trente-cinq."<br>"Environnement Canada recommande de limiter les déplacements. Les conditions routières seront très difficiles."<br>"Pour mardi, le temps sera plus calme avec du soleil, mais les températures resteront très froides à moins vingt."</p>
<p>[Vous parlez à votre conjoint(e):]</p>
<p>"As-tu entendu ça? Y va faire tempête demain!"<br>"Encore une tempête? C'est la troisième en deux semaines!"<br>"Mets-en! Je pense qu'on devrait rester à la maison. Je vais appeler le bureau pour dire que je travaille de la maison."<br>"Bonne idée. Faudrait aller au dépanneur à soir acheter du pain pis du lait avant la tempête."<br>"Oui, pis faut s'assurer que la souffleuse marche!"</p>
<p><em>(You're watching the weather report on TV on a winter evening. "Good evening! Here is tomorrow's forecast. Warning: a snowstorm warning is in effect for the greater Montreal area." "We expect between twenty-five and thirty centimeters of snow with violent winds. The wind chill will bring the temperature to minus thirty-five." "Environment Canada recommends limiting travel. Road conditions will be very difficult." "For Tuesday, the weather will be calmer with sun, but temperatures will remain very cold at minus twenty." [You talk to your partner:] "Did you hear that? There's going to be a storm tomorrow!" "Another storm? That's the third in two weeks!" "You bet! I think we should stay home. I'll call the office to say I'm working from home." "Good idea. We should go to the corner store tonight to buy bread and milk before the storm." "Yes, and we need to make sure the snowblower works!")</em></p>

"""
    html = insert_before(html, marker_8_end, new_8)

    # =========================================================================
    # UNIT 9: INVITATIONS & EVENTS
    # =========================================================================

    marker_9_end = '<h2 id="h-unit-10-phone">'
    new_9 = """
<p><strong>Quebec Social Events – Complete Vocabulary (🍁):</strong></p>
<table>
<thead><tr><th>Event Type</th><th>French</th><th>Description</th></tr></thead>
<tbody>
<tr><td>5 à 7</td><td>un cinq à sept</td><td>After-work drinks/socializing (5 PM to 7 PM). Very popular in QC workplaces!</td></tr>
<tr><td>Party</td><td>un party (pronounced "par-tee")</td><td>A party. "On fait un party samedi!" (We're having a party Saturday!)</td></tr>
<tr><td>BBQ</td><td>un barbecue / un BBQ</td><td>Summer gathering around the grill. "On fait un BBQ chez nous!" (We're having a BBQ at our place!)</td></tr>
<tr><td>Potluck</td><td>un repas-partage / un "pot luck"</td><td>"Chacun apporte un plat." (Everyone brings a dish.)</td></tr>
<tr><td>Épluchette de blé d'Inde</td><td>une épluchette</td><td>Corn husking party! A beloved QC summer tradition.</td></tr>
<tr><td>Shower</td><td>un shower (de bébé / nuptial)</td><td>Baby shower or bridal shower. "Ma sœur organise un shower pour Julie."</td></tr>
<tr><td>Sugar shack outing</td><td>une sortie à la cabane à sucre</td><td>Group outing to a maple sugar shack in spring.</td></tr>
<tr><td>Camping trip</td><td>un camping / une fin de semaine de camping</td><td>"On va faire du camping en gang." (We're going camping as a group.)</td></tr>
</tbody>
</table>
<p><strong>Inviting Someone – Complete Phrase Guide:</strong></p>
<table>
<thead><tr><th>Formality</th><th>Invitation Phrase</th><th>English</th></tr></thead>
<tbody>
<tr><td>Casual</td><td>Ça te tente-tu de venir?</td><td>Do you feel like coming?</td></tr>
<tr><td>Casual</td><td>T'es-tu libre en fin de semaine?</td><td>Are you free this weekend?</td></tr>
<tr><td>Casual</td><td>On fait un party, viens-tu?</td><td>We're having a party, you coming?</td></tr>
<tr><td>Normal</td><td>Est-ce que tu voudrais venir souper?</td><td>Would you like to come for dinner?</td></tr>
<tr><td>Normal</td><td>Ça te dirait de venir au cinéma?</td><td>How about coming to the movies?</td></tr>
<tr><td>Polite</td><td>Je vous invite à notre fête.</td><td>I invite you to our party.</td></tr>
<tr><td>Formal</td><td>Nous avons le plaisir de vous inviter à...</td><td>We have the pleasure of inviting you to...</td></tr>
</tbody>
</table>
<p><strong>Accepting and Declining – Quebec Style:</strong></p>
<table>
<thead><tr><th>Accepting (Quebec)</th><th>English</th></tr></thead>
<tbody>
<tr><td>Ben oui! / C'est sûr!</td><td>Of course! / For sure!</td></tr>
<tr><td>Mets-en que j'suis là!</td><td>You bet I'll be there!</td></tr>
<tr><td>Ça va me faire plaisir!</td><td>It'll be my pleasure!</td></tr>
<tr><td>Count me in! / Chu dedans!</td><td>Count me in!</td></tr>
<tr><td>J'apporte quoi? (potluck)</td><td>What should I bring?</td></tr>
</tbody>
</table>
<table>
<thead><tr><th>Declining (Quebec)</th><th>English</th></tr></thead>
<tbody>
<tr><td>Ah, j'peux pas, j'travaille.</td><td>Oh, I can't, I'm working.</td></tr>
<tr><td>Ça adonne pas cette fois-ci.</td><td>It doesn't work out this time. (Very QC!)</td></tr>
<tr><td>J'aurais ben aimé ça, mais j'peux pas.</td><td>I would have loved to, but I can't.</td></tr>
<tr><td>C'est plate, mais j'ai déjà quelque chose.</td><td>Too bad, but I already have something.</td></tr>
<tr><td>Une autre fois peut-être!</td><td>Another time maybe!</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Planning an Épluchette de Blé d'Inde:</strong></p>
<p><em>Vous organisez une épluchette de blé d'Inde (corn roast) avec des amis.</em></p>
<p>"Heille gang! On fait-tu une épluchette de blé d'Inde samedi prochain?"<br>"Oh oui! C'est un de mes événements préférés de l'été!"<br>"On va en faire un gros! Je vais acheter cent épis de maïs au marché Jean-Talon."<br>"J'apporte les hot-dogs pis les condiments!"<br>"Moi, je fais une salade de patates pis des brownies."<br>"Parfait! C'est chez qui?"<br>"Chez nous, dans la cour. On a assez de place."<br>"C'est quoi l'heure?"<br>"Disons quatre heures. On commence par épluchette pis après on mange vers six heures."<br>"J'apporte ma guitare! On va chanter!"<br>"Yes! Ça va être l'fun en titi!"</p>
<p><em>(You're organizing a corn roast with friends. "Hey guys! Should we do a corn roast next Saturday?" "Oh yes! It's one of my favourite summer events!" "We'll make it big! I'll buy a hundred ears of corn at Jean-Talon Market." "I'll bring the hot dogs and condiments!" "I'll make a potato salad and brownies." "Perfect! At whose place?" "At our place, in the backyard. We have enough room." "What time?" "Let's say four o'clock. We start with corn husking and then we eat around six." "I'll bring my guitar! We'll sing!" "Yes! It's going to be so much fun!")</em></p>

"""
    html = insert_before(html, marker_9_end, new_9)

    # =========================================================================
    # UNIT 10: PHONE CALLS & MESSAGES
    # =========================================================================

    marker_10_end = '<h1 id="h-part-iii-social">'
    new_10 = """
<p><strong>Quebec Texting Abbreviations (🍁):</strong></p>
<p>Quebecers have their own texting style that mixes French abbreviations with English and Québécois expressions:</p>
<table>
<thead><tr><th>Abbreviation</th><th>Full Form</th><th>English</th></tr></thead>
<tbody>
<tr><td>tse / tsé</td><td>tu sais</td><td>you know</td></tr>
<tr><td>pcq / pck</td><td>parce que</td><td>because</td></tr>
<tr><td>stp</td><td>s'il te plaît</td><td>please</td></tr>
<tr><td>svp</td><td>s'il vous plaît</td><td>please (formal)</td></tr>
<tr><td>bcp</td><td>beaucoup</td><td>a lot</td></tr>
<tr><td>tjrs</td><td>toujours</td><td>always</td></tr>
<tr><td>ds</td><td>dans</td><td>in</td></tr>
<tr><td>rdv</td><td>rendez-vous</td><td>appointment / meeting</td></tr>
<tr><td>qqn</td><td>quelqu'un</td><td>someone</td></tr>
<tr><td>qqch</td><td>quelque chose</td><td>something</td></tr>
<tr><td>ns</td><td>nous</td><td>we/us</td></tr>
<tr><td>vs</td><td>vous</td><td>you (formal/plural)</td></tr>
<tr><td>ct</td><td>c'était</td><td>it was</td></tr>
<tr><td>pk</td><td>pourquoi</td><td>why</td></tr>
<tr><td>jsp</td><td>je sais pas</td><td>I dunno</td></tr>
<tr><td>lol / mdr</td><td>mort de rire</td><td>LOL (dying of laughter)</td></tr>
<tr><td>fds</td><td>fin de semaine</td><td>weekend</td></tr>
<tr><td>dsl</td><td>désolé(e)</td><td>sorry</td></tr>
<tr><td>en tk</td><td>en tout cas</td><td>anyway</td></tr>
</tbody>
</table>
<p><strong>Phone Call Scripts – Useful Templates:</strong></p>
<p><strong>Calling a business:</strong></p>
<ul>
<li>"Bonjour, j'appelle pour prendre un rendez-vous." (Hello, I'm calling to make an appointment.)</li>
<li>"Est-ce que je pourrais parler à [nom], s'il vous plaît?" (Could I speak to [name], please?)</li>
<li>"C'est à quel sujet?" (What is this regarding?)</li>
<li>"Je rappelle au sujet de [sujet]." (I'm calling back about [subject].)</li>
</ul>
<p><strong>Leaving a voicemail:</strong></p>
<ul>
<li>"Bonjour, c'est [nom]. Mon numéro est le [numéro]. Pourriez-vous me rappeler quand vous aurez le temps? Merci!" (Hello, this is [name]. My number is [number]. Could you call me back when you have time? Thanks!)</li>
</ul>
<p><strong>Customer service call:</strong></p>
<ul>
<li>"Bonjour, j'aurais besoin d'aide avec mon compte." (Hello, I need help with my account.)</li>
<li>"J'ai un problème avec ma facture." (I have a problem with my bill.)</li>
<li>"Pouvez-vous vérifier mon dossier?" (Can you check my file?)</li>
<li>"Quand est-ce que le technicien va venir?" (When is the technician coming?)</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – Calling Hydro-Québec About a Power Outage:</strong></p>
<p><em>Il y a une panne de courant chez vous. Vous appelez Hydro-Québec.</em></p>
<p>"Bienvenue chez Hydro-Québec. Pour le français, appuyez sur le un. For English, press two."<br>[Vous appuyez sur le un.]<br>"Pour signaler une panne de courant, appuyez sur le trois."<br>[Vous appuyez sur le trois.]<br>"Veuillez entrer votre numéro de compte ou votre code postal."<br>[Vous entrez votre code postal.]<br>"Nous sommes au courant d'une panne dans votre secteur. Environ cinq mille clients sont touchés. Le rétablissement est prévu pour vingt-deux heures. Pour parler à un agent, restez en ligne."<br>[Après quelques minutes d'attente:]<br>"Hydro-Québec, bonjour! Comment puis-je vous aider?"<br>"Bonjour! J'ai pas de courant depuis ce matin. C'est-tu normal que ça prenne aussi longtemps?"<br>"Je comprends votre frustration. On a eu beaucoup de verglas dans votre région. Nos équipes travaillent fort pour rétablir le courant."<br>"D'accord. Merci pour l'information!"</p>
<p><em>(There's a power outage at your place. You call Hydro-Quebec. After automated prompts and entering your postal code: "We are aware of an outage in your area. About five thousand customers are affected. Restoration is expected by 10 PM." After waiting to speak to an agent: "Hello! I've had no power since this morning. Is it normal that it's taking this long?" "I understand your frustration. We've had a lot of freezing rain in your area. Our teams are working hard to restore power.")</em></p>

"""
    html = insert_before(html, marker_10_end, new_10)

    write_file(path, html)
    print("A2 Part 2 done: Units 6-10 expanded successfully!")

if __name__ == '__main__':
    main()
