#!/usr/bin/env python3
"""Generate A2 HTML - Part 2: Units 1-5 content"""
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2.html")

content = """
<h1 id="h-a2-textbook">Canadian French A2 Level Complete Textbook</h1>
<h2 id="h-a2-guide">A Comprehensive Guide for English Speakers</h2>
<hr>
<h2 id="h-a2-toc">TABLE OF CONTENTS</h2>
<p><strong>PART I: REVIEWING &amp; DEEPENING</strong></p>
<ul>
<li>Unit 1: Review of A1 Essentials</li>
<li>Unit 2: The Imparfait (Imperfect Tense)</li>
<li>Unit 3: Futur Simple (Simple Future)</li>
<li>Unit 4: Passé Récent &amp; Venir de</li>
</ul>
<p><strong>PART II: EXPANDING DAILY LIFE</strong></p>
<ul>
<li>Unit 5: Shopping &amp; Money</li>
<li>Unit 6: Housing &amp; Home</li>
<li>Unit 7: Transportation &amp; Directions</li>
<li>Unit 8: Weather &amp; Climate</li>
</ul>
<p><strong>PART III: SOCIAL INTERACTIONS</strong></p>
<ul>
<li>Unit 9: Invitations &amp; Events</li>
<li>Unit 10: Phone Calls &amp; Messages</li>
<li>Unit 11: Giving Instructions &amp; Advice</li>
<li>Unit 12: Comparisons &amp; Superlatives</li>
</ul>
<p><strong>PART IV: HEALTH &amp; SERVICES</strong></p>
<ul>
<li>Unit 13: Body &amp; Health</li>
<li>Unit 14: At the Doctor &amp; Pharmacy</li>
<li>Unit 15: Banking &amp; Administrative Tasks</li>
<li>Unit 16: Emergency Situations</li>
</ul>
<p><strong>PART V: TRAVEL &amp; CULTURE</strong></p>
<ul>
<li>Unit 17: Travel Planning</li>
<li>Unit 18: At the Hotel &amp; Airport</li>
<li>Unit 19: Quebec Culture &amp; Festivals</li>
<li>Unit 20: Review &amp; B1 Preparation</li>
</ul>
<hr>

<h1 id="h-part-i-reviewing">PART I: REVIEWING &amp; DEEPENING</h1>

<h2 id="h-unit-1-a1-review">UNIT 1: REVIEW OF A1 ESSENTIALS</h2>

<h3 id="h-1-1-key-verbs-review">1.1 Key Verbs Review</h3>
<p>Before advancing to A2, let&#39;s review the most important verbs from A1. Mastery of <strong>être</strong> (to be) and <strong>avoir</strong> (to have) is essential for everything that follows.</p>

<table>
<thead><tr><th>Pronoun</th><th>Être (to be)</th><th>Avoir (to have)</th><th>Aller (to go)</th><th>Faire (to do/make)</th></tr></thead>
<tbody>
<tr><td>Je</td><td>suis</td><td>ai</td><td>vais</td><td>fais</td></tr>
<tr><td>Tu</td><td>es</td><td>as</td><td>vas</td><td>fais</td></tr>
<tr><td>Il/Elle/On</td><td>est</td><td>a</td><td>va</td><td>fait</td></tr>
<tr><td>Nous</td><td>sommes</td><td>avons</td><td>allons</td><td>faisons</td></tr>
<tr><td>Vous</td><td>êtes</td><td>avez</td><td>allez</td><td>faites</td></tr>
<tr><td>Ils/Elles</td><td>sont</td><td>ont</td><td>vont</td><td>font</td></tr>
</tbody></table>

<p><strong>Review Examples:</strong></p>
<ul>
<li><strong>Je suis étudiant à l&#39;Université de Montréal depuis deux ans.</strong> (I have been a student at the University of Montreal for two years.)</li>
<li><strong>Nous avons trois enfants qui vont à l&#39;école primaire dans notre quartier.</strong> (We have three children who go to elementary school in our neighbourhood.)</li>
<li><strong>Est-ce que tu vas au dépanneur pour acheter du lait avant que le magasin ferme?</strong> (Are you going to the corner store to buy milk before the store closes?)</li>
<li><strong>Qu&#39;est-ce que vous faites pendant la fin de semaine quand il fait beau dehors?</strong> (What do you do on weekends when the weather is nice outside?)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Monday Morning at the Office:</strong></p>
<p><em>C&#39;est lundi matin au bureau. Vous arrivez et vous saluez vos collègues.</em></p>
<p>&quot;Salut Marc! Comment ça va ce matin?&quot;<br>&quot;Ça va bien, merci! J&#39;ai passé une belle fin de semaine au chalet avec ma famille.&quot;<br>&quot;Ah oui? Qu&#39;est-ce que vous avez fait?&quot;<br>&quot;On a fait du ski de fond et les enfants ont joué dehors dans la neige toute la journée.&quot;<br>&quot;Super! Moi, je suis allé au Carnaval de Québec avec des amis. C&#39;était vraiment le fun!&quot;</p>
<p><em>(It&#39;s Monday morning at the office. You arrive and greet your colleagues. &quot;Hi Marc! How are you this morning?&quot; &quot;I&#39;m good, thanks! I spent a nice weekend at the cottage with my family.&quot; &quot;Oh yeah? What did you do?&quot; &quot;We went cross-country skiing and the kids played outside in the snow all day.&quot; &quot;Great! I went to the Quebec Winter Carnival with friends. It was really fun!&quot;)</em></p>

<h3 id="h-1-2-essential-vocabulary">1.2 Essential Vocabulary Recap</h3>
<p>At A2, you should already know these basic categories. Here is a quick refresher with expanded examples:</p>

<p><strong>Greetings (Expanded):</strong></p>
<ul>
<li><strong>Allô!</strong> – Hello! (informal, very Québécois) (Hello!)</li>
<li><strong>Comment ça va, toi?</strong> – How are you? (informal) (How are you?)</li>
<li><strong>Pas pire, et toi?</strong> – Not bad, and you? (typical Québécois response) (Not bad, and you?)</li>
<li><strong>Bonne journée!</strong> – Have a good day! (Have a good day!)</li>
</ul>

<p><strong>Daily Life Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example Sentence</th></tr></thead>
<tbody>
<tr><td>le déjeuner</td><td>breakfast (QC) / lunch (FR)</td><td>Je prends mon déjeuner à sept heures. (I eat breakfast at seven.)</td></tr>
<tr><td>le dîner</td><td>lunch (QC) / dinner (FR)</td><td>On dîne ensemble à midi? (Shall we have lunch together at noon?)</td></tr>
<tr><td>le souper</td><td>dinner/supper (QC)</td><td>Le souper est prêt à six heures. (Dinner is ready at six.)</td></tr>
<tr><td>la job</td><td>the job (QC, feminine)</td><td>J&#39;aime ma job au centre-ville. (I like my job downtown.)</td></tr>
<tr><td>le char</td><td>the car (QC, informal)</td><td>Mon char est au garage. (My car is at the garage.)</td></tr>
<tr><td>le dépanneur</td><td>corner store (QC)</td><td>Je vais au dépanneur chercher du pain. (I&#39;m going to the corner store to get bread.)</td></tr>
</tbody></table>

<h3 id="h-1-3-sentence-building">1.3 Building Longer Sentences</h3>
<p>At A2, you need to move beyond simple subject-verb-object sentences. Here are key connectors:</p>

<table>
<thead><tr><th>Connector</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>parce que</td><td>because</td><td>Je reste à la maison parce qu&#39;il neige beaucoup. (I&#39;m staying home because it&#39;s snowing a lot.)</td></tr>
<tr><td>donc</td><td>therefore/so</td><td>Il fait froid, donc je mets mon manteau. (It&#39;s cold, so I put on my coat.)</td></tr>
<tr><td>mais</td><td>but</td><td>Je veux sortir, mais je suis fatiguée. (I want to go out, but I&#39;m tired.)</td></tr>
<tr><td>quand</td><td>when</td><td>Quand il pleut, je prends l&#39;autobus. (When it rains, I take the bus.)</td></tr>
<tr><td>si</td><td>if</td><td>Si tu veux, on peut aller au cinéma ce soir. (If you want, we can go to the cinema tonight.)</td></tr>
<tr><td>pendant que</td><td>while</td><td>Je cuisine pendant que les enfants font leurs devoirs. (I cook while the children do their homework.)</td></tr>
<tr><td>avant de</td><td>before (+ infinitive)</td><td>Avant de partir, n&#39;oublie pas tes clés! (Before leaving, don&#39;t forget your keys!)</td></tr>
<tr><td>après</td><td>after</td><td>Après le souper, on regarde la télé ensemble. (After dinner, we watch TV together.)</td></tr>
</tbody></table>

<p><strong>Practice with longer sentences:</strong></p>
<ul>
<li><strong>Je vais au gymnase trois fois par semaine parce que je veux rester en forme pour jouer au hockey avec mes amis.</strong> (I go to the gym three times a week because I want to stay in shape to play hockey with my friends.)</li>
<li><strong>Ma sœur habite à Québec, mais elle travaille à Montréal, donc elle prend le train tous les lundis matin.</strong> (My sister lives in Quebec City, but she works in Montreal, so she takes the train every Monday morning.)</li>
</ul>

<h3 id="h-1-4-cdn-french-a1-review">1.4 Canadian French Review (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong> Remember that Quebec French has its own rhythm and vocabulary. Key differences from France French that you learned at A1:</p>
<ul>
<li><strong>Tu/Vous:</strong> Quebecers use <strong>&quot;tu&quot;</strong> much more quickly and widely than in France. It is common to say <strong>&quot;tu&quot;</strong> to strangers in casual settings.</li>
<li><strong>Affrication:</strong> The sounds &quot;t&quot; and &quot;d&quot; before &quot;i&quot; and &quot;u&quot; become &quot;ts&quot; and &quot;dz&quot;: <strong>&quot;tu&quot;</strong> sounds like <strong>&quot;tsu&quot;</strong>, <strong>&quot;dire&quot;</strong> sounds like <strong>&quot;dzire&quot;</strong>.</li>
<li><strong>Meal names:</strong> In Quebec, <strong>déjeuner</strong> = breakfast, <strong>dîner</strong> = lunch, <strong>souper</strong> = dinner. In France, <strong>petit-déjeuner</strong> = breakfast, <strong>déjeuner</strong> = lunch, <strong>dîner</strong> = dinner.</li>
<li><strong>&quot;Icitte&quot;</strong> instead of &quot;ici&quot; (here), <strong>&quot;pis&quot;</strong> instead of &quot;puis&quot; (then/and).</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Ordering at a Québécois Restaurant:</strong></p>
<p><em>Vous êtes dans un petit restaurant à Trois-Rivières avec un ami.</em></p>
<p>&quot;Bonjour! Bienvenue chez nous! Qu&#39;est-ce que je peux vous servir?&quot;<br>&quot;Salut! On va prendre deux poutines, s&#39;il vous plaît.&quot;<br>&quot;Parfait! Vous voulez-tu quelque chose à boire avec ça?&quot;<br>&quot;Oui, deux Pepsi, s&#39;il vous plaît.&quot;<br>&quot;Correct! Ça va être prêt dans cinq minutes.&quot;</p>
<p><em>(You are in a small restaurant in Trois-Rivières with a friend. &quot;Hello! Welcome! What can I serve you?&quot; &quot;Hi! We&#39;ll have two poutines, please.&quot; &quot;Perfect! Do you want something to drink with that?&quot; &quot;Yes, two Pepsis, please.&quot; &quot;All right! It will be ready in five minutes.&quot;)</em></p>

<hr>
<h2 id="h-unit-2-imparfait">UNIT 2: THE IMPARFAIT (IMPERFECT TENSE)</h2>

<h3 id="h-2-1-intro-imparfait">2.1 Introduction to the Imparfait</h3>
<p>The <strong>imparfait</strong> (imperfect tense) is used to describe ongoing or repeated actions in the past, habits, descriptions, and background information. Think of it as &quot;was doing&quot; or &quot;used to do&quot; in English.</p>

<p><strong>When to use the imparfait:</strong></p>
<ul>
<li><strong>Habits in the past:</strong> Quand j&#39;étais jeune, je jouais dehors tous les jours. (When I was young, I used to play outside every day.)</li>
<li><strong>Descriptions:</strong> Il faisait beau et le soleil brillait sur le fleuve Saint-Laurent. (The weather was nice and the sun was shining on the St. Lawrence River.)</li>
<li><strong>Ongoing actions:</strong> Pendant que je mangeais, le téléphone a sonné. (While I was eating, the phone rang.)</li>
<li><strong>States of mind/emotion:</strong> Elle était triste parce que son ami était parti. (She was sad because her friend had left.)</li>
<li><strong>Age in the past:</strong> Quand j&#39;avais dix ans, j&#39;habitais à Gatineau. (When I was ten, I lived in Gatineau.)</li>
</ul>

<h3 id="h-2-2-forming-imparfait">2.2 Forming the Imparfait</h3>
<p>To form the imparfait, take the <strong>nous</strong> form of the present tense, remove <strong>-ons</strong>, and add the imparfait endings:</p>

<table>
<thead><tr><th>Pronoun</th><th>Ending</th><th>Parler (parl-)</th><th>Finir (finiss-)</th><th>Prendre (pren-)</th></tr></thead>
<tbody>
<tr><td>Je</td><td>-ais</td><td>parlais</td><td>finissais</td><td>prenais</td></tr>
<tr><td>Tu</td><td>-ais</td><td>parlais</td><td>finissais</td><td>prenais</td></tr>
<tr><td>Il/Elle/On</td><td>-ait</td><td>parlait</td><td>finissait</td><td>prenait</td></tr>
<tr><td>Nous</td><td>-ions</td><td>parlions</td><td>finissions</td><td>prenions</td></tr>
<tr><td>Vous</td><td>-iez</td><td>parliez</td><td>finissiez</td><td>preniez</td></tr>
<tr><td>Ils/Elles</td><td>-aient</td><td>parlaient</td><td>finissaient</td><td>prenaient</td></tr>
</tbody></table>

<p><strong>Important:</strong> The only irregular verb in the imparfait is <strong>être</strong>:</p>
<table>
<thead><tr><th>Pronoun</th><th>Être (imparfait)</th></tr></thead>
<tbody>
<tr><td>J&#39;</td><td>étais</td></tr>
<tr><td>Tu</td><td>étais</td></tr>
<tr><td>Il/Elle/On</td><td>était</td></tr>
<tr><td>Nous</td><td>étions</td></tr>
<tr><td>Vous</td><td>étiez</td></tr>
<tr><td>Ils/Elles</td><td>étaient</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>Quand j&#39;étais petite, ma grand-mère me racontait des histoires tous les soirs avant de dormir.</strong> (When I was little, my grandmother used to tell me stories every night before sleeping.)</li>
<li><strong>Nous habitions dans une petite maison à côté du lac et nous allions pêcher chaque samedi.</strong> (We used to live in a small house next to the lake and we went fishing every Saturday.)</li>
<li><strong>Il neigeait beaucoup et les enfants faisaient des bonhommes de neige dans la cour.</strong> (It was snowing a lot and the children were making snowmen in the yard.)</li>
</ul>

<h3 id="h-2-3-uses-imparfait">2.3 Uses of the Imparfait</h3>
<p><strong>1. Describing habits and routines in the past:</strong></p>
<ul>
<li><strong>Chaque été, on allait au chalet de mes grands-parents à Charlevoix.</strong> (Every summer, we used to go to my grandparents&#39; cottage in Charlevoix.)</li>
<li><strong>Le dimanche, mon père préparait toujours des crêpes pour le déjeuner.</strong> (On Sundays, my father always used to make crêpes for breakfast.)</li>
</ul>

<p><strong>2. Describing people, places, weather, and feelings:</strong></p>
<ul>
<li><strong>La maison était grande avec un jardin magnifique plein de fleurs de toutes les couleurs.</strong> (The house was big with a magnificent garden full of flowers of all colours.)</li>
<li><strong>Il faisait moins trente degrés et le vent soufflait très fort dans les rues de Montréal.</strong> (It was minus thirty degrees and the wind was blowing very hard in the streets of Montreal.)</li>
</ul>

<p><strong>3. Setting the scene for a story:</strong></p>
<ul>
<li><strong>C&#39;était un beau matin d&#39;automne. Les feuilles étaient rouges et orange, et l&#39;air sentait le froid.</strong> (It was a beautiful autumn morning. The leaves were red and orange, and the air smelled cold.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Remembering Childhood in Quebec:</strong></p>
<p><em>Vous parlez avec votre ami de votre enfance au Québec.</em></p>
<p>&quot;Tu te souviens quand on était jeunes? On jouait au hockey dans la rue après l&#39;école.&quot;<br>&quot;Oui! Et ma mère criait toujours: &#39;Rentrez, c&#39;est l&#39;heure du souper!&#39;&quot;<br>&quot;Et l&#39;hiver, on construisait des forts de neige énormes dans la cour.&quot;<br>&quot;C&#39;est vrai. On avait tellement de fun. Mon père nous emmenait à la cabane à sucre chaque printemps.&quot;<br>&quot;Ah oui, le sirop d&#39;érable! Ma grand-mère faisait de la tire sur la neige. C&#39;était le meilleur moment de l&#39;année!&quot;</p>
<p><em>(You are talking with your friend about your childhood in Quebec. &quot;Do you remember when we were young? We used to play hockey in the street after school.&quot; &quot;Yes! And my mother always used to yell: &#39;Come in, it&#39;s suppertime!&#39;&quot; &quot;And in winter, we used to build huge snow forts in the yard.&quot; &quot;That&#39;s true. We had so much fun. My father used to take us to the sugar shack every spring.&quot; &quot;Oh yes, maple syrup! My grandmother used to make taffy on the snow. It was the best time of the year!&quot;)</em></p>

<h3 id="h-2-4-imparfait-vs-pc">2.4 Imparfait vs. Passé Composé</h3>
<p>This is one of the most important distinctions in French. The <strong>passé composé</strong> is used for completed actions, while the <strong>imparfait</strong> is for ongoing/habitual past actions.</p>

<table>
<thead><tr><th>Imparfait (Background/Ongoing)</th><th>Passé Composé (Completed Event)</th></tr></thead>
<tbody>
<tr><td>Je regardais la télé... (I was watching TV...)</td><td>...quand mon ami est arrivé. (...when my friend arrived.)</td></tr>
<tr><td>Il pleuvait... (It was raining...)</td><td>...quand je suis sorti du bureau. (...when I left the office.)</td></tr>
<tr><td>Nous mangions au restaurant... (We were eating at the restaurant...)</td><td>...quand le serveur a renversé l&#39;eau. (...when the waiter spilled the water.)</td></tr>
</tbody></table>

<p><strong>Key signals for imparfait:</strong> toujours (always), souvent (often), chaque jour (every day), d&#39;habitude (usually), quand j&#39;étais jeune (when I was young), pendant que (while).</p>
<p><strong>Key signals for passé composé:</strong> hier (yesterday), soudain (suddenly), tout à coup (all of a sudden), une fois (once), ce jour-là (that day).</p>

<p><strong>Practice examples:</strong></p>
<ul>
<li><strong>D&#39;habitude, je prenais le métro, mais hier, j&#39;ai pris un taxi parce qu&#39;il faisait trop froid.</strong> (Usually, I used to take the metro, but yesterday I took a taxi because it was too cold.)</li>
<li><strong>Nous étions au parc quand il a commencé à neiger très fort.</strong> (We were at the park when it started to snow very hard.)</li>
<li><strong>Elle lisait un livre pendant que son frère faisait ses devoirs, et soudain, le chat a sauté sur la table.</strong> (She was reading a book while her brother was doing his homework, and suddenly the cat jumped on the table.)</li>
</ul>

<h3 id="h-2-5-cdn-imparfait">2.5 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong> In spoken Quebec French, the imparfait is used very naturally and frequently in everyday conversation.</p>
<ul>
<li>Quebecers often use <strong>&quot;on&quot;</strong> instead of <strong>&quot;nous&quot;</strong> in casual speech: <strong>&quot;On allait toujours au chalet&quot;</strong> instead of <strong>&quot;Nous allions toujours au chalet.&quot;</strong> (We always used to go to the cottage.)</li>
<li>The expression <strong>&quot;dans le temps&quot;</strong> means &quot;back then&quot;: <strong>&quot;Dans le temps, y avait pas d&#39;internet.&quot;</strong> (Back then, there was no internet.)</li>
<li>In casual Quebec French, <strong>&quot;il&quot;</strong> is often shortened to <strong>&quot;y&quot;</strong>: <strong>&quot;Y faisait frette en maudit!&quot;</strong> (It was really cold!) – &quot;frette&quot; is Québécois for &quot;froid&quot; (cold).</li>
</ul>

<hr>
<h2 id="h-unit-3-futur-simple">UNIT 3: FUTUR SIMPLE (SIMPLE FUTURE)</h2>

<h3 id="h-3-1-intro-futur">3.1 Introduction to Futur Simple</h3>
<p>The <strong>futur simple</strong> is used to talk about events that will happen in the future. While at A1 you learned <strong>aller + infinitive</strong> (near future), the futur simple is used for more formal or distant future events.</p>
<p><strong>Comparison:</strong></p>
<ul>
<li><strong>Near future (aller +inf):</strong> Je vais manger bientôt. (I&#39;m going to eat soon.) – informal, immediate</li>
<li><strong>Futur simple:</strong> Je mangerai quand j&#39;aurai le temps. (I will eat when I have time.) – more formal, distant</li>
</ul>

<h3 id="h-3-2-regular-futur">3.2 Regular Verb Conjugations</h3>
<p>For regular verbs, add the futur endings to the <strong>full infinitive</strong>:</p>

<table>
<thead><tr><th>Pronoun</th><th>Ending</th><th>Parler</th><th>Finir</th><th>Vendre</th></tr></thead>
<tbody>
<tr><td>Je</td><td>-ai</td><td>parlerai</td><td>finirai</td><td>vendrai</td></tr>
<tr><td>Tu</td><td>-as</td><td>parleras</td><td>finiras</td><td>vendras</td></tr>
<tr><td>Il/Elle/On</td><td>-a</td><td>parlera</td><td>finira</td><td>vendra</td></tr>
<tr><td>Nous</td><td>-ons</td><td>parlerons</td><td>finirons</td><td>vendrons</td></tr>
<tr><td>Vous</td><td>-ez</td><td>parlerez</td><td>finirez</td><td>vendrez</td></tr>
<tr><td>Ils/Elles</td><td>-ont</td><td>parleront</td><td>finiront</td><td>vendront</td></tr>
</tbody></table>

<p><strong>Note:</strong> For -RE verbs, drop the final <strong>e</strong> before adding endings: vendre → vendr- + ai = vendrai.</p>

<h3 id="h-3-3-irregular-futur">3.3 Irregular Stems</h3>
<p>Some common verbs have irregular stems in the futur simple. You must memorize these:</p>

<table>
<thead><tr><th>Verb</th><th>Irregular Stem</th><th>Example (je)</th><th>Translation</th></tr></thead>
<tbody>
<tr><td>être</td><td>ser-</td><td>je serai</td><td>I will be</td></tr>
<tr><td>avoir</td><td>aur-</td><td>j&#39;aurai</td><td>I will have</td></tr>
<tr><td>aller</td><td>ir-</td><td>j&#39;irai</td><td>I will go</td></tr>
<tr><td>faire</td><td>fer-</td><td>je ferai</td><td>I will do/make</td></tr>
<tr><td>pouvoir</td><td>pourr-</td><td>je pourrai</td><td>I will be able to</td></tr>
<tr><td>vouloir</td><td>voudr-</td><td>je voudrai</td><td>I will want</td></tr>
<tr><td>devoir</td><td>devr-</td><td>je devrai</td><td>I will have to</td></tr>
<tr><td>savoir</td><td>saur-</td><td>je saurai</td><td>I will know</td></tr>
<tr><td>venir</td><td>viendr-</td><td>je viendrai</td><td>I will come</td></tr>
<tr><td>voir</td><td>verr-</td><td>je verrai</td><td>I will see</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>L&#39;année prochaine, j&#39;irai à Percé pour voir le rocher et les fous de Bassan.</strong> (Next year, I will go to Percé to see the rock and the gannets.)</li>
<li><strong>Quand tu auras dix-huit ans, tu pourras voter aux élections provinciales.</strong> (When you are eighteen, you will be able to vote in provincial elections.)</li>
<li><strong>Nous ferons une grande fête quand ma sœur reviendra de son voyage en Europe.</strong> (We will have a big party when my sister comes back from her trip to Europe.)</li>
</ul>

<h3 id="h-3-4-uses-futur">3.4 Uses of Futur Simple</h3>
<p><strong>1. Predictions and promises:</strong></p>
<ul>
<li><strong>Demain, il neigera toute la journée selon la météo.</strong> (Tomorrow, it will snow all day according to the weather forecast.)</li>
<li><strong>Je te promets que je serai à l&#39;heure pour ton spectacle ce soir.</strong> (I promise you I will be on time for your show tonight.)</li>
</ul>
<p><strong>2. After &quot;quand&quot; and &quot;si&quot; constructions:</strong></p>
<ul>
<li><strong>Quand j&#39;arriverai à Montréal, je t&#39;appellerai tout de suite.</strong> (When I arrive in Montreal, I will call you right away.)</li>
<li><strong>Si tu étudies bien, tu réussiras ton examen de français.</strong> (If you study well, you will pass your French exam.) – Note: after &quot;si&quot;, use present tense, NOT futur.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Planning a Summer Trip:</strong></p>
<p><em>Vous planifiez un voyage d&#39;été avec vos amis.</em></p>
<p>&quot;Qu&#39;est-ce qu&#39;on fera cet été? Avez-vous des idées?&quot;<br>&quot;Moi, j&#39;aimerais aller aux Îles-de-la-Madeleine. On pourra faire du kayak et manger du homard!&quot;<br>&quot;Bonne idée! On prendra le traversier ou l&#39;avion?&quot;<br>&quot;Le traversier, c&#39;est moins cher. Le voyage durera environ cinq heures.&quot;<br>&quot;Parfait! Je réserverai un chalet pour une semaine. Ça sera incroyable!&quot;</p>
<p><em>(You are planning a summer trip with your friends. &quot;What will we do this summer? Do you have any ideas?&quot; &quot;I would like to go to the Magdalen Islands. We&#39;ll be able to kayak and eat lobster!&quot; &quot;Good idea! Will we take the ferry or the plane?&quot; &quot;The ferry, it&#39;s less expensive. The trip will last about five hours.&quot; &quot;Perfect! I will book a cottage for a week. It will be incredible!&quot;)</em></p>

<h3 id="h-3-5-cdn-futur">3.5 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong> In everyday spoken Quebec French, the futur simple is relatively rare. Quebecers strongly prefer the <strong>futur proche</strong> (aller + infinitive) for most future statements:</p>
<ul>
<li><strong>Standard:</strong> Je parlerai avec lui demain. (I will speak with him tomorrow.)</li>
<li><strong>Québécois (common):</strong> Je vais y parler demain. / M&#39;a y parler demain. (I&#39;m going to talk to him tomorrow.)</li>
</ul>
<p>The contraction <strong>&quot;m&#39;a&quot;</strong> (from &quot;je m&#39;en vais&quot;) is very common in informal Quebec French to express the near future: <strong>&quot;M&#39;a faire ça tantôt.&quot;</strong> (I&#39;ll do that later.)</p>
<p>However, the futur simple is still important for formal writing, news, and professional communication in Quebec.</p>

<hr>
<h2 id="h-unit-4-recent-past-near-future">UNIT 4: PASSÉ RÉCENT &amp; VENIR DE</h2>

<h3 id="h-4-1-passe-recent">4.1 Passé Récent (Venir de + Infinitive)</h3>
<p>The <strong>passé récent</strong> expresses something that just happened. It uses <strong>venir de + infinitive</strong>:</p>

<table>
<thead><tr><th>Pronoun</th><th>Venir de</th><th>Example</th><th>Translation</th></tr></thead>
<tbody>
<tr><td>Je</td><td>viens de</td><td>Je viens de manger.</td><td>I just ate.</td></tr>
<tr><td>Tu</td><td>viens de</td><td>Tu viens d&#39;arriver?</td><td>Did you just arrive?</td></tr>
<tr><td>Il/Elle</td><td>vient de</td><td>Elle vient de partir.</td><td>She just left.</td></tr>
<tr><td>Nous</td><td>venons de</td><td>Nous venons de finir.</td><td>We just finished.</td></tr>
<tr><td>Vous</td><td>venez de</td><td>Vous venez de téléphoner?</td><td>Did you just call?</td></tr>
<tr><td>Ils/Elles</td><td>viennent de</td><td>Ils viennent de rentrer.</td><td>They just came back.</td></tr>
</tbody></table>

<p><strong>More examples:</strong></p>
<ul>
<li><strong>Je viens de recevoir un courriel de mon professeur de français à propos de l&#39;examen final.</strong> (I just received an email from my French teacher about the final exam.)</li>
<li><strong>Les voisins viennent de déménager dans une maison plus grande dans le quartier Limoilou.</strong> (The neighbours just moved to a bigger house in the Limoilou neighbourhood.)</li>
</ul>

<h3 id="h-4-2-etre-en-train-de">4.2 Être en train de (Ongoing Actions)</h3>
<p>To express an action that is happening right now, use <strong>être en train de + infinitive</strong>:</p>
<ul>
<li><strong>Je suis en train de cuisiner le souper pour toute la famille.</strong> (I am in the middle of cooking dinner for the whole family.)</li>
<li><strong>Les enfants sont en train de jouer dehors malgré la pluie.</strong> (The children are playing outside despite the rain.)</li>
<li><strong>Ne me dérange pas, je suis en train d&#39;étudier pour mon examen de demain.</strong> (Don&#39;t bother me, I&#39;m studying for my exam tomorrow.)</li>
</ul>

<h3 id="h-4-3-timeline-expressions">4.3 Timeline Expressions</h3>
<p>Combining tenses to express a timeline:</p>

<table>
<thead><tr><th>Timeline</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Just happened</td><td>venir de + inf.</td><td>Je viens de finir mon travail. (I just finished my work.)</td></tr>
<tr><td>Happening now</td><td>être en train de + inf.</td><td>Je suis en train de me reposer. (I am resting.)</td></tr>
<tr><td>About to happen</td><td>aller + inf.</td><td>Je vais sortir bientôt. (I am going to go out soon.)</td></tr>
<tr><td>Will happen</td><td>futur simple</td><td>Ce soir, je regarderai un film. (Tonight, I will watch a movie.)</td></tr>
</tbody></table>

<p><strong>🇫🇷 Real-Life Scene – A Busy Day in Sherbrooke:</strong></p>
<p><em>Votre ami vous appelle pendant une journée très chargée.</em></p>
<p>&quot;Allô! Qu&#39;est-ce que tu fais?&quot;<br>&quot;Je suis en train de faire l&#39;épicerie au IGA. Je viens de déposer les enfants à la garderie.&quot;<br>&quot;Est-ce que tu veux prendre un café après?&quot;<br>&quot;Oui! Je vais finir dans vingt minutes. On se retrouvera au Tim Hortons sur la rue King?&quot;<br>&quot;Parfait! J&#39;arrive tantôt!&quot;</p>
<p><em>(Your friend calls you during a very busy day. &quot;Hello! What are you doing?&quot; &quot;I&#39;m in the middle of grocery shopping at IGA. I just dropped off the kids at daycare.&quot; &quot;Do you want to grab a coffee after?&quot; &quot;Yes! I&#39;ll be done in twenty minutes. We&#39;ll meet at the Tim Hortons on King Street?&quot; &quot;Perfect! I&#39;ll be there soon!&quot;)</em></p>

<h3 id="h-4-4-cdn-recent">4.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Tantôt&quot;</strong> in Quebec French can mean &quot;earlier today&quot; or &quot;later today&quot;, depending on context. In France, it is rarely used.</li>
<li><strong>&quot;Là là&quot;</strong> is a common filler: <strong>&quot;Je viens de finir, là là.&quot;</strong> (I just finished, you know.)</li>
<li>The expression <strong>&quot;faire l&#39;épicerie&quot;</strong> (to do the grocery shopping) is Québécois. In France, people say <strong>&quot;faire les courses.&quot;</strong></li>
<li><strong>&quot;La garderie&quot;</strong> (daycare) is a very common word in Quebec, where the government subsidizes daycare at $8.85/day (as of 2024).</li>
</ul>

"""

with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write(content)

print(f"Part 2 (Units 1-4) done. File size: {os.path.getsize(OUTPUT)} bytes")
