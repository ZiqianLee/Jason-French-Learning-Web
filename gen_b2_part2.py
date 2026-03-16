#!/usr/bin/env python3
"""Generate B2 HTML - Part 2: Units 5-8"""
import os
DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(DIR, "b2.html")

content = """
<h1 id="h-b2-part-ii">PART II: PROFESSIONAL &amp; ACADEMIC</h1>

<h2 id="h-b2-u5">UNIT 5: BUSINESS FRENCH</h2>

<h3 id="h-b2-5-1">5.1 Corporate Vocabulary</h3>
<p>To succeed in a francophone workplace, you must master the jargon of business.</p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>le chiffre d'affaires</td><td>turnover / revenue</td></tr>
<tr><td>une succursale / une filiale</td><td>a branch / subsidiary</td></tr>
<tr><td>les ressources humaines (RH)</td><td>human resources (HR)</td></tr>
<tr><td>le conseil d'administration</td><td>board of directors</td></tr>
<tr><td>un ordre du jour</td><td>an agenda (for a meeting)</td></tr>
<tr><td>un procès-verbal</td><td>minutes (of a meeting)</td></tr>
<tr><td>un actionnaire</td><td>a shareholder</td></tr>
<tr><td>la rentabilité</td><td>profitability</td></tr>
<tr><td>un bilan financier</td><td>a financial statement</td></tr>
<tr><td>un siège social</td><td>headquarters</td></tr>
</tbody></table>

<h3 id="h-b2-5-2">5.2 Formal Emails (Les courriels professionnels)</h3>
<p>B2 requires you to write formal, nuanced emails without sounding robotic.</p>
<ul>
<li><strong>Opening:</strong> Bonjour Madame/Monsieur [Nom], Suite à notre conversation téléphonique... (Following our telephone conversation...)</li>
<li><strong>Making a request:</strong> Je vous serais reconnaissant(e) de bien vouloir m'envoyer... (I would be grateful if you would send me...)</li>
<li><strong>Attaching a file:</strong> Veuillez trouver ci-joint le dossier en question. (Please find attached the file in question.)</li>
<li><strong>Following up:</strong> Je me permets de vous relancer concernant... (Allow me to follow up with you regarding...)</li>
<li><strong>Closing:</strong> Cordialement, (Regards,) ou Salutations distinguées, (Sincerely, - formal).</li>
</ul>

<h3 id="h-b2-5-3">5.3 Running a Meeting (Animer une réunion)</h3>
<ul>
<li><strong>Opening:</strong> Merci à tous d'être présents. L'objectif de la réunion d'aujourd'hui est de... (Thank you all for being here. The objective of today's meeting is to...)</li>
<li><strong>Transitioning:</strong> Passons maintenant au deuxième point de l'ordre du jour. (Let's move now to the second item on the agenda.)</li>
<li><strong>Dealing with interruptions:</strong> Si vous permettez, j'aimerais terminer mon explication avant de prendre vos questions. (If you'll allow it, I would like to finish my explanation before taking your questions.)</li>
<li><strong>Concluding:</strong> Pour résumer, nous avons convenu que... (To summarize, we have agreed that...)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing Quarterly Results:</strong></p>
<p><em>Une réunion de gestion dans une grande entreprise.</em></p>
<p>"Bienvenue à tous. Tel qu'indiqué à l'ordre du jour, nous allons examiner les résultats du troisième trimestre. Comme vous pouvez le constater dans le rapport ci-joint, notre chiffre d'affaires a augmenté de 5%."<br>"C'est une excellente nouvelle. Cependant, la rentabilité de notre filiale ontarienne a chuté. Quelles en sont les causes?"<br>"Il semblerait que les coûts d'exploitation aient considérablement augmenté cette année. Le conseil d'administration exige que nous présentions un plan de restructuration d'ici vendredi."<br>"Je vais charger l'équipe des finances de préparer une analyse détaillée. Nous ferons un suivi lors de la prochaine réunion."</p>
<p><em>(A management meeting in a large company. "Welcome everyone. As indicated on the agenda, we are going to examine the third quarter results. As you can observe in the attached report, our revenue has increased by 5%." "This is excellent news. However, the profitability of our Ontario subsidiary has dropped. What are the causes of this?" "It would seem that operating costs have increased considerably this year. The board of directors demands that we present a restructuring plan by Friday." "I am going to task the finance team with preparing a detailed analysis. We will follow up at the next meeting.")</em></p>

<h3 id="h-b2-5-4">5.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, the word <strong>"courriel"</strong> (a blend of courrier + électronique) is universally used instead of the English "e-mail/mail" used in France.</li>
<li>A meeting is universally referred to as <strong>"un meeting"</strong> or <strong>"une rencontre"</strong> in spoken Quebec French, though <strong>"une réunion"</strong> remains standard in writing.</li>
<li><strong>Le PDG</strong> (Président-directeur général) is the equivalent of the CEO.</li>
</ul>
<hr>

<h2 id="h-b2-u6">UNIT 6: LAW &amp; RIGHTS</h2>

<h3 id="h-b2-6-1">6.1 Legal Vocabulary</h3>
<p>Understanding basic legal and administrative terminology is crucial at the B2 level.</p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un avocat / une avocate</td><td>a lawyer</td></tr>
<tr><td>les droits de la personne</td><td>human rights</td></tr>
<tr><td>un procès</td><td>a trial / lawsuit</td></tr>
<tr><td>un tribunal / une cour</td><td>a court</td></tr>
<tr><td>le code civil / criminel</td><td>the civil / criminal code</td></tr>
<tr><td>coupable / innocent(e)</td><td>guilty / innocent</td></tr>
<tr><td>un témoin</td><td>a witness</td></tr>
<tr><td>poursuivre (en justice)</td><td>to sue</td></tr>
<tr><td>un bail (des baux)</td><td>a lease (rent agreement)</td></tr>
<tr><td>le droit du travail</td><td>labor law</td></tr>
</tbody></table>

<h3 id="h-b2-6-2">6.2 Understanding Contracts</h3>
<p>B2 learners should be able to read standard clauses in leases or employment contracts.</p>
<ul>
<li><strong>Conformément à l'alinéa 3...</strong> (In accordance with paragraph 3...)</li>
<li><strong>Sous réserve de modifications...</strong> (Subject to modifications...)</li>
<li><strong>Les parties s'engagent à...</strong> (The parties commit to...)</li>
<li><strong>En cas de litige...</strong> (In the event of a dispute...)</li>
<li><strong>Il est formellement interdit de...</strong> (It is strictly forbidden to...)</li>
</ul>

<h3 id="h-b2-6-3">6.3 Civil Rights &amp; Duties</h3>
<ul>
<li><strong>Tout individu a droit à la liberté d'expression, sous réserve des limites imposées par la loi.</strong> (Every individual has the right to freedom of expression, subject to the limits imposed by law.)</li>
<li><strong>Le suspect a été acquitté faute de preuves suffisantes.</strong> (The suspect was acquitted due to a lack of sufficient evidence.)</li>
<li><strong>En tant que citoyen, vous avez le devoir de respecter le code de la route.</strong> (As a citizen, you have the duty to respect the highway code.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing a Tenancy Dispute:</strong></p>
<p><em>Un locataire consulte un avocat au sujet d'une éviction.</em></p>
<p>"Maître, mon propriétaire m'a envoyé un avis d'éviction la semaine dernière. Il prétend vouloir loger sa fille dans mon appartement."<br>"Je comprends. Au Québec, la reprise de logement est encadrée de façon très stricte par le Tribunal administratif du logement. Avez-vous signé le document?"<br>"Non, j'ai refusé de le signer car je doute de ses intentions. Je crois qu'il veut simplement rénover et augmenter le loyer."<br>"Vous avez bien fait. Selon la loi, vous avez un mois pour refuser. S'il maintient sa décision, c'est à lui de prouver sa bonne foi devant le juge. Dans l'intervalle, continuez de payer votre loyer normalement."</p>
<p><em>(A tenant consults a lawyer regarding an eviction. "Counsel, my landlord sent me an eviction notice last week. He claims he wants to house his daughter in my apartment." "I understand. In Quebec, repossession of a dwelling is very strictly regulated by the Administrative Housing Tribunal. Did you sign the document?" "No, I refused to sign it because I doubt his intentions. I believe he simply wants to renovate and raise the rent." "You did well. According to the law, you have one month to refuse. If he maintains his decision, it is up to him to prove his good faith before the judge. In the meantime, continue paying your rent normally.")</em></p>

<h3 id="h-b2-6-4">6.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>Quebec has a <strong>bijuridical</strong> system: It uses the <strong>Code civil du Québec</strong> (derived from French law) for private/civil matters (contracts, property, family), and the <strong>Common Law</strong> (British) for criminal matters.</li>
<li>Lawyers and notaries are addressed as <strong>"Maître"</strong> (Master) in formal or professional contexts.</li>
<li>The <strong>TAL</strong> (Tribunal administratif du logement, formerly La Régie du logement) is the provincial body that governs relations between landlords (propriétaires) and tenants (locataires).</li>
</ul>
<hr>

<h2 id="h-b2-u7">UNIT 7: SCIENCE &amp; TECH</h2>

<h3 id="h-b2-7-1">7.1 Scientific Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>la recherche et développement (R&amp;D)</td><td>research and development</td></tr>
<tr><td>une expérience / une expérimentation</td><td>an experiment</td></tr>
<tr><td>un chercheur / une chercheuse</td><td>a researcher</td></tr>
<tr><td>l'intelligence artificielle (IA)</td><td>artificial intelligence (AI)</td></tr>
<tr><td>les données (f. pl.)</td><td>data</td></tr>
<tr><td>une percée scientifique</td><td>a scientific breakthrough</td></tr>
<tr><td>le génie (logiciel/mécanique)</td><td>(software/mechanical) engineering</td></tr>
<tr><td>l'espace (m.) / un astronaute</td><td>space / an astronaut</td></tr>
<tr><td>une découverte</td><td>a discovery</td></tr>
</tbody></table>

<h3 id="h-b2-7-2">7.2 Information Technology</h3>
<ul>
<li><strong>Une mise à jour:</strong> Il est recommandé d'installer la dernière mise à jour de sécurité. (It is recommended to install the latest security update.)</li>
<li><strong>Un logiciel:</strong> Ce logiciel open-source permet de traiter des milliers de données à la seconde. (This open-source software allows processing thousands of data points per second.)</li>
<li><strong>Le télétravail / le réseau:</strong> Depuis la pandémie, la sécurité des réseaux informatiques est devenue un enjeu majeur pour les entreprises. (Since the pandemic, the security of IT networks has become a major issue for companies.)</li>
<li><strong>Un algorithme:</strong> L'algorithme de ce réseau social favorise le contenu controversé. (This social network's algorithm favors controversial content.)</li>
</ul>

<h3 id="h-b2-7-3">7.3 Discussing Innovation</h3>
<p>At B2, you should be able to argue the pros and cons of technological advances.</p>
<ul>
<li><strong>Si le développement de l'IA promet des avancées médicales spectaculaires, il soulève également d'importantes questions éthiques quant à la vie privée.</strong> (While the development of AI promises spectacular medical advances, it also raises important ethical questions regarding privacy.)</li>
<li><strong>L'intégration de la robotique dans le secteur manufacturier pourrait entraîner des pertes d'emplois massives.</strong> (The integration of robotics in the manufacturing sector could lead to massive job losses.)</li>
<li><strong>Les chercheurs ont publié une étude démontrant l'efficacité de ce nouveau vaccin.</strong> (Researchers have published a study demonstrating the efficacy of this new vaccine.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing AI in the Workplace:</strong></p>
<p><em>Lors d'un congrès sur les technologies de l'information à Montréal.</em></p>
<p>"Pensez-vous que l'intelligence artificielle générative finira par remplacer les programmeurs?"<br>"Non, je ne le crois pas. L'IA est un outil extrêmement puissant pour automatiser les tâches répétitives, mais elle manque de créativité et de pensée critique. Les ingénieurs logiciels devront simplement s'adapter et apprendre à collaborer avec ces algorithmes."<br>"C'est un point de vue optimiste. Toutefois, plusieurs experts craignent une fracture numérique entre ceux qui maîtrisent cette technologie et ceux qui seront laissés pour compte."<br>"C'est effectivement un risque. C'est pourquoi la formation continue sera la clé dans les prochaines décennies."</p>
<p><em>(During an IT conference in Montreal. "Do you think generative artificial intelligence will eventually replace programmers?" "No, I don't believe so. AI is an extremely powerful tool to automate repetitive tasks, but it lacks creativity and critical thinking. Software engineers will simply have to adapt and learn to collaborate with these algorithms." "That is an optimistic point of view. However, several experts fear a digital divide between those who master this technology and those who will be left behind." "That is indeed a risk. That is why continuing education will be key in the coming decades.")</em></p>

<h3 id="h-b2-7-4">7.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>Montreal is considered one of the leading global hubs for Artificial Intelligence research (e.g., the Mila institute).</li>
<li>Quebec's Office québécois de la langue française (OQLF) often creates French equivalents for English tech terms. For example, <strong>"courriel"</strong> (email), <strong>"clavardage"</strong> (chatting, from clavier + bavardage), and <strong>"balado"</strong> (podcast).</li>
</ul>
<hr>

<h2 id="h-b2-u8">UNIT 8: HIGHER EDUCATION</h2>

<h3 id="h-b2-8-1">8.1 Academic Research Terminology</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>une thèse de doctorat</td><td>a PhD thesis</td></tr>
<tr><td>un mémoire de maîtrise</td><td>a Master's thesis/dissertation</td></tr>
<tr><td>une bourse de recherche</td><td>a research grant</td></tr>
<tr><td>un comité d'évaluation</td><td>an evaluation committee</td></tr>
<tr><td>la méthodologie</td><td>the methodology</td></tr>
<tr><td>une bibliographie / les sources</td><td>a bibliography / the sources</td></tr>
<tr><td>la rentrée universitaire</td><td>the start of the university year</td></tr>
<tr><td>le plagiat</td><td>plagiarism</td></tr>
</tbody></table>

<h3 id="h-b2-8-2">8.2 Writing Essays (Dissertations)</h3>
<p>The French educational system strongly values rhetorical structure. A classic essay format is:</p>
<ol>
<li><strong>Introduction:</strong> Amener le sujet (hook), poser la problématique (the central question), annoncer le plan (outline the structure).</li>
<li><strong>Thèse:</strong> Argument in favor.</li>
<li><strong>Antithèse:</strong> Counter-argument (nuance).</li>
<li><strong>Synthèse:</strong> Resolving the paradox or offering a compromise.</li>
<li><strong>Conclusion:</strong> Résumé (summary) AND ouverture (opening to a broader topic).</li>
</ol>
<p><em>Note: This rigid "thèse-antithèse-synthèse" structure is less mandatory in Quebec than in France, but knowing it is essential for B2/C1 exams.</em></p>

<h3 id="h-b2-8-3">8.3 Defending a Thesis</h3>
<ul>
<li><strong>L'objectif primaire de cette étude était de déterminer les causes de...</strong> (The primary objective of this study was to determine the causes of...)</li>
<li><strong>Les résultats préliminaires contredisent notre hypothèse initiale.</strong> (The preliminary results contradict our initial hypothesis.)</li>
<li><strong>En conclusion, cette recherche ouvre la voie à de nouvelles avenues thérapeutiques.</strong> (In conclusion, this research paves the way for new therapeutic avenues.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A meeting with a Thesis Advisor:</strong></p>
<p><em>Une étudiante à la maîtrise discute de son projet avec son directeur de recherche.</em></p>
<p>"J'ai lu la première ébauche de votre cadre théorique, Camille. C'est intéressant, mais je trouve que la problématique manque un peu de précision."<br>"D'accord. Voulez-vous que je restreigne mon champ d'étude à une période historique plus courte?"<br>"Oui, exactement. Par ailleurs, votre méthodologie est très solide. Avez-vous terminé la collecte de données qualitatives?"<br>"Presque. Il me reste deux entrevues à mener la semaine prochaine. Ensuite, je commencerai l'analyse des résultats."<br>"Parfait. N'oubliez pas de bien citer vos sources; le comité est très strict sur le plagiat. On se revoit dans deux semaines pour faire le point."</p>
<p><em>(A master's student discusses her project with her research director. "I read the first draft of your theoretical framework, Camille. It's interesting, but I find that the research question lacks a bit of precision." "Okay. Do you want me to restrict my field of study to a shorter historical period?" "Yes, exactly. Furthermore, your methodology is very solid. Have you finished collecting qualitative data?" "Almost. I have two interviews left to conduct next week. Then, I will start analyzing the results." "Perfect. Don't forget to cite your sources properly; the committee is very strict about plagiarism. We will meet again in two weeks to take stock.")</em></p>

<h3 id="h-b2-8-4">8.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, degrees are named slightly differently than in France.
<ul>
<li><strong>Le baccalauréat (le bac):</strong> A 3-4 year undergraduate university degree (Bachelor's).</li>
<li><strong>La maîtrise:</strong> A 1-2 year graduate degree (Master's).</li>
<li><strong>Le doctorat (un Ph.D.):</strong> A doctoral degree.</li>
</ul></li>
<li><strong>"Une session"</strong> is the term used for a semester at university (Session d'automne, session d'hiver).</li>
</ul>
"""

with open(OUTPUT, 'a', encoding='utf-8') as f:
    f.write(content)

print(f"B2 Part 2 (Units 5-8) done. File size: {os.path.getsize(OUTPUT)} bytes")
