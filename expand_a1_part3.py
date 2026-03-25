#!/usr/bin/env python3
"""Expand A1 Units 11-14 with more Quebec French content."""

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
    # UNIT 11: ADJECTIVES & AGREEMENT
    # =========================================================================

    marker_11_end = '<h2 id="h-unit-12-regular-verbs-er-ir-re">'
    new_11 = """
<p><strong>Quebec French Adjective Preferences and Expressions (🍁):</strong></p>
<p>Quebec French uses some adjectives differently from France French and has many unique descriptive expressions:</p>
<table>
<thead><tr><th>Quebec Expression</th><th>France French Equivalent</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>C'est écœurant!</td><td>C'est incroyable!</td><td>It's amazing! (positive SLANG)</td><td>"Le show était écœurant!" (The show was incredible!)</td></tr>
<tr><td>C'est malade!</td><td>C'est génial!</td><td>It's awesome! (slang)</td><td>"Ton nouveau char est malade!" (Your new car is awesome!)</td></tr>
<tr><td>C'est capotant!</td><td>C'est dingue/fou!</td><td>It's crazy/amazing!</td><td>"C'est capotant ce qu'y fait!" (What he does is insane!)</td></tr>
<tr><td>C'est plate</td><td>C'est ennuyeux</td><td>It's boring / It sucks</td><td>"Le film était plate." (The movie was boring.)</td></tr>
<tr><td>C'est poche</td><td>C'est nul</td><td>It sucks / It's bad</td><td>"C'est poche qu'y pleut." (It sucks that it's raining.)</td></tr>
<tr><td>C'est cute</td><td>C'est mignon</td><td>It's cute</td><td>"Le bébé est cute en titi!" (The baby is super cute!)</td></tr>
<tr><td>C'est hot</td><td>C'est cool/génial</td><td>It's cool/awesome</td><td>"C'est hot, ton projet!" (Your project is awesome!)</td></tr>
<tr><td>C'est tough</td><td>C'est difficile</td><td>It's tough/hard</td><td>"L'examen était tough!" (The exam was tough!)</td></tr>
<tr><td>C'est fin</td><td>C'est gentil</td><td>He/she is kind/nice</td><td>"T'es ben fin!" (You're really nice!)</td></tr>
<tr><td>C'est smatte</td><td>C'est gentil/intelligent</td><td>That's nice/smart</td><td>"C'est smatte de ta part." (That's nice of you.)</td></tr>
</tbody>
</table>
<p><strong>Quebec French Intensifiers (Making Adjectives Stronger) (🍁):</strong></p>
<p>Quebecers use different words to intensify adjectives than France French speakers:</p>
<table>
<thead><tr><th>Quebec Intensifier</th><th>France Equivalent</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>ben</td><td>très / bien</td><td>very / really</td><td>"C'est ben bon!" (It's really good!)</td></tr>
<tr><td>pas mal</td><td>assez / plutôt</td><td>quite / pretty</td><td>"C'est pas mal beau." (It's pretty nice.)</td></tr>
<tr><td>en masse</td><td>beaucoup / plein de</td><td>a lot / plenty</td><td>"Y'a du monde en masse!" (There are tons of people!)</td></tr>
<tr><td>en titi</td><td>vraiment / très</td><td>really (emphatic)</td><td>"Y fait frette en titi!" (It's really cold!)</td></tr>
<tr><td>en maudit</td><td>vraiment / extrêmement</td><td>really (strong emphasis)</td><td>"Chu fatigué en maudit!" (I'm really exhausted!)</td></tr>
<tr><td>à planche</td><td>à fond / au maximum</td><td>full blast / all out</td><td>"La musique joue à planche!" (The music is blasting!)</td></tr>
<tr><td>rare</td><td>très / tellement</td><td>so (intensifier)</td><td>"C'est rare bon!" (It's so good!)</td></tr>
<tr><td>full</td><td>très / complètement</td><td>totally / very</td><td>"C'est full beau!" (It's totally beautiful!)</td></tr>
</tbody>
</table>
<p><strong>Note on Quebec "Sacres" (Swear Words as Intensifiers):</strong></p>
<p>Quebec has a unique system of swear words derived from Catholic religious terms (tabernacle, calice, crisse, etc.). These are used as intensifiers in informal speech but are considered vulgar. As a beginner, be aware they exist but avoid using them – they can be very offensive in formal contexts. Think of them as equivalent to strong English swear words.</p>
<p><strong>Describing People in Quebec – Personality Adjectives:</strong></p>
<table>
<thead><tr><th>Quebec French</th><th>Standard French</th><th>English</th></tr></thead>
<tbody>
<tr><td>fin(e)</td><td>gentil(le)</td><td>kind, nice</td></tr>
<tr><td>smatte</td><td>intelligent(e) / gentil(le)</td><td>smart, nice</td></tr>
<tr><td>niaiseux / niaiseuse</td><td>bête / stupide</td><td>silly, foolish</td></tr>
<tr><td>gossant(e)</td><td>énervant(e) / agaçant(e)</td><td>annoying</td></tr>
<tr><td>tannant(e)</td><td>ennuyant(e) / agaçant(e)</td><td>annoying, tiresome</td></tr>
<tr><td>chialeux / chialeuse</td><td>râleur / râleuse</td><td>whiny, complaining</td></tr>
<tr><td>ratoureux / ratoureuse</td><td>rusé(e) / malin(e)</td><td>crafty, sly</td></tr>
<tr><td>grouillant(e)</td><td>énergique / actif(ve)</td><td>energetic, active</td></tr>
<tr><td>frais chié(e)</td><td>prétentieux / prétentieuse</td><td>stuck-up, snobbish (vulgar)</td></tr>
<tr><td>jasant(e)</td><td>bavard(e)</td><td>talkative, chatty</td></tr>
</tbody>
</table>
<p><strong>Describing Weather with Adjectives – Quebec Essentials:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example Sentence</th></tr></thead>
<tbody>
<tr><td>frette</td><td>cold (QC)</td><td>"Y fait frette en hiver au Québec." (It's cold in winter in Quebec.)</td></tr>
<tr><td>doux / doux</td><td>mild</td><td>"Pour janvier, c'est doux: juste moins cinq." (For January, it's mild: only minus five.)</td></tr>
<tr><td>humide</td><td>humid</td><td>"L'été montréalais est chaud et humide." (Montreal summers are hot and humid.)</td></tr>
<tr><td>venteux / venteuse</td><td>windy</td><td>"C'est toujours venteux à Québec en hiver." (It's always windy in Quebec City in winter.)</td></tr>
<tr><td>glacé(e)</td><td>icy</td><td>"Les trottoirs sont glacés ce matin." (The sidewalks are icy this morning.)</td></tr>
<tr><td>enneigé(e)</td><td>snow-covered</td><td>"Les rues sont enneigées après la tempête." (The streets are snow-covered after the storm.)</td></tr>
<tr><td>ensoleillé(e)</td><td>sunny</td><td>"C'est une belle journée ensoleillée!" (It's a beautiful sunny day!)</td></tr>
<tr><td>nuageux / nuageuse</td><td>cloudy</td><td>"C'est nuageux, mais y fait pas frette." (It's cloudy but not cold.)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Describing Your New Apartment in Quebec:</strong></p>
<p><em>Vous décrivez votre nouvel appartement à un ami.</em></p>
<p>"Comment est ton nouvel appart?"<br>"Y est pas mal beau! C'est un grand cinq et demie sur le Plateau."<br>"Cinq et demie, c'est quoi exactement?"<br>"C'est un appartement avec deux chambres, un salon, une cuisine et une salle de bain. Le demi, c'est la salle de bain."<br>"C'est grand! Y est-tu cher?"<br>"Pas pire. Je paye mille deux cents par mois. C'est correct pour le Plateau."<br>"T'as-tu un balcon?"<br>"Oui! Un beau grand balcon en arrière avec un escalier extérieur. C'est typiquement montréalais!"<br>"Pis le quartier?"<br>"C'est l'fun! Y'a plein de restos pis de cafés. Le parc La Fontaine est juste à côté. C'est parfait."</p>
<p><em>(You're describing your new apartment to a friend. "How's your new apartment?" "It's pretty nice! It's a large five-and-a-half on the Plateau." "What's a five-and-a-half exactly?" "It's an apartment with two bedrooms, a living room, a kitchen, and a bathroom. The 'half' is the bathroom." "That's big! Is it expensive?" "Not bad. I pay twelve hundred a month. That's okay for the Plateau." "Do you have a balcony?" "Yes! A nice big back balcony with an exterior staircase. Very typically Montreal!" "And the neighbourhood?" "It's fun! There are tonnes of restaurants and cafés. La Fontaine Park is right next door. It's perfect.")</em></p>
<p><strong>Note:</strong> In Quebec, apartments are measured by the number of rooms plus a "half" for the bathroom: a "3½" has one bedroom + living room + kitchen + bathroom. A "5½" has two bedrooms + living room + kitchen + dining room + bathroom.</p>

"""
    html = insert_before(html, marker_11_end, new_11)

    # =========================================================================
    # UNIT 12: REGULAR VERBS (-ER, -IR, -RE)
    # =========================================================================

    marker_12_end = '<h1 id="h-part-iv-daily-communication">'
    new_12 = """
<p><strong>Quebec French Verb Usage – Key Differences (🍁):</strong></p>
<p>While verb conjugation rules are identical, Quebec French has notable differences in which verbs are used and how they're pronounced:</p>
<table>
<thead><tr><th>Quebec Verb</th><th>France Equivalent</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>barrer</td><td>verrouiller / fermer à clé</td><td>to lock</td><td>"Barre la porte!" (Lock the door!)</td></tr>
<tr><td>débarrer</td><td>déverrouiller</td><td>to unlock</td><td>"Débarre la porte, j'arrive!" (Unlock the door, I'm coming!)</td></tr>
<tr><td>magasiner</td><td>faire du shopping</td><td>to shop</td><td>"On va magasiner à Place Laurier." (We're going shopping at Place Laurier.)</td></tr>
<tr><td>jaser</td><td>bavarder / discuter</td><td>to chat</td><td>"On a jasé pendant des heures." (We chatted for hours.)</td></tr>
<tr><td>placoter</td><td>bavarder</td><td>to chat / gossip</td><td>"Les voisines placotent sur le balcon." (The neighbours are chatting on the balcony.)</td></tr>
<tr><td>pogner</td><td>attraper / prendre</td><td>to catch / grab</td><td>"Pogne la balle!" (Catch the ball!)</td></tr>
<tr><td>gosser</td><td>embêter / sculpter</td><td>to annoy / to whittle</td><td>"Arrête de me gosser!" (Stop annoying me!)</td></tr>
<tr><td>niaiser</td><td>plaisanter / perdre le temps</td><td>to joke around / waste time</td><td>"Arrête de niaiser!" (Stop fooling around!)</td></tr>
<tr><td>achaler</td><td>déranger / importuner</td><td>to bother / pester</td><td>"Achale-moi pas!" (Don't bother me!)</td></tr>
<tr><td>embarquer</td><td>monter (dans un véhicule)</td><td>to get in/on</td><td>"Embarque dans le char!" (Get in the car!)</td></tr>
<tr><td>débarquer</td><td>descendre (d'un véhicule)</td><td>to get off/out</td><td>"Je débarque au prochain arrêt." (I'm getting off at the next stop.)</td></tr>
<tr><td>chauffer</td><td>conduire</td><td>to drive</td><td>"C'est qui qui chauffe?" (Who's driving?)</td></tr>
<tr><td>checker</td><td>vérifier / regarder</td><td>to check / look at</td><td>"Checke ça!" (Check that out!)</td></tr>
</tbody>
</table>
<p><strong>-ER Verb Pronunciation in Quebec French:</strong></p>
<p>In Quebec spoken French, -ER verb endings are pronounced the same way as in standard French. However, the pronoun combinations change:</p>
<ul>
<li><strong>"Je mange"</strong> → "J'mange" (the "e" of "je" is almost always dropped before a consonant)</li>
<li><strong>"Tu manges"</strong> → "Tu manges" (but remember: "tu" sounds like "tsu" with affrication!)</li>
<li><strong>"Il mange"</strong> → "Y mange" ("il" becomes "y")</li>
<li><strong>"Elle mange"</strong> → "A mange" ("elle" becomes "a")</li>
<li><strong>"Nous mangeons"</strong> → "On mange" ("nous" is rarely used, replaced by "on")</li>
<li><strong>"Vous mangez"</strong> → "Vous mangez" (stays the same in formal contexts)</li>
<li><strong>"Ils mangent"</strong> → "Y mangent" ("ils" becomes "y")</li>
</ul>
<p><strong>Common -ER Verbs for Daily Life in Quebec:</strong></p>
<table>
<thead><tr><th>Verb</th><th>English</th><th>Quebec Example</th></tr></thead>
<tbody>
<tr><td>pelleter</td><td>to shovel (snow)</td><td>"Faut que je pellette l'entrée!" (I have to shovel the driveway!)</td></tr>
<tr><td>déneiger</td><td>to clear snow from</td><td>"Faut déneiger le char." (Gotta clear snow off the car.)</td></tr>
<tr><td>glisser</td><td>to slide / toboggan</td><td>"Les enfants vont glisser au parc." (The kids are going tobogganing at the park.)</td></tr>
<tr><td>patiner</td><td>to skate</td><td>"On va patiner sur le canal?" (Shall we go skating on the canal?)</td></tr>
<tr><td>camper</td><td>to camp</td><td>"On va camper au parc national." (We're going camping at the national park.)</td></tr>
<tr><td>se baigner</td><td>to swim / bathe</td><td>"On va se baigner au lac." (We're going swimming at the lake.)</td></tr>
<tr><td>cabaner</td><td>to stay in a cabin</td><td>"On va cabaner au bord du lac." (We're going to stay in a cabin by the lake.)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – A Typical Winter Morning in Quebec:</strong></p>
<p><em>Vous décrivez votre routine d'hiver au Québec.</em></p>
<p>"L'hiver au Québec, ça change tout! Le matin, je me réveille pis je regarde dehors. Y'a deux pieds de neige?"<br>"Faut que je pellette l'entrée avant de partir travailler. Ça me prend une bonne demi-heure!"<br>"Après, je déneige le char. Je gratte le pare-brise, j'enlève la neige sur le toit pis je démarre le moteur pour le faire chauffer."<br>"Pendant que le char chauffe, je rentre en dedans pis je mets mes bottes d'hiver, mon manteau, ma tuque pis mes mitaines."<br>"Quand je pars enfin, les routes sont glissantes. Faut chauffer doucement!"<br>"Mais tu sais quoi? J'aime ça pareil. L'hiver au Québec, c'est beau en titi!"</p>
<p><em>(You're describing your winter routine in Quebec. "Winter in Quebec changes everything! In the morning, I wake up and look outside. Two feet of snow?" "I have to shovel the driveway before going to work. That takes me a good half hour!" "After, I clear snow off the car. I scrape the windshield, remove snow from the roof and start the engine to warm it up." "While the car warms up, I go back inside and put on my winter boots, coat, beanie and mittens." "When I finally leave, the roads are slippery. Gotta drive carefully!" "But you know what? I like it anyway. Winter in Quebec is really beautiful!")</em></p>

"""
    html = insert_before(html, marker_12_end, new_12)

    # =========================================================================
    # UNIT 13: DAILY ROUTINES & REFLEXIVE VERBS
    # =========================================================================

    marker_13_end = '<h2 id="h-unit-14-food-eating">'
    new_13 = """
<p><strong>Quebec Daily Life Vocabulary (🍁):</strong></p>
<p>Daily routines in Quebec have vocabulary and customs specific to the province:</p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th></tr></thead>
<tbody>
<tr><td>se réveiller de bonne heure</td><td>se réveiller tôt</td><td>to wake up early</td></tr>
<tr><td>prendre sa douche</td><td>prendre sa douche</td><td>to take a shower (same)</td></tr>
<tr><td>déjeuner (le matin)</td><td>prendre le petit-déjeuner</td><td>to have breakfast</td></tr>
<tr><td>dîner (le midi)</td><td>déjeuner</td><td>to have lunch</td></tr>
<tr><td>souper (le soir)</td><td>dîner</td><td>to have dinner</td></tr>
<tr><td>partir le char</td><td>démarrer la voiture</td><td>to start the car</td></tr>
<tr><td>prendre l'autobus</td><td>prendre le bus</td><td>to take the bus</td></tr>
<tr><td>revenir de l'ouvrage</td><td>rentrer du travail</td><td>to come home from work</td></tr>
<tr><td>faire le souper</td><td>préparer le dîner</td><td>to make dinner</td></tr>
<tr><td>écouter la télé</td><td>regarder la télé</td><td>to watch TV (QC uses "écouter"!)</td></tr>
<tr><td>se coucher de bonne heure</td><td>se coucher tôt</td><td>to go to bed early</td></tr>
</tbody>
</table>
<p><strong>Important Note about Meal Names (🍁):</strong></p>
<p>This is one of THE most confusing differences for language learners visiting Quebec:</p>
<table>
<thead><tr><th>Meal</th><th>Quebec French</th><th>France French</th></tr></thead>
<tbody>
<tr><td>Morning meal</td><td><strong>Le déjeuner</strong></td><td>Le petit-déjeuner</td></tr>
<tr><td>Noon meal</td><td><strong>Le dîner</strong></td><td>Le déjeuner</td></tr>
<tr><td>Evening meal</td><td><strong>Le souper</strong></td><td>Le dîner</td></tr>
</tbody>
</table>
<p>If someone in Quebec invites you for "le dîner," they mean LUNCH, not dinner! And if they invite you for "le souper," they mean the evening meal.</p>
<p><strong>Quebec TV and Media Vocabulary:</strong></p>
<p>Quebecers say "écouter la télé" (to listen to the TV) rather than "regarder la télé" (to watch TV). Other media-related vocabulary:</p>
<ul>
<li><strong>"Écouter un film"</strong> = to watch a movie (QC uses "écouter" even for visual media!)</li>
<li><strong>"Téléromans"</strong> = Quebec soap operas/TV dramas (hugely popular!)</li>
<li><strong>"Un balado"</strong> = a podcast (OQLF term)</li>
<li><strong>"Zapper"</strong> = to channel surf</li>
<li><strong>"La télécommande"</strong> = remote control (also called "la manette" in QC)</li>
</ul>
<p><strong>A Typical Quebec Family Day – Extended Description:</strong></p>
<p><em>Here's a full day described using reflexive verbs and daily routine vocabulary:</em></p>
<p>"Le matin, je me réveille à six heures et quart. Je me lève tout de suite parce que je dois me préparer pour le travail. D'abord, je me brosse les dents et je me lave le visage. Ensuite, je m'habille – en hiver, je mets des vêtements chauds parce qu'il fait frette!"</p>
<p>"Je déjeune à sept heures: du gruau avec du sirop d'érable, un café et un jus d'orange. Les enfants se réveillent à sept heures et demie et se préparent pour l'école."</p>
<p>"Je pars de la maison à huit heures moins quart. Je déneige le char, je me rends au travail en auto – ça me prend quarante-cinq minutes avec le trafic."</p>
<p>"À midi, je dîne à la cafétéria avec mes collègues. On mange un sandwich et on jase un peu."</p>
<p>"Après l'ouvrage, à cinq heures, je fais l'épicerie au IGA ou au Métro. Quand j'arrive à la maison, je fais le souper pour toute la famille."</p>
<p>"Après le souper, les enfants font leurs devoirs. Nous, on se détend en écoutant la télé ou en lisant un livre. Parfois, on joue aux cartes en famille."</p>
<p>"Vers neuf heures, les enfants se couchent. Moi, je me couche vers dix heures et demie. Je m'endors toujours en lisant!"</p>
<p><strong>🇫🇷 Real-Life Scene – Morning Rush in a Quebec Family:</strong></p>
<p><em>C'est un matin typique dans une famille québécoise.</em></p>
<p>"Les enfants! Levez-vous! Y est sept heures!"<br>"Maman, je veux pas me lever. Y fait trop frette!"<br>"Ben là, tu vas être en retard à l'école! Habille-toi vite!"<br>"J'arrive pas à trouver mes bas!"<br>"Y sont dans le tiroir, comme d'habitude. Pis brosse-toi les dents!"<br>"Qu'est-ce qu'on mange pour déjeuner?"<br>"J'ai fait des toasts pis y'a du beurre de peanut et de la confiture."<br>"Je veux des céréales!"<br>"D'accord, mais dépêche-toi. L'autobus passe dans quinze minutes!"<br>"Maman! Félix m'achale!"<br>"Félix, arrête de gosser ta sœur! Tout le monde met ses bottes, son manteau et sa tuque. On sort dans cinq minutes!"</p>
<p><em>(It's a typical morning in a Quebec family. "Kids! Get up! It's seven o'clock!" "Mom, I don't want to get up. It's too cold!" "Come on, you'll be late for school! Get dressed quickly!" "I can't find my socks!" "They're in the drawer, as usual. And brush your teeth!" "What are we having for breakfast?" "I made toast and there's peanut butter and jam." "I want cereal!" "Fine, but hurry up. The bus comes in fifteen minutes!" "Mom! Félix is annoying me!" "Félix, stop bugging your sister! Everyone put on your boots, coat and hat. We're leaving in five minutes!")</em></p>

"""
    html = insert_before(html, marker_13_end, new_13)

    # =========================================================================
    # UNIT 14: FOOD & EATING
    # =========================================================================

    marker_14_end = '<h2 id="h-unit-15-prepositions-locations">'
    new_14 = """
<p><strong>Quebec Cuisine – A Complete Guide (🍁):</strong></p>
<p>Quebec has one of the richest culinary traditions in North America. Here's a comprehensive guide to Quebec food vocabulary and culture:</p>
<table>
<thead><tr><th>Dish</th><th>Description</th><th>When It's Eaten</th></tr></thead>
<tbody>
<tr><td>La poutine</td><td>Frites, sauce brune et fromage en grains ("cheese curds")</td><td>Anytime, especially late night!</td></tr>
<tr><td>La tourtière</td><td>Pâté à la viande (porc, bœuf, parfois gibier)</td><td>Christmas & holidays</td></tr>
<tr><td>Le pâté chinois</td><td>Couches de viande hachée, maïs et purée de patates</td><td>Family weeknight dinner</td></tr>
<tr><td>La soupe aux pois</td><td>Soupe épaisse aux pois jaunes avec jambon</td><td>Cold winter days</td></tr>
<tr><td>Les fèves au lard</td><td>Baked beans with maple syrup and pork</td><td>Sugar shack meals, brunch</td></tr>
<tr><td>Les oreilles de crisse</td><td>Deep-fried salted pork rinds</td><td>Sugar shack meals</td></tr>
<tr><td>La tire sur la neige</td><td>Hot maple syrup poured on snow, rolled on a stick</td><td>Sugar shack visits, spring</td></tr>
<tr><td>Le cipaille (ou cipâte)</td><td>Multi-layered meat pie with pastry</td><td>Special occasions, holidays</td></tr>
<tr><td>La tarte au sucre</td><td>Sugar pie (brown sugar, maple syrup, cream)</td><td>Dessert, holidays</td></tr>
<tr><td>Le pouding chômeur</td><td>"Poor man's pudding" – cake with hot maple/caramel sauce</td><td>Classic Quebec dessert</td></tr>
<tr><td>Les cretons</td><td>Cold meat spread (like pork rillettes)</td><td>Breakfast, on toast</td></tr>
<tr><td>Le smoked meat</td><td>Montreal-style smoked meat (beef brisket)</td><td>Lunch, at delis (Schwartz's!)</td></tr>
<tr><td>Le bagel montréalais</td><td>Smaller, sweeter, wood-oven baked bagel</td><td>Any time (St-Viateur, Fairmount)</td></tr>
<tr><td>La gibelotte</td><td>Fish and vegetable stew from Sorel-Tracy</td><td>Summer</td></tr>
</tbody>
</table>
<p><strong>Quebec Breakfast (Le déjeuner québécois):</strong></p>
<p>A typical Quebec breakfast includes:</p>
<ul>
<li><strong>Des toasts</strong> avec du beurre et de la confiture (toast with butter and jam)</li>
<li><strong>Du gruau</strong> avec du sirop d'érable (oatmeal with maple syrup)</li>
<li><strong>Des crêpes</strong> ou des <strong>pancakes</strong> avec du sirop d'érable</li>
<li><strong>Des œufs</strong> (au miroir, brouillés, à la coque) – eggs (sunny-side up, scrambled, soft-boiled)</li>
<li><strong>Du bacon</strong> et des <strong>saucisses</strong></li>
<li><strong>Des cretons</strong> sur du pain (meat spread on bread)</li>
<li><strong>Un café</strong> – Quebecers are big coffee drinkers! ("Tim Hortons" or "un café du Tim")</li>
</ul>
<p><strong>Quebec Restaurant Tipping Culture (🍁):</strong></p>
<p>Restaurant tipping culture in Quebec differs from France:</p>
<ul>
<li><strong>In Quebec:</strong> Tips are expected at 15-20% (similar to the rest of North America). A tip of less than 15% is considered rude.</li>
<li><strong>In France:</strong> Service is included ("service compris"). Tips are optional and small (rounding up).</li>
<li><strong>Quick tip calculation in Quebec:</strong> "Just double the taxes!" – Quebec taxes (TVQ + TPS/GST) add up to about 15%, so doubling the tax line gives you approximately a 15% tip.</li>
<li><strong>"Le pourboire"</strong> = the tip. "Est-ce que le pourboire est inclus?" (Is the tip included?) – Usually, the answer in Quebec is "non".</li>
</ul>
<p><strong>Quebec Drinking Culture Vocabulary:</strong></p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un breuvage</td><td>une boisson</td><td>a beverage/drink</td></tr>
<tr><td>une liqueur</td><td>un soda</td><td>a soft drink</td></tr>
<tr><td>une slush</td><td>une granita</td><td>a slushie</td></tr>
<tr><td>un verre de lait</td><td>un verre de lait</td><td>a glass of milk (QC is a big dairy province!)</td></tr>
<tr><td>une bière en fût</td><td>une bière pression</td><td>a draft beer</td></tr>
<tr><td>un pichet</td><td>un pichet</td><td>a pitcher (of beer)</td></tr>
<tr><td>la SAQ</td><td>le magasin de vin</td><td>the liquor store (government-run in QC)</td></tr>
<tr><td>un dépanneur (pour la bière)</td><td>un épicier</td><td>convenience store (sells beer in QC!)</td></tr>
<tr><td>un caribou</td><td>(no equivalent)</td><td>wine + spirits drink (Carnival specialty)</td></tr>
<tr><td>du cidre de glace</td><td>(no equivalent)</td><td>ice cider (Quebec specialty!)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Ordering at a Typical Quebec Diner (Casse-croûte):</strong></p>
<p><em>Vous êtes dans un casse-croûte typiquement québécois.</em></p>
<p>"Bonjour! Qu'est-ce que je peux faire pour vous?"<br>"Euh, qu'est-ce que vous avez de bon?"<br>"On est connus pour notre poutine! On a la classique, la poutine italienne pis la poutine BBQ."<br>"C'est quoi la poutine italienne?"<br>"C'est des frites avec de la sauce à spaghetti et du fromage en grains."<br>"Ah, j'ai jamais essayé ça! Je vais prendre une poutine italienne régulière."<br>"Parfait! Avec ou sans boisson?"<br>"Avec une liqueur. Un Pepsi, s'il vous plaît."<br>"Un Pepsi. Ça fait neuf piasses et cinquante."<br>"Voilà!"<br>"Merci! Ça va prendre cinq minutes."<br>[Cinq minutes plus tard]<br>"Voici votre poutine! Bon appétit!"<br>"Merci! Wow, c'est une grosse portion!"<br>"Ben oui, ici on est généreux! Revenez quand vous voulez!"</p>
<p><em>(You're at a typical Quebec snack bar. "Hello! What can I do for you?" "Um, what's good?" "We're known for our poutine! We have classic, Italian poutine, and BBQ poutine." "What's Italian poutine?" "It's fries with spaghetti sauce and cheese curds." "Oh, I've never tried that! I'll have a regular Italian poutine." "Perfect! With or without a drink?" "With a soft drink. A Pepsi, please." "A Pepsi. That's nine fifty." "Here you go!" "Thanks! It'll take five minutes." [Five minutes later] "Here's your poutine! Enjoy!" "Thanks! Wow, it's a huge portion!" "Of course, we're generous here! Come back anytime!")</em></p>

"""
    html = insert_before(html, marker_14_end, new_14)

    write_file(path, html)
    print("Part 3 done: Units 11-14 expanded successfully!")

if __name__ == '__main__':
    main()
