#!/usr/bin/env python3
"""Generate A2 HTML - Part 4: Units 11-16"""
import os
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2.html")

content = """
<h1 id="h-part-iii-social">PART III: SOCIAL INTERACTIONS</h1>

<h2 id="h-unit-11-instructions">UNIT 11: GIVING INSTRUCTIONS &amp; ADVICE</h2>

<h3 id="h-11-1-imperatif">11.1 The Impératif (Commands)</h3>
<p>The <strong>impératif</strong> is used to give orders, instructions, or advice. It exists in three forms: <strong>tu</strong>, <strong>nous</strong>, and <strong>vous</strong>. The subject pronoun is dropped.</p>

<table>
<thead><tr><th>Verb</th><th>Tu form</th><th>Nous form</th><th>Vous form</th></tr></thead>
<tbody>
<tr><td>parler (to speak)</td><td>Parle!</td><td>Parlons!</td><td>Parlez!</td></tr>
<tr><td>finir (to finish)</td><td>Finis!</td><td>Finissons!</td><td>Finissez!</td></tr>
<tr><td>attendre (to wait)</td><td>Attends!</td><td>Attendons!</td><td>Attendez!</td></tr>
<tr><td>être (to be)</td><td>Sois!</td><td>Soyons!</td><td>Soyez!</td></tr>
<tr><td>avoir (to have)</td><td>Aie!</td><td>Ayons!</td><td>Ayez!</td></tr>
</tbody></table>

<p><strong>Important:</strong> For -ER verbs and &quot;aller&quot;, the <strong>tu</strong> form drops the final <strong>-s</strong>:</p>
<ul>
<li><strong>Mange tes légumes avant de quitter la table!</strong> (Eat your vegetables before leaving the table!)</li>
<li><strong>Va à l&#39;épicerie chercher du pain et du beurre, s&#39;il te plaît.</strong> (Go to the grocery store to get bread and butter, please.)</li>
<li><strong>BUT:</strong> When followed by <strong>y</strong> or <strong>en</strong>, the -s returns: <strong>Vas-y!</strong> (Go ahead!) <strong>Manges-en!</strong> (Eat some!)</li>
</ul>

<p><strong>Negative commands:</strong></p>
<ul>
<li><strong>Ne touche pas à ça! C&#39;est chaud!</strong> (Don&#39;t touch that! It&#39;s hot!)</li>
<li><strong>Ne parle pas la bouche pleine, c&#39;est impoli.</strong> (Don&#39;t talk with your mouth full, it&#39;s rude.)</li>
<li><strong>N&#39;oubliez pas d&#39;éteindre les lumières avant de partir du bureau.</strong> (Don&#39;t forget to turn off the lights before leaving the office.)</li>
</ul>

<h3 id="h-11-2-giving-advice">11.2 Giving Advice</h3>
<p><strong>Structures for giving advice:</strong></p>
<ul>
<li><strong>Tu devrais + infinitive:</strong> Tu devrais prendre des cours de français au cégep. (You should take French classes at the CEGEP.)</li>
<li><strong>Il faut + infinitive:</strong> Il faut mettre de la crème solaire quand il fait chaud. (One must put on sunscreen when it&#39;s hot.)</li>
<li><strong>Je te conseille de + infinitive:</strong> Je te conseille de visiter le Vieux-Québec en hiver, c&#39;est magnifique. (I advise you to visit Old Quebec in winter, it&#39;s magnificent.)</li>
<li><strong>À ta place, je + conditional:</strong> À ta place, je prendrais le métro au lieu du taxi. (If I were you, I would take the metro instead of a taxi.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Giving Directions to a Tourist:</strong></p>
<p><em>Un touriste vous demande comment aller au Château Frontenac.</em></p>
<p>&quot;Excusez-moi, comment est-ce que je peux me rendre au Château Frontenac?&quot;<br>&quot;C&#39;est facile! Continuez tout droit sur cette rue pendant trois coins de rue.&quot;<br>&quot;D&#39;accord, et après?&quot;<br>&quot;Tournez à gauche sur la rue Saint-Louis. Marchez pendant environ cinq minutes et vous allez voir le Château en face de vous.&quot;<br>&quot;Merci beaucoup! C&#39;est loin d&#39;ici?&quot;<br>&quot;Non, c&#39;est à environ dix minutes à pied. Et prenez votre temps, il y a de belles boutiques en chemin!&quot;</p>
<p><em>(A tourist asks you how to get to the Château Frontenac. &quot;Excuse me, how can I get to the Château Frontenac?&quot; &quot;It&#39;s easy! Continue straight on this street for three blocks.&quot; &quot;Okay, and then?&quot; &quot;Turn left on Saint-Louis Street. Walk for about five minutes and you will see the Château in front of you.&quot; &quot;Thank you very much! Is it far from here?&quot; &quot;No, it&#39;s about ten minutes on foot. And take your time, there are beautiful shops along the way!&quot;)</em></p>

<h3 id="h-11-3-recipes">11.3 Following Recipes &amp; Instructions</h3>
<p>The impératif is used extensively in recipes. Here is a simple <strong>poutine</strong> recipe:</p>
<p><strong>Recette de Poutine Classique</strong> (Classic Poutine Recipe)</p>
<ul>
<li><strong>Coupez les pommes de terre en frites épaisses.</strong> (Cut the potatoes into thick fries.)</li>
<li><strong>Faites frire les frites dans l&#39;huile chaude jusqu&#39;à ce qu&#39;elles soient dorées et croustillantes.</strong> (Fry the fries in hot oil until they are golden and crispy.)</li>
<li><strong>Préparez la sauce brune en mélangeant le bouillon de bœuf avec la farine et le beurre.</strong> (Prepare the brown gravy by mixing beef broth with flour and butter.)</li>
<li><strong>Mettez les frites dans un grand bol et ajoutez les grains de fromage par-dessus.</strong> (Put the fries in a large bowl and add the cheese curds on top.)</li>
<li><strong>Versez la sauce chaude sur les frites et le fromage. Servez immédiatement!</strong> (Pour the hot gravy over the fries and cheese. Serve immediately!)</li>
</ul>

<h3 id="h-11-4-cdn-instructions">11.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>&quot;Grains de fromage&quot;</strong> or <strong>&quot;fromage en crottes&quot;</strong> (cheese curds) are essential for poutine and uniquely Québécois. They should squeak when you bite them – that&#39;s how you know they&#39;re fresh!</li>
<li>In Quebec, the impératif is often softened with <strong>&quot;donc&quot;</strong>: <strong>&quot;Viens donc!&quot;</strong> (Come on!, in a friendly way), <strong>&quot;Regarde donc ça!&quot;</strong> (Just look at that!)</li>
<li>A <strong>cégep</strong> (collège d&#39;enseignement général et professionnel) is a Quebec pre-university/vocational college unique to the province.</li>
</ul>
<hr>

<h2 id="h-unit-12-comparisons">UNIT 12: COMPARISONS &amp; SUPERLATIVES</h2>

<h3 id="h-12-1-comparatif">12.1 The Comparatif</h3>
<p>Comparisons let you describe differences and similarities between things.</p>

<table>
<thead><tr><th>Type</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>More than (+)</td><td>plus + adj. + que</td><td>Montréal est plus grande que Québec. (Montreal is bigger than Quebec City.)</td></tr>
<tr><td>Less than (-)</td><td>moins + adj. + que</td><td>L&#39;autobus est moins rapide que le métro. (The bus is less fast than the metro.)</td></tr>
<tr><td>As much as (=)</td><td>aussi + adj. + que</td><td>Le français est aussi important que l&#39;anglais au Canada. (French is as important as English in Canada.)</td></tr>
</tbody></table>

<p><strong>Comparing quantities:</strong></p>
<ul>
<li><strong>plus de + noun + que:</strong> Il y a plus de neige à Québec qu&#39;à Montréal. (There is more snow in Quebec City than in Montreal.)</li>
<li><strong>moins de + noun + que:</strong> Il y a moins de circulation le dimanche que le lundi. (There is less traffic on Sunday than on Monday.)</li>
<li><strong>autant de + noun + que:</strong> J&#39;ai autant de livres français que de livres anglais. (I have as many French books as English books.)</li>
</ul>

<p><strong>Comparing actions (verbs):</strong></p>
<ul>
<li><strong>verb + plus que:</strong> Mon frère mange plus que moi au souper. (My brother eats more than me at dinner.)</li>
<li><strong>verb + moins que:</strong> Je dors moins que ma sœur pendant la semaine. (I sleep less than my sister during the week.)</li>
<li><strong>verb + autant que:</strong> Elle travaille autant que son mari à la maison. (She works as much as her husband at home.)</li>
</ul>

<h3 id="h-12-2-superlatif">12.2 The Superlatif</h3>
<p>Superlatives express &quot;the most&quot; or &quot;the least&quot;:</p>

<table>
<thead><tr><th>Type</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>The most</td><td>le/la/les plus + adj.</td><td>Le Mont-Tremblant est la plus belle station de ski au Québec. (Mont-Tremblant is the most beautiful ski resort in Quebec.)</td></tr>
<tr><td>The least</td><td>le/la/les moins + adj.</td><td>Janvier est le mois le moins agréable pour conduire. (January is the least pleasant month for driving.)</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>Montréal est la ville la plus peuplée du Québec avec environ deux millions d&#39;habitants.</strong> (Montreal is the most populated city in Quebec with about two million inhabitants.)</li>
<li><strong>Poutine est le plat le plus connu de la cuisine québécoise dans le monde entier.</strong> (Poutine is the most well-known dish of Québécois cuisine worldwide.)</li>
<li><strong>Le lac Saint-Jean est l&#39;un des plus grands lacs du Québec.</strong> (Lake Saint-Jean is one of the largest lakes in Quebec.)</li>
</ul>

<h3 id="h-12-3-irregular-comparisons">12.3 Irregular Comparisons</h3>
<table>
<thead><tr><th>Adjective</th><th>Comparative</th><th>Superlative</th></tr></thead>
<tbody>
<tr><td>bon (good)</td><td>meilleur(e) (better)</td><td>le/la meilleur(e) (the best)</td></tr>
<tr><td>mauvais (bad)</td><td>pire (worse)</td><td>le/la pire (the worst)</td></tr>
<tr><td>bien (well - adverb)</td><td>mieux (better)</td><td>le mieux (the best)</td></tr>
</tbody></table>

<p><strong>Examples:</strong></p>
<ul>
<li><strong>La poutine de ce restaurant est meilleure que celle qu&#39;on fait à la maison.</strong> (The poutine at this restaurant is better than the one we make at home.)</li>
<li><strong>Le pire moment pour conduire à Montréal, c&#39;est l&#39;heure de pointe le vendredi soir.</strong> (The worst time to drive in Montreal is rush hour on Friday evening.)</li>
<li><strong>Tu parles mieux français qu&#39;avant! Tu as beaucoup progressé.</strong> (You speak French better than before! You have progressed a lot.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Comparing Cities in Quebec:</strong></p>
<p><em>Vous discutez avec un ami sur les meilleures villes où vivre au Québec.</em></p>
<p>&quot;Pour toi, c&#39;est quoi la meilleure ville où vivre au Québec?&quot;<br>&quot;Moi, je dirais Québec. C&#39;est plus tranquille que Montréal et les gens sont super gentils.&quot;<br>&quot;Oui, mais Montréal a plus de restaurants et plus de spectacles. La vie culturelle est plus riche.&quot;<br>&quot;C&#39;est vrai, mais le coût de la vie est aussi plus cher à Montréal. Les loyers sont moins abordables.&quot;<br>&quot;Et Sherbrooke? C&#39;est la ville la moins chère des trois et c&#39;est quand même une belle ville.&quot;<br>&quot;Tu as raison. Chaque ville a ses avantages!&quot;</p>
<p><em>(You are discussing with a friend about the best cities to live in Quebec. &quot;For you, what&#39;s the best city to live in Quebec?&quot; &quot;For me, I would say Quebec City. It&#39;s more peaceful than Montreal and the people are really nice.&quot; &quot;Yes, but Montreal has more restaurants and more shows. The cultural life is richer.&quot; &quot;That&#39;s true, but the cost of living is also more expensive in Montreal. Rents are less affordable.&quot; &quot;And Sherbrooke? It&#39;s the least expensive city of the three and it&#39;s still a beautiful city.&quot; &quot;You&#39;re right. Every city has its advantages!&quot;)</em></p>

<h3 id="h-12-4-cdn-comparisons">12.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In informal Quebec French, <strong>&quot;ben&quot;</strong> (from &quot;bien&quot;) is often used to intensify: <strong>&quot;C&#39;est ben meilleur!&quot;</strong> (It&#39;s way better!)</li>
<li><strong>&quot;Pas mal&quot;</strong> is used as &quot;pretty/quite&quot;: <strong>&quot;C&#39;est pas mal bon!&quot;</strong> (It&#39;s pretty good!)</li>
<li><strong>&quot;En masse&quot;</strong> means &quot;a lot&quot; or &quot;plenty&quot;: <strong>&quot;Y a du monde en masse!&quot;</strong> (There are plenty of people!)</li>
</ul>
<hr>

<h1 id="h-part-iv-health">PART IV: HEALTH &amp; SERVICES</h1>

<h2 id="h-unit-13-body-health">UNIT 13: BODY &amp; HEALTH</h2>

<h3 id="h-13-1-body-parts">13.1 Body Parts</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>la tête</td><td>the head</td></tr>
<tr><td>les yeux (un œil)</td><td>the eyes (an eye)</td></tr>
<tr><td>le nez</td><td>the nose</td></tr>
<tr><td>la bouche</td><td>the mouth</td></tr>
<tr><td>les oreilles</td><td>the ears</td></tr>
<tr><td>le cou</td><td>the neck</td></tr>
<tr><td>les épaules</td><td>the shoulders</td></tr>
<tr><td>le bras</td><td>the arm</td></tr>
<tr><td>la main</td><td>the hand</td></tr>
<tr><td>les doigts</td><td>the fingers</td></tr>
<tr><td>le dos</td><td>the back</td></tr>
<tr><td>le ventre</td><td>the stomach/belly</td></tr>
<tr><td>la jambe</td><td>the leg</td></tr>
<tr><td>le genou</td><td>the knee</td></tr>
<tr><td>le pied</td><td>the foot</td></tr>
<tr><td>la cheville</td><td>the ankle</td></tr>
</tbody></table>

<h3 id="h-13-2-symptoms">13.2 Describing Symptoms</h3>
<p>Use <strong>&quot;avoir mal à + body part&quot;</strong> to express pain:</p>
<ul>
<li><strong>J&#39;ai mal à la tête depuis ce matin. Je pense que j&#39;ai attrapé un rhume.</strong> (I&#39;ve had a headache since this morning. I think I caught a cold.)</li>
<li><strong>Mon fils a mal au ventre parce qu&#39;il a mangé trop de bonbons hier soir à l&#39;Halloween.</strong> (My son has a stomachache because he ate too much candy last night on Halloween.)</li>
<li><strong>Elle a mal à la gorge et elle a de la fièvre. Elle devrait aller voir le médecin.</strong> (She has a sore throat and she has a fever. She should go see the doctor.)</li>
</ul>

<p><strong>Common health expressions:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>J&#39;ai la grippe.</td><td>I have the flu.</td></tr>
<tr><td>J&#39;ai un rhume.</td><td>I have a cold.</td></tr>
<tr><td>Je tousse beaucoup.</td><td>I&#39;m coughing a lot.</td></tr>
<tr><td>J&#39;ai de la fièvre.</td><td>I have a fever.</td></tr>
<tr><td>Je suis fatigué(e).</td><td>I&#39;m tired.</td></tr>
<tr><td>J&#39;ai des allergies.</td><td>I have allergies.</td></tr>
<tr><td>Je me suis blessé(e).</td><td>I hurt myself.</td></tr>
<tr><td>Je me sens mal.</td><td>I feel sick/unwell.</td></tr>
</tbody></table>

<h3 id="h-13-3-health-expressions">13.3 Health Expressions</h3>
<ul>
<li><strong>Est-ce que tu te sens bien? Tu as l&#39;air pâle.</strong> (Are you feeling okay? You look pale.)</li>
<li><strong>Je ne me sens pas bien du tout. Je pense que je devrais rester à la maison aujourd&#39;hui.</strong> (I don&#39;t feel well at all. I think I should stay home today.)</li>
<li><strong>Mon médecin m&#39;a dit de me reposer pendant au moins trois jours.</strong> (My doctor told me to rest for at least three days.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Calling in Sick:</strong></p>
<p><em>Vous appelez votre patron parce que vous êtes malade.</em></p>
<p>&quot;Allô, bonjour Marc. C&#39;est Julie. Je suis désolée, mais je ne pourrai pas venir au bureau aujourd&#39;hui.&quot;<br>&quot;Oh non! Qu&#39;est-ce qui se passe?&quot;<br>&quot;Je pense que j&#39;ai la grippe. J&#39;ai de la fièvre et j&#39;ai mal partout.&quot;<br>&quot;Ah, le virus de la grippe circule beaucoup en ce moment. Repose-toi bien et va voir le docteur si ça ne s&#39;améliore pas.&quot;<br>&quot;Merci Marc. J&#39;espère être de retour demain ou après-demain.&quot;<br>&quot;Ne t&#39;inquiète pas. Ta santé, c&#39;est le plus important. Prends soin de toi!&quot;</p>
<p><em>(You call your boss because you are sick. &quot;Hello, good morning Marc. It&#39;s Julie. I&#39;m sorry, but I won&#39;t be able to come to the office today.&quot; &quot;Oh no! What&#39;s going on?&quot; &quot;I think I have the flu. I have a fever and I ache everywhere.&quot; &quot;Ah, the flu virus is going around a lot right now. Rest well and go see the doctor if it doesn&#39;t improve.&quot; &quot;Thank you Marc. I hope to be back tomorrow or the day after.&quot; &quot;Don&#39;t worry. Your health is the most important thing. Take care of yourself!&quot;)</em></p>

<h3 id="h-13-4-cdn-health">13.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, the healthcare system is public and covered by the <strong>RAMQ</strong> (Régie de l&#39;assurance maladie du Québec). You need a <strong>&quot;carte soleil&quot;</strong> (sun card / health insurance card) to access services.</li>
<li><strong>&quot;Un CLSC&quot;</strong> (Centre local de services communautaires) is a community health centre found in every neighbourhood in Quebec.</li>
<li>Informal: <strong>&quot;Être maganné(e)&quot;</strong> means to feel worn out or beaten up: <strong>&quot;Je suis pas mal maganné aujourd&#39;hui.&quot;</strong> (I&#39;m feeling pretty beat up today.)</li>
</ul>
<hr>

<h2 id="h-unit-14-doctor">UNIT 14: AT THE DOCTOR &amp; PHARMACY</h2>

<h3 id="h-14-1-appointment">14.1 Making an Appointment</h3>
<ul>
<li><strong>Bonjour, je voudrais prendre un rendez-vous avec le docteur Lapointe, s&#39;il vous plaît.</strong> (Hello, I would like to make an appointment with Dr. Lapointe, please.)</li>
<li><strong>Est-ce qu&#39;il y a de la disponibilité cette semaine? C&#39;est assez urgent.</strong> (Is there any availability this week? It&#39;s quite urgent.)</li>
<li><strong>Je n&#39;ai pas de médecin de famille. Est-ce que je peux aller à la clinique sans rendez-vous?</strong> (I don&#39;t have a family doctor. Can I go to the walk-in clinic?)</li>
</ul>

<h3 id="h-14-2-consultation">14.2 The Consultation</h3>
<p><strong>Common doctor-patient dialogue:</strong></p>
<ul>
<li><strong>Doctor:</strong> Qu&#39;est-ce qui vous amène aujourd&#39;hui? (What brings you in today?)</li>
<li><strong>Patient:</strong> J&#39;ai mal à la gorge depuis trois jours et je tousse beaucoup la nuit. (I&#39;ve had a sore throat for three days and I cough a lot at night.)</li>
<li><strong>Doctor:</strong> Est-ce que vous avez de la fièvre? (Do you have a fever?)</li>
<li><strong>Patient:</strong> Oui, j&#39;ai pris ma température ce matin et j&#39;avais 38,5 degrés. (Yes, I took my temperature this morning and I had 38.5 degrees.)</li>
<li><strong>Doctor:</strong> Je vais vous examiner. Ouvrez la bouche et dites &quot;Ah.&quot; (I&#39;m going to examine you. Open your mouth and say &quot;Ah.&quot;)</li>
<li><strong>Doctor:</strong> Vous avez une infection de la gorge. Je vais vous prescrire des antibiotiques. (You have a throat infection. I&#39;m going to prescribe antibiotics.)</li>
</ul>

<h3 id="h-14-3-pharmacy">14.3 At the Pharmacy</h3>
<ul>
<li><strong>Bonjour, j&#39;ai une prescription du docteur Lapointe. Est-ce que vous pouvez la remplir?</strong> (Hello, I have a prescription from Dr. Lapointe. Can you fill it?)</li>
<li><strong>Combien de temps est-ce que ça va prendre?</strong> (How long will it take?)</li>
<li><strong>Comment est-ce que je dois prendre ce médicament?</strong> (How should I take this medication?)</li>
<li><strong>Pharmacien:</strong> Prenez un comprimé deux fois par jour, matin et soir, avec de la nourriture. (Take one tablet twice a day, morning and evening, with food.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – At the Walk-In Clinic:</strong></p>
<p><em>Vous allez à une clinique sans rendez-vous à Longueuil.</em></p>
<p>&quot;Bonjour, bienvenue à la clinique médicale du boulevard. Avez-vous votre carte soleil?&quot;<br>&quot;Oui, la voici.&quot;<br>&quot;Merci. Quel est le motif de votre visite?&quot;<br>&quot;J&#39;ai mal au dos depuis une semaine et ça ne s&#39;améliore pas avec le repos.&quot;<br>&quot;D&#39;accord, asseyez-vous dans la salle d&#39;attente. Le docteur va vous voir dans environ quarante-cinq minutes.&quot;<br>&quot;Quarante-cinq minutes! C&#39;est long!&quot;<br>&quot;Je sais, on a beaucoup de patients aujourd&#39;hui. Désolée pour l&#39;attente.&quot;</p>
<p><em>(You go to a walk-in clinic in Longueuil. &quot;Hello, welcome to the Boulevard medical clinic. Do you have your health insurance card?&quot; &quot;Yes, here it is.&quot; &quot;Thank you. What is the reason for your visit?&quot; &quot;I&#39;ve had back pain for a week and it&#39;s not improving with rest.&quot; &quot;Okay, sit in the waiting room. The doctor will see you in about forty-five minutes.&quot; &quot;Forty-five minutes! That&#39;s long!&quot; &quot;I know, we have a lot of patients today. Sorry for the wait.&quot;)</em></p>

<h3 id="h-14-4-cdn-doctor">14.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, <strong>&quot;une clinique sans rendez-vous&quot;</strong> (walk-in clinic) is very common because many people do not have a <strong>&quot;médecin de famille&quot;</strong> (family doctor).</li>
<li><strong>&quot;Jean Coutu&quot;</strong> and <strong>&quot;Pharmaprix&quot;</strong> (Shoppers Drug Mart in English) are the two most common pharmacy chains in Quebec. They also sell snacks, cosmetics, and household items.</li>
<li>In Quebec French, <strong>&quot;une prescription&quot;</strong> is commonly used instead of <strong>&quot;une ordonnance&quot;</strong> (as in France).</li>
</ul>
<hr>

<h2 id="h-unit-15-banking">UNIT 15: BANKING &amp; ADMINISTRATIVE TASKS</h2>

<h3 id="h-15-1-bank-vocab">15.1 Banking Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un compte bancaire</td><td>a bank account</td></tr>
<tr><td>un compte chèques</td><td>a chequing account</td></tr>
<tr><td>un compte d&#39;épargne</td><td>a savings account</td></tr>
<tr><td>une carte de débit</td><td>a debit card</td></tr>
<tr><td>une carte de crédit</td><td>a credit card</td></tr>
<tr><td>un guichet automatique</td><td>an ATM</td></tr>
<tr><td>un virement</td><td>a transfer</td></tr>
<tr><td>un prêt / une hypothèque</td><td>a loan / a mortgage</td></tr>
<tr><td>le taux d&#39;intérêt</td><td>the interest rate</td></tr>
<tr><td>un relevé de compte</td><td>an account statement</td></tr>
</tbody></table>

<h3 id="h-15-2-transactions">15.2 Common Transactions</h3>
<ul>
<li><strong>Je voudrais déposer ce chèque dans mon compte chèques, s&#39;il vous plaît.</strong> (I would like to deposit this cheque into my chequing account, please.)</li>
<li><strong>Est-ce que je peux retirer deux cents dollars au guichet?</strong> (Can I withdraw two hundred dollars at the counter?)</li>
<li><strong>Je voudrais faire un virement de mon compte d&#39;épargne à mon compte chèques.</strong> (I would like to make a transfer from my savings account to my chequing account.)</li>
<li><strong>Mon relevé de compte montre des frais que je ne reconnais pas. Pouvez-vous vérifier?</strong> (My account statement shows charges I don&#39;t recognize. Can you check?)</li>
</ul>

<h3 id="h-15-3-admin-tasks">15.3 Administrative Tasks</h3>
<ul>
<li><strong>Je dois renouveler mon permis de conduire. Où est le bureau de la SAAQ le plus proche?</strong> (I need to renew my driver&#39;s licence. Where is the nearest SAAQ office?)</li>
<li><strong>J&#39;ai besoin de faire mon changement d&#39;adresse auprès de Postes Canada et du gouvernement.</strong> (I need to do my change of address with Canada Post and the government.)</li>
<li><strong>Est-ce que je peux payer mes impôts en ligne ou je dois aller au bureau?</strong> (Can I pay my taxes online or do I have to go to the office?)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Opening a Bank Account:</strong></p>
<p><em>Vous venez d&#39;arriver au Québec et vous ouvrez un compte bancaire à la Caisse Desjardins.</em></p>
<p>&quot;Bonjour! En quoi est-ce que je peux vous aider?&quot;<br>&quot;Bonjour, je viens d&#39;arriver au Québec et j&#39;aimerais ouvrir un compte bancaire.&quot;<br>&quot;Bien sûr! Avez-vous vos pièces d&#39;identité? Passeport et permis de travail?&quot;<br>&quot;Oui, les voici.&quot;<br>&quot;Parfait. On va ouvrir un compte chèques et un compte d&#39;épargne. Vous allez aussi recevoir une carte de débit Interac.&quot;<br>&quot;Est-ce qu&#39;il y a des frais mensuels?&quot;<br>&quot;Le forfait de base est à quatre dollars quatre-vingt-quinze par mois, avec des transactions illimitées.&quot;</p>
<p><em>(You have just arrived in Quebec and you are opening a bank account at Caisse Desjardins. &quot;Hello! How can I help you?&quot; &quot;Hello, I just arrived in Quebec and I would like to open a bank account.&quot; &quot;Of course! Do you have your identification documents? Passport and work permit?&quot; &quot;Yes, here they are.&quot; &quot;Perfect. We will open a chequing account and a savings account. You will also receive an Interac debit card.&quot; &quot;Are there monthly fees?&quot; &quot;The basic plan is four dollars ninety-five a month, with unlimited transactions.&quot;)</em></p>

<h3 id="h-15-4-cdn-banking">15.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>Desjardins</strong> is a cooperative financial group based in Quebec and is the largest federation of credit unions in North America. Many Quebecers bank with Desjardins rather than traditional banks.</li>
<li>The <strong>SAAQ</strong> (Société de l&#39;assurance automobile du Québec) handles driver&#39;s licences and vehicle registration in Quebec.</li>
<li><strong>&quot;Interac&quot;</strong> is the Canadian debit card network. Paying by &quot;Interac&quot; is equivalent to paying by debit card.</li>
<li>The <strong>&quot;NAS&quot;</strong> (numéro d&#39;assurance sociale) is the Social Insurance Number, required for working and paying taxes in Canada.</li>
</ul>
<hr>

<h2 id="h-unit-16-emergencies">UNIT 16: EMERGENCY SITUATIONS</h2>

<h3 id="h-16-1-emergency-vocab">16.1 Emergency Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Appelez le 911!</td><td>Call 911!</td></tr>
<tr><td>Au secours!</td><td>Help!</td></tr>
<tr><td>une urgence</td><td>an emergency</td></tr>
<tr><td>les pompiers</td><td>the firefighters</td></tr>
<tr><td>la police</td><td>the police</td></tr>
<tr><td>une ambulance</td><td>an ambulance</td></tr>
<tr><td>un accident</td><td>an accident</td></tr>
<tr><td>un vol</td><td>a theft</td></tr>
<tr><td>un incendie</td><td>a fire</td></tr>
<tr><td>les premiers soins</td><td>first aid</td></tr>
</tbody></table>

<h3 id="h-16-2-calling-help">16.2 Calling for Help</h3>
<p><strong>When calling 911:</strong></p>
<ul>
<li><strong>Allô, c&#39;est une urgence! Il y a eu un accident de voiture sur l&#39;autoroute 20 près de la sortie Drummondville.</strong> (Hello, this is an emergency! There was a car accident on Highway 20 near the Drummondville exit.)</li>
<li><strong>J&#39;ai besoin d&#39;une ambulance. Une personne s&#39;est évanouie dans le métro à la station Berri-UQAM.</strong> (I need an ambulance. A person fainted in the metro at the Berri-UQAM station.)</li>
<li><strong>Il y a un incendie dans l&#39;immeuble à côté du mien. Je vois de la fumée qui sort des fenêtres du troisième étage.</strong> (There is a fire in the building next to mine. I see smoke coming from the third-floor windows.)</li>
</ul>

<h3 id="h-16-3-describing-problems">16.3 Describing Problems</h3>
<ul>
<li><strong>On m&#39;a volé mon portefeuille dans le métro pendant l&#39;heure de pointe.</strong> (Someone stole my wallet in the metro during rush hour.)</li>
<li><strong>J&#39;ai perdu mes clés quelque part entre le bureau et la station de métro.</strong> (I lost my keys somewhere between the office and the metro station.)</li>
<li><strong>Ma voiture est tombée en panne sur l&#39;autoroute et je ne peux pas la déplacer.</strong> (My car broke down on the highway and I can&#39;t move it.)</li>
<li><strong>Il y a une fuite d&#39;eau dans mon appartement. L&#39;eau coule du plafond de la cuisine.</strong> (There is a water leak in my apartment. Water is flowing from the kitchen ceiling.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Car Trouble in Winter:</strong></p>
<p><em>Votre voiture ne démarre pas par un matin de grand froid.</em></p>
<p>&quot;Ah non! Le char part pas! Il fait trop frette!&quot;<br>&quot;As-tu essayé de le booster avec des câbles?&quot;<br>&quot;Non, j&#39;ai pas de câbles. Est-ce que tu peux venir me donner un boost?&quot;<br>&quot;Oui, j&#39;arrive dans dix minutes. Mais si ça marche pas, appelle le CAA.&quot;<br>&quot;T&#39;as raison. J&#39;aurais dû brancher le chauffe-moteur hier soir!&quot;<br>&quot;Ben oui, quand y fait moins trente, faut toujours le brancher!&quot;</p>
<p><em>(Your car won&#39;t start on a very cold morning. &quot;Oh no! The car won&#39;t start! It&#39;s too cold!&quot; &quot;Did you try to boost it with cables?&quot; &quot;No, I don&#39;t have cables. Can you come give me a boost?&quot; &quot;Yes, I&#39;ll be there in ten minutes. But if it doesn&#39;t work, call CAA.&quot; &quot;You&#39;re right. I should have plugged in the block heater last night!&quot; &quot;Yeah, when it&#39;s minus thirty, you always have to plug it in!&quot;)</em></p>

<h3 id="h-16-4-cdn-emergencies">16.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, the emergency number is <strong>911</strong>, just like in the rest of Canada and the US.</li>
<li>A <strong>&quot;chauffe-moteur&quot;</strong> (block heater) is an electric heater plugged into a car&#39;s engine overnight in extreme cold to prevent the engine from freezing. You will see electrical outlets in parking lots throughout Quebec!</li>
<li>The <strong>CAA</strong> (Canadian Automobile Association) provides roadside assistance.</li>
<li><strong>&quot;Booster&quot;</strong> or <strong>&quot;donner un boost&quot;</strong> means to jump-start a car with cables – a very common winter occurrence in Quebec.</li>
<li><strong>&quot;Le char part pas&quot;</strong> is typical spoken Quebec French for &quot;La voiture ne démarre pas&quot; (The car won&#39;t start).</li>
</ul>
"""

with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write(content)

print(f"Part 4 (Units 11-16) done. File size: {os.path.getsize(OUTPUT)} bytes")
