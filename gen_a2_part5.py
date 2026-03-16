#!/usr/bin/env python3
"""Generate A2 HTML - Part 5: Units 17-20 + Footer/JS"""
import os
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2.html")
A1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a1.html")

with open(A1, 'r', encoding='utf-8') as f:
    a1_content = f.read()
js_start = a1_content.index('<script>') + len('<script>')
js_end = a1_content.index('</script>')
js_block = a1_content[js_start:js_end]

content = """
<h1 id="h-part-v-travel">PART V: TRAVEL &amp; CULTURE</h1>

<h2 id="h-unit-17-travel">UNIT 17: TRAVEL PLANNING</h2>

<h3 id="h-17-1-travel-vocab">17.1 Travel Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un voyage</td><td>a trip</td></tr>
<tr><td>un billet d&#39;avion</td><td>a plane ticket</td></tr>
<tr><td>un passeport</td><td>a passport</td></tr>
<tr><td>une valise</td><td>a suitcase</td></tr>
<tr><td>un sac à dos</td><td>a backpack</td></tr>
<tr><td>une réservation</td><td>a reservation</td></tr>
<tr><td>l&#39;aéroport</td><td>the airport</td></tr>
<tr><td>la gare</td><td>the train station</td></tr>
<tr><td>un aller simple</td><td>a one-way ticket</td></tr>
<tr><td>un aller-retour</td><td>a round-trip ticket</td></tr>
<tr><td>les vacances</td><td>vacation/holidays</td></tr>
<tr><td>un itinéraire</td><td>an itinerary</td></tr>
</tbody></table>

<h3 id="h-17-2-booking">17.2 Booking &amp; Reservations</h3>
<ul>
<li><strong>Je voudrais réserver un billet aller-retour Montréal-Québec pour le quinze juillet.</strong> (I would like to book a round-trip ticket from Montreal to Quebec City for July 15th.)</li>
<li><strong>Est-ce qu&#39;il y a des tarifs réduits pour les étudiants?</strong> (Are there reduced rates for students?)</li>
<li><strong>Je préfère un siège côté fenêtre, s&#39;il vous plaît.</strong> (I prefer a window seat, please.)</li>
<li><strong>Jusqu&#39;à quand est-ce que je peux annuler ma réservation sans frais?</strong> (Until when can I cancel my reservation without fees?)</li>
</ul>

<h3 id="h-17-3-packing">17.3 Packing &amp; Preparation</h3>
<ul>
<li><strong>N&#39;oublie pas d&#39;apporter ton manteau d&#39;hiver et ta tuque si tu viens au Québec en janvier.</strong> (Don&#39;t forget to bring your winter coat and your beanie if you come to Quebec in January.)</li>
<li><strong>J&#39;ai fait ma valise hier soir. J&#39;ai mis des vêtements chauds et mon appareil photo.</strong> (I packed my suitcase last night. I put warm clothes and my camera.)</li>
<li><strong>Est-ce que tu as vérifié la météo pour notre destination? Il paraît qu&#39;il va pleuvoir toute la semaine.</strong> (Did you check the weather for our destination? It seems it&#39;s going to rain all week.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Planning a Road Trip on the Route des Fromages:</strong></p>
<p><em>Vous planifiez un road trip dans les Cantons-de-l&#39;Est avec votre conjoint(e).</em></p>
<p>&quot;Ça te dit de faire un road trip dans les Cantons-de-l&#39;Est cette fin de semaine?&quot;<br>&quot;Oui! On pourrait faire la Route des Fromages et visiter des fromageries.&quot;<br>&quot;Bonne idée! On pourrait partir vendredi après le travail et revenir dimanche soir.&quot;<br>&quot;Parfait. J&#39;ai trouvé un gîte touristique à Knowlton. C&#39;est cent vingt dollars par nuit.&quot;<br>&quot;C&#39;est correct. Je vais préparer un itinéraire avec les fromageries qu&#39;on veut visiter. Et on pourra s&#39;arrêter pour dîner à Magog, au bord du lac Memphrémagog.&quot;<br>&quot;Super! J&#39;ai hâte! N&#39;oublie pas de faire le plein d&#39;essence avant de partir.&quot;</p>
<p><em>(You are planning a road trip in the Eastern Townships with your partner. &quot;Do you feel like doing a road trip in the Eastern Townships this weekend?&quot; &quot;Yes! We could do the Cheese Route and visit cheese factories.&quot; &quot;Good idea! We could leave Friday after work and come back Sunday evening.&quot; &quot;Perfect. I found a B&amp;B in Knowlton. It&#39;s one hundred and twenty dollars a night.&quot; &quot;That&#39;s fine. I&#39;ll prepare an itinerary with the cheese factories we want to visit. And we can stop for lunch in Magog, by Lake Memphremagog.&quot; &quot;Great! I can&#39;t wait! Don&#39;t forget to fill up on gas before we leave.&quot;)</em></p>

<h3 id="h-17-4-cdn-travel">17.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>A <strong>&quot;gîte touristique&quot;</strong> is a bed and breakfast (B&amp;B). The term <strong>&quot;chambre d&#39;hôtes&quot;</strong> is more common in France.</li>
<li><strong>&quot;Faire le plein&quot;</strong> means to fill up the gas tank. Gas stations in Quebec are often called <strong>&quot;des postes d&#39;essence&quot;</strong> or <strong>&quot;des stations-service.&quot;</strong></li>
<li>The <strong>Cantons-de-l&#39;Est</strong> (Eastern Townships) is a popular tourist region south-east of Montreal, known for its scenic countryside, wine, cheese, and craft beer.</li>
</ul>
<hr>

<h2 id="h-unit-18-hotel-airport">UNIT 18: AT THE HOTEL &amp; AIRPORT</h2>

<h3 id="h-18-1-hotel">18.1 Hotel Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>une chambre simple</td><td>a single room</td></tr>
<tr><td>une chambre double</td><td>a double room</td></tr>
<tr><td>la réception</td><td>the front desk</td></tr>
<tr><td>la clé de la chambre</td><td>the room key</td></tr>
<tr><td>le petit-déjeuner inclus</td><td>breakfast included</td></tr>
<tr><td>le stationnement</td><td>parking (QC) / le parking (FR)</td></tr>
<tr><td>le Wi-Fi gratuit</td><td>free Wi-Fi</td></tr>
<tr><td>le service aux chambres</td><td>room service</td></tr>
</tbody></table>

<h3 id="h-18-2-checking-in">18.2 Checking In &amp; Out</h3>
<ul>
<li><strong>Bonjour, j&#39;ai une réservation au nom de Tremblay pour deux nuits.</strong> (Hello, I have a reservation under the name Tremblay for two nights.)</li>
<li><strong>À quelle heure est le départ? Est-ce que je peux laisser mes bagages après le check-out?</strong> (What time is checkout? Can I leave my luggage after checkout?)</li>
<li><strong>Est-ce que le déjeuner est inclus dans le prix de la chambre?</strong> (Is breakfast included in the room price?)</li>
<li><strong>Le Wi-Fi ne fonctionne pas dans ma chambre. Pourriez-vous vérifier, s&#39;il vous plaît?</strong> (The Wi-Fi is not working in my room. Could you check, please?)</li>
</ul>

<h3 id="h-18-3-airport">18.3 At the Airport</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>l&#39;enregistrement</td><td>check-in</td></tr>
<tr><td>la porte d&#39;embarquement</td><td>the boarding gate</td></tr>
<tr><td>la carte d&#39;embarquement</td><td>the boarding pass</td></tr>
<tr><td>les bagages à main</td><td>carry-on luggage</td></tr>
<tr><td>la douane</td><td>customs</td></tr>
<tr><td>le contrôle de sécurité</td><td>security checkpoint</td></tr>
<tr><td>un vol direct</td><td>a direct flight</td></tr>
<tr><td>une escale / une correspondance</td><td>a layover / a connection</td></tr>
<tr><td>le décalage horaire</td><td>jet lag</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>Mon vol pour Paris part de l&#39;aéroport Trudeau à huit heures du matin. Je dois y être au moins deux heures avant.</strong> (My flight to Paris leaves from Trudeau Airport at eight in the morning. I have to be there at least two hours before.)</li>
<li><strong>Le vol a été retardé de deux heures à cause d&#39;une tempête de neige. Tous les passagers doivent attendre dans le terminal.</strong> (The flight was delayed by two hours because of a snowstorm. All passengers must wait in the terminal.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Checking into a Hotel in Quebec City:</strong></p>
<p><em>Vous arrivez à un hôtel dans le Vieux-Québec après un long voyage.</em></p>
<p>&quot;Bonsoir! Bienvenue à l&#39;Hôtel du Vieux-Québec.&quot;<br>&quot;Bonsoir! J&#39;ai une réservation au nom de Bergeron pour trois nuits.&quot;<br>&quot;Oui, je vois votre réservation. Chambre 305, au troisième étage avec vue sur le fleuve Saint-Laurent.&quot;<br>&quot;Magnifique! Est-ce qu&#39;il y a un stationnement pour notre voiture?&quot;<br>&quot;Oui, le stationnement souterrain est à vingt-cinq dollars par nuit. Voici vos clés. Les ascenseurs sont juste là, à gauche.&quot;<br>&quot;Merci beaucoup. À quelle heure est servi le déjeuner demain matin?&quot;<br>&quot;De sept heures à dix heures, dans la salle à manger au premier étage. Bonne nuit!&quot;</p>
<p><em>(You arrive at a hotel in Old Quebec after a long trip. &quot;Good evening! Welcome to the Hotel du Vieux-Québec.&quot; &quot;Good evening! I have a reservation under the name Bergeron for three nights.&quot; &quot;Yes, I see your reservation. Room 305, on the third floor with a view of the St. Lawrence River.&quot; &quot;Wonderful! Is there parking for our car?&quot; &quot;Yes, underground parking is twenty-five dollars per night. Here are your keys. The elevators are right there, on the left.&quot; &quot;Thank you very much. What time is breakfast served tomorrow morning?&quot; &quot;From seven to ten, in the dining room on the first floor. Good night!&quot;)</em></p>

<h3 id="h-18-4-cdn-hotel">18.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>Montreal&#39;s international airport is officially <strong>Aéroport international Pierre-Elliott-Trudeau de Montréal</strong> (YUL), commonly known as &quot;Trudeau Airport.&quot;</li>
<li>In Quebec, <strong>&quot;stationnement&quot;</strong> is used instead of <strong>&quot;parking&quot;</strong> (as in France).</li>
<li>Remember: <strong>&quot;déjeuner&quot;</strong> in Quebec means breakfast (served in the morning), not lunch as in France.</li>
</ul>
<hr>

<h2 id="h-unit-19-quebec-culture">UNIT 19: QUEBEC CULTURE &amp; FESTIVALS</h2>

<h3 id="h-19-1-festivals">19.1 Major Quebec Festivals</h3>
<table>
<thead><tr><th>Festival</th><th>When</th><th>Description</th></tr></thead>
<tbody>
<tr><td>Le Carnaval de Québec</td><td>February</td><td>Le plus grand carnaval d&#39;hiver au monde avec Bonhomme Carnaval, les courses de canot sur glace et la tire d&#39;érable. (The largest winter carnival in the world with Bonhomme Carnaval, ice canoe races, and maple taffy.)</td></tr>
<tr><td>Le Festival de jazz de Montréal</td><td>Late June - July</td><td>Un des plus grands festivals de jazz au monde avec des spectacles gratuits dans le Quartier des spectacles. (One of the largest jazz festivals in the world with free shows in the Quartier des spectacles.)</td></tr>
<tr><td>Juste pour rire</td><td>July</td><td>Le plus grand festival d&#39;humour au monde, avec des spectacles en français et en anglais. (The largest comedy festival in the world, with shows in French and English.)</td></tr>
<tr><td>La Fête nationale du Québec</td><td>June 24</td><td>La fête nationale des Québécois, aussi appelée la Saint-Jean-Baptiste. Il y a des spectacles, des feux d&#39;artifice et des défilés. (The national holiday of Quebecers, also called Saint-Jean-Baptiste Day. There are shows, fireworks, and parades.)</td></tr>
<tr><td>Le Festival d&#39;été de Québec</td><td>July</td><td>Un grand festival de musique en plein air à Québec avec des artistes internationaux. (A large outdoor music festival in Quebec City with international artists.)</td></tr>
</tbody></table>

<h3 id="h-19-2-traditions">19.2 Traditions &amp; Customs</h3>
<ul>
<li><strong>La cabane à sucre:</strong> Au printemps, les Québécois vont à la cabane à sucre pour manger un repas traditionnel avec du jambon, des fèves au lard, des oreilles de crisse et de la tire d&#39;érable sur la neige. (In spring, Quebecers go to the sugar shack to eat a traditional meal with ham, baked beans, fried pork rinds, and maple taffy on snow.)</li>
<li><strong>Le temps des fêtes:</strong> La période de Noël et du Nouvel An est très importante au Québec. Les familles se réunissent pour de grands repas, incluant la tourtière, le ragoût de boulettes et la bûche de Noël. (The holiday season is very important in Quebec. Families gather for big meals, including meat pie, meatball stew, and Yule log cake.)</li>
<li><strong>Le hockey:</strong> Le hockey est le sport national au Québec. Les Canadiens de Montréal sont l&#39;équipe la plus suivie. (Hockey is the national sport in Quebec. The Montreal Canadiens are the most followed team.)</li>
</ul>

<h3 id="h-19-3-cuisine">19.3 Québécois Cuisine</h3>
<table>
<thead><tr><th>Dish</th><th>Description (French)</th><th>Description (English)</th></tr></thead>
<tbody>
<tr><td>La poutine</td><td>Des frites, du fromage en grains et de la sauce brune.</td><td>Fries, cheese curds, and brown gravy.</td></tr>
<tr><td>La tourtière</td><td>Un pâté à la viande traditionnel du temps des fêtes.</td><td>A traditional meat pie for the holidays.</td></tr>
<tr><td>La soupe aux pois</td><td>Une soupe épaisse aux pois jaunes avec du jambon.</td><td>A thick pea soup with ham.</td></tr>
<tr><td>Les cretons</td><td>Un pâté de porc épicé servi sur du pain grillé au déjeuner.</td><td>A spiced pork spread served on toast for breakfast.</td></tr>
<tr><td>Le pâté chinois</td><td>Des couches de bœuf haché, de maïs et de purée de pommes de terre.</td><td>Layers of ground beef, corn, and mashed potatoes.</td></tr>
<tr><td>La tire d&#39;érable</td><td>Du sirop d&#39;érable bouilli versé sur la neige.</td><td>Boiled maple syrup poured over snow.</td></tr>
<tr><td>Le pouding chômeur</td><td>Un gâteau au sirop d&#39;érable très riche et sucré.</td><td>A rich, sweet maple syrup cake.</td></tr>
</tbody></table>

<p><strong>🇫🇷 Real-Life Scene – A Visit to the Sugar Shack:</strong></p>
<p><em>C&#39;est le printemps et vous allez à la cabane à sucre avec des amis.</em></p>
<p>&quot;On est arrivés! Regarde, les érables sont déjà entaillés et la sève coule dans les chaudières!&quot;<br>&quot;Ça sent tellement bon! J&#39;ai faim!&quot;<br>&quot;Moi aussi! On va commencer par la soupe aux pois, du jambon dans le sirop, des fèves au lard et des oreilles de crisse.&quot;<br>&quot;Et pour le dessert?&quot;<br>&quot;Du pouding chômeur et de la tire sur la neige, bien sûr!&quot;<br>&quot;Miam! C&#39;est le meilleur repas de l&#39;année! Vive le temps des sucres!&quot;</p>
<p><em>(It&#39;s spring and you go to the sugar shack with friends. &quot;We&#39;re here! Look, the maples are already tapped and the sap is flowing into the buckets!&quot; &quot;It smells so good! I&#39;m hungry!&quot; &quot;Me too! We&#39;re going to start with pea soup, ham in syrup, baked beans, and fried pork rinds.&quot; &quot;And for dessert?&quot; &quot;Maple syrup cake and taffy on snow, of course!&quot; &quot;Yum! It&#39;s the best meal of the year! Long live sugar season!&quot;)</em></p>

<h3 id="h-19-4-cdn-culture">19.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Le temps des sucres&quot;</strong> (sugar season) runs from late February to April, when maple sap flows. Quebec produces about 70% of the world&#39;s maple syrup!</li>
<li><strong>&quot;Bonhomme Carnaval&quot;</strong> is the iconic snowman mascot of the Quebec Winter Carnival.</li>
<li><strong>&quot;La Saint-Jean&quot;</strong> (June 24) is Quebec&#39;s national holiday – not Canada Day (July 1). It is a very important day of celebration and pride for Quebecers.</li>
<li><strong>&quot;Les Canadiens&quot;</strong> or <strong>&quot;le CH&quot;</strong> or <strong>&quot;le Tricolore&quot;</strong> are all names for the Montreal Canadiens hockey team.</li>
</ul>
<hr>

<h2 id="h-unit-20-review-b1">UNIT 20: REVIEW &amp; B1 PREPARATION</h2>

<h3 id="h-20-1-grammar-review">20.1 Grammar Review</h3>
<p>Here is a summary of the key grammar concepts covered in A2:</p>
<table>
<thead><tr><th>Concept</th><th>Formation</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Imparfait</td><td>nous stem + endings (-ais, -ais, -ait, -ions, -iez, -aient)</td><td>Je parlais français quand j&#39;étais petit. (I used to speak French when I was little.)</td></tr>
<tr><td>Futur simple</td><td>infinitive + endings (-ai, -as, -a, -ons, -ez, -ont)</td><td>Demain, j&#39;irai au marché. (Tomorrow, I will go to the market.)</td></tr>
<tr><td>Passé récent</td><td>venir de + infinitive</td><td>Je viens d&#39;arriver. (I just arrived.)</td></tr>
<tr><td>En train de</td><td>être en train de + infinitive</td><td>Je suis en train de manger. (I am eating.)</td></tr>
<tr><td>Impératif</td><td>conjugated verb (no subject pronoun)</td><td>Mange! Mangeons! Mangez! (Eat!)</td></tr>
<tr><td>Comparatif</td><td>plus/moins/aussi + adj. + que</td><td>Montréal est plus grande que Québec. (Montreal is bigger than Quebec City.)</td></tr>
<tr><td>Superlatif</td><td>le/la/les plus/moins + adj.</td><td>C&#39;est le plus beau parc de la ville. (It&#39;s the most beautiful park in the city.)</td></tr>
</tbody></table>

<h3 id="h-20-2-vocab-review">20.2 Vocabulary Review</h3>
<p>At the end of A2, you should be comfortable with vocabulary in these areas:</p>
<ul>
<li><strong>Shopping &amp; money:</strong> stores, prices, clothing, payments</li>
<li><strong>Housing:</strong> rooms, furniture, renting, moving</li>
<li><strong>Transportation:</strong> vehicles, directions, public transit</li>
<li><strong>Weather &amp; seasons:</strong> temperatures, forecasts, Quebec climate</li>
<li><strong>Social life:</strong> invitations, phone calls, events</li>
<li><strong>Health:</strong> body parts, symptoms, doctor visits</li>
<li><strong>Services:</strong> banking, administration, emergencies</li>
<li><strong>Travel &amp; culture:</strong> booking, hotels, airports, Quebec traditions</li>
</ul>

<h3 id="h-20-3-b1-preview">20.3 What to Expect at B1</h3>
<p>At B1, you will learn to:</p>
<ul>
<li>Express opinions and argue a point of view using more complex structures.</li>
<li>Use the <strong>subjonctif</strong> and <strong>conditionnel</strong> to express wishes, doubts, and hypotheses.</li>
<li>Understand and discuss media, news, and current events in Quebec and the francophone world.</li>
<li>Write longer texts: formal letters, reports, and essays.</li>
<li>Talk about abstract topics like the environment, politics, and society.</li>
</ul>

<h3 id="h-20-4-study-tips">20.4 Study Tips</h3>
<ul>
<li><strong>Regardez des séries québécoises</strong> comme &quot;Série noire,&quot; &quot;Les Invincibles,&quot; ou &quot;District 31&quot; pour vous habituer à l&#39;accent et aux expressions. (Watch Québécois TV shows to get used to the accent and expressions.)</li>
<li><strong>Écoutez la radio de Radio-Canada</strong> (ICI Première) pour entendre du français québécois dans des contextes variés. (Listen to Radio-Canada radio to hear Quebec French in various contexts.)</li>
<li><strong>Pratiquez avec des Québécois.</strong> Ne soyez pas timide! Les Québécois sont généralement très patients et contents quand quelqu&#39;un essaie de parler français. (Practice with Quebecers. Don&#39;t be shy! Quebecers are generally very patient and happy when someone tries to speak French.)</li>
<li><strong>Tenez un journal en français.</strong> Écrivez quelques phrases chaque jour sur ce que vous avez fait. (Keep a journal in French. Write a few sentences each day about what you did.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Reflecting on Your French Learning Journey:</strong></p>
<p><em>Vous parlez avec votre professeur de français à la fin du cours A2.</em></p>
<p>&quot;Félicitations! Tu as terminé le niveau A2! Comment tu te sens?&quot;<br>&quot;Je suis vraiment content! Au début, je comprenais presque rien quand les gens parlaient vite.&quot;<br>&quot;Et maintenant?&quot;<br>&quot;Maintenant, je suis capable de suivre une conversation normale et de me débrouiller au magasin, au restaurant et au téléphone.&quot;<br>&quot;C&#39;est excellent! Tu es prêt pour le B1. Ça va être plus difficile, mais tu as une bonne base.&quot;<br>&quot;Merci! J&#39;ai vraiment hâte de continuer. Le français québécois, c&#39;est vraiment le fun à apprendre!&quot;</p>
<p><em>(You are talking with your French teacher at the end of the A2 course. &quot;Congratulations! You have finished the A2 level! How do you feel?&quot; &quot;I&#39;m really happy! In the beginning, I understood almost nothing when people spoke fast.&quot; &quot;And now?&quot; &quot;Now, I am able to follow a normal conversation and manage at the store, the restaurant, and on the phone.&quot; &quot;That&#39;s excellent! You are ready for B1. It will be more difficult, but you have a good foundation.&quot; &quot;Thank you! I really can&#39;t wait to continue. Quebec French is really fun to learn!&quot;)</em></p>
<hr>

<h1 id="h-a2-conclusion">CONCLUSION</h1>
<p>Congratulations on completing the A2 level! You now have a solid foundation in everyday Canadian French. You can handle basic conversations about daily life, navigate shopping, transportation, and health situations, and appreciate Quebec&#39;s rich culture and traditions.</p>
<p>Your next step is B1, where you will deepen your grammar, expand your expression, and begin tackling more complex topics. <strong>Bonne continuation et lâche pas!</strong> (Keep going and don&#39;t give up!)</p>

            </div>
        </main>
    </div>
    <script>
""" + js_block + """
    </script>
</body>
</html>
"""

with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write(content)

print(f"A2 COMPLETE. Final file size: {os.path.getsize(OUTPUT)} bytes")
