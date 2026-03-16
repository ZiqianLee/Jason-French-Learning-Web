#!/usr/bin/env python3
"""Generate A2 HTML - Part 3: Units 5-10"""
import os
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2.html")

content = """
<h2 id="h-unit-5-shopping">UNIT 5: SHOPPING &amp; MONEY</h2>

<h3 id="h-5-1-store-vocabulary">5.1 Store Vocabulary</h3>
<p>Quebec has its own distinct shopping vocabulary. Here are essential words for shopping in la Belle Province:</p>
<table>
<thead><tr><th>French (Quebec)</th><th>French (France)</th><th>English</th></tr></thead>
<tbody>
<tr><td>le magasin</td><td>le magasin</td><td>store/shop</td></tr>
<tr><td>le dépanneur</td><td>l&#39;épicerie de quartier</td><td>corner store / convenience store</td></tr>
<tr><td>le centre d&#39;achats</td><td>le centre commercial</td><td>shopping mall</td></tr>
<tr><td>la pharmacie</td><td>la pharmacie</td><td>pharmacy</td></tr>
<tr><td>la quincaillerie</td><td>le magasin de bricolage</td><td>hardware store</td></tr>
<tr><td>la tabagie</td><td>le bureau de tabac</td><td>tobacco / magazine shop</td></tr>
<tr><td>la buanderie</td><td>la laverie</td><td>laundromat</td></tr>
<tr><td>la SAQ</td><td>le caviste</td><td>liquor store (Société des alcools du Québec)</td></tr>
<tr><td>les aubaines</td><td>les soldes</td><td>sales / bargains</td></tr>
<tr><td>le spécial</td><td>la promotion</td><td>sale / special offer</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>Je vais au centre d&#39;achats pour trouver un cadeau d&#39;anniversaire pour ma mère.</strong> (I&#39;m going to the mall to find a birthday gift for my mother.)</li>
<li><strong>Il y a de bonnes aubaines au Canadian Tire cette semaine sur les outils de jardinage.</strong> (There are good sales at Canadian Tire this week on garden tools.)</li>
<li><strong>Est-ce que tu peux passer au dépanneur me chercher un sac de lait?</strong> (Can you stop by the corner store to get me a bag of milk?)</li>
</ul>

<h3 id="h-5-2-asking-prices">5.2 Asking About Prices</h3>
<p><strong>Useful phrases:</strong></p>
<ul>
<li><strong>Combien ça coûte?</strong> (How much does it cost?)</li>
<li><strong>C&#39;est combien?</strong> (How much is it?)</li>
<li><strong>Ça fait combien en tout?</strong> (How much is it in total?)</li>
<li><strong>Est-ce que c&#39;est en spécial?</strong> (Is it on sale?) – Québécois expression</li>
<li><strong>Avez-vous quelque chose de moins cher?</strong> (Do you have something cheaper?)</li>
<li><strong>C&#39;est trop cher pour moi, malheureusement.</strong> (It&#39;s too expensive for me, unfortunately.)</li>
</ul>

<p><strong>Talking about prices:</strong></p>
<ul>
<li><strong>Ça coûte vingt-cinq dollars et quarante-neuf sous.</strong> (It costs twenty-five dollars and forty-nine cents.) – Note: In Quebec, &quot;sous&quot; = cents.</li>
<li><strong>Les taxes ne sont pas incluses dans le prix affiché au Québec.</strong> (Taxes are not included in the displayed price in Quebec.)</li>
<li><strong>La TPS est de cinq pour cent et la TVQ est de 9,975 pour cent.</strong> (The GST is five percent and the QST is 9.975 percent.)</li>
</ul>

<h3 id="h-5-3-clothing">5.3 Clothing &amp; Sizes</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un chandail</td><td>a sweater (QC) / un pull (FR)</td></tr>
<tr><td>un manteau d&#39;hiver</td><td>a winter coat</td></tr>
<tr><td>des bas</td><td>socks (QC) / des chaussettes (FR)</td></tr>
<tr><td>des souliers</td><td>shoes (QC) / des chaussures (FR)</td></tr>
<tr><td>une tuque</td><td>a winter hat / beanie (QC)</td></tr>
<tr><td>des mitaines</td><td>mittens (QC) / des moufles (FR)</td></tr>
<tr><td>un pantalon</td><td>pants / trousers</td></tr>
<tr><td>une robe</td><td>a dress</td></tr>
<tr><td>une jupe</td><td>a skirt</td></tr>
<tr><td>des bottes</td><td>boots</td></tr>
</tbody></table>

<p><strong>Trying on clothes:</strong></p>
<ul>
<li><strong>Est-ce que je peux essayer cette robe en taille moyen, s&#39;il vous plaît?</strong> (Can I try on this dress in medium, please?)</li>
<li><strong>C&#39;est trop petit. Avez-vous la taille au-dessus?</strong> (It&#39;s too small. Do you have the next size up?)</li>
<li><strong>Où sont les cabines d&#39;essayage?</strong> (Where are the fitting rooms?)</li>
</ul>

<h3 id="h-5-4-paying">5.4 Paying &amp; Transactions</h3>
<ul>
<li><strong>Je vais payer par carte de débit, s&#39;il vous plaît.</strong> (I will pay by debit card, please.)</li>
<li><strong>Acceptez-vous les cartes de crédit?</strong> (Do you accept credit cards?)</li>
<li><strong>Je voudrais un reçu, s&#39;il vous plaît.</strong> (I would like a receipt, please.)</li>
<li><strong>Est-ce que je peux retourner cet article si ça ne fait pas?</strong> (Can I return this item if it doesn&#39;t fit?)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Shopping at the Centre d&#39;achats:</strong></p>
<p><em>Vous êtes dans un magasin de vêtements au centre d&#39;achats Laurier à Québec.</em></p>
<p>&quot;Bonjour! Est-ce que je peux vous aider?&quot;<br>&quot;Oui, je cherche un chandail chaud pour l&#39;hiver. Quelque chose en laine, si possible.&quot;<br>&quot;Bien sûr! On a de beaux chandails en laine mérinos. Quelle taille faites-vous?&quot;<br>&quot;Je fais du moyen, habituellement. C&#39;est combien, celui-ci?&quot;<br>&quot;Il est à soixante-quinze dollars, mais il est en spécial cette semaine à cinquante-cinq.&quot;<br>&quot;Parfait! Je vais l&#39;essayer. Où sont les cabines?&quot;<br>&quot;Juste au fond, à droite.&quot;</p>
<p><em>(You are in a clothing store at the Laurier shopping centre in Quebec City. &quot;Hello! Can I help you?&quot; &quot;Yes, I&#39;m looking for a warm sweater for winter. Something wool, if possible.&quot; &quot;Of course! We have beautiful merino wool sweaters. What size are you?&quot; &quot;I&#39;m usually a medium. How much is this one?&quot; &quot;It&#39;s seventy-five dollars, but it&#39;s on sale this week for fifty-five.&quot; &quot;Perfect! I&#39;ll try it on. Where are the fitting rooms?&quot; &quot;Right at the back, on the right.&quot;)</em></p>

<h3 id="h-5-5-cdn-shopping">5.5 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Magasiner&quot;</strong> means &quot;to shop&quot; in Quebec French. In France, they say <strong>&quot;faire du shopping&quot;</strong> or <strong>&quot;faire les boutiques.&quot;</strong></li>
<li>Prices in Quebec are in <strong>Canadian dollars (CAD)</strong>. Remember that taxes (TPS + TVQ ≈ 15%) are added at the register, not included in the price tag.</li>
<li><strong>&quot;Un sac de lait&quot;</strong> (a bag of milk) – Milk comes in bags in Quebec, not just in cartons!</li>
<li><strong>&quot;Piastre&quot;</strong> is informal Québécois for &quot;dollar&quot;: <strong>&quot;Ça coûte dix piastres.&quot;</strong> (It costs ten bucks.)</li>
</ul>
<hr>

<h2 id="h-unit-6-housing">UNIT 6: HOUSING &amp; HOME</h2>

<h3 id="h-6-1-rooms">6.1 Rooms &amp; Furniture</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>la cuisine</td><td>the kitchen</td></tr>
<tr><td>le salon</td><td>the living room</td></tr>
<tr><td>la chambre à coucher</td><td>the bedroom</td></tr>
<tr><td>la salle de bain</td><td>the bathroom</td></tr>
<tr><td>la salle à manger</td><td>the dining room</td></tr>
<tr><td>le sous-sol</td><td>the basement</td></tr>
<tr><td>le grenier</td><td>the attic</td></tr>
<tr><td>le balcon</td><td>the balcony</td></tr>
<tr><td>le corridor / le couloir</td><td>the hallway</td></tr>
<tr><td>le garde-robe</td><td>the closet (QC) / le placard (FR)</td></tr>
</tbody></table>

<p><strong>Furniture:</strong></p>
<ul>
<li><strong>un divan</strong> – a couch (QC) / un canapé (FR)</li>
<li><strong>un lit</strong> – a bed</li>
<li><strong>une commode</strong> – a dresser</li>
<li><strong>une table de cuisine</strong> – a kitchen table</li>
<li><strong>un poêle</strong> – a stove (QC) / une cuisinière (FR)</li>
<li><strong>un frigidaire / un frigo</strong> – a fridge</li>
<li><strong>une laveuse</strong> – a washing machine (QC) / un lave-linge (FR)</li>
<li><strong>une sécheuse</strong> – a dryer (QC) / un sèche-linge (FR)</li>
</ul>

<h3 id="h-6-2-describing-home">6.2 Describing Your Home</h3>
<ul>
<li><strong>J&#39;habite dans un quatre et demie au deuxième étage d&#39;un triplex dans le quartier Rosemont.</strong> (I live in a 4½ apartment on the second floor of a triplex in the Rosemont neighbourhood.)</li>
<li><strong>Notre maison a trois chambres, deux salles de bain et un grand sous-sol fini.</strong> (Our house has three bedrooms, two bathrooms, and a large finished basement.)</li>
<li><strong>L&#39;appartement est lumineux avec de grandes fenêtres qui donnent sur le parc.</strong> (The apartment is bright with large windows overlooking the park.)</li>
</ul>

<p><strong>Quebec apartment numbering:</strong> In Quebec, apartments are measured by the number of rooms plus a half (the bathroom). A <strong>trois et demie (3½)</strong> has a kitchen, living room, one bedroom, and one bathroom. A <strong>cinq et demie (5½)</strong> has a kitchen, living room, three bedrooms, and a bathroom.</p>

<h3 id="h-6-3-renting">6.3 Renting an Apartment</h3>
<p><strong>Key vocabulary:</strong></p>
<ul>
<li><strong>un bail</strong> – a lease</li>
<li><strong>le loyer</strong> – the rent</li>
<li><strong>le propriétaire</strong> – the landlord</li>
<li><strong>le locataire</strong> – the tenant</li>
<li><strong>les charges / les services inclus</strong> – utilities included</li>
<li><strong>un déménagement</strong> – a move</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Apartment Hunting in Montreal:</strong></p>
<p><em>Vous cherchez un appartement à Montréal et vous appelez un propriétaire.</em></p>
<p>&quot;Bonjour, j&#39;appelle pour le quatre et demie sur la rue Saint-Denis. Est-ce qu&#39;il est encore disponible?&quot;<br>&quot;Oui, il est toujours disponible! Le loyer est de neuf cent cinquante par mois.&quot;<br>&quot;Est-ce que le chauffage et l&#39;eau chaude sont inclus?&quot;<br>&quot;Oui, le chauffage est inclus, mais l&#39;électricité est à votre charge.&quot;<br>&quot;D&#39;accord. Est-ce que je pourrais visiter l&#39;appartement samedi matin?&quot;<br>&quot;Bien sûr! À dix heures, ça vous va?&quot;<br>&quot;Parfait, à samedi!&quot;</p>
<p><em>(You are looking for an apartment in Montreal and you call a landlord. &quot;Hello, I&#39;m calling about the 4½ on Saint-Denis Street. Is it still available?&quot; &quot;Yes, it&#39;s still available! The rent is nine hundred and fifty a month.&quot; &quot;Is the heating and hot water included?&quot; &quot;Yes, the heating is included, but electricity is at your expense.&quot; &quot;Okay. Could I visit the apartment Saturday morning?&quot; &quot;Of course! At ten, does that work for you?&quot; &quot;Perfect, see you Saturday!&quot;)</em></p>

<h3 id="h-6-4-cdn-housing">6.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, <strong>July 1st</strong> is traditionally <strong>&quot;le jour du déménagement&quot;</strong> (moving day), when most leases end and begin. Thousands of Quebecers move on the same day!</li>
<li>The <strong>&quot;Régie du logement&quot;</strong> (now called the <strong>Tribunal administratif du logement</strong>) is the government body that protects tenant rights in Quebec.</li>
<li><strong>&quot;Un bloc&quot;</strong> is Québécois for &quot;un immeuble d&#39;appartements&quot; (an apartment building).</li>
</ul>
<hr>

<h2 id="h-unit-7-transport">UNIT 7: TRANSPORTATION &amp; DIRECTIONS</h2>

<h3 id="h-7-1-transport-vocab">7.1 Transportation Vocabulary</h3>
<table>
<thead><tr><th>French (Quebec)</th><th>English</th></tr></thead>
<tbody>
<tr><td>un char / une auto</td><td>a car</td></tr>
<tr><td>un autobus</td><td>a bus</td></tr>
<tr><td>le métro</td><td>the subway</td></tr>
<tr><td>un bicycle / un vélo</td><td>a bicycle</td></tr>
<tr><td>le train de banlieue</td><td>the commuter train</td></tr>
<tr><td>un taxi</td><td>a taxi</td></tr>
<tr><td>le traversier</td><td>the ferry (QC) / le ferry (FR)</td></tr>
<tr><td>une motoneige</td><td>a snowmobile</td></tr>
<tr><td>un VUS</td><td>an SUV</td></tr>
<tr><td>un permis de conduire</td><td>a driver&#39;s licence</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>Je prends le métro tous les matins pour aller travailler au centre-ville de Montréal.</strong> (I take the metro every morning to go to work downtown Montreal.)</li>
<li><strong>En hiver, beaucoup de Québécois utilisent leurs motoneiges pour se déplacer dans les régions rurales.</strong> (In winter, many Quebecers use their snowmobiles to get around in rural areas.)</li>
</ul>

<h3 id="h-7-2-giving-directions">7.2 Giving &amp; Asking Directions</h3>
<ul>
<li><strong>Excusez-moi, comment est-ce que je peux me rendre à la gare centrale?</strong> (Excuse me, how can I get to the central station?)</li>
<li><strong>Tournez à gauche au prochain feu de circulation, puis continuez tout droit pendant deux coins de rue.</strong> (Turn left at the next traffic light, then continue straight for two blocks.)</li>
<li><strong>C&#39;est juste en face de la pharmacie Jean Coutu, à côté du dépanneur.</strong> (It&#39;s right across from the Jean Coutu pharmacy, next to the corner store.)</li>
</ul>

<p><strong>Direction vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>tout droit</td><td>straight ahead</td></tr>
<tr><td>à gauche</td><td>to the left</td></tr>
<tr><td>à droite</td><td>to the right</td></tr>
<tr><td>au coin de</td><td>at the corner of</td></tr>
<tr><td>en face de</td><td>across from</td></tr>
<tr><td>à côté de</td><td>next to</td></tr>
<tr><td>le feu de circulation</td><td>traffic light (QC) / le feu rouge (FR)</td></tr>
<tr><td>un coin de rue</td><td>a street corner / block (QC)</td></tr>
</tbody></table>

<h3 id="h-7-3-public-transit">7.3 Public Transit in Quebec</h3>
<p>Montreal has an extensive public transit system operated by the <strong>STM</strong> (Société de transport de Montréal):</p>
<ul>
<li><strong>Le métro de Montréal a quatre lignes: la verte, l&#39;orange, la bleue et la jaune.</strong> (The Montreal metro has four lines: the green, orange, blue, and yellow.)</li>
<li><strong>Une carte OPUS est nécessaire pour prendre le métro et l&#39;autobus à Montréal.</strong> (An OPUS card is needed to take the metro and bus in Montreal.)</li>
<li><strong>Le REM est un nouveau train léger qui relie la Rive-Sud au centre-ville et à l&#39;aéroport.</strong> (The REM is a new light rail that connects the South Shore to downtown and the airport.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Taking the Bus in Laval:</strong></p>
<p><em>Vous êtes à un arrêt d&#39;autobus à Laval et vous demandez de l&#39;aide à un passant.</em></p>
<p>&quot;Excusez-moi, est-ce que le 55 passe par ici?&quot;<br>&quot;Non, le 55, c&#39;est l&#39;arrêt de l&#39;autre côté de la rue. Ici, c&#39;est le 42.&quot;<br>&quot;Merci! Est-ce que le 42 va au métro Montmorency?&quot;<br>&quot;Oui, le 42 s&#39;arrête juste devant le métro. Ça prend environ quinze minutes.&quot;<br>&quot;Super, merci beaucoup!&quot;</p>
<p><em>(You are at a bus stop in Laval and you ask a passerby for help. &quot;Excuse me, does the 55 pass through here?&quot; &quot;No, the 55 is the stop on the other side of the street. This one is the 42.&quot; &quot;Thank you! Does the 42 go to Montmorency metro?&quot; &quot;Yes, the 42 stops right in front of the metro. It takes about fifteen minutes.&quot; &quot;Great, thank you very much!&quot;)</em></p>

<h3 id="h-7-4-cdn-transport">7.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Embarquer&quot;</strong> means &quot;to get on&quot; (a bus, car) in Quebec. In France, they say <strong>&quot;monter dans.&quot;</strong> Example: <strong>&quot;Embarque dans le char!&quot;</strong> (Get in the car!)</li>
<li><strong>&quot;Débarquer&quot;</strong> means &quot;to get off&quot;: <strong>&quot;Je débarque au prochain arrêt.&quot;</strong> (I&#39;m getting off at the next stop.)</li>
<li>In Quebec, winter driving is serious. <strong>&quot;Les pneus d&#39;hiver&quot;</strong> (winter tires) are mandatory by law from December 1 to March 15.</li>
</ul>
<hr>

<h2 id="h-unit-8-weather">UNIT 8: WEATHER &amp; CLIMATE</h2>

<h3 id="h-8-1-weather-vocab">8.1 Weather Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Il fait beau.</td><td>The weather is nice.</td></tr>
<tr><td>Il fait chaud.</td><td>It&#39;s hot.</td></tr>
<tr><td>Il fait froid. / Il fait frette. (QC)</td><td>It&#39;s cold.</td></tr>
<tr><td>Il pleut.</td><td>It&#39;s raining.</td></tr>
<tr><td>Il neige.</td><td>It&#39;s snowing.</td></tr>
<tr><td>Il vente. (QC) / Il y a du vent.</td><td>It&#39;s windy.</td></tr>
<tr><td>Il y a un orage.</td><td>There is a storm.</td></tr>
<tr><td>Il y a du verglas.</td><td>There is freezing rain / black ice.</td></tr>
<tr><td>une tempête de neige</td><td>a snowstorm / blizzard</td></tr>
<tr><td>la poudrerie</td><td>blowing snow (QC)</td></tr>
<tr><td>le facteur vent / éolien</td><td>wind chill factor</td></tr>
</tbody></table>

<h3 id="h-8-2-describing-weather">8.2 Describing the Weather</h3>
<ul>
<li><strong>Aujourd&#39;hui, il fait moins quinze avec le facteur éolien. C&#39;est dangereux de rester dehors trop longtemps.</strong> (Today, it&#39;s minus fifteen with the wind chill. It&#39;s dangerous to stay outside too long.)</li>
<li><strong>Demain, on annonce une grosse tempête de neige avec trente centimètres de neige.</strong> (Tomorrow, they&#39;re forecasting a big snowstorm with thirty centimetres of snow.)</li>
<li><strong>En été à Montréal, il fait souvent trente degrés avec beaucoup d&#39;humidité.</strong> (In summer in Montreal, it&#39;s often thirty degrees with a lot of humidity.)</li>
</ul>

<h3 id="h-8-3-seasons-quebec">8.3 Seasons in Quebec</h3>
<p>Quebec has dramatically different seasons:</p>
<ul>
<li><strong>L&#39;hiver</strong> (Winter: November-March): Very cold, lots of snow. <strong>L&#39;hiver québécois est long et rigoureux, avec des températures qui peuvent descendre à moins quarante degrés.</strong> (Quebec winter is long and harsh, with temperatures that can drop to minus forty degrees.)</li>
<li><strong>Le printemps</strong> (Spring: April-May): Maple syrup season! <strong>Au printemps, on va à la cabane à sucre pour manger de la tire d&#39;érable.</strong> (In spring, we go to the sugar shack to eat maple taffy.)</li>
<li><strong>L&#39;été</strong> (Summer: June-August): Festival season. <strong>L&#39;été à Montréal est rempli de festivals: le Festival de jazz, Juste pour rire, et Osheaga.</strong> (Summer in Montreal is full of festivals: the Jazz Festival, Just for Laughs, and Osheaga.)</li>
<li><strong>L&#39;automne</strong> (Fall: September-October): Beautiful foliage. <strong>Les couleurs d&#39;automne dans les Laurentides sont spectaculaires avec le rouge, l&#39;orange et le jaune des érables.</strong> (The autumn colours in the Laurentians are spectacular with the red, orange, and yellow of the maples.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Winter Day in Saguenay:</strong></p>
<p><em>Vous regardez les nouvelles à la télé un matin d&#39;hiver.</em></p>
<p>&quot;Il fait moins vingt-cinq ce matin au Saguenay avec un facteur éolien de moins trente-huit.&quot;<br>&quot;Mon Dieu! C&#39;est frette en maudit! Je ne sors pas de la maison aujourd&#39;hui.&quot;<br>&quot;On annonce aussi de la poudrerie cet après-midi. Les routes vont être dangereuses.&quot;<br>&quot;J&#39;espère qu&#39;ils vont fermer les écoles. Les autobus scolaires ne devraient pas rouler par un temps pareil.&quot;<br>&quot;Tu as raison. Restons au chaud et faisons du chocolat chaud!&quot;</p>
<p><em>(You are watching the news on TV on a winter morning. &quot;It&#39;s minus twenty-five this morning in Saguenay with a wind chill of minus thirty-eight.&quot; &quot;My God! It&#39;s really cold! I&#39;m not leaving the house today.&quot; &quot;They&#39;re also calling for blowing snow this afternoon. The roads will be dangerous.&quot; &quot;I hope they close the schools. School buses shouldn&#39;t run in weather like this.&quot; &quot;You&#39;re right. Let&#39;s stay warm and make hot chocolate!&quot;)</em></p>

<h3 id="h-8-4-cdn-weather">8.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Frette&quot;</strong> is the Québécois word for &quot;very cold&quot;. Standard French uses &quot;froid.&quot;</li>
<li><strong>&quot;Y mouille&quot;</strong> means &quot;it&#39;s raining&quot; in informal Quebec French (instead of &quot;il pleut&quot;).</li>
<li>Quebec uses <strong>Celsius</strong>, not Fahrenheit. Zero degrees Celsius is the freezing point.</li>
<li><strong>&quot;La sloche&quot;</strong> (from English &quot;slush&quot;) is the wet, slushy snow on the streets in spring.</li>
</ul>
<hr>

<h2 id="h-unit-9-invitations">UNIT 9: INVITATIONS &amp; EVENTS</h2>

<h3 id="h-9-1-inviting">9.1 Inviting Someone</h3>
<p><strong>Formal invitations:</strong></p>
<ul>
<li><strong>Est-ce que vous aimeriez venir souper chez nous samedi soir?</strong> (Would you like to come for dinner at our place Saturday evening?)</li>
<li><strong>Nous organisons une fête pour l&#39;anniversaire de Marie. Seriez-vous disponible le 15 mars?</strong> (We are organizing a party for Marie&#39;s birthday. Would you be available on March 15th?)</li>
</ul>
<p><strong>Informal invitations:</strong></p>
<ul>
<li><strong>Hey, ça te tente de venir prendre une bière tantôt?</strong> (Hey, do you feel like coming over for a beer later?)</li>
<li><strong>On va chez Alexandre ce soir. Tu viens-tu?</strong> (We&#39;re going to Alexandre&#39;s tonight. Are you coming?)</li>
<li><strong>Ça te dit d&#39;aller au cinéma après le souper?</strong> (Do you feel like going to the movies after dinner?)</li>
</ul>

<h3 id="h-9-2-accepting-declining">9.2 Accepting &amp; Declining</h3>
<p><strong>Accepting:</strong></p>
<ul>
<li><strong>Oui, avec plaisir! À quelle heure est-ce qu&#39;on se retrouve?</strong> (Yes, with pleasure! What time do we meet?)</li>
<li><strong>Bonne idée! J&#39;apporte quelque chose? Du vin ou un dessert?</strong> (Good idea! Should I bring something? Wine or a dessert?)</li>
<li><strong>Super! J&#39;ai ben hâte!</strong> (Great! I can&#39;t wait!) – &quot;ben&quot; = &quot;bien&quot; in Quebec</li>
</ul>
<p><strong>Declining politely:</strong></p>
<ul>
<li><strong>C&#39;est vraiment gentil, mais malheureusement je ne peux pas ce jour-là.</strong> (That&#39;s really kind, but unfortunately I can&#39;t that day.)</li>
<li><strong>J&#39;aurais bien aimé, mais j&#39;ai déjà quelque chose de prévu.</strong> (I would have liked to, but I already have something planned.)</li>
<li><strong>Peut-être une prochaine fois? Je suis libre la semaine prochaine.</strong> (Maybe next time? I&#39;m free next week.)</li>
</ul>

<h3 id="h-9-3-event-vocab">9.3 Event Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>une fête</td><td>a party</td></tr>
<tr><td>un party (QC)</td><td>a party (informal, from English)</td></tr>
<tr><td>un spectacle</td><td>a show / performance</td></tr>
<tr><td>un souper entre amis</td><td>a dinner party with friends</td></tr>
<tr><td>un épluchette de blé d&#39;Inde</td><td>a corn roast (QC tradition)</td></tr>
<tr><td>un BBQ</td><td>a barbecue</td></tr>
<tr><td>un 5 à 7</td><td>a happy hour / after-work drinks (QC)</td></tr>
</tbody></table>

<p><strong>🇫🇷 Real-Life Scene – Planning a Surprise Party:</strong></p>
<p><em>Vous organisez une fête surprise pour votre ami.</em></p>
<p>&quot;Psst! On organise un party surprise pour Guillaume. C&#39;est sa fête vendredi!&quot;<br>&quot;Ah oui? Super! Qu&#39;est-ce que je peux apporter?&quot;<br>&quot;Si tu pouvais apporter un gâteau, ça serait parfait. Moi, je m&#39;occupe des décorations.&quot;<br>&quot;D&#39;accord! À quelle heure?&quot;<br>&quot;Arrive à sept heures. Guillaume va arriver vers sept heures et demie. On va tous crier &#39;Surprise!&#39; quand il va ouvrir la porte.&quot;<br>&quot;Ha ha, il ne se doute de rien! Ça va être tellement drôle!&quot;</p>
<p><em>(You are organizing a surprise party for your friend. &quot;Hey! We&#39;re organizing a surprise party for Guillaume. It&#39;s his birthday Friday!&quot; &quot;Oh really? Great! What can I bring?&quot; &quot;If you could bring a cake, that would be perfect. I&#39;m taking care of the decorations.&quot; &quot;Okay! What time?&quot; &quot;Arrive at seven. Guillaume is going to arrive around seven thirty. We&#39;re all going to yell &#39;Surprise!&#39; when he opens the door.&quot; &quot;Ha ha, he doesn&#39;t suspect anything! It&#39;s going to be so funny!&quot;)</em></p>

<h3 id="h-9-4-cdn-invitations">9.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Ça te tente?&quot;</strong> is the most common way to invite someone informally in Quebec. It literally means &quot;Does it tempt you?&quot;</li>
<li><strong>&quot;Un 5 à 7&quot;</strong> (cinq à sept) is a Québécois tradition – after-work socializing from 5 to 7 PM, often at a bar or restaurant.</li>
<li><strong>&quot;C&#39;est sa fête&quot;</strong> means &quot;It&#39;s his/her birthday&quot; in Quebec. In France, one more often says <strong>&quot;C&#39;est son anniversaire.&quot;</strong></li>
<li><strong>&quot;Avoir hâte&quot;</strong> means &quot;to look forward to&quot; or &quot;can&#39;t wait&quot;: <strong>&quot;J&#39;ai hâte à Noël!&quot;</strong> (I can&#39;t wait for Christmas!)</li>
</ul>
<hr>

<h2 id="h-unit-10-phone">UNIT 10: PHONE CALLS &amp; MESSAGES</h2>

<h3 id="h-10-1-phone-vocab">10.1 Phone Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un cellulaire (QC) / un portable (FR)</td><td>a cell phone</td></tr>
<tr><td>un texto / un message texte</td><td>a text message</td></tr>
<tr><td>un courriel (QC) / un e-mail (FR)</td><td>an email</td></tr>
<tr><td>la boîte vocale</td><td>voicemail</td></tr>
<tr><td>raccrocher</td><td>to hang up</td></tr>
<tr><td>appeler / téléphoner</td><td>to call</td></tr>
<tr><td>sonner</td><td>to ring</td></tr>
<tr><td>un indicatif régional</td><td>an area code</td></tr>
</tbody></table>

<h3 id="h-10-2-making-calls">10.2 Making &amp; Receiving Calls</h3>
<p><strong>Making a call:</strong></p>
<ul>
<li><strong>Allô, est-ce que je pourrais parler à Madame Tremblay, s&#39;il vous plaît?</strong> (Hello, could I speak to Mrs. Tremblay, please?)</li>
<li><strong>Bonjour, je voudrais prendre un rendez-vous avec le docteur Gagnon.</strong> (Hello, I would like to make an appointment with Dr. Gagnon.)</li>
<li><strong>C&#39;est de la part de qui?</strong> (Who is calling?) – Common question from the person answering.</li>
</ul>
<p><strong>Receiving a call:</strong></p>
<ul>
<li><strong>Allô?</strong> – Standard way to answer the phone in Quebec.</li>
<li><strong>Un instant, je vous le passe.</strong> (One moment, I&#39;ll put him/her on.)</li>
<li><strong>Il/Elle n&#39;est pas disponible en ce moment. Voulez-vous laisser un message?</strong> (He/She is not available right now. Would you like to leave a message?)</li>
</ul>

<h3 id="h-10-3-texting">10.3 Text Messages &amp; Email</h3>
<p><strong>Common texting abbreviations in French:</strong></p>
<table>
<thead><tr><th>Abbreviation</th><th>Full Form</th><th>English</th></tr></thead>
<tbody>
<tr><td>slt</td><td>salut</td><td>hi</td></tr>
<tr><td>stp / svp</td><td>s&#39;il te plaît / s&#39;il vous plaît</td><td>please</td></tr>
<tr><td>bcp</td><td>beaucoup</td><td>a lot / very much</td></tr>
<tr><td>mdr</td><td>mort de rire</td><td>LOL (dying of laughter)</td></tr>
<tr><td>pcq / pck</td><td>parce que</td><td>because</td></tr>
<tr><td>rdv</td><td>rendez-vous</td><td>appointment / meeting</td></tr>
<tr><td>dsl</td><td>désolé(e)</td><td>sorry</td></tr>
<tr><td>ajd</td><td>aujourd&#39;hui</td><td>today</td></tr>
</tbody></table>

<p><strong>Writing a simple email:</strong></p>
<p><strong>Objet:</strong> Demande de renseignements (Subject: Information request)</p>
<p><strong>Bonjour Madame Lavoie,</strong></p>
<p>Je vous écris pour demander des renseignements au sujet des cours de francisation offerts par votre organisme. Pourriez-vous m&#39;envoyer les horaires et les tarifs, s&#39;il vous plaît?</p>
<p>Merci beaucoup de votre aide.</p>
<p>Cordialement,<br>Jean Dupont</p>
<p><em>(Hello Mrs. Lavoie, I am writing to ask for information about the French classes offered by your organization. Could you send me the schedules and rates, please? Thank you very much for your help. Best regards, Jean Dupont)</em></p>

<p><strong>🇫🇷 Real-Life Scene – Calling to Book a Restaurant:</strong></p>
<p><em>Vous téléphonez pour réserver une table dans un restaurant à Gatineau.</em></p>
<p>&quot;Allô, Restaurant Le Pied de cochon, bonsoir!&quot;<br>&quot;Bonsoir! Je voudrais réserver une table pour quatre personnes pour vendredi soir, s&#39;il vous plaît.&quot;<br>&quot;Bien sûr! Pour quelle heure?&quot;<br>&quot;Dix-neuf heures, si c&#39;est possible.&quot;<br>&quot;Parfait! C&#39;est à quel nom?&quot;<br>&quot;Bélanger. B-É-L-A-N-G-E-R.&quot;<br>&quot;C&#39;est noté! À vendredi, Monsieur Bélanger!&quot;</p>
<p><em>(You call to reserve a table at a restaurant in Gatineau. &quot;Hello, Le Pied de cochon Restaurant, good evening!&quot; &quot;Good evening! I would like to reserve a table for four people for Friday evening, please.&quot; &quot;Of course! For what time?&quot; &quot;Seven PM, if possible.&quot; &quot;Perfect! Under what name?&quot; &quot;Bélanger. B-É-L-A-N-G-E-R.&quot; &quot;It&#39;s noted! See you Friday, Mr. Bélanger!&quot;)</em></p>

<h3 id="h-10-4-cdn-phone">10.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, the word <strong>&quot;courriel&quot;</strong> (from &quot;courrier électronique&quot;) is the official term for &quot;email.&quot; It was coined in Quebec and is now used in official documents across all of French-speaking Canada.</li>
<li>Phone numbers in Canada follow the format <strong>(514) 555-1234</strong>. Common Quebec area codes include: 514/438 (Montreal), 418/581 (Quebec City), 450/579 (suburbs), 819/873 (regional).</li>
<li>When spelling names on the phone, Quebecers sometimes use English letter names rather than the <strong>&quot;alphabet téléphonique&quot;</strong> (phonetic alphabet).</li>
</ul>
"""

with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write(content)

print(f"Part 3 (Units 5-10) done. File size: {os.path.getsize(OUTPUT)} bytes")
