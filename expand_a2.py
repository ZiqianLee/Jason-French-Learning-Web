import os
import re

# We will read a2.html, and for every unit, right before the </div> closing the unit-content, we will inject new content.
file_path = "a2.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the additions for each of the 20 A2 units.
# The keys correspond to the unit number as found in the HTML headers, e.g., "UNIT 1:"
additions = {
    "UNIT 1:": """
<h4>1.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The verb <em>aller</em> (to go) is highly irregular. Unlike standard -er verbs, it does not follow the regular pattern. Also, when saying "to the" before a masculine country or place starting with a consonant, use <em>au</em> (e.g., <em>au Canada</em>), but use <em>en</em> for feminine (<em>en France</em>).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't say "Je suis faim" (I am hungry). In French, you "have" hunger: <strong>J'ai faim</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Le lendemain</em> - The next day</li>
    <li><em>Quotidien(ne)</em> - Daily</li>
    <li><em>Se réveiller</em> - To wake up</li>
    <li><em>Se brosser les dents</em> - To brush one's teeth</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je vais travailler.</em> -> I am going to work.</li>
    <li><em>Elles ont chaud.</em> -> They are hot.</li>
    <li><em>Nous faisons du sport.</em> -> We play sports.</li>
    <li><em>Il est en retard.</em> -> He is late.</li>
    <li><em>Tu as quel âge ?</em> -> How old are you?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 2:": """
<h4>2.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The only irregular stem in the imparfait is <em>être</em> (j'étais). All other verbs, including usually irregular ones like <em>faire</em> (je faisais) and <em>aller</em> (j'allais), follow the standard rule of taking the <em>nous</em> form in the present minus -ons.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use the imparfait for an action that happened once at a specific time. (E.g., Don't say "Hier soir, je mangeais à 18h." Say: <strong>Hier soir, j'ai mangé à 18h.</strong>)</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Autrefois</em> - In the past / Formerly</li>
    <li><em>À l'époque</em> - At the time</li>
    <li><em>D'habitude</em> - Usually</li>
    <li><em>Fréquemment</em> - Frequently</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je lisais souvent.</em> -> I used to read often.</li>
    <li><em>Il faisait beau.</em> -> The weather was nice.</li>
    <li><em>Nous aimions jouer dehors.</em> -> We liked to play outside.</li>
    <li><em>Quand j'étais petit...</em> -> When I was little...</li>
    <li><em>Elle portait un manteau rouge.</em> -> She was wearing a red coat.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 3:": """
<h4>3.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Verbs ending in -yer change 'y' to 'i' in all forms of the futur simple (e.g., <em>nettoyer</em> -> <em>je nettoierai</em>). Verbs with a silent 'e' in the stem drop it or change to 'è' (e.g., <em>acheter</em> -> <em>j'achèterai</em>).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use the futur simple after "si" in conditional clauses. Say <strong>Si je peux, je viendrai</strong> (If I can, I will come), not "Si je pourrai...".</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Bientôt</em> - Soon</li>
    <li><em>Dans l'avenir</em> - In the future</li>
    <li><em>Le mois prochain</em> - Next month</li>
    <li><em>Désormais</em> - From now on</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je finirai demain.</em> -> I will finish tomorrow.</li>
    <li><em>Nous irons au parc.</em> -> We will go to the park.</li>
    <li><em>Ils seront contents.</em> -> They will be happy.</li>
    <li><em>Tu auras le temps.</em> -> You will have time.</li>
    <li><em>Elle saura la vérité.</em> -> She will know the truth.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 4:": """
<h4>4.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> <em>Venir de</em> is only used for the very recent past ("just"). It cannot be used with a specific timestamp. You cannot say "Je viens d'arriver hier."</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use "juste" to translate the English "I just did X". Say <strong>Je viens de le faire</strong>, not "J'ai juste fait ça".</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>À l'instant</em> - Just now / Right now</li>
    <li><em>Il y a deux minutes</em> - Two minutes ago</li>
    <li><em>Actuellement</em> - Currently</li>
    <li><em>En ce moment</em> - At this moment</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je viens de terminer.</em> -> I just finished.</li>
    <li><em>Ils viennent de partir.</em> -> They just left.</li>
    <li><em>Nous sommes en train de manger.</em> -> We are in the middle of eating.</li>
    <li><em>Elle vient d'appeler.</em> -> She just called.</li>
    <li><em>Tu es en train d'étudier.</em> -> You are currently studying.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 5:": """
<h4>5.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When expressing prices, the euro symbol (€) goes after the number in France, but the dollar sign ($) goes before in English Canada. In Quebec French, it is written <em>10,00 $</em>. Notice the comma instead of a decimal.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't say "Je paie pour le repas." The verb <em>payer</em> already means "to pay for". Say <strong>Je paie le repas</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un rabais</em> - A discount</li>
    <li><em>La caisse</em> - The cash register</li>
    <li><em>Un reçu / Une facture</em> - A receipt / An invoice</li>
    <li><em>Abordable</em> - Affordable</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>C'est combien ?</em> -> How much is it?</li>
    <li><em>C'est trop cher !</em> -> It's too expensive!</li>
    <li><em>Je chausse du 40.</em> -> I wear size 40 (shoes).</li>
    <li><em>Par carte, s'il vous plaît.</em> -> By card, please.</li>
    <li><em>Avez-vous la taille au-dessus ?</em> -> Do you have the next size up?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 6:": """
<h4>6.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In Quebec, the first floor (ground floor) is called <em>le rez-de-chaussée</em>, and the floor above it is <em>le premier étage</em>. This can confuse North Americans. Also, apartments are often described by total room count: a "4 et demi" (4 ½) means 1 bedroom, 1 living room, 1 kitchen, 1 bathroom (the half).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use "dans" to say you are at someone's house. Say <strong>chez moi</strong> (at my place) or <strong>chez Paul</strong> (at Paul's).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Le sous-sol</em> - The basement</li>
    <li><em>Un loyer</em> - Rent (the payment)</li>
    <li><em>Un propriétaire</em> - A landlord / owner</li>
    <li><em>Le chauffage</em> - Heating</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je cherche un appartement.</em> -> I am looking for an apartment.</li>
    <li><em>Le loyer est cher.</em> -> The rent is expensive.</li>
    <li><em>Mon lit est confortable.</em> -> My bed is comfortable.</li>
    <li><em>J'habite au premier étage.</em> -> I live on the second floor (US).</li>
    <li><em>La cuisine est équipée.</em> -> The kitchen is fully equipped.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 7:": """
<h4>7.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When using modes of transport you can step inside (train, bus, car, plane), use the preposition <em>en</em>: <strong>en voiture</strong>, <strong>en train</strong>. For things you ride on top of, use <em>à</em>: <strong>à vélo</strong>, <strong>à moto</strong>, <strong>à pied</strong>.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't say "Je prends le bus à Paris." (I take the bus to Paris). <em>Prendre</em> means you use the vehicle. To say where you are going, say: <strong>Je vais à Paris en bus.</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un embouteillage</em> - A traffic jam</li>
    <li><em>Le quai</em> - The platform (train)</li>
    <li><em>Un aller-retour</em> - A round trip ticket</li>
    <li><em>Traverser</em> - To cross</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Allez tout droit.</em> -> Go straight ahead.</li>
    <li><em>Tournez à gauche.</em> -> Turn left.</li>
    <li><em>Où est la station de métro ?</em> -> Where is the subway station?</li>
    <li><em>Je préfère prendre le train.</em> -> I prefer to take the train.</li>
    <li><em>C'est le prochain arrêt.</em> -> It's the next stop.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 8:": """
<h4>8.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Weather expressions almost always use the verb <em>faire</em> (Il fait beau, il fait froid) in the third person singular. The exception is precipitation, which uses its own verbs: <strong>Il pleut</strong> (It rains) and <strong>Il neige</strong> (It snows).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use <em>être</em> for weather. Never say "Il est chaud" to mean "It is hot out" (that refers to a physical object being hot). Always say <strong>Il fait chaud.</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>La météo</em> - The weather forecast</li>
    <li><em>Nuageux</em> - Cloudy</li>
    <li><em>Une tempête</em> - A storm</li>
    <li><em>Il gèle</em> - It's freezing</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Quel temps fait-il ?</em> -> What's the weather like?</li>
    <li><em>Il pleut à verse.</em> -> It's pouring rain.</li>
    <li><em>Le ciel est bleu.</em> -> The sky is blue.</li>
    <li><em>Il fait moins dix.</em> -> It's minus ten degrees.</li>
    <li><em>C'est la canicule.</em> -> It's a heatwave.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 9:": """
<h4>9.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When declining an invitation gently, the verb <em>devoir</em> (must) is heavily used to soften the blow: <strong>Je dois travailler</strong> (I have to work) sounds better than a flat refusal.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't say "Je suis désolé mais je peux pas" without giving a reason in French culture; it can be seen as abrupt. Add context: <strong>J'aimerais bien, mais j'ai déjà des plans.</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Se rassembler</em> - To gather</li>
    <li><em>Un empêchement</em> - A prior engagement / A hold-up</li>
    <li><em>À la prochaine</em> - Until next time</li>
    <li><em>Prévenir</em> - To give notice / To warn</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Tu veux venir avec nous ?</em> -> Do you want to come with us?</li>
    <li><em>Ça te dit de sortir ?</em> -> Are you up for going out?</li>
    <li><em>Avec plaisir !</em> -> With pleasure!</li>
    <li><em>Je suis occupé ce soir.</em> -> I'm busy tonight.</li>
    <li><em>On se voit où ?</em> -> Where are we meeting?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 10:": """
<h4>10.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The verb <em>répondre</em> (to answer) always takes the preposition <em>à</em>. You answer <em>to</em> someone. <strong>Je réponds à mon ami</strong>, not "Je réponds mon ami".</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> When answering the phone, say <strong>"Allô ?"</strong> (Quebec) or <strong>"Oui, allô ?"</strong> (France). Do not answer with a simple "Bonjour" until the conversation starts.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>La messagerie vocale</em> - Voicemail</li>
    <li><em>Un texto</em> - A text message</li>
    <li><em>Une application</em> - An app</li>
    <li><em>Une pièce jointe</em> - An attachment</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>C'est de la part de qui ?</em> -> Who is calling?</li>
    <li><em>Je vous le passe.</em> -> I will put him/her through to you.</li>
    <li><em>Laissez un message.</em> -> Leave a message.</li>
    <li><em>Je n'ai pas de réseau.</em> -> I don't have a signal.</li>
    <li><em>Je t'envoie un courriel.</em> -> I'm sending you an email.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 11:": """
<h4>11.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In the imperative (giving commands), -ER verbs drop the ending 's' in the <em>tu</em> form. <em>Tu manges</em> becomes <strong>Mange !</strong> (Eat!). However, if followed by an object pronoun "y" or "en", the 's' is added back for pronunciation: <strong>Manges-en !</strong> (Eat some!).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use the subject pronoun in the imperative. "Tu vas à gauche" is a statement. <strong>Va à gauche</strong> is a command.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Mélanger</em> - To mix</li>
    <li><em>Ajouter</em> - To add</li>
    <li><em>Faire cuire</em> - To bake/cook</li>
    <li><em>Un conseil</em> - A piece of advice</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Ne touchez pas !</em> -> Don't touch!</li>
    <li><em>Écoutez bien.</em> -> Listen closely.</li>
    <li><em>Coupez les légumes.</em> -> Cut the vegetables.</li>
    <li><em>Faites attention.</em> -> Be careful.</li>
    <li><em>Tu devrais te reposer.</em> -> You should rest.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 12:": """
<h4>12.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> <em>Bon</em> (good) becomes <em>meilleur</em> (better). <em>Bien</em> (well) becomes <em>mieux</em> (better). Never say "plus bon" or "plus bien". E.g., <strong>Ce vin est meilleur. Il chante mieux que moi.</strong></li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> When comparing nouns, you must use <strong>plus de</strong> (more of) or <strong>moins de</strong> (less of). "J'ai plus amis que lui" is wrong. It must be <strong>J'ai plus d'amis que lui.</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Autant (que)</em> - As much (as)</li>
    <li><em>Pire</em> - Worse</li>
    <li><em>Identique</em> - Identical</li>
    <li><em>Différent</em> - Different</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il est plus grand que moi.</em> -> He is taller than me.</li>
    <li><em>C'est le plus beau film.</em> -> It's the most beautiful movie.</li>
    <li><em>Elle a autant d'argent que lui.</em> -> She has as much money as him.</li>
    <li><em>C'est le pire scénario.</em> -> It's the worst-case scenario.</li>
    <li><em>Je vais mieux.</em> -> I'm doing better.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 13:": """
<h4>13.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When expressing pain, the structure is <strong>avoir mal à + body part</strong>. You must contract <em>à + le</em> into <strong>au</strong>, and <em>à + les</em> into <strong>aux</strong>. E.g., J'ai mal <strong>au</strong> dos, j'ai mal <strong>aux</strong> dents.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use possessive adjectives for body parts in French. Instead of saying "Ma tête me fait mal" (My head hurts), French speakers say <strong>J'ai mal à la tête</strong> (I have pain in the head).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une blessure</em> - An injury</li>
    <li><em>Guérir</em> - To heal/cure</li>
    <li><em>Éternuer</em> - To sneeze</li>
    <li><em>La toux</em> - A cough</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>J'ai un rhume.</em> -> I have a cold.</li>
    <li><em>Mon bras est cassé.</em> -> My arm is broken.</li>
    <li><em>Je me sens malade.</em> -> I feel sick.</li>
    <li><em>Où as-tu mal ?</em> -> Where does it hurt?</li>
    <li><em>J'ai mal au ventre.</em> -> I have a stomach ache.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 14:": """
<h4>14.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Medical specialists are often referred to as "le médecin" locally, but terms like <em>l'ophtalmologue</em> (eye doctor) and <em>le/la dentiste</em> are common. Note that "un physicien" means a physicist. A doctor is <strong>un médecin</strong>.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> In Quebec, the healthcare card is called <strong>la carte d'assurance maladie</strong> or informally <em>la carte soleil</em>. Don't use the French term "la carte Vitale".</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>La salle d'attente</em> - The waiting room</li>
    <li><em>Une ordonnance</em> - A prescription</li>
    <li><em>Une pilule</em> - A pill</li>
    <li><em>Des effets secondaires</em> - Side effects</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je dois voir un médecin.</em> -> I need to see a doctor.</li>
    <li><em>Prenez ce médicament.</em> -> Take this medication.</li>
    <li><em>Avez-vous de la fièvre ?</em> -> Do you have a fever?</li>
    <li><em>Respirez profondément.</em> -> Breathe deeply.</li>
    <li><em>Ça va passer.</em> -> It will go away.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 15:": """
<h4>15.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In Canada, a checking account is <strong>un compte chèque</strong> while in France it is <em>un compte courant</em>. A savings account is <strong>un compte épargne</strong> everywhere.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Never say "tirer de l'argent" (to pull money) at an ATM. The correct verb is <strong>retirer</strong> (to withdraw): <strong>Je dois retirer de l'argent.</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un virement</em> - A bank transfer</li>
    <li><em>Le solde</em> - The balance</li>
    <li><em>Un guichet automatique</em> - An ATM</li>
    <li><em>Une succursale</em> - A branch (of a bank)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je veux ouvrir un compte.</em> -> I want to open an account.</li>
    <li><em>Voici ma carte de crédit.</em> -> Here is my credit card.</li>
    <li><em>Quel est le taux d'intérêt ?</em> -> What is the interest rate?</li>
    <li><em>Je dois faire un dépôt.</em> -> I need to make a deposit.</li>
    <li><em>Signez ici.</em> -> Sign here.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 16:": """
<h4>16.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The universal emergency number in North America is 911 (said <em>neuf un un</em>). In France, it's 112 or 15/17/18. Always know local emergency numbers.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> If you are lost, don't say "Je suis perdu" (though grammatically correct, it sounds poetic/metaphorical). Just say <strong>Je me suis perdu(e).</strong> (I have gotten myself lost.)</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Au secours !</em> - Help!</li>
    <li><em>L'incendie</em> - The fire (uncontrolled)</li>
    <li><em>Les pompiers</em> - The firefighters</li>
    <li><em>Urgences</em> - Emergency room</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Appelez la police !</em> -> Call the police!</li>
    <li><em>Il y a eu un accident.</em> -> There has been an accident.</li>
    <li><em>Quelqu'un est blessé.</em> -> Someone is hurt.</li>
    <li><em>Restez calme.</em> -> Stay calm.</li>
    <li><em>On m'a volé mon sac.</em> -> My bag was stolen.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 17:": """
<h4>17.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> To express going to a country, the preposition is based on the noun's gender. <strong>En</strong> for feminine (<em>En France, En Chine</em>), <strong>Au</strong> for masculine singular (<em>Au Canada, Au Japon</em>), and <strong>Aux</strong> for plural (<em>Aux États-Unis</em>).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't translate "I miss my flight" using <em>manquer</em> like a direct object normally. It's safe to say: <strong>J'ai raté mon vol.</strong> (I missed my flight's departure).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>L'itinéraire</em> - The itinerary</li>
    <li><em>La douane</em> - Customs</li>
    <li><em>Une escale</em> - A layover</li>
    <li><em>Annuler</em> - To cancel</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Quand partez-vous ?</em> -> When are you leaving?</li>
    <li><em>J'ai réservé mes billets.</em> -> I booked my tickets.</li>
    <li><em>Où est la porte d'embarquement ?</em> -> Where is the boarding gate?</li>
    <li><em>Je dois faire ma valise.</em> -> I have to pack my suitcase.</li>
    <li><em>Avez-vous votre passeport ?</em> -> Do you have your passport?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 18:": """
<h4>18.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> While checking out of a North American hotel is usually stated via English overlap <em>faire le checkout</em> informally in Quebec, the formal French is <strong>régler la note</strong> (settle the bill) or <strong>libérer la chambre</strong> (vacate the room).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> The word <em>location</em> in French means "a rental", not "a place/location". A location is <strong>un emplacement</strong>. If a hotel sign says <em>Location de voitures</em>, it means Car Rentals.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un lit double</em> - A double bed</li>
    <li><em>La climatisation</em> - Air conditioning</li>
    <li><em>Complet</em> - Fully booked / No vacancies</li>
    <li><em>Le vol est retardé</em> - The flight is delayed</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>J'ai une réservation.</em> -> I have a reservation.</li>
    <li><em>À quelle heure est le déjeuner ?</em> -> What time is breakfast (QC)?</li>
    <li><em>La chambre est propre.</em> -> The room is clean.</li>
    <li><em>Mon vol est annulé.</em> -> My flight is canceled.</li>
    <li><em>Où récupérer les bagages ?</em> -> Where is baggage claim?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 19:": """
<h4>19.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Quebec has a unique holiday not celebrated elsewhere in Canada: <strong>La Saint-Jean-Baptiste</strong> (or La Fête nationale du Québec) on June 24. This is functionally the national independence day equivalent in terms of cultural scale.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't assume all French culture applies to Quebec. Do not praise the "baguette" or "Eiffel Tower" to a local as local pride; recognize <strong>la tourtière</strong>, <strong>le sirop d'érable</strong>, and <strong>les cabanes à sucre</strong> as distinct Québécois heritage.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Les Premières Nations</em> - First Nations (Indigenous peoples)</li>
    <li><em>Le patrimoine</em> - Heritage</li>
    <li><em>Une manifestation</em> - A protest / large public event</li>
    <li><em>L'hiver s'en vient</em> - Winter is coming (Very Québécois phrasing)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>C'est la fête nationale.</em> -> It's the national holiday.</li>
    <li><em>On célèbre dans les rues.</em> -> People celebrate in the streets.</li>
    <li><em>J'adore la poutine.</em> -> I love poutine.</li>
    <li><em>Il faut protéger la langue.</em> -> We must protect the language.</li>
    <li><em>Connaissez-vous ce chanteur ?</em> -> Do you know this singer?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 20:": """
<h4>20.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> B1 testing will enforce stricter adherence to genders, prepositions with infinitives (e.g., <em>commencer à</em> vs <em>décider de</em>), and relative pronouns like <em>qui</em>, <em>que</em>, <em>où</em>. These must be flawlessly identified.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't try to use overly complex tenses you haven't mastered yet. Stick to what you know perfectly. A polished Passé Composé beats a broken Plus-Que-Parfait.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>La réussite</em> - Success</li>
    <li><em>Une épreuve</em> - A trial / A highly formal test</li>
    <li><em>Améliorer</em> - To improve</li>
    <li><em>Un but</em> - A goal</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je suis prêt pour l'examen.</em> -> I am ready for the exam.</li>
    <li><em>J'ai beaucoup étudié.</em> -> I studied a lot.</li>
    <li><em>Mon français s'améliore.</em> -> My French is improving.</li>
    <li><em>Je veux voyager à Paris.</em> -> I want to travel to Paris.</li>
    <li><em>Merci pour votre aide.</em> -> Thank you for your help.</li>
  </ul>
</li>
</ul>
"""
}

# The regex should find the closing </div> of each unit's "unit-content" 
# Notice the structure:
# <h2 id="..."><span class="unit-title">UNIT 1: REVIEW OF A1 ESSENTIALS</span></h2>
# ...
# </div> <!-- this is the end of the unit-content -->

modified_content = content
for u, block in additions.items():
    # Remove the <h4> title to blend in seamlessly
    block = re.sub(r'<h4>.*?</h4>\n', '', block)
    
    # Target the h2 tag for the unit in the main content
    # This avoids matching the sidebar TOC link
    pattern_h2 = re.compile(rf'<h2[^>]* id="h-[^>]*">.*?{re.escape(u)}.*?</h2>', re.IGNORECASE)
    match_h2 = pattern_h2.search(modified_content)
    
    if match_h2:
        u_header_end = match_h2.end()
        # Search for the next boundary (<hr>, next h2, or conclusion)
        search_pattern = re.compile(r'(<hr>|<h2 id="h-unit|<h1|<h2 id="h-a2-conclusion|<h2 id="h-b1-conclusion|<h2 id="h-b2-conclusion)')
        match_boundary = search_pattern.search(modified_content[u_header_end:])
        
        if match_boundary:
            insert_pos = u_header_end + match_boundary.start()
            modified_content = modified_content[:insert_pos] + "\n" + block + "\n\n" + modified_content[insert_pos:]
        else:
            print(f"Failed to find boundary for {u}")
    else:
        print(f"Could not find header for {u}")

with open("a2_expanded.html", "w", encoding="utf-8") as f:
    f.write(modified_content)

print(f"A2 Expand script completed, testing logic.")
