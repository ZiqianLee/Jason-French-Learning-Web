import os
import re

file_path = "b2.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Define the additions for each of the 20 B2 units.
additions = {
    "UNIT 1:": """
<h4>1.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The <em>subjonctif passé</em> is essential in B2 for expressing past emotions/doubts about a completed event: "Je suis ravi qu'il <strong>soit venu</strong>." It uses the present subjunctive of the auxiliary + past participle.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use the subjunctive after <em>après que</em> (after). It takes the indicative! Use it only after <em>avant que</em> (before).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Il est douteux que</em> - It is doubtful that</li>
    <li><em>Nier que</em> - To deny that</li>
    <li><em>Craindre que</em> - To fear that</li>
    <li><em>Bien que</em> - Even though</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je suis surpris qu'il ait dit ça.</em> -> I am surprised he said that.</li>
    <li><em>Il faut que nous soyons partis avant midi.</em> -> We must have left before noon.</li>
    <li><em>Je regrette qu'elle n'ait pas pu venir.</em> -> I regret that she couldn't come.</li>
    <li><em>Je doute qu'ils aient fini.</em> -> I doubt they have finished.</li>
    <li><em>C'est dommage que tu aies raté ça.</em> -> It's a shame you missed that.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 2:": """
<h4>2.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The <em>conditionnel passé</em> expresses regrets or missed opportunities ("I would have..."). It requires the conditional of the auxiliary (<em>aurais/serais</em>) + past participle. Note the agreement with <em>être</em> verbs.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> In English we say "He should have gone." In French, this is the conditional past of <em>devoir</em>: <strong>Il aurait dû aller</strong>, not "Il devrait avoir allé."</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un regret</em> - A regret</li>
    <li><em>Un reproche</em> - A reproach / criticism</li>
    <li><em>Il aurait mieux valu</em> - It would have been better to</li>
    <li><em>Rater une occasion</em> - To miss an opportunity</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>J'aurais aimé te voir.</em> -> I would have liked to see you.</li>
    <li><em>Tu aurais pu me le dire !</em> -> You could have told me!</li>
    <li><em>Nous y serions allés si...</em> -> We would have gone there if...</li>
    <li><em>Il n'aurait pas dû faire ça.</em> -> He shouldn't have done that.</li>
    <li><em>Qu'aurais-tu fait à ma place ?</em> -> What would you have done in my place?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 3:": """
<h4>3.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The passive voice is formed with <em>être</em> + past participle. But French prefers the active voice or <strong>"on"</strong>. Instead of saying "La maison a été vendue," it sounds more natural to say <strong>On a vendu la maison</strong> in casual speech.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't forget that in the passive voice, the past participle ALWAYS agrees with the subject. "La lettre a été écrit<strong>e</strong> par Marie."</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Subir</em> - To subject / undergo</li>
    <li><em>Être censé</em> - To be supposed to</li>
    <li><em>Être accusé de</em> - To be accused of</li>
    <li><em>Par le biais de</em> - By means of</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Le voleur a été arrêté.</em> -> The thief was arrested.</li>
    <li><em>Cette chanson est chantée par Céline Dion.</em> -> This song is sung by Céline Dion.</li>
    <li><em>Le projet sera complété demain.</em> -> The project will be completed tomorrow.</li>
    <li><em>On m'a offert un emploi.</em> -> I was offered a job (They offered me a job).</li>
    <li><em>La décision a été prise.</em> -> The decision has been made.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 4:": """
<h4>4.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> The <em>gérondif</em> (en + -ant) implies two actions happening simultaneously by the SAME subject. "Je mange <strong>en regardant</strong> la télé." If subjects differ, you must use a relative clause.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use the present participle as an adjective without checking agreement. As a verb (gérondif) it never agrees. As an adjective ("une personne charmante"), it does agree.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Tout en</em> - While (emphasizes simultaneity or contrast)</li>
    <li><em>Provoquant</em> - Provoking / Shocking</li>
    <li><em>Fascinant(e)</em> - Fascinating</li>
    <li><em>Épuisant(e)</em> - Exhausting</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il est parti en pleurant.</em> -> He left crying.</li>
    <li><em>J'ai appris le français en écoutant des podcasts.</em> -> I learned French by listening to podcasts.</li>
    <li><em>C'est un travail fatigant.</em> -> It's a tiring job.</li>
    <li><em>Tout en souriant, elle a refusé.</em> -> While smiling, she refused.</li>
    <li><em>En cherchant mes clés, j'ai trouvé 10 dollars.</em> -> While looking for my keys, I found $10.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 5:": """
<h4>5.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In B2, you must structure arguments fluidly using connectors. Words like <em>d'une part / d'autre part</em> (on the one hand / on the other hand) organize multi-point debates perfectly.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't translate "I disagree" as "Je suis désagréable". It's <strong>Je ne suis pas d'accord</strong>. "Désagréable" means unpleasant/rude.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un atout</em> - An asset / advantage</li>
    <li><em>Un inconvénient</em> - A disadvantage</li>
    <li><em>Souligner</em> - To emphasize / point out</li>
    <li><em>Être convaincu(e)</em> - To be convinced</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je tiens à souligner que...</em> -> I want to point out that...</li>
    <li><em>L'avantage principal est...</em> -> The main advantage is...</li>
    <li><em>Il faut peser le pour et le contre.</em> -> We must weigh the pros and cons.</li>
    <li><em>C'est un argument de poids.</em> -> It's a strong argument.</li>
    <li><em>Je suis tout à fait contre cette idée.</em> -> I am completely against this idea.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 6:": """
<h4>6.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> When persuading, subtlety is key. Instead of <em>Il faut</em> (You must), use <em>Il vaudrait mieux</em> (It would be better to) or <em>Je vous suggère fortement de</em> (I strongly suggest you...).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Do not overuse "très". In B2, escalate your vocabulary: <em>très bon -> excellent</em>; <em>très mauvais -> pire / médiocre</em>; <em>très grand -> immense</em>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une preuve</em> - A piece of evidence</li>
    <li><em>Démontrer</em> - To demonstrate</li>
    <li><em>Incontournable</em> - Unavoidable / Essential</li>
    <li><em>Pertinent(e)</em> - Relevant</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Laissez-moi vous convaincre.</em> -> Let me convince you.</li>
    <li><em>Les données prouvent que...</em> -> The data proves that...</li>
    <li><em>C'est une opportunité incontournable.</em> -> This is a must-seize opportunity.</li>
    <li><em>Je comprends votre point de vue, mais...</em> -> I understand your point of view, but...</li>
    <li><em>Cela ne fait aucun doute.</em> -> There is no doubt about it.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 7:": """
<h4>7.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Concession structures are vital. <em>Bien que</em> takes the subjunctive (Bien qu'il <strong>soit</strong> riche), while <em>Même si</em> takes the indicative (Même s'il <strong>est</strong> riche).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Do not translate "despite" as "en dépit de que". It is simply <strong>Malgré + noun</strong> (Malgré la pluie).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Toutefois</em> - However</li>
    <li><em>Néanmoins</em> - Nevertheless</li>
    <li><em>En revanche</em> - On the other hand (contrasting positive/negative)</li>
    <li><em>Par contre</em> - However (informal contrast)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Malgré ses efforts, il a échoué.</em> -> Despite his efforts, he failed.</li>
    <li><em>Bien qu'elle soit jeune, elle est très mature.</em> -> Although she is young, she is very mature.</li>
    <li><em>C'est cher; néanmoins, c'est de bonne qualité.</em> -> It's expensive; nevertheless, it's good quality.</li>
    <li><em>Il est intelligent, en revanche il est paresseux.</em> -> He is smart, but on the other hand, he is lazy.</li>
    <li><em>Cependant, il reste des problèmes.</em> -> However, problems remain.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 8:": """
<h4>8.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> B2 formal register requires proper polite formulas in correspondence. Do not end a formal letter with "Cordialement" if addressing a high official. Use: <strong>Veuillez agréer, Monsieur, mes salutations distinguées.</strong></li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Using "tu" when you should use "vous". In professional Quebec, "vous" is expected in the first contact, though they shift to "tu" much faster than in France.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un entretien</em> - An interview / discussion</li>
    <li><em>Ci-joint</em> - Attached (in an email/letter)</li>
    <li><em>Dans l'attente de votre réponse</em> - Looking forward to your reply</li>
    <li><em>Une requête</em> - A request</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je vous prie de bien vouloir...</em> -> Please find it in you to... (Very formal "Please")</li>
    <li><em>Suite à notre conversation téléphonique...</em> -> Following our phone conversation...</li>
    <li><em>Veuillez trouver ci-joint le document.</em> -> Please find attached the document.</li>
    <li><em>Je me tiens à votre disposition.</em> -> I remain at your disposal.</li>
    <li><em>Je vous remercie d'avance.</em> -> I thank you in advance.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 9:": """
<h4>9.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In Quebec, corporate titles often differ from France. A CEO is <strong>un PDG</strong> (Président-directeur général). A manager is <strong>un(e) gestionnaire</strong> or <strong>un(e) cadre</strong>.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> "A business" is not "un business". It's <strong>une entreprise</strong>, <strong>une compagnie</strong> (common in QC), or <strong>une société</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un chiffre d'affaires</em> - Revenue / Turnover</li>
    <li><em>Un syndicat</em> - A union</li>
    <li><em>Le siège social</em> - Headquarters</li>
    <li><em>Embaucher</em> - To hire</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Nous avons signé le contrat.</em> -> We signed the contract.</li>
    <li><em>La réunion est reportée.</em> -> The meeting is postponed.</li>
    <li><em>Je travaille dans le secteur informatique.</em> -> I work in the IT sector.</li>
    <li><em>Quel est l'ordre du jour ?</em> -> What is the agenda?</li>
    <li><em>L'entreprise est rentable.</em> -> The company is profitable.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 10:": """
<h4>10.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Formal essays (dissertations) follow a strict structure in French exams: Introduction, Développement (Thèse, Antithèse), and Conclusion. You cannot deviate from this logic freely.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't use bullet points in a formal B2 DELF essay unless expressly asked. It must be written in fluid, linked paragraphs.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une problématique</em> - A central question / issue</li>
    <li><em>Dans un premier temps</em> - Initially / Firstly</li>
    <li><em>En guise de conclusion</em> - By way of conclusion</li>
    <li><em>Mettre en évidence</em> - To highlight</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Cet article traite de l'intelligence artificielle.</em> -> This article is about artificial intelligence.</li>
    <li><em>Il soulève une question importante.</em> -> It raises an important question.</li>
    <li><em>D'abord, examinons les causes.</em> -> First, let's examine the causes.</li>
    <li><em>Ensuite, analysons les conséquences.</em> -> Next, let's analyze the consequences.</li>
    <li><em>Pour conclure, il est impératif d'agir.</em> -> To conclude, it is imperative to act.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 11:": """
<h4>11.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> In presentations, linking devices are the core metric of fluency. Use <em>De plus</em> (Furthermore), <em>En outre</em> (Moreover), and <em>Sans parler de</em> (Not to mention).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't read your notes verbatim. Native speakers use filler words perfectly to buy time: <strong>Euh...</strong>, <strong>C'est-à-dire...</strong>, <strong>En fait...</strong>. Don't use the English "um".</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un graphique</em> - A chart / graph</li>
    <li><em>Une diapositive</em> - A slide (PowerPoint)</li>
    <li><em>Aborder (un sujet)</em> - To tackle / approach (a topic)</li>
    <li><em>L'auditoire</em> - The audience</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Bienvenue à cette présentation.</em> -> Welcome to this presentation.</li>
    <li><em>Le but de cette réunion est de...</em> -> The goal of this meeting is to...</li>
    <li><em>Comme vous pouvez le voir sur ce graphique...</em> -> As you can see on this chart...</li>
    <li><em>Passons à la diapositive suivante.</em> -> Let's move to the next slide.</li>
    <li><em>Merci de votre attention.</em> -> Thank you for your attention.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 12:": """
<h4>12.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Negotiation requires a firm but polite conditional tense. "I need a discount" becomes <strong>Nous souhaiterions obtenir une réduction.</strong></li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> A "compromise" is <strong>un compromis</strong>, but to say "we made a compromise", use <strong>Nous avons trouvé un compromis</strong> (not "fait un compromis").</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Les modalités</em> - Terms and conditions</li>
    <li><em>Un accord gagnant-gagnant</em> - A win-win agreement</li>
    <li><em>Rejeter</em> - To reject</li>
    <li><em>Faire une concession</em> - To make a concession</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>C'est notre dernière offre.</em> -> This is our final offer.</li>
    <li><em>Pouvons-nous en discuter ?</em> -> Can we discuss it?</li>
    <li><em>Nous ne pouvons pas accepter ces conditions.</em> -> We cannot accept these terms.</li>
    <li><em>Trouvons un terrain d'entente.</em> -> Let's find common ground.</li>
    <li><em>Le marché est conclu.</em> -> It's a deal.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 13:": """
<h4>13.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Quebec literature often uses <em>Joual</em> (Montreal working-class dialect) in dialogue, but standard international French in narration. E.g., Michel Tremblay's works.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> A "novel" is not "une nouvelle" (which means a short story or a piece of news). A novel is <strong>un roman</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Le personnage principal</em> - The main character</li>
    <li><em>L'intrigue</em> - The plot</li>
    <li><em>Une maison d'édition</em> - A publishing house</li>
    <li><em>Un poème</em> - A poem</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Ce roman est un chef-d'œuvre.</em> -> This novel is a masterpiece.</li>
    <li><em>L'histoire se déroule à Québec.</em> -> The story takes place in Quebec.</li>
    <li><em>L'auteur a remporté un prix.</em> -> The author won an award.</li>
    <li><em>C'est un classique de la littérature.</em> -> It's a literary classic.</li>
    <li><em>J'ai lu ce livre d'une traite.</em> -> I read this book in one sitting.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 14:": """
<h4>14.6 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Quebec cinema has exploded globally (Xavier Dolan, Denis Villeneuve). Understand that films from Quebec aren't usually dubbed in France, they are SUBTITLED in France due to the strong accent differences.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> "A director" (of a film) is not "un directeur". It is <strong>un réalisateur</strong> (or <em>une réalisatrice</em>).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un long-métrage</em> - A feature film</li>
    <li><em>Le scénario</em> - The script</li>
    <li><em>Une bande-annonce</em> - A trailer</li>
    <li><em>Les sous-titres</em> - Subtitles</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Le dernier film de Villeneuve est incroyable.</em> -> Villeneuve's latest film is incredible.</li>
    <li><em>Les effets spéciaux sont très réussis.</em> -> The special effects are very well done.</li>
    <li><em>Ce film a gagné un Oscar.</em> -> This movie won an Oscar.</li>
    <li><em>C'est un film muet.</em> -> It's a silent film.</li>
    <li><em>As-tu vu la bande-annonce ?</em> -> Did you see the trailer?</li>
  </ul>
</li>
</ul>
""",
    "UNIT 15:": """
<h4>15.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Idioms cannot be translated literally. "It's raining cats and dogs" is <strong>Il pleut des cordes</strong> (It's raining ropes) or in Quebec: <strong>Il mouille à boire debout</strong> (It's raining hard enough to drink standing up).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Don't force idioms into formal B2 essays. They belong in the speaking exam (oral comprehension) or informal letters.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Avoir du pain sur la planche</em> - To have a lot on one's plate</li>
    <li><em>Tomber dans les pommes</em> - To faint</li>
    <li><em>Jeter un œil</em> - To take a look / cast an eye</li>
    <li><em>Ça coûte un bras</em> - It costs an arm and a leg</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je suis fatigué, je jette l'éponge.</em> -> I'm tired, I throw in the towel.</li>
    <li><em>Il a un poil dans la main.</em> -> He is very lazy.</li>
    <li><em>Elle m'a posé un lapin.</em> -> She stood me up.</li>
    <li><em>C'est la goutte d'eau qui fait déborder le vase.</em> -> It's the straw that broke the camel's back.</li>
    <li><em>Revenons à nos moutons.</em> -> Let's get back on topic.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 16:": """
<h4>16.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Quebec humor relies heavily on self-deprecation and linguistic interplay between English and French. Comedian Louis-José Houde is famous for ultra-fast, culturally precise wordplay.</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> French sarcasm (le second degré) is dry and deadpan. If a French person says "C'est malin" (That's smart) when you drop a glass, it means "That's stupid."</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Une blague / Une farce</em> - A joke</li>
    <li><em>L'humour noir</em> - Black comedy / Dark humor</li>
    <li><em>Faire un jeu de mots</em> - To make a pun</li>
    <li><em>Rire aux éclats</em> - To burst out laughing</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Il a beaucoup d'humour.</em> -> He has a great sense of humor.</li>
    <li><em>C'était très drôle.</em> -> It was very funny.</li>
    <li><em>C'est juste pour rire !</em> -> It's just for laughs! (Also a famous QC festival)</li>
    <li><em>Elle n'a pas compris le sarcasme.</em> -> She didn't get the sarcasm.</li>
    <li><em>Arrête de faire le clown.</em> -> Stop acting the fool.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 17:": """
<h4>17.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> French has registers: <em>Soutenu</em> (formal/literary), <em>Courant</em> (standard daily), <em>Familier</em> (slang/friends). E.g., A car: Un véhicule (S), Une voiture (C), Un char (F - Quebec) / Une bagnole (F - France).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Never mix registers in the same sentence. Don't say "Veuillez agréer mes salutations, mon pote." (Please accept my regards, buddy).</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Le verlan</em> - French slang reversing syllables (France)</li>
    <li><em>Les sacres</em> - Quebec swear words derived from Catholicism</li>
    <li><em>Un mec / Un gars</em> - A guy</li>
    <li><em>Une meuf / Une blonde</em> - A woman / A girlfriend (France vs QC)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>On se casse. (Familier)</em> -> Let's get out of here.</li>
    <li><em>Je suis épuisé(e). (Courant)</em> -> I am exhausted.</li>
    <li><em>Je vous en prie. (Soutenu)</em> -> You are welcome / Please go ahead.</li>
    <li><em>C'est plate. (QC Familier)</em> -> It's boring.</li>
    <li><em>C'est ouf ! (FR Familier - Verlan for fou)</em> -> It's crazy!</li>
  </ul>
</li>
</ul>
""",
    "UNIT 18:": """
<h4>18.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> To sound native, drop the "ne" in negative spoken sentences: "Je <em>ne</em> sais pas" -> "<strong>Ché pas</strong>" (Spoken contraction). "Il <em>ne</em> pleut pas" -> "<strong>Y pleut pas</strong>".</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> When looking for words in a spontaneous conversation, use French fillers. <strong>"Euh..."</strong>, <strong>"Bah..."</strong>, <strong>"C'est-à-dire..."</strong>, <strong>"Enfin..."</strong>. Do not use English versions!</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Du coup</em> - So / Therefore (Very common filler in France)</li>
    <li><em>Faque</em> - So (from "Ça fait que" - Very common filler in Quebec)</li>
    <li><em>Bref</em> - Anyway / Long story short</li>
    <li><em>Tsé</em> - Y'know (from "Tu sais" - Quebec filler)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Bref, on est rentrés tôt.</em> -> Long story short, we went home early.</li>
    <li><em>Du coup, t'as dit quoi ?</em> -> So, what did you say?</li>
    <li><em>Faque là, je sais plus quoi faire.</em> -> So now, I don't know what to do anymore.</li>
    <li><em>Franchement, c'était génial.</em> -> Honestly, it was awesome.</li>
    <li><em>Avoue que c'est vrai !</em> -> Admit that it's true!</li>
  </ul>
</li>
</ul>
""",
    "UNIT 19:": """
<h4>19.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> Meals differ entirely. In France: Petit-déjeuner (morning), Déjeuner (noon), Dîner (night). In Quebec: <strong>Déjeuner</strong> (morning), <strong>Dîner</strong> (noon), <strong>Souper</strong> (night).</li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Using <em>Glymmer</em> anglicisms in France vs Quebec. In France, they say "le weekend", "le parking". Quebec aggressively defends French and uses <strong>la fin de semaine</strong>, <strong>le stationnement</strong>.</li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Un chandail</em> - A sweater (QC) vs <em>Un pull</em> (FR)</li>
    <li><em>Des espadrilles</em> - Sneakers (QC) vs <em>Des baskets</em> (FR)</li>
    <li><em>Un cellulaire</em> - Cellphone (QC) vs <em>Un portable</em> (FR)</li>
    <li><em>Un breuvage</em> - A beverage/drink (QC) vs <em>Une boisson</em> (FR)</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>On va magasiner en fin de semaine ? (QC)</em> -> Are we going shopping this weekend?</li>
    <li><em>Non, je dois nettoyer mon char. (QC)</em> -> No, I have to clean my car.</li>
    <li><em>J'ai oublié mon cellulaire dans le taxi. (QC)</em> -> I forgot my cell phone in the taxi.</li>
    <li><em>Voulez-vous un breuvage ? (QC)</em> -> Would you like a beverage?</li>
    <li><em>L'addition, s'il vous plaît. (FR) / La facture, s'il vous plaît. (QC)</em> -> The check, please.</li>
  </ul>
</li>
</ul>
""",
    "UNIT 20:": """
<h4>20.5 Extra Learning Materials 📚</h4>
<ul>
<li>🚨 <strong>Exceptions & Edge Cases:</strong> B2 tests independent fluency. You are expected to defend your opinion against an examiner who will deliberately challenge you. Use structures like <strong>"Je concède que... mais il n'en reste pas moins que..."</strong></li>
<li>❌ <strong>Common Mistakes to Avoid:</strong> Silence is the enemy in spoken B2. If you don't understand the examiner, ask them to rephrase professionally: <strong>Pourriez-vous reformuler votre question, s'il vous plaît ?</strong></li>
<li>📖 <strong>Extended Vocabulary Expansion:</strong> 
  <ul>
    <li><em>Le bilinguisme</em> - Bilingualism</li>
    <li><em>L'immersion</em> - Immersion</li>
    <li><em>Un locuteur natif</em> - A native speaker</li>
    <li><em>La francophonie</em> - The French-speaking world</li>
  </ul>
</li>
<li>🗣️ <strong>Rapid-Fire Practice:</strong> 
  <ul>
    <li><em>Je suis enfin prêt à passer l'examen.</em> -> I am finally ready to take the exam.</li>
    <li><em>C'est l'aboutissement de mois d'efforts.</em> -> This is the culmination of months of effort.</li>
    <li><em>La maîtrise d'une langue ouvre des portes.</em> -> Fluency in a language opens doors.</li>
    <li><em>Je continuerai à pratiquer tous les jours.</em> -> I will continue to practice every day.</li>
    <li><em>Félicitations pour votre réussite !</em> -> Congratulations on your success!</li>
  </ul>
</li>
</ul>
"""
}

# Apply the same regex replacement logic
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

with open("b2_expanded.html", "w", encoding="utf-8") as f:
    f.write(modified_content)

print(f"B2 Expand script completed.")
