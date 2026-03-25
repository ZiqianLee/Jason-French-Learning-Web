#!/usr/bin/env python3
"""Expand A1 Units 6-10 with more Quebec French content."""

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
    # UNIT 6: DAYS, MONTHS & TIME
    # =========================================================================

    marker_6_end = '<h2 id="h-unit-7-family-relationships">'
    new_6 = """
<p><strong>Quebec Calendar & Holiday Vocabulary (🍁):</strong></p>
<p>Quebec has many unique holidays and cultural events that are important to know:</p>
<table>
<thead><tr><th>Date</th><th>Holiday (French)</th><th>English</th><th>Note</th></tr></thead>
<tbody>
<tr><td>1er janvier</td><td>Le Jour de l'An</td><td>New Year's Day</td><td>Big family celebrations in Quebec</td></tr>
<tr><td>Février</td><td>Le Carnaval de Québec</td><td>Quebec Winter Carnival</td><td>World's biggest winter carnival with "Bonhomme"</td></tr>
<tr><td>Mars/Avril</td><td>Le temps des sucres</td><td>Maple sugar season</td><td>Cabanes à sucre (sugar shacks) open!</td></tr>
<tr><td>Mars/Avril</td><td>Pâques</td><td>Easter</td><td>"Joyeuses Pâques!" (Happy Easter!)</td></tr>
<tr><td>24 mai</td><td>La Journée nationale des patriotes</td><td>National Patriots' Day</td><td>In rest of Canada: Victoria Day</td></tr>
<tr><td>24 juin</td><td>La Saint-Jean-Baptiste</td><td>Quebec National Holiday</td><td>THE biggest celebration in Quebec!</td></tr>
<tr><td>1er juillet</td><td>La fête du Canada</td><td>Canada Day</td><td>Also "le jour du déménagement" (moving day) in QC!</td></tr>
<tr><td>1er lundi de sept.</td><td>La fête du Travail</td><td>Labour Day</td><td>End of summer, back to school</td></tr>
<tr><td>2e lundi d'oct.</td><td>L'Action de grâce</td><td>Thanksgiving</td><td>Earlier than US Thanksgiving</td></tr>
<tr><td>31 octobre</td><td>L'Halloween</td><td>Halloween</td><td>"Passer l'Halloween" = to go trick-or-treating</td></tr>
<tr><td>25 décembre</td><td>Noël</td><td>Christmas</td><td>"Joyeux Noël!" (Merry Christmas!)</td></tr>
<tr><td>31 décembre</td><td>Le réveillon du Nouvel An</td><td>New Year's Eve</td><td>"Le party du jour de l'An" very important in QC</td></tr>
</tbody>
</table>
<p><strong>Quebec Seasons – Cultural Context (🍁):</strong></p>
<p>Seasons have a special significance in Quebec due to the extreme climate:</p>
<table>
<thead><tr><th>Season</th><th>French</th><th>Quebec Cultural Significance</th></tr></thead>
<tbody>
<tr><td>Winter (Dec-Mar)</td><td>L'hiver</td><td>The defining season of Quebec. Temperatures can reach -30°C. Activities: hockey, ski, motoneige (snowmobiling), patinage (skating), glissade (sledding). Quebecers embrace winter – they don't just survive it!</td></tr>
<tr><td>Spring (Apr-May)</td><td>Le printemps</td><td>Maple sugar season ("le temps des sucres"). Everyone visits cabanes à sucre. The melting snow creates "la slush". "Le ménage du printemps" (spring cleaning) is a big tradition.</td></tr>
<tr><td>Summer (Jun-Aug)</td><td>L'été</td><td>Festival season! Montreal Jazz Festival, Just for Laughs, Francofolies. Quebecers are outdoors constantly – camping, swimming, biking. "Les vacances de la construction" (construction holiday) in late July.</td></tr>
<tr><td>Fall (Sep-Nov)</td><td>L'automne</td><td>The spectacular fall colours ("les couleurs d'automne") draw tourists. Apple picking ("la cueillette de pommes"). Back to school ("la rentrée scolaire"). Thanksgiving ("l'Action de grâce").</td></tr>
</tbody>
</table>
<p><strong>Time-Related Quebec Expressions (🍁):</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Standard French</th><th>English</th></tr></thead>
<tbody>
<tr><td>à matin</td><td>ce matin</td><td>this morning</td></tr>
<tr><td>à soir</td><td>ce soir</td><td>tonight / this evening</td></tr>
<tr><td>à c't'heure (asteure)</td><td>maintenant</td><td>now / right now</td></tr>
<tr><td>tantôt</td><td>tout à l'heure</td><td>a little while ago / in a little while</td></tr>
<tr><td>l'autre jour</td><td>l'autre jour</td><td>the other day</td></tr>
<tr><td>l'autre bord</td><td>de l'autre côté</td><td>on the other side</td></tr>
<tr><td>en fin de semaine</td><td>le week-end</td><td>on the weekend</td></tr>
<tr><td>la semaine passée</td><td>la semaine dernière</td><td>last week</td></tr>
<tr><td>la semaine prochaine</td><td>la semaine prochaine</td><td>next week</td></tr>
<tr><td>de bonne heure</td><td>tôt</td><td>early</td></tr>
</tbody>
</table>
<p><strong>Important:</strong> In Quebec, "fin de semaine" is used instead of "week-end" (which is considered an anglicism). The OQLF (Office québécois de la langue française) recommends "fin de semaine" and "courriel" (instead of "email") as proper French alternatives to English words.</p>
<p><strong>🇫🇷 Real-Life Scene – Planning Summer Vacation in Quebec:</strong></p>
<p><em>Vous planifiez vos vacances d'été au Québec.</em></p>
<p>"Qu'est-ce qu'on fait cet été? On a trois semaines de vacances."<br>"En juillet, on pourrait aller à la plage aux Îles-de-la-Madeleine."<br>"Bonne idée! Pis en août, on pourrait faire du camping en Gaspésie."<br>"Oui! On pourrait aller voir le Rocher Percé et le parc national Forillon."<br>"C'est quand, la semaine de la construction? C'est toujours la dernière semaine de juillet, non?"<br>"Oui, la dernière semaine de juillet et la première d'août. Faut réserver de bonne heure parce que tout le monde est en vacances en même temps!"<br>"Tu l'dis! L'année passée, on n'avait plus trouvé de camping."<br>"Correct, je m'en occupe à soir. On va réserver les campings et le traversier pour les Îles."</p>
<p><em>(You're planning your summer vacation in Quebec. "What do we do this summer? We have three weeks of vacation." "In July, we could go to the beach at the Magdalen Islands." "Good idea! And in August, we could go camping in the Gaspé." "Yes! We could go see Percé Rock and Forillon National Park." "When is the construction holiday? It's always the last week of July, right?" "Yes, the last week of July and the first of August. We have to book early because everyone's on vacation at the same time!" "You said it! Last year, we couldn't find a campsite." "Right, I'll take care of it tonight. We'll book the campsites and the ferry for the Islands.")</em></p>

"""
    html = insert_before(html, marker_6_end, new_6)

    # =========================================================================
    # UNIT 7: FAMILY & RELATIONSHIPS
    # =========================================================================

    marker_7_end = '<h2 id="h-unit-8-nationalities-professions">'
    new_7 = """
<p><strong>Quebec Family Vocabulary – Extended (🍁):</strong></p>
<p>Quebec French has several unique terms for family members and relationship status:</p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th><th>Usage Note</th></tr></thead>
<tbody>
<tr><td>mon chum</td><td>mon petit ami / mon copain</td><td>my boyfriend</td><td>Most common term in QC. Also means "buddy" in some contexts.</td></tr>
<tr><td>ma blonde</td><td>ma petite amie / ma copine</td><td>my girlfriend</td><td>Regardless of hair colour! A blonde is always "une blonde" in QC.</td></tr>
<tr><td>mon/ma conjoint(e)</td><td>mon/ma conjoint(e)</td><td>my partner/spouse</td><td>Used for common-law partners (very common in QC)</td></tr>
<tr><td>mon/ma ex</td><td>mon/ma ex</td><td>my ex</td><td>Same usage as English</td></tr>
<tr><td>les beaux-parents</td><td>les beaux-parents</td><td>in-laws</td><td>"Ma belle-mère" = mother-in-law</td></tr>
<tr><td>matante</td><td>ma tante</td><td>my aunt</td><td>Contracted form, very familiar/affectionate</td></tr>
<tr><td>mononcle</td><td>mon oncle</td><td>my uncle</td><td>Contracted form, can also mean "an older out-of-touch man"</td></tr>
<tr><td>mémère</td><td>grand-mère</td><td>grandma</td><td>Affectionate, can also mean "a gossipy woman" (careful!)</td></tr>
<tr><td>pépère</td><td>grand-père</td><td>grandpa</td><td>Affectionate, can also mean "a boring/lazy man"</td></tr>
<tr><td>les p'tits</td><td>les enfants</td><td>the kids</td><td>"Les p'tits sont à l'école." (The kids are at school.)</td></tr>
<tr><td>un bébé / un poupon</td><td>un bébé</td><td>a baby</td><td>"Poupon" is more QC-specific</td></tr>
<tr><td>la gang</td><td>le groupe d'amis</td><td>group of friends</td><td>"Ma gang" = my group of friends (no negative connotation in QC!)</td></tr>
</tbody>
</table>
<p><strong>Common-Law Relationships in Quebec (Cultural Note):</strong></p>
<p>Quebec has the highest rate of common-law relationships (union libre / conjoints de fait) in North America. Many couples live together and raise families without being married. This is completely socially accepted and normal. When filling out forms, you'll often see:</p>
<ul>
<li><strong>Célibataire</strong> – Single</li>
<li><strong>Marié(e)</strong> – Married</li>
<li><strong>Conjoint(e) de fait</strong> – Common-law partner</li>
<li><strong>Divorcé(e)</strong> – Divorced</li>
<li><strong>Séparé(e)</strong> – Separated</li>
<li><strong>Veuf/Veuve</strong> – Widowed</li>
</ul>
<p><strong>Talking About Family in Quebec – Key Phrases:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>On est une famille de quatre.</td><td>We're a family of four.</td></tr>
<tr><td>Mon chum pis moi, on a deux enfants.</td><td>My boyfriend and I have two children.</td></tr>
<tr><td>Ma mère est née au Lac-Saint-Jean.</td><td>My mother was born in Lac-Saint-Jean.</td></tr>
<tr><td>Ma famille est originaire de la Beauce.</td><td>My family is originally from the Beauce.</td></tr>
<tr><td>On est une grosse famille – j'ai cinq frères et sœurs.</td><td>We're a big family – I have five brothers and sisters.</td></tr>
<tr><td>Mes grands-parents parlent juste français.</td><td>My grandparents only speak French.</td></tr>
<tr><td>Ma belle-sœur est anglophone, mais elle parle bien français.</td><td>My sister-in-law is English-speaking, but she speaks French well.</td></tr>
<tr><td>On se retrouve chez ma mère pour le souper du dimanche.</td><td>We get together at my mom's for Sunday dinner.</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Introducing Your Family at a Quebec BBQ:</strong></p>
<p><em>Vous êtes invité à un barbecue chez votre voisin québécois.</em></p>
<p>"Heille, bienvenue! Venez, je vais vous présenter tout le monde."<br>"Ça, c'est ma blonde, Marie-Pier. Pis nos deux p'tits: Félix pis Rosalie."<br>"Enchantée! Ton plus jeune a quel âge?"<br>"Rosalie a trois ans. Pis Félix, y a six ans. Y commence la maternelle en septembre."<br>"Ah c'est un beau bonhomme! Pis vos parents, y sont-tu icitte aussi?"<br>"Ma mère est dans la cuisine. Mon père est à côté du BBQ avec mononcle Réjean."<br>"Ta famille est grande, hein?"<br>"Mets-en! On est huit enfants dans la famille. C'est une vraie famille québécoise d'autrefois!"<br>"Ben, c'est le fun d'avoir une grosse famille. Chez nous, on est juste deux."<br>"Viens, on va aller se chercher une bière pis je te présente le reste de la gang!"</p>
<p><em>(You're invited to a BBQ at your Quebec neighbour's place. "Hey, welcome! Come, I'll introduce you to everyone." "That's my girlfriend, Marie-Pier. And our two kids: Félix and Rosalie." "Nice to meet you! How old is your youngest?" "Rosalie is three. And Félix is six. He starts kindergarten in September." "What a handsome little guy! And your parents, are they here too?" "My mom is in the kitchen. My dad is next to the BBQ with uncle Réjean." "Your family is big, eh?" "You bet! There are eight children in the family. A real old-fashioned Quebec family!" "Well, it's fun to have a big family. At our place, there are just two of us." "Come, let's go grab a beer and I'll introduce you to the rest of the gang!")</em></p>

"""
    html = insert_before(html, marker_7_end, new_7)

    # =========================================================================
    # UNIT 8: NATIONALITIES & PROFESSIONS
    # =========================================================================

    marker_8_end = '<h1 id="h-part-iii-everyday-grammar">'
    new_8 = """
<p><strong>Quebec-Specific Professions and Work Culture (🍁):</strong></p>
<p>Quebec has unique professional vocabulary and workplace culture:</p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th><th>Note</th></tr></thead>
<tbody>
<tr><td>un(e) commis</td><td>un(e) employé(e)</td><td>a clerk</td><td>Common in retail: "commis de magasin"</td></tr>
<tr><td>un(e) intervenant(e)</td><td>un(e) travailleur social(e)</td><td>social worker / counselor</td><td>Very common in QC health/social services</td></tr>
<tr><td>un(e) préposé(e)</td><td>un(e) aide-soignant(e)</td><td>orderly / attendant</td><td>"Préposé aux bénéficiaires" in healthcare</td></tr>
<tr><td>un dépanneur (owner)</td><td>un épicier de quartier</td><td>convenience store owner</td><td>Also refers to the store itself</td></tr>
<tr><td>un(e) camionneur(euse)</td><td>un(e) routier(ère)</td><td>truck driver</td><td>Important profession in this vast province</td></tr>
<tr><td>un(e) ébéniste</td><td>un(e) ébéniste</td><td>cabinetmaker</td><td>Strong tradition of woodworking in QC</td></tr>
<tr><td>une job / un emploi</td><td>un emploi / un travail</td><td>a job</td><td>"Job" is feminine in QC: "une job"</td></tr>
<tr><td>travailler à temps plein</td><td>travailler à plein temps</td><td>to work full-time</td><td>Slightly different word order in QC</td></tr>
<tr><td>être sur le chômage</td><td>être au chômage</td><td>to be on unemployment</td><td>QC uses "sur" instead of "au"</td></tr>
<tr><td>un horaire de travail</td><td>un emploi du temps</td><td>work schedule</td><td>"Mon horaire" = my schedule</td></tr>
</tbody>
</table>
<p><strong>Quebec Workplace Culture – Important Facts for Newcomers:</strong></p>
<ul>
<li><strong>Language at work:</strong> Quebec's Charter of the French Language (Bill 101) requires that French be the language of the workplace. All businesses with 50+ employees must use French for internal communications.</li>
<li><strong>"Tu" at work:</strong> Quebec workplaces are generally more casual than France's. Many bosses and colleagues use "tu" with each other from day one.</li>
<li><strong>5 à 7:</strong> An after-work social gathering (from 5 PM to 7 PM). Very popular in Quebec workplace culture: "On va au 5 à 7?" (Are we going to the after-work drinks?)</li>
<li><strong>Vacation:</strong> Quebec workers generally get 2-3 weeks of vacation per year. Many people take their main vacation during "la construction" (late July).</li>
<li><strong>"C'est pas ma job"</strong> = "That's not my job" – A common (though frowned-upon) workplace expression.</li>
</ul>
<p><strong>Immigration and Nationality in Quebec Context:</strong></p>
<p>Quebec has its own immigration system separate from the rest of Canada. Here's useful vocabulary:</p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>un immigrant / une immigrante</td><td>an immigrant</td></tr>
<tr><td>un nouvel arrivant / une nouvelle arrivante</td><td>a newcomer</td></tr>
<tr><td>un résident permanent / une résidente permanente</td><td>a permanent resident</td></tr>
<tr><td>un citoyen canadien / une citoyenne canadienne</td><td>a Canadian citizen</td></tr>
<tr><td>un réfugié / une réfugiée</td><td>a refugee</td></tr>
<tr><td>le CSQ (Certificat de sélection du Québec)</td><td>Quebec Selection Certificate</td></tr>
<tr><td>la francisation</td><td>French language training (for immigrants)</td></tr>
<tr><td>le MIDI (Ministère de l'Immigration)</td><td>Ministry of Immigration</td></tr>
<tr><td>les cours de français pour immigrants</td><td>French courses for immigrants</td></tr>
<tr><td>la diversité culturelle</td><td>cultural diversity</td></tr>
</tbody>
</table>
<p><strong>Talking About Where You Come From – Quebec Style:</strong></p>
<ul>
<li>"D'où est-ce que tu viens?" → "Tu viens d'où?" (Where are you from?)</li>
<li>"Moi, je viens du [pays]. J'habite au Québec depuis [temps]." (I come from [country]. I've been living in Quebec for [time].)</li>
<li>"Je suis arrivé(e) au Québec en [année]." (I arrived in Quebec in [year].)</li>
<li>"Je suis Québécois(e) d'adoption." (I'm Quebecois by adoption – said by immigrants who feel at home.)</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – At a Quebec Job Interview:</strong></p>
<p><em>Vous passez une entrevue d'emploi à Montréal.</em></p>
<p>"Bonjour! Assoyez-vous. Parlez-moi un peu de vous."<br>"Je m'appelle Ana. Je suis colombienne, mais j'habite à Montréal depuis deux ans."<br>"Qu'est-ce que vous faisiez dans votre pays?"<br>"J'étais comptable. J'ai travaillé dans une grande entreprise pendant cinq ans."<br>"C'est intéressant. Et ici au Québec, est-ce que vous avez fait reconnaître vos diplômes?"<br>"Oui, j'ai fait mon évaluation comparative des études. Mon diplôme est reconnu."<br>"Parfait. Votre français est très bon! Vous avez suivi des cours de francisation?"<br>"Oui, j'ai fait les cours offerts par le gouvernement. Pis après, j'ai pratiqué avec mes voisins québécois."<br>"Excellent! On travaille en français ici, comme dans la plupart des entreprises au Québec."<br>"Oui, je sais. C'est important pour moi de travailler en français."</p>
<p><em>(You're at a job interview in Montreal. "Hello! Sit down. Tell me a bit about yourself." "My name is Ana. I'm Colombian, but I've been living in Montreal for two years." "What did you do in your country?" "I was an accountant. I worked at a large company for five years." "Interesting. And here in Quebec, have you had your credentials recognized?" "Yes, I did my comparative education assessment. My diploma is recognized." "Perfect. Your French is very good! Did you take francisation courses?" "Yes, I took the courses offered by the government. And then I practiced with my Quebec neighbours." "Excellent! We work in French here, like most companies in Quebec." "Yes, I know. It's important to me to work in French.")</em></p>

"""
    html = insert_before(html, marker_8_end, new_8)

    # =========================================================================
    # UNIT 9: NOUNS & GENDER
    # =========================================================================

    marker_9_end = '<h2 id="h-unit-10-articles-definite-indefinite">'
    new_9 = """
<p><strong>Quebec French Gender Differences – Important Cases (🍁):</strong></p>
<p>While most noun genders are the same across all French variants, Quebec French has some notable differences from France French:</p>
<table>
<thead><tr><th>Word</th><th>Quebec Gender</th><th>France Gender</th><th>English</th><th>Note</th></tr></thead>
<tbody>
<tr><td>une job</td><td>Feminine</td><td>Masculine (un job)</td><td>a job</td><td>Always feminine in Quebec!</td></tr>
<tr><td>une bus</td><td>Feminine (sometimes)</td><td>Masculine (un bus)</td><td>a bus</td><td>Both genders heard in QC</td></tr>
<tr><td>un trampoline</td><td>Masculine</td><td>Masculine or Feminine</td><td>a trampoline</td><td>Usually masculine in QC</td></tr>
<tr><td>une sandwich</td><td>Feminine (sometimes)</td><td>Masculine (un sandwich)</td><td>a sandwich</td><td>Gender varies in QC</td></tr>
</tbody>
</table>
<p><strong>Quebec French Vocabulary – Anglicisms and OQLF Recommendations:</strong></p>
<p>Quebec has the OQLF (Office québécois de la langue française) which actively creates French alternatives to English words. Here are important ones to know:</p>
<table>
<thead><tr><th>English</th><th>OQLF Recommended French</th><th>Anglicism (sometimes still used)</th></tr></thead>
<tbody>
<tr><td>email</td><td>un courriel</td><td>un e-mail</td></tr>
<tr><td>parking lot</td><td>un stationnement</td><td>un parking</td></tr>
<tr><td>shopping</td><td>magasinage</td><td>shopping</td></tr>
<tr><td>weekend</td><td>la fin de semaine</td><td>le week-end</td></tr>
<tr><td>computer</td><td>un ordinateur</td><td>(same in France)</td></tr>
<tr><td>software</td><td>un logiciel</td><td>(same in France)</td></tr>
<tr><td>podcast</td><td>un balado</td><td>un podcast</td></tr>
<tr><td>smartphone</td><td>un téléphone intelligent</td><td>un smartphone</td></tr>
<tr><td>hashtag</td><td>un mot-clic</td><td>un hashtag</td></tr>
<tr><td>streaming</td><td>la diffusion en continu</td><td>le streaming</td></tr>
</tbody>
</table>
<p><strong>Common Noun Patterns in Quebec French:</strong></p>
<p>While the rules for determining gender are the same, Quebec French has some vocabulary preferences:</p>
<ul>
<li><strong>Quebec prefers the full French word</strong> while France often uses shortened forms: "une automobile" (QC) vs. "une auto" (France), "un autobus" (QC) vs. "un bus" (France)</li>
<li><strong>Feminine job titles</strong> are used more consistently in Quebec than in France: "une auteure" (QC) vs. sometimes "un auteur" for a woman in France; "une professeure" (QC); "une docteure" (QC)</li>
<li><strong>Quebec creates French nouns</strong> for things that France leaves in English: "un clavardage" (chatting online) from "clavier" (keyboard) + "bavardage" (chatting)</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – At an OQLF French Course:</strong></p>
<p><em>Vous assistez à un cours de français pour immigrants au Québec.</em></p>
<p>"Aujourd'hui, on va parler du genre des noms. En français, chaque nom est masculin ou féminin."<br>"Monsieur, comment je sais si un mot est masculin ou féminin?"<br>"Il y a des règles générales. Par exemple, les mots qui finissent en '-tion' sont généralement féminins: la nation, la solution, la situation."<br>"Et les mots en '-ment'?"<br>"Ils sont généralement masculins: le gouvernement, le département, le stationnement."<br>"Et 'job', c'est masculin ou féminin?"<br>"Bonne question! Au Québec, on dit 'une job'. C'est féminin chez nous, même si dans d'autres pays francophones, on dit parfois 'un job'."<br>"C'est compliqué!"<br>"Ne vous inquiétez pas. Avec le temps, ça va devenir naturel. Le truc, c'est de toujours apprendre le nom avec son article: 'la maison', 'le bureau', pas juste 'maison' ou 'bureau'."</p>
<p><em>(You're attending a French course for immigrants in Quebec. "Today we'll talk about noun gender. In French, every noun is masculine or feminine." "Sir, how do I know if a word is masculine or feminine?" "There are general rules. For example, words ending in '-tion' are generally feminine." "And words in '-ment'?" "They're generally masculine." "And 'job', is it masculine or feminine?" "Good question! In Quebec, we say 'une job'. It's feminine here." "It's complicated!" "Don't worry. With time, it'll become natural. The trick is to always learn the noun with its article.")</em></p>

"""
    html = insert_before(html, marker_9_end, new_9)

    # =========================================================================
    # UNIT 10: ARTICLES
    # =========================================================================

    marker_10_end = '<h2 id="h-unit-11-adjectives-agreement">'
    new_10 = """
<p><strong>Quebec French Article Usage Notes (🍁):</strong></p>
<p>While article rules are the same across all French variants, Quebec spoken French has some distinctive patterns:</p>
<table>
<thead><tr><th>Feature</th><th>Standard Written French</th><th>Quebec Spoken French</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Article + possessive</td><td>Not used together</td><td>Sometimes combined informally</td><td>"la mienne de voiture" (my car – emphatic)</td></tr>
<tr><td>"À" + possessive meaning</td><td>Less common</td><td>Very common</td><td>"le char à Paul" = Paul's car (= "la voiture de Paul")</td></tr>
<tr><td>Articles before names</td><td>Not standard</td><td>Sometimes used in rural QC</td><td>"La Marie est venue" = Marie came</td></tr>
<tr><td>Partitive in negative</td><td>"de" replaces article</td><td>Same rule applies</td><td>"J'ai pas de pain" (I don't have bread)</td></tr>
</tbody>
</table>
<p><strong>The Quebec Possessive Construction "à" (🍁):</strong></p>
<p>In Quebec French, you'll often hear possessives formed with "à" instead of "de":</p>
<ul>
<li><strong>"Le char à Paul"</strong> = Paul's car (standard: "la voiture de Paul")</li>
<li><strong>"La maison à ma mère"</strong> = My mother's house (standard: "la maison de ma mère")</li>
<li><strong>"Le livre à Marie"</strong> = Marie's book (standard: "le livre de Marie")</li>
<li><strong>"Le chien à mon voisin"</strong> = My neighbour's dog</li>
</ul>
<p>This "à" construction is informal but extremely common in spoken Quebec French. Don't use it in formal writing, but do understand it when you hear it!</p>
<p><strong>Articles with Quebec-Specific Vocabulary:</strong></p>
<p>Here are common Quebec nouns with their proper articles that every learner should know:</p>
<table>
<thead><tr><th>Article + Noun</th><th>English</th><th>Usage Example</th></tr></thead>
<tbody>
<tr><td>le dépanneur</td><td>convenience store</td><td>"Je vais au dépanneur chercher du lait."</td></tr>
<tr><td>la tuque</td><td>winter hat/beanie</td><td>"Mets ta tuque, y fait frette!"</td></tr>
<tr><td>les mitaines</td><td>mittens</td><td>"T'as-tu tes mitaines?"</td></tr>
<tr><td>la motoneige</td><td>snowmobile</td><td>"On va faire de la motoneige en fin de semaine."</td></tr>
<tr><td>le traversier</td><td>ferry</td><td>"Le traversier part à chaque heure."</td></tr>
<tr><td>la cabane à sucre</td><td>sugar shack</td><td>"On va à la cabane à sucre en mars."</td></tr>
<tr><td>le cégep</td><td>college (QC system)</td><td>"Mon fils est au cégep."</td></tr>
<tr><td>la polyvalente</td><td>comprehensive high school</td><td>"J'allais à la polyvalente de mon quartier."</td></tr>
<tr><td>le chalet</td><td>cottage/cabin</td><td>"On a un chalet dans les Laurentides."</td></tr>
<tr><td>la poutine</td><td>poutine (fries+gravy+curds)</td><td>"La meilleure poutine est chez Ashton!"</td></tr>
<tr><td>l'arbre à feuilles</td><td>deciduous tree</td><td>"Les arbres à feuilles perdent leurs feuilles en automne."</td></tr>
<tr><td>les bleuets</td><td>blueberries</td><td>"Les bleuets du Lac-Saint-Jean sont les meilleurs!"</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Shopping at a Quebec Grocery Store:</strong></p>
<p><em>Vous faites l'épicerie au Québec.</em></p>
<p>"Bonjour! Est-ce que vous avez du sirop d'érable?"<br>"Oui, c'est dans l'allée trois. On a du sirop en canne et en bouteille."<br>"Je voudrais une canne de sirop. C'est combien?"<br>"La petite canne, c'est douze dollars. La grosse, c'est vingt-deux."<br>"Je prends la petite. J'aurais aussi besoin de la farine, du beurre et des œufs."<br>"La farine est dans l'allée cinq, le beurre est dans le rayon des produits laitiers, et les œufs sont juste à côté."<br>"Merci! Est-ce que vous avez des bleuets frais?"<br>"Malheureusement, les bleuets sont pas en saison en ce moment. Mais on a des bleuets congelés."<br>"D'accord, je vais prendre un sac de bleuets congelés. Merci pour votre aide!"<br>"De rien! Bonne journée!"</p>
<p><em>(You're grocery shopping in Quebec. "Hello! Do you have maple syrup?" "Yes, it's in aisle three. We have syrup in cans and bottles." "I'd like a can of syrup. How much is it?" "The small can is twelve dollars. The big one is twenty-two." "I'll take the small one. I'd also need flour, butter, and eggs." "Flour is in aisle five, butter is in the dairy section, and eggs are right next to it." "Thanks! Do you have fresh blueberries?" "Unfortunately, blueberries aren't in season right now. But we have frozen blueberries." "Okay, I'll take a bag of frozen blueberries. Thanks for your help!" "You're welcome! Have a good day!")</em></p>

"""
    html = insert_before(html, marker_10_end, new_10)

    write_file(path, html)
    print("Part 2 done: Units 6-10 expanded successfully!")

if __name__ == '__main__':
    main()
