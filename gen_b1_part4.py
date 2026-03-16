#!/usr/bin/env python3
"""Generate B1 HTML - Part 4: Units 17-20 + Footer/JS"""
import os
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "b1.html")
A1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a1.html")

with open(A1, 'r', encoding='utf-8') as f:
    a1_content = f.read()
js_start = a1_content.index('<script>') + len('<script>')
js_end = a1_content.index('</script>')
js_block = a1_content[js_start:js_end]

content = """
<h1 id="h-b1-part-v">PART V: QUEBEC CULTURE</h1>

<h2 id="h-b1-u17">UNIT 17: QUEBEC HISTORY</h2>

<h3 id="h-b1-17-1">17.1 Key Historical Events</h3>
<p>To understand modern Quebec, you need a basic vocabulary of its history:</p>
<ul>
<li><strong>La Nouvelle-France (1534 - 1763):</strong> The era of French colonization, founded by Jacques Cartier and later Samuel de Champlain.</li>
<li><strong>La Conquête (1759 - 1760):</strong> The British conquest of New France, culminating in the Battle of the Plains of Abraham (la bataille des plaines d'Abraham).</li>
<li><strong>La Révolution tranquille (1960s):</strong> The "Quiet Revolution"—a period of rapid secularization and modernization, leading to the creation of the modern Quebec welfare state.</li>
<li><strong>La Loi 101 (1977):</strong> The Charter of the French Language, making French the official language of Quebec.</li>
</ul>

<h3 id="h-b1-17-2">17.2 Historical Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>le patrimoine</td><td>heritage</td></tr>
<tr><td>les ancêtres</td><td>ancestors</td></tr>
<tr><td>la colonisation</td><td>colonization</td></tr>
<tr><td>un colon / un pionnier</td><td>a settler / pioneer</td></tr>
<tr><td>une bataille</td><td>a battle</td></tr>
<tr><td>l'indépendance (f.)</td><td>independence</td></tr>
<tr><td>la souveraineté</td><td>sovereignty</td></tr>
<tr><td>un référendum</td><td>a referendum</td></tr>
<tr><td>la laïcité</td><td>secularism</td></tr>
<tr><td>un traité</td><td>a treaty</td></tr>
</tbody></table>

<h3 id="h-b1-17-3">17.3 Discussing History</h3>
<ul>
<li><strong>La Révolution tranquille a profondément transformé la société québécoise.</strong> (The Quiet Revolution profoundly transformed Quebec society.)</li>
<li><strong>Avant les années 1960, l'Église catholique contrôlait l'éducation et les hôpitaux.</strong> (Before the 1960s, the Catholic Church controlled education and hospitals.)</li>
<li><strong>Le Québec a tenu deux référendums sur la souveraineté, en 1980 et en 1995.</strong> (Quebec held two referendums on sovereignty, in 1980 and 1995.)</li>
<li><strong>Le Vieux-Québec est un site du patrimoine mondial de l'UNESCO.</strong> (Old Quebec is a UNESCO World Heritage site.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Museum Visit:</strong></p>
<p><em>Vous visitez le Musée de la civilisation à Québec avec un guide.</em></p>
<p>"Bienvenue dans l'exposition sur la Nouvelle-France. Plus de dix mille colons français sont venus s'installer ici avant 1760."<br>"C'est fascinant. Est-ce que la plupart des Québécois francophones descendent de ces premiers colons?"<br>"Oui, en grande partie. C'est pour ça que la généalogie est très populaire au Québec."<br>"Qu'est-ce qui s'est passé avec les Premières Nations pendant cette période?"<br>"Les Français ont formé des alliances avec certaines nations autochtones pour le commerce de la fourrure. C'est une partie complexe et importante de notre histoire."</p>
<p><em>(You are visiting the Museum of Civilization in Quebec City with a guide. "Welcome to the exhibition on New France. More than ten thousand French settlers came to settle here before 1760." "It's fascinating. Do most francophone Quebecers descend from these first settlers?" "Yes, largely. That is why genealogy is very popular in Quebec." "What happened with the First Nations during this period?" "The French formed alliances with certain Indigenous nations for the fur trade. It is a complex and important part of our history.")</em></p>

<h3 id="h-b1-17-4">17.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>"Je me souviens"</strong> (I remember) is the official motto of Quebec, printed on all license plates. It refers to remembering Quebec's history and heritage.</li>
<li><strong>Les Premières Nations</strong> (First Nations), <strong>les Inuits</strong>, and <strong>les Métis</strong> are the recognized Indigenous peoples in Canada. The term "Indien" is considered outdated and offensive.</li>
</ul>
<hr>

<h2 id="h-b1-u18">UNIT 18: ARTS &amp; MUSIC</h2>

<h3 id="h-b1-18-1">18.1 The Quebec Music Scene</h3>
<p>Quebec has a vibrant and distinct music industry, separate from both France and English Canada.</p>
<ul>
<li><strong>La chanson populaire:</strong> Celine Dion is famous worldwide, but artists like Les Cowboys Fringants, Jean Leloup, and Charlotte Cardin are massive in Quebec.</li>
<li><strong>Le rap québ (Quebec rap):</strong> Very popular among youth, blending French, English, and street slang (e.g., Alaclair Ensemble, Loud).</li>
<li><strong>La musique traditionnelle (trad):</strong> Folk music featuring the fiddle, accordion, and foot-tapping (la podorythmie). (e.g., La Bottine Souriante).</li>
</ul>

<h3 id="h-b1-18-2">18.2 Literature &amp; Cinema</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un réalisateur / une réalisatrice</td><td>a film director</td></tr>
<tr><td>un roman (policier/historique)</td><td>a (detective/historical) novel</td></tr>
<tr><td>un écrivain / un auteur</td><td>a writer / author</td></tr>
<tr><td>une pièce de théâtre</td><td>a play</td></tr>
<tr><td>un chef-d'œuvre</td><td>a masterpiece</td></tr>
<tr><td>le scénario</td><td>the script / screenplay</td></tr>
<tr><td>un poème / la poésie</td><td>a poem / poetry</td></tr>
<tr><td>les sous-titres</td><td>subtitles</td></tr>
</tbody></table>

<h3 id="h-b1-18-3">18.3 Expressing Artistic Opinions</h3>
<ul>
<li><strong>J'ai été très touché par ce film de Denis Villeneuve. Le scénario est brillant.</strong> (I was very moved by this film by Denis Villeneuve. The script is brilliant.)</li>
<li><strong>Ce roman de Michel Tremblay dépeint de façon très réaliste le Montréal des années 60.</strong> (This novel by Michel Tremblay depicts 1960s Montreal very realistically.)</li>
<li><strong>La performance des acteurs était médiocre, mais les effets spéciaux étaient impressionnants.</strong> (The actors' performance was mediocre, but the special effects were impressive.)</li>
<li><strong>C'est un incontournable de la culture québécoise.</strong> (It is a must-see/must-read of Quebec culture.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing a Movie:</strong></p>
<p><em>Vous sortez du cinéma après avoir vu un film québécois.</em></p>
<p>"Alors, comment as-tu trouvé le film?"<br>"J'ai adoré! Xavier Dolan a vraiment un style unique. La cinématographie était magnifique."<br>"Moi, j'ai eu de la difficulté avec l'accent au début. Ils parlaient tellement vite."<br>"C'est vrai que le joual était très prononcé. Heureusement, le contexte aidait à comprendre."<br>"Oui, l'histoire était très touchante. D'ailleurs, la bande sonore était excellente aussi."<br>"On pourrait acheter l'album! Et si on allait prendre un verre pour en discuter?"</p>
<p><em>(You leave the cinema after seeing a Quebec film. "So, how did you find the film?" "I loved it! Xavier Dolan really has a unique style. The cinematography was beautiful." "Me, I had difficulty with the accent at first. They spoke so fast." "It's true that the joual was very pronounced. Fortunately, the context helped to understand." "Yes, the story was very touching. Besides, the soundtrack was excellent too." "We could buy the album! What if we went for a drink to discuss it?")</em></p>

<h3 id="h-b1-18-4">18.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>Le joual:</strong> The working-class sociolect of Montreal French, characterized by specific vocabulary, grammar, and pronunciation. It was heavily used in plays by Michel Tremblay (like <em>Les Belles-Sœurs</em>) to represent authentic Quebec voices.</li>
<li><strong>L'ADISQ:</strong> The association that runs the "Gala de l'ADISQ" (the Quebec equivalent of the Grammys or the Victoires de la musique).</li>
</ul>
<hr>

<h2 id="h-b1-u19">UNIT 19: POLITICS &amp; SOCIETY</h2>

<h3 id="h-b1-19-1">19.1 Political Vocabulary</h3>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un parti politique</td><td>a political party</td></tr>
<tr><td>les élections (provinciales/fédérales)</td><td>(provincial/federal) elections</td></tr>
<tr><td>voter pour/contre</td><td>to vote for/against</td></tr>
<tr><td>le Premier ministre</td><td>the Prime Minister / Premier</td></tr>
<tr><td>le gouvernement</td><td>the government</td></tr>
<tr><td>une loi / un projet de loi</td><td>a law / a bill</td></tr>
<tr><td>le maire / la mairesse</td><td>the mayor</td></tr>
<tr><td>une manifestation / faire la grève</td><td>a protest / to go on strike</td></tr>
<tr><td>les impôts / les taxes</td><td>(income) taxes / (sales) taxes</td></tr>
<tr><td>un syndicat</td><td>a labor union</td></tr>
</tbody></table>

<h3 id="h-b1-19-2">19.2 The Quebec Political System</h3>
<p>Quebec has three levels of government:</p>
<ol>
<li><strong>Fédéral (Ottawa):</strong> Deals with currency, military, foreign affairs, and criminal law. Prime Minister: Le Premier ministre du Canada.</li>
<li><strong>Provincial (Québec):</strong> Deals with health, education, natural resources, and civil law. Premier: Le Premier ministre du Québec. (The provincial legislature is called <em>l'Assemblée nationale</em>).</li>
<li><strong>Municipal (Les municipalités):</strong> Deals with local roads, garbage collection, and zoning. Leader: Le maire / la mairesse.</li>
</ol>

<h3 id="h-b1-19-3">19.3 Discussing Social Issues</h3>
<ul>
<li><strong>Le système de santé manque cruellement de personnel infirmier.</strong> (The healthcare system is severely lacking nursing staff.)</li>
<li><strong>Le projet de loi sur le logement suscite beaucoup de débats à l'Assemblée nationale.</strong> (The housing bill is generating a lot of debate at the National Assembly.)</li>
<li><strong>Les syndicats ont déclenché une grève pour obtenir de meilleurs salaires.</strong> (The unions have launched a strike to obtain better salaries.)</li>
<li><strong>Il est crucial d'investir davantage dans l'éducation et les infrastructures.</strong> (It is crucial to invest more in education and infrastructures.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing Housing:</strong></p>
<p><em>Deux collègues discutent de la crise du logement pendant la pause.</em></p>
<p>"Sérieusement, as-tu vu le prix des loyers à Montréal dernièrement? C'est rendu fou!"<br>"Oui, c'est inabordable pour les jeunes familles. Le gouvernement doit intervenir."<br>"À mon avis, les politiciens ne font pas assez pour construire des logements sociaux. Les promoteurs préfèrent construire des condos de luxe."<br>"Je suis d'accord. Lors des prochaines élections municipales, je vais voter pour le parti qui propose un vrai plan pour l'habitation."<br>"Moi aussi. Si ça continue comme ça, on va tous devoir s'éloigner en région."</p>
<p><em>(Two colleagues discuss the housing crisis during the break. "Seriously, have you seen the price of rent in Montreal lately? It's gone crazy!" "Yes, it's unaffordable for young families. The government must intervene." "In my opinion, politicians aren't doing enough to build social housing. Developers prefer to build luxury condos." "I agree. During the next municipal elections, I'm going to vote for the party that proposes a real plan for housing." "Me too. If this continues, we will all have to move far out to the regions.")</em></p>

<h3 id="h-b1-19-4">19.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>C'est rendu fou:</strong> A very common Québécois construction. "Rendu (adjective)" means "has become (adjective)."</li>
<li><strong>Les régions:</strong> Refers to all the areas of Quebec situated outside the major urban centers of Montreal and Quebec City.</li>
<li>In Quebec, the leader of the province is called "Le Premier ministre" (just like the leader of Canada). In English, we use "Premier" for the province and "Prime Minister" for the country to avoid confusion, but French uses the same title for both.</li>
</ul>
<hr>

<h2 id="h-b1-u20">UNIT 20: REVIEW &amp; B2 PREP</h2>

<h3 id="h-b1-20-1">20.1 Grammar Summary</h3>
<p>By the end of B1, you should be able to comfortably use these tenses and modes:</p>
<ul>
<li><strong>Plus-que-parfait (avait fait):</strong> To describe an action before a past action.</li>
<li><strong>Conditionnel présent (ferait):</strong> For hypotheses, advice, and politeness.</li>
<li><strong>Subjonctif présent (fasse):</strong> After expressions of emotion, doubt, and obligation.</li>
<li><strong>Futur antérieur (aura fait):</strong> For an action completed before a future time.</li>
<li><strong>Discours indirect (il a dit qu'il partait):</strong> To report what someone said, shifting tenses appropriately.</li>
</ul>

<h3 id="h-b1-20-2">20.2 Vocabulary Summary</h3>
<p>You can now discuss complex societal topics:</p>
<ul>
<li><strong>Work &amp; Education:</strong> Cover letters, interviews, university programs.</li>
<li><strong>Media &amp; Environment:</strong> News broadcasts, climate change, recycling.</li>
<li><strong>Relationships &amp; Emotions:</strong> Conflict resolution, expressing psychological states.</li>
<li><strong>Culture &amp; Politics:</strong> History, cinema, government structure, social issues.</li>
</ul>

<h3 id="h-b1-20-3">20.3 What to Expect at B2</h3>
<p>At the B2 level (Upper Intermediate), you will move towards fluency and nuance:</p>
<ul>
<li><strong>Argumentation détaillée:</strong> Structuring complex arguments and participating in rapid debates.</li>
<li><strong>Compréhension subtile:</strong> Understanding humour, irony, implicit meanings, and fast-paced colloquial speech.</li>
<li><strong>La voix passive et le subjonctif passé:</strong> More complex grammatical structures.</li>
<li><strong>Vocabulaire spécialisé:</strong> Mastering vocabulary for abstract concepts, science, law, and business.</li>
</ul>

<h3 id="h-b1-20-4">20.4 Study Tips for Advancing to B2</h3>
<ul>
<li><strong>Lisez la presse francophone tous les jours:</strong> Le Devoir, La Presse, Radio-Canada. Focus on op-ed pieces (les articles d'opinion).</li>
<li><strong>Écoutez des balados (podcasts):</strong> "Aujourd'hui l'histoire" or "Les années lumière" to build specialized vocabulary.</li>
<li><strong>Participez à des débats:</strong> Try to explain your views on complex issues to francophone friends without switching to English.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Evaluating Your Progress:</strong></p>
<p><em>Vous discutez de votre français avec un collègue francophone.</em></p>
<p>"Ton français s'est tellement amélioré depuis un an! Tu as presque plus d'accent."<br>"Merci! C'est gentil. J'écoute beaucoup la radio et je lis les journaux tous les matins."<br>"Ça paraît. Tu as une très bonne syntaxe. Tu te sens prêt pour le niveau avancé?"<br>"Oui, mais il me manque encore du vocabulaire pour discuter de sujets complexes, comme l'économie ou la politique internationale."<br>"C'est normal. Au niveau B2, c'est surtout une question d'enrichir ton vocabulaire et de comprendre les subtilités de la langue. Lâche pas la patate!"</p>
<p><em>(You discuss your French with a francophone colleague. "Your French has improved so much over the past year! You have almost no accent." "Thank you! That's kind. I listen to the radio a lot and I read the newspapers every morning." "It shows. You have very good syntax. Do you feel ready for the advanced level?" "Yes, but I still lack vocabulary to discuss complex subjects, like the economy or international politics." "That's normal. At the B2 level, it's mostly a matter of enriching your vocabulary and understanding the subtleties of the language. Don't give up!")</em></p>
<hr>

<h1 id="h-b1-conclusion">CONCLUSION</h1>
<p><strong>Félicitations!</strong> You have completed the B1 level. You are now an independent user of the French language. You can express your opinions, understand the news, discuss Quebec culture, handle complex real-life situations like job interviews and relationship issues, and describe events with nuanced time frames.</p>
<p>Reaching B1 is a massive achievement. You are now fully equipped to live, work, and thrive in a francophone environment. Prenez le temps de célébrer vos efforts! (Take the time to celebrate your efforts!)</p>

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

print(f"B1 COMPLETE. Final file size: {os.path.getsize(OUTPUT)} bytes")
