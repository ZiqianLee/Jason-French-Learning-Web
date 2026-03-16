import os
import re

file_path = "b1.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the additions for each of the 20 B1 units.
additions = {
    "UNIT 1:": """
<h4>1.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The plus-que-parfait relies on the imparfait of the auxiliary verb. If a verb uses <em>être</em> as an auxiliary (like <em>aller</em>, <em>venir</em>, reflexive verbs), the past participle MUST agree in gender and number with the subject: <strong>Elle était allée.</strong></li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Do not confuse the plus-que-parfait with the passé composé. "I ate" is <em>J'ai mangé</em>. "I had eaten" is <strong>J'avais mangé</strong>. It is only used to show an action happened <em>before</em> another past action.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Déjà</em> - Already</li>
    <li><em>Auparavant</em> - Previously / Beforehand</li>
    <li><em>À l'heure où...</em> - At the time when...</li>
    <li><em>Avant que</em> - Before (+ subjunctive)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il était déjà parti.</em> -> He had already left.</li>
    <li><em>Nous avions fini le travail.</em> -> We had finished the work.</li>
    <li><em>J'avais oublié mes clés.</em> -> I had forgotten my keys.</li>
    <li><em>Elle s'était réveillée tôt.</em> -> She had woken up early.</li>
    <li><em>Quand je suis arrivé, le film avait commencé.</em> -> When I arrived, the movie had started.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 2:": """
<h4>2.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Verbs with irregular stems in the futur simple share that exact same irregular stem in the conditionnel. Examples: <em>aller</em> -> <em>j'irais</em>, <em>être</em> -> <em>je serais</em>, <em>avoir</em> -> <em>j'aurais</em>.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Mixing up "si" clauses. For the conditionnel présent, the "si" clause must be in the imparfait. NEVER use the conditionnel directly after "si". <strong>Si j'avais de l'argent, j'achèterais une voiture</strong> (Not: "Si j'aurais...").</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Souhaiter</em> - To wish/hope</li>
    <li><em>Ça m'étonnerait</em> - That would surprise me / I doubt it</li>
    <li><em>À ta place</em> - In your place</li>
    <li><em>Un conseil</em> - A piece of advice</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je voudrais un café.</em> -> I would like a coffee.</li>
    <li><em>Pourriez-vous m'aider ?</em> -> Could you help me?</li>
    <li><em>À ta place, je n'irais pas.</em> -> If I were you, I wouldn't go.</li>
    <li><em>Il devrait étudier plus.</em> -> He should study more.</li>
    <li><em>Nous aimerions voyager en France.</em> -> We would like to travel to France.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 3:": """
<h4>3.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The subjunctive is triggered by necessity, emotion, doubt, and desire. However, verbs of thinking/believing (<em>penser</em>, <em>croire</em>, <em>espérer</em>) do NOT trigger the subjunctive in the affirmative. "Je pense qu'il <strong>est</strong> là." But in the negative, they do: "Je ne pense pas qu'il <strong>soit</strong> là."</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> If the subject of both clauses is the same, use the infinitive, not the subjunctive. "Je veux que je lise" is wrong. Use: <strong>Je veux lire.</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Il faut que</em> - It is necessary that</li>
    <li><em>Bien que</em> - Although / Even though</li>
    <li><em>Pour que</em> - So that / In order that</li>
    <li><em>C'est dommage que</em> - It's a shame that</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il faut que tu viennes.</em> -> You must come.</li>
    <li><em>Je veux qu'elle lise ce livre.</em> -> I want her to read this book.</li>
    <li><em>Bien qu'il pleuve, je sors.</em> -> Even though it's raining, I'm going out.</li>
    <li><em>Il est important que nous sachions la vérité.</em> -> It is important that we know the truth.</li>
    <li><em>Je suis ravi que tu sois là.</em> -> I'm delighted that you are here.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 4:": """
<h4>4.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The future anterieur is used to express an action that will be completed <em>before</em> another future action. It uses the futur simple of the auxiliary (<em>être</em> or <em>avoir</em>) + the past participle.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> In English, we often use the present perfect for future events ("When I have finished..."). In French, if the main clause is future, the "when" clause MUST use the future anterieur: <strong>Quand j'aurai fini...</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Dès que</em> - As soon as</li>
    <li><em>Aussitôt que</em> - As soon as</li>
    <li><em>Une fois que</em> - Once</li>
    <li><em>Bientôt</em> - Soon</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Quand tu auras mangé, on partira.</em> -> When you have eaten, we will leave.</li>
    <li><em>Dès qu'il sera arrivé, appelez-moi.</em> -> As soon as he has arrived, call me.</li>
    <li><em>J'aurai terminé à 17h.</em> -> I will have finished by 5 PM.</li>
    <li><em>Une fois qu'elle aura compris, tout sera facile.</em> -> Once she has understood, everything will be easy.</li>
    <li><em>Nous serons déjà partis.</em> -> We will have already left.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 5:": """
<h4>5.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Expressing opinions clearly is a hallmark of B1. Remember that <em>Je trouve que</em> takes the indicative, but <em>Je doute que</em> takes the subjunctive.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't just say "Je pense que oui" all the time. Use nuanced phrases like <strong>À mon avis...</strong> or <strong>D'après moi...</strong> to sound more fluent.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>En ce qui me concerne</em> - As far as I'm concerned</li>
    <li><em>Il me semble que</em> - It seems to me that</li>
    <li><em>Avoir tort</em> - To be wrong</li>
    <li><em>Avoir raison</em> - To be right</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>À mon avis, c'est une erreur.</em> -> In my opinion, it's a mistake.</li>
    <li><em>Je suis tout à fait d'accord.</em> -> I completely agree.</li>
    <li><em>Je ne partage pas cet avis.</em> -> I don't share that opinion.</li>
    <li><em>Tu as tort.</em> -> You are wrong.</li>
    <li><em>Personnellement, je préfère rester.</em> -> Personally, I prefer to stay.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 6:": """
<h4>6.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> <em>Parce que</em> answers "Pourquoi?" and gives a neutral cause. <em>Puisque</em> introduces a cause that is already known to the listener (Since...). <em>Grâce à</em> is for positive causes (Thanks to), while <em>À cause de</em> is for negative causes (Because of).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Never start a sentence with <em>Parce que</em> in formal writing. Use <strong>Comme</strong> (Since/As) at the beginning of a sentence.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Par conséquent</em> - Consequently</li>
    <li><em>C'est la raison pour laquelle</em> - That is the reason why</li>
    <li><em>En effet</em> - Indeed / In fact</li>
    <li><em>Provoquer</em> - To cause / provoke</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il a réussi grâce à son travail.</em> -> He succeeded thanks to his hard work.</li>
    <li><em>Le vol est annulé à cause de la tempête.</em> -> The flight is canceled because of the storm.</li>
    <li><em>Comme il pleut, je reste chez moi.</em> -> Since it's raining, I'm staying home.</li>
    <li><em>J'ai faim, donc je mange.</em> -> I am hungry, therefore I eat.</li>
    <li><em>Puisque tu es là, aide-moi.</em> -> Since you are here, help me.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 7:": """
<h4>7.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Forming hypotheses in French uses rigid tense structures. Type 1 (Likely): Si + Présent -> Futur. Type 2 (Unlikely): Si + Imparfait -> Conditionnel Présent. Type 3 (Impossible/Past): Si + Plus-que-parfait -> Conditionnel Passé.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Never put the future or conditional directly in the "Si" clause. Ever.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Supposons que</em> - Suppose that (+ subj)</li>
    <li><em>Au cas où</em> - In case (+ cond)</li>
    <li><em>À condition que</em> - On the condition that (+ subj)</li>
    <li><em>Sinon</em> - Otherwise / If not</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Si j'ai le temps, je t'aiderai.</em> -> If I have time, I will help you.</li>
    <li><em>Si j'étais toi, j'accepterais.</em> -> If I were you, I would accept.</li>
    <li><em>S'il avait su, il ne l'aurait pas fait.</em> -> If he had known, he wouldn't have done it.</li>
    <li><em>Prends un parapluie au cas où il pleuvrait.</em> -> Take an umbrella in case it rains.</li>
    <li><em>Je viendrai à condition qu'il fasse beau.</em> -> I will come on the condition that the weather is nice.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 8:": """
<h4>8.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When converting direct speech ("Je suis fatigué") to indirect past speech (Il a dit qu'il <em>était</em> fatigué), tenses shift back. Present becomes imparfait, passé composé becomes plus-que-parfait, futur becomes conditionnel.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't forget that time markers also change in past reported speech. "Aujourd'hui" becomes <strong>ce jour-là</strong>, "demain" becomes <strong>le lendemain</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Avouer</em> - To confess/admit</li>
    <li><em>Affirmer</em> - To assert/claim</li>
    <li><em>Le lendemain</em> - The following day</li>
    <li><em>La veille</em> - The day before</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il m'a dit qu'il viendrait.</em> -> He told me he would come.</li>
    <li><em>Elle a demandé si j'étais prêt.</em> -> She asked if I was ready.</li>
    <li><em>Il a affirmé qu'il l'avait vu.</em> -> He claimed that he had seen it.</li>
    <li><em>Je me demande ce qu'il fait.</em> -> I wonder what he is doing.</li>
    <li><em>Il m'a conseillé de partir.</em> -> He advised me to leave.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 9:": """
<h4>9.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In B1, you must be able to read short news articles. The passive voice is heavily used in French journalism (e.g., <em>La loi a été votée</em>).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use "journal" to mean a personal diary. A <strong>journal</strong> is a newspaper. A personal diary is <strong>un journal intime</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>L'actualité</em> - Current events / The news</li>
    <li><em>Une manchette</em> - A headline</li>
    <li><em>Les réseaux sociaux</em> - Social media</li>
    <li><em>Un présentateur</em> - A news anchor</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>J'ai lu ça dans le journal.</em> -> I read that in the newspaper.</li>
    <li><em>C'est à la une.</em> -> It's on the front page.</li>
    <li><em>Les nouvelles sont bonnes.</em> -> The news is good. (Remember: "nouvelles" is plural)</li>
    <li><em>Il écoute la radio tous les matins.</em> -> He listens to the radio every morning.</li>
    <li><em>Un sondage révèle que...</em> -> A poll reveals that...</li>
  </ul>
</li>
</ul>
""",
    "UNIT 10:": """
<h4>10.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The environment is a major topic in B1 exams. Note that "un écologiste" is an environmentalist, while "l'écologie" is the study of the environment or the green movement.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Do not translate "global warming" literally. The French term is <strong>le réchauffement climatique</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Le gaspillage</em> - Waste (the act of wasting)</li>
    <li><em>Les ordures</em> - Garbage / Trash</li>
    <li><em>Renouvelable</em> - Renewable</li>
    <li><em>Trier les déchets</em> - To recycle/sort trash</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il faut protéger l'environnement.</em> -> We must protect the environment.</li>
    <li><em>La pollution de l'air augmente.</em> -> Air pollution is increasing.</li>
    <li><em>Nous recyclons le plastique et le verre.</em> -> We recycle plastic and glass.</li>
    <li><em>L'énergie solaire est propre.</em> -> Solar energy is clean.</li>
    <li><em>C'est une espèce en voie de disparition.</em> -> It's an endangered species.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 11:": """
<h4>11.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In French, professions generally don't take an article after <em>être</em>. "Je suis professeur" (not "un professeur"). However, if customized with an adjective, add the article: "C'est <strong>un excellent professeur</strong>."</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use <em>travailler</em> for students doing homework. Students <strong>étudient</strong> or <strong>font leurs devoirs</strong>. <em>Travailler</em> implies a job.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un entretien d'embauche</em> - A job interview</li>
    <li><em>Le chômage</em> - Unemployment</li>
    <li><em>Postuler (à)</em> - To apply (for)</li>
    <li><em>Un atout</em> - An asset / advantage</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je cherche un emploi à temps plein.</em> -> I'm looking for a full-time job.</li>
    <li><em>Elle travaille dans les ressources humaines.</em> -> She works in human resources.</li>
    <li><em>Il a été renvoyé.</em> -> He got fired.</li>
    <li><em>Mon patron est très exigeant.</em> -> My boss is very demanding.</li>
    <li><em>J'ai envoyé mon CV.</em> -> I sent my resume.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 12:": """
<h4>12.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In Quebec, the education system has a unique step between high school and university called <strong>le cégep</strong> (Collège d'enseignement général et professionnel).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't say "Je vais graduer". The correct French is <strong>obtenir son diplôme</strong>. "Graduer" means measuring something in degrees.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Les frais de scolarité</em> - Tuition fees</li>
    <li><em>Une bourse</em> - A scholarship</li>
    <li><em>Échouer à (un examen)</em> - To fail (an exam)</li>
    <li><em>La rentrée</em> - Back-to-school (September)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je suis à l'université.</em> -> I am in college/university.</li>
    <li><em>Elle a réussi son examen.</em> -> She passed her exam.</li>
    <li><em>Je dois rédiger une dissertation.</em> -> I have to write an essay.</li>
    <li><em>Le professeur donne beaucoup de devoirs.</em> -> The teacher assigns a lot of homework.</li>
    <li><em>Quelles matières étudies-tu ?</em> -> What subjects are you studying?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 13:": """
<h4>13.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When telling a story in writing, the Passé Simple is used instead of the Passé Composé in formal literature. However, in spoken French and everyday B1 writing, always stick to the Passé Composé + Imparfait dynamic.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> When describing an interruption in a story, the background is Imparfait, the interrupter is Passé Composé. "Je dormais (imp) quand le téléphone a sonné (pc)."</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Tout à coup</em> - All of a sudden</li>
    <li><em>Finalement</em> - Finally / In the end</li>
    <li><em>Heureusement</em> - Fortunately</li>
    <li><em>C'est ainsi que</em> - That is how</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il était une fois...</em> -> Once upon a time...</li>
    <li><em>Soudain, il y a eu un bruit.</em> -> Suddenly, there was a noise.</li>
    <li><em>Au début, tout allait bien.</em> -> At first, everything was fine.</li>
    <li><em>Pendant ce temps, j'attendais.</em> -> Meanwhile, I was waiting.</li>
    <li><em>À la fin du conte, ils se marient.</em> -> At the end of the tale, they get married.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 14:": """
<h4>14.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Almost all expressions of fear, joy, sorrow, and surprise trigger the subjunctive. Example: <em>Je suis triste que tu partes</em> (I am sad that you are leaving). Note that <em>espérer</em> (to hope) does NOT trigger subjunctive; it takes the indicative/futur.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't confuse <em>excité</em> with "excited" in general joy. In French, <em>excité</em> often carries sexual overtones or means "hyperactive" for children. To say "I'm excited for the trip", use <strong>J'ai hâte de voyager !</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Être déçu(e)</em> - To be disappointed</li>
    <li><em>Ressentir</em> - To feel (an emotion)</li>
    <li><em>La colère</em> - Anger</li>
    <li><em>Avoir peur</em> - To be afraid</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je suis tellement heureux pour toi.</em> -> I am so happy for you.</li>
    <li><em>Ça me rend fou.</em> -> That makes me crazy.</li>
    <li><em>Il a honte de son comportement.</em> -> He is ashamed of his behavior.</li>
    <li><em>J'ai hâte de te voir.</em> -> I can't wait to see you.</li>
    <li><em>Elle est tombée en larmes.</em> -> She burst into tears.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 15:": """
<h4>15.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Verbs of reciprocity use reflexive pronouns (se) and often require <em>être</em> in the passé composé. However, if the reflexive pronoun acts as an indirect object, the past participle does not agree. Example: <em>Elles se sont parlé</em> (They spoke to each other).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use <em>rencontrer</em> for hanging out with friends you already know. <em>Rencontrer</em> usually means meeting someone for the first time by chance. To meet up with friends, use <strong>voir</strong> or <strong>retrouver</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une dispute</em> - An argument</li>
    <li><em>Faire confiance (à quelqu'un)</em> - To trust (someone)</li>
    <li><em>Tomber amoureux (de)</em> - To fall in love (with)</li>
    <li><em>Le soutien</em> - Support</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>On s'entend très bien.</em> -> We get along very well.</li>
    <li><em>Ils se sont fâchés.</em> -> They got angry at each other.</li>
    <li><em>C'est mon meilleur ami.</em> -> He is my best friend.</li>
    <li><em>Puis-je te faire confiance ?</em> -> Can I trust you?</li>
    <li><em>Elles ont rompu hier.</em> -> They broke up yesterday.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 16:": """
<h4>16.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When complaining formally (e.g., in a letter or at a service desk), tone is everything in French. The conditional is heavily utilized to soften demands: <strong>J'aimerais signaler un problème</strong> is better than "J'ai un problème".</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> <em>S'excuser</em> means "to apologize". If you say "Je m'excuse", technically you are excusing yourself. The polite way to tell someone you are sorry is: <strong>Je vous présente mes excuses</strong> or simply <strong>Désolé(e)</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Se plaindre</em> - To complain</li>
    <li><em>Rembourser</em> - To refund</li>
    <li><em>Un malentendu</em> - A misunderstanding</li>
    <li><em>Être mécontent(e)</em> - To be dissatisfied</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Ce n'est pas ce que j'ai commandé.</em> -> This is not what I ordered.</li>
    <li><em>Puis-je parler au gérant ?</em> -> May I speak to the manager?</li>
    <li><em>Je suis vraiment désolé du dérangement.</em> -> I am truly sorry for the inconvenience.</li>
    <li><em>Ce produit est défectueux.</em> -> This product is defective.</li>
    <li><em>Je voudrais un remboursement.</em> -> I would like a refund.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 17:": """
<h4>17.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The history of Quebec is tied closely to the date 1759 (Battle of the Plains of Abraham). Knowing this context is vital for B1/B2 reading comprehension regarding Québécois identity and the motto <em>Je me souviens</em>.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> A Francophone is anyone who speaks French. A <strong>Québécois(e)</strong> specifically refers to a resident of the province of Quebec. Do not call someone from Montreal "French" (Français) unless they are actually from France.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>La Nouvelle-France</em> - New France (Historical)</li>
    <li><em>Les ancêtres</em> - Ancestors</li>
    <li><em>Un colon</em> - A settler / colonist</li>
    <li><em>L'assimilation</em> - Assimilation</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>La devise du Québec est "Je me souviens".</em> -> The motto of Quebec is "I remember."</li>
    <li><em>Montréal a été fondée en 1642.</em> -> Montreal was founded in 1642.</li>
    <li><em>L'histoire est fascinante.</em> -> History is fascinating.</li>
    <li><em>De quelle origine êtes-vous ?</em> -> What is your origin?</li>
    <li><em>Il est fier de ses racines.</em> -> He is proud of his roots.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 18:": """
<h4>18.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When talking about playing instruments, use <strong>jouer de</strong> (Jouer du piano, de la guitare). When talking about playing sports/games, use <strong>jouer à</strong> (Jouer au soccer, aux cartes).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't say "un spectacle de théâtre". The correct term is <strong>une pièce de théâtre</strong> (a play).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une exposition</em> - An exhibition</li>
    <li><em>Un chef-d'œuvre</em> - A masterpiece</li>
    <li><em>Le public</em> - The audience</li>
    <li><em>Répéter</em> - To rehearse</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>J'adore la musique classique.</em> -> I love classical music.</li>
    <li><em>J'ai acheté des billets pour le concert.</em> -> I bought tickets for the concert.</li>
    <li><em>Ce peintre est très célèbre.</em> -> This painter is very famous.</li>
    <li><em>Le film était époustouflant.</em> -> The movie was breathtaking.</li>
    <li><em>Aimez-vous les musées d'art contemporain ?</em> -> Do you like modern art museums?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 19:": """
<h4>19.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Quebec has a civil law system separate from the rest of Canada, based historically on the French Napoleonic code. Words like <em>un notaire</em> hold different, more powerful legal weight here than a "notary" in the US.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> In Canadian politics, the leader of the province is called <strong>le Premier ministre</strong> (same term as the federal Prime Minister). Do not translate "Governor" to <em>Gouverneur</em> for a provincial leader.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une loi</em> - A law</li>
    <li><em>Un parti politique</em> - A political party</li>
    <li><em>Les élections</em> - Elections</li>
    <li><em>Laïcité</em> - Secularism</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Allons voter demain.</em> -> Let's go vote tomorrow.</li>
    <li><em>Le débat télévisé était intéressant.</em> -> The televised debate was interesting.</li>
    <li><em>Le gouvernement a passé une nouvelle loi.</em> -> The government passed a new law.</li>
    <li><em>Quels sont les enjeux sociaux actuels ?</em> -> What are the current social issues?</li>
    <li><em>C'est une société démocratique.</em> -> It's a democratic society.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 20:": """
<h4>20.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Transitioning from B1 to B2 requires mastering logical connectors (<em>cependant</em>, <em>néanmoins</em>, <em>en revanche</em>). Native fluency isn't about speaking fast, but linking ideas smoothly.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Stopping at translation. At B2, you must think in French. Stop translating "It makes sense" literally. Start using <strong>C'est logique</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Maîtriser</em> - To master</li>
    <li><em>L'aisance</em> - Fluency / Ease</li>
    <li><em>Surmonter (une difficulté)</em> - To overcome</li>
    <li><em>Un palier</em> - A plateau / A step up</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je me prépare pour le niveau B2.</em> -> I am preparing for the B2 level.</li>
    <li><em>Je veux parler couramment.</em> -> I want to speak fluently.</li>
    <li><em>Mes efforts portent fruit.</em> -> My efforts are paying off.</li>
    <li><em>Il me reste beaucoup de vocabulaire à apprendre.</em> -> I still have a lot of vocabulary to learn.</li>
    <li><em>Je suis fier de mes progrès.</em> -> I am proud of my progress.</li>
  </ul>
</li>
</ul>
"""
}

# Apply the same regex replacement logic as expand_a2.py
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

with open("b1_expanded.html", "w", encoding="utf-8") as f:
    f.write(modified_content)

print(f"B1 Expand script completed.")
