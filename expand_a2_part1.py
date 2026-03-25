#!/usr/bin/env python3
"""Expand A2 Units 1-5 with more Quebec French content."""

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
    path = r'e:\MyProjects\Web\Jason-French-Learning-Web\a2.html'
    html = read_file(path)

    # =========================================================================
    # UNIT 1: REVIEW OF A1 ESSENTIALS – Expand all sub-sections
    # =========================================================================

    # --- 1.1 Key Verbs Review – add more verb tables and examples ---
    marker_1_1 = '<h3 id="h-1-2-essential-vocabulary">'
    new_1_1 = """
<p><strong>Additional Essential Verbs for A2 – Full Conjugation Review:</strong></p>
<p>At A2 level, you need to master more verbs beyond être, avoir, aller, and faire. Here are critical verbs with their present tense conjugations:</p>
<table>
<thead><tr><th>Pronoun</th><th>Pouvoir (can)</th><th>Vouloir (want)</th><th>Devoir (must)</th><th>Savoir (know)</th><th>Connaître (know)</th></tr></thead>
<tbody>
<tr><td>Je</td><td>peux</td><td>veux</td><td>dois</td><td>sais</td><td>connais</td></tr>
<tr><td>Tu</td><td>peux</td><td>veux</td><td>dois</td><td>sais</td><td>connais</td></tr>
<tr><td>Il/Elle/On</td><td>peut</td><td>veut</td><td>doit</td><td>sait</td><td>connaît</td></tr>
<tr><td>Nous</td><td>pouvons</td><td>voulons</td><td>devons</td><td>savons</td><td>connaissons</td></tr>
<tr><td>Vous</td><td>pouvez</td><td>voulez</td><td>devez</td><td>savez</td><td>connaissez</td></tr>
<tr><td>Ils/Elles</td><td>peuvent</td><td>veulent</td><td>doivent</td><td>savent</td><td>connaissent</td></tr>
</tbody>
</table>
<p><strong>Savoir vs. Connaître – A Key Distinction:</strong></p>
<table>
<thead><tr><th>Savoir (to know facts/how to)</th><th>Connaître (to know/be familiar with)</th></tr></thead>
<tbody>
<tr><td>Je sais nager. (I know how to swim.)</td><td>Je connais Montréal. (I know/am familiar with Montreal.)</td></tr>
<tr><td>Tu sais la réponse? (Do you know the answer?)</td><td>Tu connais mon frère? (Do you know my brother?)</td></tr>
<tr><td>On sait que c'est difficile. (We know it's hard.)</td><td>On connaît un bon restaurant. (We know a good restaurant.)</td></tr>
<tr><td>Je sais parler français. (I know how to speak French.)</td><td>Je connais bien la ville de Québec. (I know Quebec City well.)</td></tr>
</tbody>
</table>
<p><strong>More Essential Verb Conjugations – Prendre, Mettre, Voir:</strong></p>
<table>
<thead><tr><th>Pronoun</th><th>Prendre (take)</th><th>Mettre (put)</th><th>Voir (see)</th><th>Dire (say)</th><th>Venir (come)</th></tr></thead>
<tbody>
<tr><td>Je</td><td>prends</td><td>mets</td><td>vois</td><td>dis</td><td>viens</td></tr>
<tr><td>Tu</td><td>prends</td><td>mets</td><td>vois</td><td>dis</td><td>viens</td></tr>
<tr><td>Il/Elle/On</td><td>prend</td><td>met</td><td>voit</td><td>dit</td><td>vient</td></tr>
<tr><td>Nous</td><td>prenons</td><td>mettons</td><td>voyons</td><td>disons</td><td>venons</td></tr>
<tr><td>Vous</td><td>prenez</td><td>mettez</td><td>voyez</td><td>dites</td><td>venez</td></tr>
<tr><td>Ils/Elles</td><td>prennent</td><td>mettent</td><td>voient</td><td>disent</td><td>viennent</td></tr>
</tbody>
</table>
<p><strong>Quebec French Verb Pronunciation Reminders (🍁):</strong></p>
<ul>
<li><strong>"Je"</strong> → "J'" or "Chu" before consonants: "J'peux pas" / "Chu pas capable"</li>
<li><strong>"Il"</strong> → "Y": "Y peut pas venir" (He can't come)</li>
<li><strong>"Elle"</strong> → "A": "A veut pas" (She doesn't want to)</li>
<li><strong>"Ils/Elles"</strong> → "Y": "Y savent pas" (They don't know)</li>
<li><strong>"Tu"</strong> → affricated "Tsu": "Tsu veux-tu venir?" (Do you want to come?)</li>
</ul>
<p><strong>Verb Expressions Essential for Quebec Daily Life:</strong></p>
<table>
<thead><tr><th>Expression</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>être capable de</td><td>to be able to (QC preference)</td><td>"Chu pas capable de dormir." (I can't sleep.)</td></tr>
<tr><td>avoir besoin de</td><td>to need</td><td>"J'ai besoin d'un char." (I need a car.)</td></tr>
<tr><td>avoir envie de</td><td>to feel like</td><td>"J'ai envie de poutine." (I feel like having poutine.)</td></tr>
<tr><td>avoir le goût de (QC)</td><td>to feel like</td><td>"J'ai le goût d'aller glisser." (I feel like going sledding.)</td></tr>
<tr><td>être en train de</td><td>to be in the process of</td><td>"Chu en train de manger." (I'm eating right now.)</td></tr>
<tr><td>venir de</td><td>to have just</td><td>"Je viens de finir." (I just finished.)</td></tr>
<tr><td>devoir + infinitif</td><td>must / have to</td><td>"Je dois pelleter l'entrée." (I have to shovel the driveway.)</td></tr>
<tr><td>falloir (il faut)</td><td>it's necessary / must</td><td>"Faut que j'y aille." (I have to go.)</td></tr>
</tbody>
</table>

"""
    html = insert_before(html, marker_1_1, new_1_1)

    # --- 1.2 Essential Vocabulary – add more categories ---
    marker_1_2 = '<h3 id="h-1-3-sentence-building">'
    new_1_2 = """
<p><strong>Extended Daily Life Vocabulary for A2:</strong></p>
<table>
<thead><tr><th>Category</th><th>French (Quebec)</th><th>English</th><th>Example Sentence</th></tr></thead>
<tbody>
<tr><td>Home</td><td>le loyer</td><td>rent</td><td>"Mon loyer est de mille piasses par mois." (My rent is a thousand bucks a month.)</td></tr>
<tr><td>Home</td><td>le propriétaire</td><td>landlord</td><td>"Mon propriétaire est ben correct." (My landlord is really nice.)</td></tr>
<tr><td>Home</td><td>le concierge</td><td>superintendent/janitor</td><td>"Le concierge va venir réparer le robinet." (The super will come fix the faucet.)</td></tr>
<tr><td>Work</td><td>l'horaire</td><td>schedule</td><td>"Mon horaire change chaque semaine." (My schedule changes every week.)</td></tr>
<tr><td>Work</td><td>le patron / la patronne</td><td>boss</td><td>"Ma patronne est fine." (My boss is nice.)</td></tr>
<tr><td>Work</td><td>la paie</td><td>pay/paycheck</td><td>"Je reçois ma paie aux deux semaines." (I get paid every two weeks.)</td></tr>
<tr><td>Transport</td><td>la passe d'autobus</td><td>bus pass</td><td>"Ma passe coûte quatre-vingt-dix piasses par mois." (My pass costs ninety bucks a month.)</td></tr>
<tr><td>Transport</td><td>le covoiturage</td><td>carpooling</td><td>"Je fais du covoiturage avec ma collègue." (I carpool with my colleague.)</td></tr>
<tr><td>Health</td><td>la carte d'assurance maladie</td><td>health insurance card (RAMQ)</td><td>"N'oublie pas ta carte d'assurance maladie!" (Don't forget your health card!)</td></tr>
<tr><td>Health</td><td>le rendez-vous</td><td>appointment</td><td>"J'ai un rendez-vous chez le dentiste à deux heures." (I have a dentist appointment at two.)</td></tr>
<tr><td>Social</td><td>un party</td><td>a party</td><td>"On fait un party samedi soir." (We're having a party Saturday night.)</td></tr>
<tr><td>Social</td><td>un 5 à 7</td><td>after-work drinks</td><td>"On se voit au 5 à 7 après l'ouvrage?" (See you at the after-work drinks?)</td></tr>
</tbody>
</table>
<p><strong>Quebec French Emotion & Feeling Vocabulary:</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Standard French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Chu content(e)</td><td>Je suis content(e)</td><td>I'm happy</td></tr>
<tr><td>Chu tanné(e)</td><td>J'en ai marre</td><td>I'm fed up</td></tr>
<tr><td>Chu fâché(e)</td><td>Je suis en colère</td><td>I'm angry</td></tr>
<tr><td>Chu stressé(e)</td><td>Je suis stressé(e)</td><td>I'm stressed</td></tr>
<tr><td>Chu mêlé(e)</td><td>Je suis confus(e)</td><td>I'm confused</td></tr>
<tr><td>Chu gêné(e)</td><td>Je suis gêné(e)</td><td>I'm embarrassed</td></tr>
<tr><td>Chu surpris(e)</td><td>Je suis surpris(e)</td><td>I'm surprised</td></tr>
<tr><td>Chu de bonne humeur</td><td>Je suis de bonne humeur</td><td>I'm in a good mood</td></tr>
<tr><td>Chu découragé(e)</td><td>Je suis découragé(e)</td><td>I'm discouraged</td></tr>
<tr><td>Chu écœuré(e)</td><td>J'en ai assez</td><td>I'm sick of it / disgusted</td></tr>
</tbody>
</table>

"""
    html = insert_before(html, marker_1_2, new_1_2)

    # --- 1.3 Building Longer Sentences – add more connectors ---
    marker_1_3 = '<h3 id="h-1-4-cdn-french-a1-review">'
    new_1_3 = """
<p><strong>Additional Sentence Connectors for A2 Level:</strong></p>
<table>
<thead><tr><th>Connector</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>pourtant</td><td>however / yet</td><td>"Il fait froid, pourtant les enfants jouent dehors." (It's cold, yet the kids play outside.)</td></tr>
<tr><td>alors</td><td>so / then</td><td>"J'ai fini mon travail, alors je suis rentré à la maison." (I finished work, so I went home.)</td></tr>
<tr><td>en plus</td><td>moreover / in addition</td><td>"C'est loin. En plus, il neige!" (It's far. In addition, it's snowing!)</td></tr>
<tr><td>d'abord... ensuite... enfin</td><td>first... then... finally</td><td>"D'abord, je me lève. Ensuite, je déjeune. Enfin, je pars travailler." (First I get up. Then I have breakfast. Finally I leave for work.)</td></tr>
<tr><td>c'est pourquoi</td><td>that's why</td><td>"Il fait tempête, c'est pourquoi l'école est fermée." (There's a storm, that's why school is closed.)</td></tr>
<tr><td>en fait</td><td>in fact / actually</td><td>"En fait, j'habite pas à Montréal, j'habite à Laval." (Actually, I don't live in Montreal, I live in Laval.)</td></tr>
<tr><td>au lieu de</td><td>instead of</td><td>"Au lieu de prendre le métro, j'ai marché." (Instead of taking the metro, I walked.)</td></tr>
<tr><td>grâce à</td><td>thanks to</td><td>"Grâce à mon cours de francisation, je parle mieux." (Thanks to my French class, I speak better.)</td></tr>
<tr><td>malgré</td><td>despite</td><td>"Malgré le froid, on est allés patiner." (Despite the cold, we went skating.)</td></tr>
<tr><td>à cause de</td><td>because of</td><td>"À cause de la tempête, les routes sont fermées." (Because of the storm, roads are closed.)</td></tr>
</tbody>
</table>
<p><strong>Quebec-Specific Connectors and Fillers (🍁):</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Standard French</th><th>English</th><th>Usage</th></tr></thead>
<tbody>
<tr><td>pis</td><td>puis / et</td><td>and / then</td><td>"J'ai mangé pis j'suis parti." (I ate and I left.)</td></tr>
<tr><td>faque / ça fait que</td><td>donc / alors</td><td>so / therefore</td><td>"Y neigeait, faque j'suis resté chez nous." (It was snowing, so I stayed home.)</td></tr>
<tr><td>ben</td><td>bien / eh bien</td><td>well / so</td><td>"Ben, c'est comme ça." (Well, that's how it is.)</td></tr>
<tr><td>tsé (tu sais)</td><td>tu sais</td><td>you know</td><td>"C'est compliqué, tsé." (It's complicated, you know.)</td></tr>
<tr><td>genre</td><td>genre / du genre</td><td>like / kind of</td><td>"C'était genre dix personnes." (There were like ten people.)</td></tr>
<tr><td>mettons</td><td>disons</td><td>let's say</td><td>"Mettons qu'on part à huit heures?" (Let's say we leave at eight?)</td></tr>
<tr><td>en tout cas</td><td>en tout cas</td><td>anyway / in any case</td><td>"En tout cas, c'est ce que je pense." (Anyway, that's what I think.)</td></tr>
<tr><td>par exemple</td><td>voyons / par exemple</td><td>honestly / come on (QC)</td><td>"Par exemple, tu peux pas faire ça!" (Honestly, you can't do that!)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Telling a Story with Connectors:</strong></p>
<p><em>Vous racontez votre journée à votre colocataire.</em></p>
<p>"Ouf, quelle journée! D'abord, j'suis arrivé en retard au bureau parce que le métro était en panne. Ensuite, mon patron m'a donné un gros projet à finir pour vendredi. Pourtant, j'avais déjà trois dossiers en cours! En plus, j'ai oublié mon lunch à la maison, faque j'ai dû manger à la cafétéria. C'était pas pire, mais c'est cher. Enfin, à cinq heures, je suis parti au 5 à 7 avec mes collègues. En tout cas, demain ça va être mieux, j'espère!"</p>
<p><em>(Phew, what a day! First, I arrived late to the office because the metro broke down. Then my boss gave me a big project due Friday. Yet I already had three files in progress! On top of that, I forgot my lunch at home, so I had to eat at the cafeteria. It wasn't bad, but it's expensive. Finally, at five, I went to the after-work drinks with my colleagues. Anyway, tomorrow will be better, I hope!)</em></p>

"""
    html = insert_before(html, marker_1_3, new_1_3)

    # --- 1.4 Canadian French Review – add more QC specifics ---
    marker_1_4 = '<h2 id="h-unit-2-imparfait">'
    new_1_4 = """
<p><strong>Quebec French Pronoun Contractions – Complete Reference (🍁):</strong></p>
<p>At A2, you should now be comfortable recognizing these spoken contractions:</p>
<table>
<thead><tr><th>Standard Written</th><th>Quebec Spoken</th><th>Phonetic</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Je suis</td><td>Chu / J'suis</td><td>shoo</td><td>"Chu prêt." (I'm ready.)</td></tr>
<tr><td>Je ne sais pas</td><td>Ché pas</td><td>shay pah</td><td>"Ché pas quoi faire." (I dunno what to do.)</td></tr>
<tr><td>Il y a</td><td>Y'a</td><td>yah</td><td>"Y'a du monde en masse!" (There are lots of people!)</td></tr>
<tr><td>Il faut que</td><td>Faut que / Faut</td><td>foh kuh</td><td>"Faut que j'y aille." (I gotta go.)</td></tr>
<tr><td>Tu es</td><td>T'es</td><td>tay</td><td>"T'es-tu correct?" (Are you okay?)</td></tr>
<tr><td>Elle est</td><td>A'est / Est</td><td>ah-ay</td><td>"A'est partie." (She left.)</td></tr>
<tr><td>Ils sont</td><td>Y sont</td><td>ee son</td><td>"Y sont arrivés." (They arrived.)</td></tr>
<tr><td>Il fait</td><td>Y fait</td><td>ee fay</td><td>"Y fait frette!" (It's cold!)</td></tr>
<tr><td>Ce n'est pas</td><td>C'est pas</td><td>say pah</td><td>"C'est pas grave." (It's no big deal.)</td></tr>
<tr><td>Quelque chose</td><td>Quèque chose</td><td>kek shohz</td><td>"T'as-tu quèque chose à manger?" (Do you have something to eat?)</td></tr>
<tr><td>Je vais</td><td>M'a / J'va</td><td>mah / zhvah</td><td>"M'a faire ça tantôt." (I'll do that later.)</td></tr>
<tr><td>Regarde</td><td>R'garde</td><td>rr-gard</td><td>"R'garde ça!" (Look at that!)</td></tr>
</tbody>
</table>
<p><strong>Quebec Expressions You'll Hear Daily (🍁):</strong></p>
<table>
<thead><tr><th>Expression</th><th>Meaning</th><th>When to Use</th></tr></thead>
<tbody>
<tr><td>C'est l'fun!</td><td>It's fun! / Great!</td><td>Expressing enjoyment: "Le party était l'fun!"</td></tr>
<tr><td>C'est plate</td><td>It's boring / That sucks</td><td>Expressing disappointment: "C'est plate, y pleut."</td></tr>
<tr><td>C'est correct / C'est chill</td><td>It's fine / No worries</td><td>Reassuring someone: "C'est correct, t'excuse pas."</td></tr>
<tr><td>Ben voyons!</td><td>Come on! / Really?!</td><td>Expressing disbelief: "Ben voyons, c'est pas vrai!"</td></tr>
<tr><td>Voyons donc!</td><td>Oh come on!</td><td>Stronger disbelief: "Voyons donc, tu peux pas faire ça!"</td></tr>
<tr><td>Mets-en!</td><td>You bet! / Absolutely!</td><td>Strong agreement: "Y fait frette? – Mets-en!"</td></tr>
<tr><td>Pas pire!</td><td>Not bad! (= quite good)</td><td>Positive understatement: "Comment ça va? – Pas pire!"</td></tr>
<tr><td>Lâche pas!</td><td>Don't give up! / Keep going!</td><td>Encouragement: "T'es presque fini, lâche pas!"</td></tr>
<tr><td>Check ben ça!</td><td>Watch this! / Check this out!</td><td>Drawing attention: "Check ben ça, tu vas capoter!"</td></tr>
<tr><td>Ça a pas de bon sens!</td><td>That's crazy! / Unbelievable!</td><td>Expressing shock: "Ça a pas de bon sens, ce prix-là!"</td></tr>
</tbody>
</table>

"""
    html = insert_before(html, marker_1_4, new_1_4)

    # =========================================================================
    # UNIT 2: THE IMPARFAIT – Expand all sub-sections
    # =========================================================================

    # --- 2.3 Uses – add more examples ---
    marker_2_3 = '<h3 id="h-2-4-imparfait-vs-pc">'
    new_2_3 = """
<p><strong>4. Polite requests and suggestions (conditional feel):</strong></p>
<ul>
<li><strong>Je voulais vous demander quelque chose.</strong> (I wanted to ask you something.) – more polite than "je veux"</li>
<li><strong>Est-ce que tu savais que le musée est gratuit le mercredi?</strong> (Did you know the museum is free on Wednesdays?)</li>
<li><strong>Je pensais qu'on pourrait aller au cinéma ce soir.</strong> (I was thinking we could go to the movies tonight.)</li>
</ul>
<p><strong>5. Describing simultaneous ongoing actions:</strong></p>
<ul>
<li><strong>Pendant que ma mère cuisinait, mon père lisait le journal et les enfants jouaient dans le salon.</strong> (While my mother was cooking, my father was reading the newspaper and the kids were playing in the living room.)</li>
<li><strong>L'orchestre jouait de la musique douce pendant que les invités dansaient et riaient.</strong> (The orchestra was playing soft music while the guests were dancing and laughing.)</li>
</ul>
<p><strong>Imparfait with Time Expressions – Complete Guide:</strong></p>
<table>
<thead><tr><th>Time Expression</th><th>Translation</th><th>Example with Imparfait</th></tr></thead>
<tbody>
<tr><td>chaque jour / tous les jours</td><td>every day</td><td>"Chaque jour, je prenais le même autobus." (Every day, I used to take the same bus.)</td></tr>
<tr><td>chaque été / hiver</td><td>every summer / winter</td><td>"Chaque été, on allait au Lac-Saint-Jean." (Every summer, we'd go to Lac-Saint-Jean.)</td></tr>
<tr><td>d'habitude</td><td>usually</td><td>"D'habitude, on soupait à six heures." (Usually, we'd have dinner at six.)</td></tr>
<tr><td>souvent</td><td>often</td><td>"On allait souvent à la cabane à sucre." (We often went to the sugar shack.)</td></tr>
<tr><td>de temps en temps</td><td>from time to time</td><td>"De temps en temps, il neigeait en avril." (From time to time, it snowed in April.)</td></tr>
<tr><td>toujours</td><td>always</td><td>"Grand-maman faisait toujours de la soupe aux pois." (Grandma always made pea soup.)</td></tr>
<tr><td>autrefois / dans le temps</td><td>in the past / back then</td><td>"Dans le temps, y'avait pas de métro à Laval." (Back then, there was no metro in Laval.)</td></tr>
<tr><td>à l'époque</td><td>at the time</td><td>"À l'époque, j'habitais dans un petit appartement." (At the time, I lived in a small apartment.)</td></tr>
<tr><td>quand j'étais jeune</td><td>when I was young</td><td>"Quand j'étais jeune, on jouait au hockey dans la rue." (When I was young, we played hockey in the street.)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Grandpa Tells Stories About Old Quebec:</strong></p>
<p><em>Grand-papa raconte comment c'était au Québec dans les années 1960.</em></p>
<p>"Dans le temps, c'était pas pareil, mon p'tit. Quand j'étais jeune, les familles étaient grosses – on était douze enfants chez nous! Mon père travaillait à l'usine de papier pis ma mère restait à la maison. A faisait à manger pour tout le monde."<br>"Y'avait pas de télévision au début. On écoutait la radio le soir. Le samedi, on allait à la messe le matin pis après, on jouait dehors toute la journée."<br>"L'hiver, on patinait sur le lac gelé pis l'été, on allait pêcher la truite dans la rivière. On avait pas besoin de grand-chose pour avoir du fun."<br>"Pis quand la Révolution tranquille est arrivée dans les années soixante, tout a changé. Les femmes allaient travailler, les enfants allaient au cégep... le Québec devenait moderne."</p>
<p><em>(Grandpa tells stories about old Quebec in the 1960s. "Back then, it was different, kiddo. When I was young, families were big – there were twelve of us! My father worked at the paper mill and my mother stayed home. She cooked for everyone." "There was no TV at first. We listened to the radio in the evening. On Saturdays, we went to mass in the morning and after, we played outside all day." "In winter, we skated on the frozen lake and in summer, we went trout fishing in the river. We didn't need much to have fun." "And when the Quiet Revolution came in the sixties, everything changed. Women went to work, young people went to CEGEP... Quebec was becoming modern.")</em></p>

"""
    html = insert_before(html, marker_2_3, new_2_3)

    # --- 2.5 Canadian French Notes – add more imparfait QC specifics ---
    marker_2_5 = '<h2 id="h-unit-3-futur-simple">'
    new_2_5 = """
<p><strong>The Imparfait in Quebec Expressions (🍁):</strong></p>
<table>
<thead><tr><th>Quebec Expression (Imparfait)</th><th>English</th><th>Context</th></tr></thead>
<tbody>
<tr><td>"Dans mon temps, on faisait pas ça."</td><td>"In my day, we didn't do that."</td><td>Older generation comparing to today</td></tr>
<tr><td>"C'était le bon temps."</td><td>"Those were the good old days."</td><td>Nostalgia</td></tr>
<tr><td>"Y'avait du monde en masse."</td><td>"There were tons of people."</td><td>Describing a past event</td></tr>
<tr><td>"On savait comment s'amuser."</td><td>"We knew how to have fun."</td><td>Fond memories</td></tr>
<tr><td>"Ça coûtait pas cher dans le temps."</td><td>"It didn't cost much back then."</td><td>Comparing past prices</td></tr>
<tr><td>"Ma grand-mère faisait les meilleurs desserts."</td><td>"My grandmother made the best desserts."</td><td>Family memories</td></tr>
</tbody>
</table>
<p><strong>Quebec Cultural References – Life Before and After the Quiet Revolution:</strong></p>
<p>The imparfait is perfect for talking about how things <em>used to be</em> in Quebec. Here are key cultural comparisons:</p>
<table>
<thead><tr><th>Before 1960s (Imparfait)</th><th>After 1960s (Present/Passé Composé)</th></tr></thead>
<tbody>
<tr><td>L'Église catholique contrôlait l'éducation.</td><td>Le gouvernement gère maintenant le système scolaire.</td></tr>
<tr><td>Les familles avaient 10-15 enfants.</td><td>Les familles ont maintenant 1-2 enfants en moyenne.</td></tr>
<tr><td>Les femmes restaient à la maison.</td><td>Les femmes travaillent dans tous les domaines.</td></tr>
<tr><td>On parlait anglais au travail à Montréal.</td><td>La loi 101 protège le français au travail depuis 1977.</td></tr>
<tr><td>Le Québec s'appelait "la Belle Province."</td><td>La devise officielle est "Je me souviens."</td></tr>
</tbody>
</table>

"""
    html = insert_before(html, marker_2_5, new_2_5)

    # =========================================================================
    # UNIT 3: FUTUR SIMPLE – Expand
    # =========================================================================

    marker_3_5 = '<h2 id="h-unit-4-recent-past-near-future">'
    new_3_5 = """
<p><strong>Futur Simple vs. Futur Proche – When to Use Which (🍁):</strong></p>
<table>
<thead><tr><th>Situation</th><th>Futur Proche (aller + inf.)</th><th>Futur Simple</th></tr></thead>
<tbody>
<tr><td>Everyday spoken language</td><td>✅ "Je vais manger." (very common in QC)</td><td>Less common in casual QC speech</td></tr>
<tr><td>Immediate plans</td><td>✅ "Je vais partir dans cinq minutes."</td><td>Sounds too formal</td></tr>
<tr><td>Formal writing/news</td><td>Acceptable but less formal</td><td>✅ "Le premier ministre annoncera sa décision."</td></tr>
<tr><td>Predictions/weather</td><td>"Il va neiger demain." (casual)</td><td>✅ "Il neigera demain." (weather forecast)</td></tr>
<tr><td>Promises</td><td>"Je vais t'aider." (casual)</td><td>✅ "Je t'aiderai, promis." (more solemn)</td></tr>
<tr><td>After "quand"</td><td>Not used</td><td>✅ "Quand tu arriveras, appelle-moi."</td></tr>
</tbody>
</table>
<p><strong>The Quebec Spoken Future – "M'a" Contraction (🍁):</strong></p>
<p>In very informal Quebec French, there's a unique future form: <strong>"m'a"</strong> (from "je m'en vais" = I'm going to). This is extremely casual:</p>
<table>
<thead><tr><th>Standard</th><th>Quebec Informal</th><th>English</th></tr></thead>
<tbody>
<tr><td>Je vais le faire.</td><td>M'a l'faire.</td><td>I'm gonna do it.</td></tr>
<tr><td>Je vais y aller.</td><td>M'a y aller.</td><td>I'm gonna go there.</td></tr>
<tr><td>Je vais te montrer.</td><td>M'a te montrer.</td><td>I'm gonna show you.</td></tr>
<tr><td>Je vais t'appeler.</td><td>M'a t'appeler.</td><td>I'm gonna call you.</td></tr>
</tbody>
</table>
<p><strong>Important:</strong> "M'a" is very informal – don't use it in writing or formal speech. But you WILL hear it constantly in everyday Quebec conversation.</p>
<p><strong>Additional Irregular Futur Simple Stems:</strong></p>
<table>
<thead><tr><th>Verb</th><th>Stem</th><th>Example</th><th>Translation</th></tr></thead>
<tbody>
<tr><td>envoyer</td><td>enverr-</td><td>J'enverrai le courriel demain.</td><td>I will send the email tomorrow.</td></tr>
<tr><td>courir</td><td>courr-</td><td>Elle courra le marathon de Montréal.</td><td>She will run the Montreal marathon.</td></tr>
<tr><td>mourir</td><td>mourr-</td><td>Cette plante mourra sans eau.</td><td>This plant will die without water.</td></tr>
<tr><td>recevoir</td><td>recevr-</td><td>Tu recevras ta paie vendredi.</td><td>You will receive your pay on Friday.</td></tr>
<tr><td>tenir</td><td>tiendr-</td><td>Ils tiendront une réunion lundi.</td><td>They will hold a meeting Monday.</td></tr>
<tr><td>pleuvoir</td><td>pleuvr-</td><td>Il pleuvra toute la semaine.</td><td>It will rain all week.</td></tr>
<tr><td>falloir</td><td>faudr-</td><td>Il faudra partir de bonne heure.</td><td>We'll have to leave early.</td></tr>
<tr><td>valoir</td><td>vaudr-</td><td>Ça vaudra la peine.</td><td>It will be worth it.</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – New Year's Resolutions in Quebec:</strong></p>
<p><em>C'est le 31 décembre. Vous parlez de vos résolutions du Nouvel An.</em></p>
<p>"Alors, quelles sont vos résolutions pour la nouvelle année?"<br>"Moi, je ferai plus d'exercice. Je m'inscrirai au gym en janvier."<br>"Bonne idée! Moi, j'apprendrai le français mieux. Je suivrai un cours au cégep."<br>"Pis moi, j'arrêterai de manger de la poutine chaque vendredi soir... ben, j'essaierai!"<br>"Ha! Ça, c'est la résolution la plus difficile au Québec!"<br>"On verra bien! En tout cas, je sais que dans trois mois, on aura tous abandonné nos résolutions!"<br>"Peut-être, mais on pourra toujours recommencer à l'automne. Bonne année à tout le monde!"</p>
<p><em>(It's December 31st. You're talking about your New Year's resolutions. "So, what are your resolutions for the new year?" "Me, I'll exercise more. I'll sign up for the gym in January." "Good idea! Me, I'll learn French better. I'll take a course at CEGEP." "And me, I'll stop eating poutine every Friday night... well, I'll try!" "Ha! That's the hardest resolution in Quebec!" "We'll see! Anyway, I know in three months, we'll all have given up our resolutions!" "Maybe, but we can always start again in the fall. Happy New Year everyone!")</em></p>

"""
    html = insert_before(html, marker_3_5, new_3_5)

    # =========================================================================
    # UNIT 4: PASSÉ RÉCENT – Expand
    # =========================================================================

    marker_4_end = '<h2 id="h-unit-5-shopping">'
    new_4 = """
<p><strong>Three Tenses Together – Practice Paragraph:</strong></p>
<p>Here's a paragraph using all three temporal constructions together. Pay attention to how they work:</p>
<p>"Je <strong>viens d'arriver</strong> au bureau (passé récent – just happened). En ce moment, je <strong>suis en train de</strong> lire mes courriels (present ongoing). Après, je <strong>vais</strong> commencer mon rapport (futur proche). Ce soir, je <strong>mangerai</strong> au restaurant avec ma blonde (futur simple)."</p>
<p><em>(I just arrived at the office. Right now, I'm reading my emails. After, I'm going to start my report. Tonight, I will eat at the restaurant with my girlfriend.)</em></p>
<p><strong>Quebec French Time Expression – "Tantôt" Clarified (🍁):</strong></p>
<p>The word <strong>"tantôt"</strong> is a uniquely Quebec expression that causes confusion because it can refer to the past OR the future, depending on context:</p>
<table>
<thead><tr><th>Usage</th><th>Example</th><th>Meaning</th><th>How to Tell</th></tr></thead>
<tbody>
<tr><td>Recent past</td><td>"J'ai vu Pierre tantôt."</td><td>"I saw Pierre earlier (today)."</td><td>Used with passé composé</td></tr>
<tr><td>Near future</td><td>"Je vais faire ça tantôt."</td><td>"I'll do that later (today)."</td><td>Used with aller + infinitive</td></tr>
<tr><td>Near future</td><td>"À tantôt!"</td><td>"See you later (today)!"</td><td>As a farewell</td></tr>
</tbody>
</table>
<p><strong>More Useful Quebec Time Expressions:</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Standard French</th><th>English</th></tr></thead>
<tbody>
<tr><td>à matin</td><td>ce matin</td><td>this morning</td></tr>
<tr><td>à soir</td><td>ce soir</td><td>tonight</td></tr>
<tr><td>hier au soir</td><td>hier soir</td><td>last night</td></tr>
<tr><td>asteure / à c't'heure</td><td>maintenant</td><td>now / right now</td></tr>
<tr><td>l'autre jour</td><td>l'autre jour</td><td>the other day</td></tr>
<tr><td>la semaine passée</td><td>la semaine dernière</td><td>last week</td></tr>
<tr><td>dans pas long</td><td>bientôt / sous peu</td><td>soon / in not long</td></tr>
<tr><td>un moment donné</td><td>à un certain moment</td><td>at some point</td></tr>
<tr><td>de bonne heure</td><td>tôt</td><td>early</td></tr>
<tr><td>su'l tard</td><td>tard</td><td>late</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Catching Up After Missing a Call:</strong></p>
<p><em>Votre ami vous rappelle après un appel manqué.</em></p>
<p>"Allô! Scuse, je viens de voir que tu m'as appelé tantôt."<br>"Pas de trouble! Je suis en train de magasiner au Costco. T'es-tu libre à soir?"<br>"Oui! Qu'est-ce que tu veux faire?"<br>"On pourrait aller voir un film. Le nouveau film québécois vient de sortir."<br>"Ah oui, j'ai vu la bande-annonce. Ça a l'air bon! M'a checker les heures pis je te rappelle."<br>"Correct! M'a finir mes commissions pis je vais être chez nous vers quatre heures."<br>"Ben parfait. À tantôt!"<br>"À tantôt!"</p>
<p><em>(Your friend calls you back after a missed call. "Hello! Sorry, I just saw that you called me earlier." "No worries! I'm in the middle of shopping at Costco. Are you free tonight?" "Yes! What do you want to do?" "We could go see a movie. The new Quebec film just came out." "Oh yeah, I saw the trailer. It looks good! I'll check the times and call you back." "Sounds good! I'll finish my errands and I'll be home around four." "Perfect. See you later!" "See you later!")</em></p>

"""
    html = insert_before(html, marker_4_end, new_4)

    # =========================================================================
    # UNIT 5: SHOPPING & MONEY – Expand
    # =========================================================================

    marker_5_end = '<h2 id="h-unit-6-housing">'
    new_5 = """
<p><strong>Quebec Tax System – What Every Shopper Needs to Know (🍁):</strong></p>
<p>Unlike many countries (and France!), prices displayed in Quebec stores do NOT include tax. Two taxes are added at the register:</p>
<table>
<thead><tr><th>Tax</th><th>Full Name</th><th>Rate</th><th>Applied To</th></tr></thead>
<tbody>
<tr><td>TPS / GST</td><td>Taxe sur les produits et services</td><td>5%</td><td>Most goods and services</td></tr>
<tr><td>TVQ / QST</td><td>Taxe de vente du Québec</td><td>9.975%</td><td>Most goods and services</td></tr>
<tr><td>Combined</td><td>Total tax</td><td>~14.975%</td><td>Applied on top of displayed price</td></tr>
</tbody>
</table>
<p><strong>Tip:</strong> To quickly estimate the total, add about 15% to any displayed price. A $100 item will cost approximately $115 after tax.</p>
<p><strong>Tax-Exempt Items in Quebec:</strong></p>
<ul>
<li>Basic grocery items (bread, milk, fruits, vegetables, meat)</li>
<li>Prescription drugs</li>
<li>Children's clothing (very small sizes)</li>
<li>Some medical devices</li>
</ul>
<p><strong>Complete Quebec Money Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>une piasse</td><td>a dollar (informal)</td><td>"Ça coûte dix piasses." (It costs ten bucks.)</td></tr>
<tr><td>une cenne / un sou</td><td>a cent</td><td>"J'ai pas une cenne." (I'm broke.)</td></tr>
<tr><td>un huard</td><td>a loonie ($1 coin)</td><td>Named after the loon bird on the coin</td></tr>
<tr><td>un deux piasses</td><td>a toonie ($2 coin)</td><td>"T'as-tu un deux piasses?"</td></tr>
<tr><td>un cinq</td><td>a $5 bill</td><td>"Passe-moi un cinq."</td></tr>
<tr><td>un vingt</td><td>a $20 bill</td><td>The most common bill in ATMs</td></tr>
<tr><td>le guichet automatique</td><td>ATM</td><td>"Y'a-tu un guichet proche d'icitte?"</td></tr>
<tr><td>le Interac</td><td>debit card payment</td><td>"Je vais payer par Interac." (uniquely Canadian!)</td></tr>
<tr><td>le sans-contact / taper</td><td>tap / contactless</td><td>"Vous pouvez taper." (You can tap.)</td></tr>
<tr><td>le reçu / la facture</td><td>receipt / invoice</td><td>"Voulez-vous votre reçu?"</td></tr>
<tr><td>les aubaines</td><td>bargains / sales</td><td>"Y'a de bonnes aubaines cette semaine."</td></tr>
<tr><td>en spécial</td><td>on sale</td><td>"Le beurre est en spécial au Metro."</td></tr>
<tr><td>la circulaire</td><td>flyer / weekly ad</td><td>"J'ai vu ça dans la circulaire du IGA."</td></tr>
</tbody>
</table>
<p><strong>Quebec Grocery Store Chains – Essential Knowledge:</strong></p>
<table>
<thead><tr><th>Store</th><th>Type</th><th>Price Level</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>IGA</td><td>Grocery</td><td>Mid-range</td><td>Quebec's most popular grocery chain</td></tr>
<tr><td>Metro</td><td>Grocery</td><td>Mid-range</td><td>Another major Quebec chain</td></tr>
<tr><td>Maxi</td><td>Grocery</td><td>Budget</td><td>Discount grocery, Loblaw-owned</td></tr>
<tr><td>Super C</td><td>Grocery</td><td>Budget</td><td>Discount grocery, Metro-owned</td></tr>
<tr><td>Costco</td><td>Wholesale</td><td>Bulk</td><td>Membership required, very popular in QC</td></tr>
<tr><td>Jean Coutu</td><td>Pharmacy</td><td>Varies</td><td>Quebec pharmacy chain, also sells groceries</td></tr>
<tr><td>Pharmaprix</td><td>Pharmacy</td><td>Varies</td><td>Quebec name for Shoppers Drug Mart</td></tr>
<tr><td>Canadian Tire</td><td>Hardware/General</td><td>Mid-range</td><td>"Le Tire" – everything for home and car</td></tr>
<tr><td>Dollarama</td><td>Dollar store</td><td>Budget</td><td>Quebec-founded chain, very popular</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Returning an Item at a Quebec Store:</strong></p>
<p><em>Vous retournez un article dans un magasin.</em></p>
<p>"Bonjour! Je voudrais retourner ce chandail, s'il vous plaît."<br>"D'accord. Avez-vous votre reçu?"<br>"Oui, le voici. Je l'ai acheté samedi passé."<br>"Parfait. C'est dans les trente jours, faque c'est correct. Quel est le problème?"<br>"Y est trop petit. J'aurais besoin d'un large au lieu d'un medium."<br>"Est-ce que vous voulez un échange ou un remboursement?"<br>"Un échange, si vous avez la bonne taille."<br>"Laissez-moi vérifier... Oui, on l'a en large! Tenez."<br>"Merci beaucoup! Est-ce que je dois payer une différence?"<br>"Non, c'est le même prix. Voici votre nouveau reçu."<br>"Parfait! Bonne journée!"<br>"Bienvenue! Bonne journée à vous aussi!"</p>
<p><em>(You're returning an item at a store. "Hello! I'd like to return this sweater, please." "Okay. Do you have your receipt?" "Yes, here it is. I bought it last Saturday." "Perfect. That's within thirty days, so it's fine. What's the problem?" "It's too small. I would need a large instead of a medium." "Do you want an exchange or a refund?" "An exchange, if you have the right size." "Let me check... Yes, we have it in large! Here you go." "Thank you! Do I have to pay a difference?" "No, it's the same price. Here's your new receipt." "Perfect! Have a good day!" "You're welcome! Have a good day too!")</em></p>

"""
    html = insert_before(html, marker_5_end, new_5)

    write_file(path, html)
    print("A2 Part 1 done: Units 1-5 expanded successfully!")

if __name__ == '__main__':
    main()
