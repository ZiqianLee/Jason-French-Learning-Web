#!/usr/bin/env python3
"""Expand A1 Units 1-5 with more Quebec French content."""

import re

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def insert_after(html, marker, new_content):
    idx = html.find(marker)
    if idx == -1:
        print(f"WARNING: marker not found: {marker[:80]}...")
        return html
    insert_pos = idx + len(marker)
    return html[:insert_pos] + new_content + html[insert_pos:]

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
    # UNIT 1: THE FRENCH ALPHABET & PRONUNCIATION
    # =========================================================================

    # --- 1.1 The French Alphabet - Add more content after the real-life scene ---
    marker_1_1 = '<h3 id="h-1-2-french-vowel-sounds">'
    new_1_1 = """
<p><strong>Quebec French Alphabet Pronunciation – Key Differences (🍁):</strong></p>
<p>While the alphabet is the same across all French-speaking regions, Quebec French has some distinctive pronunciation habits when spelling out loud:</p>
<ul>
<li><strong>W</strong> – In Quebec, "W" is often pronounced "doublé-vé" rather than France's "double-vé". Some older Quebecers say "double-vé" in the traditional way.</li>
<li><strong>R</strong> – The Quebec "R" can vary from a uvular trill (similar to France) to a more rolled "R" in rural areas, especially in the Saguenay–Lac-Saint-Jean and Beauce regions. This rolled "R" is an older French pronunciation that has disappeared in France.</li>
<li><strong>The letter combinations TI and DI</strong> – When followed by certain vowels, "T" can sound like "TS" and "D" can sound like "DZ". This is called <strong>affrication</strong>, and it's the most recognizable feature of Quebec French. For example: "petit" sounds like "p'tsit" and "dire" sounds like "dzir".</li>
</ul>
<p><strong>Spelling Out Special Characters in Quebec:</strong></p>
<p>When Quebecers need to spell something aloud (on the phone, at a government office), they typically use these terms:</p>
<table>
<thead><tr><th>Character</th><th>How to Say It</th><th>Example Word</th></tr></thead>
<tbody>
<tr><td>é</td><td>"e accent aigu"</td><td>érable (maple)</td></tr>
<tr><td>è</td><td>"e accent grave"</td><td>mère (mother)</td></tr>
<tr><td>ê</td><td>"e accent circonflexe"</td><td>fête (party/holiday)</td></tr>
<tr><td>ë</td><td>"e tréma"</td><td>Noël (Christmas)</td></tr>
<tr><td>ç</td><td>"c cédille"</td><td>français (French)</td></tr>
<tr><td>@</td><td>"arobase" (QC) / "at"</td><td>email addresses</td></tr>
<tr><td>-</td><td>"trait d'union"</td><td>peut-être (maybe)</td></tr>
<tr><td>_</td><td>"tiret bas" or "underscore"</td><td>file names</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Setting Up a Quebec Government Account:</strong></p>
<p><em>Vous créez un compte en ligne pour Revenu Québec.</em></p>
<p>"Bonjour, j'ai besoin d'aide pour créer mon compte en ligne."<br>"Bien sûr! Quel est votre nom complet?"<br>"Jean-François Côté."<br>"Pouvez-vous épeler votre nom de famille, s'il vous plaît?"<br>"Oui: C-O accent circonflexe-T-E accent aigu."<br>"Merci. Et votre adresse courriel?"<br>"C'est j-f-point-cote arobase gmail point com."<br>"Parfait. Votre numéro d'assurance sociale?"<br>"Deux-quatre-six, trois-cinq-huit, neuf-zéro-un."<br>"Merci, votre compte est maintenant créé!"</p>
<p><em>(You are creating an online account for Revenu Québec. "Hello, I need help creating my online account." "Of course! What is your full name?" "Jean-François Côté." "Can you spell your last name, please?" "Yes: C-O circumflex-T-E acute accent." "Thank you. And your email address?" "It's j-f-dot-cote at gmail dot com." "Perfect. Your social insurance number?" "Two-four-six, three-five-eight, nine-zero-one." "Thank you, your account is now created!")</em></p>
<p><strong>Common Quebec French Words Every Beginner Should Know:</strong></p>
<p>Before diving deeper into pronunciation, here are 20 essential Quebec French words that differ from France French:</p>
<table>
<thead><tr><th>Quebec French</th><th>France French</th><th>English</th></tr></thead>
<tbody>
<tr><td>char</td><td>voiture</td><td>car</td></tr>
<tr><td>blonde</td><td>petite amie</td><td>girlfriend</td></tr>
<tr><td>chum</td><td>petit ami</td><td>boyfriend</td></tr>
<tr><td>dépanneur</td><td>épicerie de coin</td><td>convenience store</td></tr>
<tr><td>magasiner</td><td>faire du shopping</td><td>to shop</td></tr>
<tr><td>niaiseux / niaiseuse</td><td>bête / stupide</td><td>silly / foolish</td></tr>
<tr><td>pogner</td><td>attraper</td><td>to catch / to grab</td></tr>
<tr><td>jaser</td><td>bavarder</td><td>to chat</td></tr>
<tr><td>pantoute</td><td>pas du tout</td><td>not at all</td></tr>
<tr><td>icitte</td><td>ici</td><td>here</td></tr>
<tr><td>tantôt</td><td>tout à l'heure</td><td>earlier / later today</td></tr>
<tr><td>correct</td><td>d'accord / bien</td><td>okay / fine</td></tr>
<tr><td>barrer</td><td>verrouiller</td><td>to lock</td></tr>
<tr><td>débarrer</td><td>déverrouiller</td><td>to unlock</td></tr>
<tr><td>fête</td><td>anniversaire</td><td>birthday</td></tr>
<tr><td>tuque</td><td>bonnet</td><td>winter hat / beanie</td></tr>
<tr><td>chandail</td><td>pull / tricot</td><td>sweater</td></tr>
<tr><td>bas</td><td>chaussettes</td><td>socks</td></tr>
<tr><td>placoter</td><td>bavarder</td><td>to chat / gossip</td></tr>
<tr><td>bienvenue</td><td>de rien</td><td>you're welcome</td></tr>
</tbody>
</table>

"""
    html = insert_before(html, marker_1_1, new_1_1)

    # --- 1.2 French Vowel Sounds - Add more content ---
    marker_1_2 = '<h3 id="h-1-3-consonant-sounds">'
    new_1_2 = """
<p><strong>Quebec French Vowel Differences – Detailed Guide (🍁):</strong></p>
<p>Quebec French preserves several Old French vowel sounds that have been lost in modern France French. Understanding these differences is crucial for anyone learning to understand spoken Québécois:</p>
<table>
<thead><tr><th>Feature</th><th>France French</th><th>Quebec French</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Long vowels</td><td>Generally short</td><td>Long vowels preserved</td><td>"pâte" (dough) has a long "a" in QC</td></tr>
<tr><td>Open/closed vowels</td><td>"ê" and "é" merging</td><td>Distinct difference maintained</td><td>"fête" (party) vs. "fée" (fairy) clearly different in QC</td></tr>
<tr><td>Diphthongisation</td><td>Does not occur</td><td>Long vowels become diphthongs</td><td>"père" may sound like "pèère" in casual QC speech</td></tr>
<tr><td>Nasal vowels</td><td>"in" and "un" merging</td><td>"in" and "un" remain distinct</td><td>"brin" (twig) vs "brun" (brown) sound different in QC</td></tr>
<tr><td>"oi" sound</td><td>"wa" (standard)</td><td>Sometimes "wé" or "wè"</td><td>"moi" can sound like "moé" in informal QC</td></tr>
</tbody>
</table>
<p><strong>Diphthongisation in Quebec French:</strong></p>
<p>One of the most distinctive features of Quebec pronunciation is <strong>diphthongisation</strong> – when a long vowel "glides" into another vowel sound. This happens most noticeably with:</p>
<ul>
<li><strong>Long "è" → "aè":</strong> "fête" (party) can sound like "faète" in casual speech</li>
<li><strong>Long "ô" → "aô":</strong> "côte" (coast/hill) can sound like "caôte"</li>
<li><strong>Long "eu" → "aeu":</strong> "heure" (hour) can sound like "haeure"</li>
<li><strong>Long "a" → "aô":</strong> "pâte" (dough) can sound like "paôte"</li>
</ul>
<p>Don't worry about reproducing these perfectly – understanding them will help you comprehend spoken Quebec French. Most educated Quebecers moderate these features in formal speech.</p>
<p><strong>Vowel Laxing in Quebec French:</strong></p>
<p>In closed syllables (syllables ending in a consonant), Quebec French "relaxes" certain vowels:</p>
<ul>
<li><strong>i → ɪ</strong> (like English "bit"): "vite" (fast) sounds closer to "vɪt"</li>
<li><strong>u → ʊ</strong> (like English "put"): "lune" (moon) sounds closer to "lʊn"</li>
<li><strong>ou → ʊ</strong>: "route" (road) sounds closer to "rʊt"</li>
</ul>
<p>This is very natural and automatic for Quebecers – you'll pick it up through exposure!</p>

"""
    html = insert_before(html, marker_1_2, new_1_2)

    # --- 1.3 Consonant Sounds - Add more content ---
    marker_1_3 = '<h3 id="h-1-4-accents-special-marks">'
    new_1_3 = """
<p><strong>Affrication in Quebec French – The Most Important Sound Change (🍁):</strong></p>
<p>The single most recognizable feature of Quebec French pronunciation is <strong>affrication</strong> of T and D before the vowels I, U, and their semi-vowel equivalents. This is so important that it deserves a detailed explanation:</p>
<table>
<thead><tr><th>Standard French</th><th>Quebec French Sound</th><th>IPA</th><th>Example Words</th></tr></thead>
<tbody>
<tr><td>T + i/u</td><td>"ts" sound</td><td>[ts]</td><td><strong>petit</strong> → "p'tsit", <strong>tu</strong> → "tsu", <strong>étudiante</strong> → "étsudiante"</td></tr>
<tr><td>D + i/u</td><td>"dz" sound</td><td>[dz]</td><td><strong>dire</strong> → "dzir", <strong>du</strong> → "dzu", <strong>lundi</strong> → "lundzi"</td></tr>
</tbody>
</table>
<p><strong>Practice affrication with these common words:</strong></p>
<ul>
<li><strong>petit</strong> (small) → "p'tsit" – "Le p'tsit garçon joue dehors." (The little boy plays outside.)</li>
<li><strong>tu</strong> (you) → "tsu" – "Tsu veux-tu venir?" (Do you want to come?)</li>
<li><strong>mardi</strong> (Tuesday) → "mardzi" – "On se voit mardzi?" (See you Tuesday?)</li>
<li><strong>difficile</strong> (difficult) → "dzificile" – "C'est pas mal dzificile." (It's pretty difficult.)</li>
<li><strong>étudier</strong> (to study) → "étsudzier" – "Je dois étsudzier ce soir." (I have to study tonight.)</li>
<li><strong>dimanche</strong> (Sunday) → "dzimanche" – "On va à la messe dzimanche." (We go to mass on Sunday.)</li>
</ul>
<p><strong>The Quebec French "R":</strong></p>
<p>While the standard French "R" is a uvular fricative (produced in the back of the throat), Quebec French has regional variations:</p>
<ul>
<li><strong>Montreal and Quebec City:</strong> Similar to the standard uvular "R" in France, though sometimes slightly more pronounced</li>
<li><strong>Rural Quebec (Beauce, Saguenay, Gaspésie):</strong> An older, rolled "R" (alveolar trill) that resembles the Spanish or Italian "R". This was the standard French R before the 18th century</li>
<li><strong>Informal speech:</strong> Final "R" may be dropped: "parler" → "parlé", "pour" → "pou"</li>
</ul>
<p><strong>Other Important Quebec Consonant Features:</strong></p>
<ul>
<li><strong>Assibilation of /t/ and /d/:</strong> Before high vowels, these become affricated (as described above)</li>
<li><strong>H aspiration:</strong> Some words that have h muet in France have h aspiré in Quebec: "les haricots" may not have liaison in Quebec</li>
<li><strong>"J" pronunciation:</strong> In some Quebec dialects, the "j" sound can shift: "je" becomes "chu" → "Chu fatigué" (I'm tired)</li>
<li><strong>Final consonant pronunciation:</strong> Quebec sometimes pronounces final consonants that are silent in France French: "fait" may be pronounced "faite" in emphatic speech</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – Understanding a Franco-Ontarien vs. a Québécois:</strong></p>
<p><em>Vous écoutez deux francophones avec des accents différents.</em></p>
<p>"Dis-moi, tu viens d'où?"<br>"Moi, je viens de Hearst en Ontario. Et toi?"<br>"Moi, chu de Chicoutimi. T'as-tu remarqué qu'on parle pas exactement pareil?"<br>"Oui! Toi, tu dis 'tsu' au lieu de 'tu', pis 'dzir' au lieu de 'dire'."<br>"C'est l'affrication! C'est typiquement québécois. Pis toi, tu roules pas tes R."<br>"Non, nous autres en Ontario, on a un accent un peu différent. Mais on se comprend bien, hein?"<br>"Ah oui, pantoute de problème!"</p>
<p><em>(You are listening to two francophones with different accents. "Tell me, where do you come from?" "I'm from Hearst in Ontario. And you?" "I'm from Chicoutimi. Have you noticed we don't speak exactly the same?" "Yes! You say 'tsu' instead of 'tu' and 'dzir' instead of 'dire'." "That's affrication! It's typically Quebecois. And you, you don't roll your Rs." "No, we in Ontario have a slightly different accent. But we understand each other well, right?" "Oh yes, no problem at all!")</em></p>

"""
    html = insert_before(html, marker_1_3, new_1_3)

    # --- 1.5 Liaison & Elision - Add more content ---
    marker_1_5 = '<h3 id="h-1-6-pronunciation-practice">'
    new_1_5 = """
<p><strong>Quebec French Liaison and Elision Differences (🍁):</strong></p>
<p>While liaison and elision rules are the same in standard French everywhere, spoken Quebec French has some distinctive patterns:</p>
<table>
<thead><tr><th>Feature</th><th>France French</th><th>Quebec French</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Optional liaisons</td><td>Often made in careful speech</td><td>Usually omitted except mandatory ones</td><td>"je suis allé" – liaison is rare in QC casual speech</td></tr>
<tr><td>"Je" before consonant</td><td>"je" stays</td><td>"je" → "j'" or "ch"</td><td>"Je suis" → "Chu" or "J'suis"</td></tr>
<tr><td>"Il" before consonant</td><td>"il" stays</td><td>"il" → "y"</td><td>"Il fait beau" → "Y fait beau"</td></tr>
<tr><td>"Elle" before consonant</td><td>"elle" stays</td><td>"elle" → "a"</td><td>"Elle est belle" → "A'est belle"</td></tr>
<tr><td>"Ils/Elles"</td><td>Stays</td><td>"ils" → "y" / "elles" → "a"</td><td>"Ils vont" → "Y vont"</td></tr>
<tr><td>"Sur le/la"</td><td>"sur le/la"</td><td>"su'l" / "su'a"</td><td>"sur la table" → "su'a table"</td></tr>
<tr><td>"Dans le/la"</td><td>"dans le/la"</td><td>"dans'l" / "dans'a"</td><td>"dans la maison" → "dans'a maison"</td></tr>
</tbody>
</table>
<p><strong>Common Quebec French Contractions in Speech:</strong></p>
<p>These contractions are extremely common in everyday spoken Quebec French. Understanding them is essential for comprehension:</p>
<table>
<thead><tr><th>Standard French</th><th>Quebec Spoken Form</th><th>English</th></tr></thead>
<tbody>
<tr><td>Je suis</td><td>Chu / J'suis</td><td>I am</td></tr>
<tr><td>Je ne sais pas</td><td>Ché pas / J'sais pas</td><td>I don't know</td></tr>
<tr><td>Il y a</td><td>Y'a</td><td>There is/are</td></tr>
<tr><td>Il n'y a pas</td><td>Y'a pas</td><td>There isn't/aren't</td></tr>
<tr><td>Tu es</td><td>T'es</td><td>You are</td></tr>
<tr><td>Elle est</td><td>A'est / Est</td><td>She is</td></tr>
<tr><td>Quelque chose</td><td>Quèque chose / Kek chose</td><td>Something</td></tr>
<tr><td>Peut-être</td><td>P't-être</td><td>Maybe</td></tr>
<tr><td>Parce que</td><td>Pasque / Pas'que</td><td>Because</td></tr>
<tr><td>Il faut que</td><td>Faut que / Faut</td><td>It's necessary that / Must</td></tr>
</tbody>
</table>
<p><strong>Important:</strong> These spoken contractions are completely normal and not "bad French" – they're how millions of native speakers naturally talk. However, don't use them in writing or very formal situations. Think of them like how English speakers say "gonna" instead of "going to" or "wanna" instead of "want to".</p>
<p><strong>🇫🇷 Real-Life Scene – Understanding Casual Quebec French:</strong></p>
<p><em>Vous écoutez une conversation entre deux amis québécois dans un café.</em></p>
<p>"Heille! T'es-tu allé à'fête à Marc en fin d'semaine?"<br>"Non, chu resté chez nous. Y faisait trop frette pour sortir."<br>"Ah ouais? Y'avait du monde en masse, c'était l'fun!"<br>"Ché pas, j'avais pas le goût. Pis t'as-tu vu Julie?"<br>"A'était pas là non plus. P't-être qu'a'travaillait."<br>"Faudrait qu'on se retrouve un moment donné. Ça fait longtemps qu'on s'a pas vu."<br>"Correct, on s'appelle la s'maine prochaine!"</p>
<p><em>(Listen to a conversation between two Quebec friends in a café. "Hey! Did you go to Marc's party this weekend?" "No, I stayed home. It was too cold to go out." "Oh yeah? There were tons of people, it was fun!" "I dunno, I didn't feel like it. Did you see Julie?" "She wasn't there either. Maybe she was working." "We should get together sometime. It's been a long time since we've seen each other." "Okay, we'll call each other next week!")</em></p>

"""
    html = insert_before(html, marker_1_5, new_1_5)

    # =========================================================================
    # UNIT 2: ESSENTIAL GREETINGS & INTRODUCTIONS
    # =========================================================================

    # --- 2.7 Canadian French Greeting Differences - Expand ---
    marker_2_7 = '<h2 id="h-unit-3-the-verb-tre-to-be">'
    new_2_7 = """
<p><strong>Quebec French Greetings – Complete Guide (🍁):</strong></p>
<p>Quebec French has many unique greeting expressions that differ significantly from France French. Here is a comprehensive guide:</p>
<table>
<thead><tr><th>Situation</th><th>Quebec French</th><th>France French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Casual hello</td><td>Allô! / Heille!</td><td>Salut!</td><td>Hi! / Hey!</td></tr>
<tr><td>Friendly greeting</td><td>Salut, ça va-tu?</td><td>Salut, ça va?</td><td>Hi, how's it going?</td></tr>
<tr><td>Informal "how are you"</td><td>Comment ça va? / Pis, toé?</td><td>Comment tu vas?</td><td>How are you? / And you?</td></tr>
<tr><td>Very casual check-in</td><td>Ça va-tu? / Coudonc?</td><td>Ça va?</td><td>Everything okay?</td></tr>
<tr><td>You're welcome</td><td>Bienvenue!</td><td>De rien / Je vous en prie</td><td>You're welcome</td></tr>
<tr><td>See you later</td><td>Bye! / Bye-bye! / À la r'voyure!</td><td>Au revoir / Salut</td><td>Bye! / See you!</td></tr>
<tr><td>Take care</td><td>Prends soin de toé!</td><td>Prends soin de toi!</td><td>Take care of yourself!</td></tr>
<tr><td>Have a good day</td><td>Bonne journée!</td><td>Bonne journée!</td><td>Have a good day! (same)</td></tr>
<tr><td>Sorry</td><td>Excuse / S'cusez</td><td>Pardon / Excusez-moi</td><td>Sorry / Excuse me</td></tr>
<tr><td>Of course</td><td>Ben oui! / C'est sûr!</td><td>Bien sûr!</td><td>Of course!</td></tr>
</tbody>
</table>
<p><strong>The Quebec "tu" – Interrogative Particle (🍁):</strong></p>
<p>One of the most distinctive features of Quebec French is the use of <strong>"tu"</strong> (or <strong>"-tu"</strong>) as a question particle. This is NOT the pronoun "tu" (you) – it's a way to turn any statement into a yes/no question:</p>
<ul>
<li><strong>"T'as-tu faim?"</strong> = Are you hungry? (literally: "You have-tu hunger?")</li>
<li><strong>"Y fait-tu beau?"</strong> = Is it nice out? (literally: "It makes-tu nice?")</li>
<li><strong>"C'est-tu correct?"</strong> = Is it okay? (literally: "It is-tu correct?")</li>
<li><strong>"Tu veux-tu venir?"</strong> = Do you want to come?</li>
<li><strong>"On y va-tu?"</strong> = Shall we go?</li>
</ul>
<p>This "-tu" question particle is ONLY used in spoken Quebec French – never write it in formal contexts. It comes from Old French and is one of the oldest features preserved in Québécois.</p>
<p><strong>Formal vs. Informal Address in Quebec:</strong></p>
<p>Quebec culture is generally more informal than France's when it comes to using "tu" vs "vous":</p>
<ul>
<li><strong>In Quebec:</strong> People switch to "tu" much faster than in France. Coworkers, service staff, and even strangers of similar age often use "tu" from the start.</li>
<li><strong>In France:</strong> "Vous" is maintained longer and more strictly in professional and unfamiliar settings.</li>
<li><strong>When to use "vous" in Quebec:</strong> With elderly people you don't know well, in very formal professional settings, with authority figures (judges, police), and in customer service when you want to be extra polite.</li>
<li><strong>Common Quebec expression:</strong> "On peut se tutoyer?" (Can we use 'tu' with each other?) – This question is asked much earlier in relationships in Quebec than in France.</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – A Typical Quebec Morning Greeting:</strong></p>
<p><em>Vous rencontrez votre voisine québécoise le matin.</em></p>
<p>"Allô! Ça va-tu à matin?"<br>"Oui, ça va bien, pis toé?"<br>"Ah, pas pire! Y fait frette en titi aujourd'hui, hein?"<br>"Met-en! J'ai mis ma grosse tuque pis mes mitaines."<br>"T'as-tu vu que le dépanneur au coin a fermé?"<br>"Ah oui? Ben voyons! On allait toujours là pour notre café."<br>"Je sais! C'est plate. Bon, faut que j'y aille. Bonne journée!"<br>"Toi aussi! Bye!"</p>
<p><em>(You meet your Quebec neighbour in the morning. "Hi! How's it going this morning?" "Good, and you?" "Not bad! It's really cold today, eh?" "You can say that again! I put on my big winter hat and my mittens." "Did you see the convenience store on the corner closed?" "Oh really? Come on! We always went there for our coffee." "I know! That's a bummer. Well, I have to go. Have a good day!" "You too! Bye!")</em></p>
<p><strong>Essential Quebec French Slang for Social Situations:</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>C'est l'fun!</td><td>It's fun!</td><td>"La fête était l'fun en maudit!" (The party was really fun!)</td></tr>
<tr><td>C'est plate</td><td>It's boring / That sucks</td><td>"Le film était plate à mort." (The movie was dead boring.)</td></tr>
<tr><td>C'est correct</td><td>It's okay / No worries</td><td>"T'excuse pas, c'est correct!" (Don't apologize, it's fine!)</td></tr>
<tr><td>C'est pas pire</td><td>It's not bad (= pretty good)</td><td>"Comment tu trouves Montréal? – C'est pas pire!" (How do you find Montreal? – Pretty good!)</td></tr>
<tr><td>En masse</td><td>A lot / plenty</td><td>"Y'a du monde en masse!" (There are tons of people!)</td></tr>
<tr><td>Pas mal</td><td>Pretty / quite</td><td>"C'est pas mal bon!" (It's pretty good!)</td></tr>
<tr><td>Ben là!</td><td>Come on! / Seriously?</td><td>"Ben là, tu peux pas faire ça!" (Come on, you can't do that!)</td></tr>
<tr><td>Voyons donc!</td><td>Come on! / Really?!</td><td>"Voyons donc, c'est pas vrai!" (Come on, that's not true!)</td></tr>
</tbody>
</table>

"""
    html = insert_before(html, marker_2_7, new_2_7)

    # =========================================================================
    # UNIT 3: THE VERB "ÊTRE" (TO BE)
    # =========================================================================

    marker_3_7 = '<h2 id="h-unit-4-the-verb-avoir-to-have">'
    new_3_7 = """
<p><strong>Quebec French Pronunciation of "Être" Forms (🍁):</strong></p>
<p>In spoken Quebec French, the conjugations of "être" undergo significant sound changes:</p>
<table>
<thead><tr><th>Standard French</th><th>Quebec Spoken Form</th><th>Phonetic</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Je suis</td><td>Chu / J'suis</td><td>shoo / zhsui</td><td>"Chu fatigué." (I'm tired.)</td></tr>
<tr><td>Tu es</td><td>T'es</td><td>tay</td><td>"T'es correct?" (You okay?)</td></tr>
<tr><td>Il est</td><td>Y'est</td><td>yay</td><td>"Y'est parti." (He left.)</td></tr>
<tr><td>Elle est</td><td>A'est / Est</td><td>ay / est</td><td>"A'est grande." (She's tall.)</td></tr>
<tr><td>On est</td><td>On est</td><td>on-ay</td><td>"On est prêts." (We're ready.)</td></tr>
<tr><td>Nous sommes</td><td>On est (more common)</td><td>on-ay</td><td>"On est contents." (We're happy.)</td></tr>
<tr><td>Ils sont</td><td>Y sont</td><td>ee son</td><td>"Y sont arrivés." (They arrived.)</td></tr>
<tr><td>Elles sont</td><td>Y sont / A sont</td><td>ee son</td><td>"Y sont belles." (They're beautiful.)</td></tr>
</tbody>
</table>
<p><strong>Important Quebec Expressions with "Être" (🍁):</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>Meaning</th><th>Usage Example</th></tr></thead>
<tbody>
<tr><td>Être tanné(e)</td><td>To be fed up / tired of</td><td>"Chu tanné de la neige!" (I'm sick of the snow!)</td></tr>
<tr><td>Être correct</td><td>To be fine / okay</td><td>"T'es-tu correct?" (Are you alright?)</td></tr>
<tr><td>Être dans le champ</td><td>To be wrong / off track</td><td>"T'es dans le champ!" (You're totally wrong!)</td></tr>
<tr><td>Être de bonne heure</td><td>To be early</td><td>"On est de bonne heure à matin." (We're early this morning.)</td></tr>
<tr><td>Être en beau fusil</td><td>To be really angry</td><td>"Le boss est en beau fusil." (The boss is furious.)</td></tr>
<tr><td>Être aux oiseaux</td><td>To be thrilled / delighted</td><td>"A'est aux oiseaux!" (She's over the moon!)</td></tr>
<tr><td>Être dans la lune</td><td>To be daydreaming</td><td>"T'es encore dans la lune!" (You're daydreaming again!)</td></tr>
<tr><td>Être bien</td><td>To be comfortable / fine</td><td>"On est bien icitte." (We're comfortable here.)</td></tr>
</tbody>
</table>
<p><strong>The Use of "On" Instead of "Nous" in Quebec (🍁):</strong></p>
<p>In Quebec French (even more than in France French), <strong>"on"</strong> has completely replaced <strong>"nous"</strong> in everyday speech. While "nous" can sound formal or stiff, "on" is natural and friendly:</p>
<ul>
<li><strong>Standard:</strong> "Nous sommes prêts." → <strong>Quebec:</strong> "On est prêts." (We're ready.)</li>
<li><strong>Standard:</strong> "Nous allons au cinéma." → <strong>Quebec:</strong> "On va au cinéma." (We're going to the movies.)</li>
<li><strong>Standard:</strong> "Nous avons faim." → <strong>Quebec:</strong> "On a faim." (We're hungry.)</li>
</ul>
<p><strong>Note:</strong> "Nous" is still used in Quebec in very formal writing, official documents, and academic texts. But in all spoken contexts and informal writing, always use "on".</p>
<p><strong>🇫🇷 Real-Life Scene – At the CLSC (Quebec Health Clinic):</strong></p>
<p><em>Vous visitez un CLSC pour la première fois.</em></p>
<p>"Bonjour, c'est ma première visite ici. Je suis nouveau dans le quartier."<br>"Bienvenue! Êtes-vous inscrit avec un médecin de famille?"<br>"Non, je ne suis pas encore inscrit. Est-ce que c'est possible de s'inscrire aujourd'hui?"<br>"Oui, bien sûr. On est là pour ça! Vous êtes résident permanent ou citoyen?"<br>"Je suis résident permanent. Je suis ici depuis six mois."<br>"Parfait. Votre carte d'assurance maladie est-elle valide?"<br>"Oui, elle est valide. La voici."<br>"Merci! On va vous assigner un médecin. Le temps d'attente est d'environ six mois."<br>"C'est long, mais je comprends. Merci beaucoup!"</p>
<p><em>(You visit a CLSC – Quebec's local community health centre – for the first time. "Hello, this is my first visit here. I'm new to the neighbourhood." "Welcome! Are you registered with a family doctor?" "No, I'm not registered yet. Is it possible to register today?" "Yes, of course. That's what we're here for! Are you a permanent resident or citizen?" "I'm a permanent resident. I've been here for six months." "Perfect. Is your health insurance card valid?" "Yes, it's valid. Here it is." "Thank you! We'll assign you a doctor. The wait time is about six months." "It's long, but I understand. Thank you very much!")</em></p>

"""
    html = insert_before(html, marker_3_7, new_3_7)

    # =========================================================================
    # UNIT 4: THE VERB "AVOIR" (TO HAVE)
    # =========================================================================

    marker_4_7 = '<h1 id="h-part-ii-personal-information">'
    new_4_7 = """
<p><strong>Quebec French Pronunciation of "Avoir" Forms (🍁):</strong></p>
<p>Like "être," the verb "avoir" undergoes spoken contractions in everyday Quebec French:</p>
<table>
<thead><tr><th>Standard French</th><th>Quebec Spoken Form</th><th>Example</th></tr></thead>
<tbody>
<tr><td>J'ai</td><td>J'ai / Ga</td><td>"J'ai faim" → "Ga faim" (very casual)</td></tr>
<tr><td>Tu as</td><td>T'as</td><td>"T'as-tu fini?" (Are you done?)</td></tr>
<tr><td>Il a</td><td>Y'a</td><td>"Y'a pas le temps." (He doesn't have time.)</td></tr>
<tr><td>Elle a</td><td>A'a / A l'a</td><td>"A l'a raison." (She's right.)</td></tr>
<tr><td>On a</td><td>On a</td><td>"On a besoin d'aide." (We need help.)</td></tr>
<tr><td>Ils ont</td><td>Y'ont</td><td>"Y'ont fini." (They finished.)</td></tr>
</tbody>
</table>
<p><strong>Essential "Avoir" Expressions in Quebec Context (🍁):</strong></p>
<table>
<thead><tr><th>Expression</th><th>Meaning</th><th>Quebec Context Example</th></tr></thead>
<tbody>
<tr><td>Avoir hâte (de)</td><td>To look forward to / to be eager</td><td>"J'ai hâte à Noël!" (I can't wait for Christmas!)</td></tr>
<tr><td>Avoir frette</td><td>To be cold (QC version)</td><td>"J'ai frette, passe-moi ma tuque!" (I'm cold, pass me my beanie!)</td></tr>
<tr><td>Avoir le goût (de)</td><td>To feel like (doing something)</td><td>"J'ai le goût d'aller glisser!" (I feel like going sledding!)</td></tr>
<tr><td>Avoir de la misère</td><td>To have difficulty</td><td>"J'ai de la misère à comprendre l'accent." (I have trouble understanding the accent.)</td></tr>
<tr><td>Avoir du fun</td><td>To have fun</td><td>"On a eu du fun en masse!" (We had tons of fun!)</td></tr>
<tr><td>Avoir l'air</td><td>To look like / seem</td><td>"T'as l'air fatigué." (You look tired.)</td></tr>
<tr><td>En avoir plein son casque</td><td>To be fed up (QC idiom)</td><td>"J'en ai plein mon casque de c'te job-là!" (I'm fed up with this job!)</td></tr>
<tr><td>Avoir les yeux plus grands que la panse</td><td>Eyes bigger than stomach</td><td>"T'as les yeux plus grands que la panse!" (Your eyes are bigger than your stomach!)</td></tr>
</tbody>
</table>
<p><strong>Quebec Weather Expressions with "Avoir" and "Faire":</strong></p>
<p>Talking about weather is essential in Quebec (it's the #1 small talk topic!). Many weather expressions use "avoir" and "faire":</p>
<ul>
<li><strong>"Y fait frette!"</strong> = It's freezing! (Quebec: "frette" instead of France's "froid")</li>
<li><strong>"Y fait chaud en titi!"</strong> = It's really hot! ("en titi" = very/really – QC intensifier)</li>
<li><strong>"Y mouille!"</strong> = It's raining! (QC verb "mouiller" for rain)</li>
<li><strong>"Y neige à plein ciel!"</strong> = It's snowing like crazy!</li>
<li><strong>"Y fait tempête!"</strong> = There's a storm! / It's stormy!</li>
<li><strong>"Les routes sont glacées!"</strong> = The roads are icy!</li>
<li><strong>"C'est la slush!"</strong> = It's slushy! (anglicism commonly used in QC)</li>
</ul>
<p><strong>🇫🇷 Real-Life Scene – Quebec Winter Small Talk:</strong></p>
<p><em>Vous jaserez avec un collègue au bureau en hiver.</em></p>
<p>"Ayoye, y fait frette en maudit à matin!"<br>"Met-en! Y fait combien, tu penses?"<br>"Y fait moins trente avec le facteur vent! J'ai eu de la misère à partir le char."<br>"Ah oui? Moi aussi, j'avais les vitres toutes gelées."<br>"T'as-tu mis ton kit d'hiver dans ton auto?"<br>"Ben oui, j'ai toujours mes câbles à batterie, une pelle pis une couverture dans le coffre."<br>"C'est correct de même. Au Québec, faut toujours être prêt pour l'hiver!"<br>"Tu l'dis! Ça va-tu faire plus chaud en fin de semaine?"<br>"Non, y annoncent encore moins vingt-cinq. C'est l'hiver québécois!"</p>
<p><em>(You're chatting with a colleague at the office in winter. "Ow, it's really freezing this morning!" "You can say that again! What's the temperature, you think?" "It's minus thirty with the wind chill! I had trouble starting the car." "Really? Me too, my windows were all frozen." "Did you put your winter kit in your car?" "Of course, I always have my jumper cables, a shovel and a blanket in the trunk." "That's the right thing to do. In Quebec, you always have to be ready for winter!" "You said it! Is it going to be warmer this weekend?" "No, they're calling for minus twenty-five again. That's Quebec winter!")</em></p>

"""
    html = insert_before(html, marker_4_7, new_4_7)

    # =========================================================================
    # UNIT 5: NUMBERS (0-100)
    # =========================================================================

    marker_5_7 = '<h2 id="h-unit-6-days-months-time">'
    new_5_7 = """
<p><strong>Quebec vs. France Number System – Detailed Comparison (🍁):</strong></p>
<p>The biggest difference between Quebec and France French numbers involves 70, 80, and 90:</p>
<table>
<thead><tr><th>Number</th><th>France French</th><th>Quebec French</th><th>Belgium/Switzerland French</th></tr></thead>
<tbody>
<tr><td>70</td><td>soixante-dix (60+10)</td><td>soixante-dix (same)</td><td>septante</td></tr>
<tr><td>71</td><td>soixante-et-onze</td><td>soixante-et-onze</td><td>septante-et-un</td></tr>
<tr><td>80</td><td>quatre-vingts (4x20)</td><td>quatre-vingts (same)</td><td>huitante/octante</td></tr>
<tr><td>90</td><td>quatre-vingt-dix (4x20+10)</td><td>quatre-vingt-dix (same)</td><td>nonante</td></tr>
</tbody>
</table>
<p><strong>Note:</strong> While Quebec uses the same number system as France (unlike Belgium and Switzerland), there are pronunciation differences. Quebecers tend to say numbers more quickly and with the characteristic affrication.</p>
<p><strong>Quebec French Number Pronunciation Tips:</strong></p>
<ul>
<li><strong>"Vingt"</strong> – In Quebec, the "t" is often pronounced even when standing alone: "vin-t" (vs. France: "vin")</li>
<li><strong>"Six" and "Dix"</strong> – At the end of a sentence, pronounced "siss" and "diss". Before a consonant: "si" and "di". Before a vowel: "siz" and "diz".</li>
<li><strong>"Cinq"</strong> – The final "q" is always pronounced in Quebec: "sink"</li>
<li><strong>Phone numbers</strong> – In Quebec, phone numbers are spoken in individual digits or pairs: 514-555-1234 = "cinq-un-quatre, cinq-cinq-cinq, un-deux-trois-quatre"</li>
</ul>
<p><strong>Numbers in Quebec Daily Life:</strong></p>
<table>
<thead><tr><th>Context</th><th>Example</th><th>Note</th></tr></thead>
<tbody>
<tr><td>Money</td><td>"Ça coûte vingt-trois piasses et cinquante." ($23.50)</td><td>"Piasses" = informal for "dollars" / "cennes" = cents</td></tr>
<tr><td>Temperature</td><td>"Y fait moins vingt-cinq." (-25°C)</td><td>Always Celsius in Quebec!</td></tr>
<tr><td>Distance</td><td>"C'est à deux cents kilomètres d'icitte."</td><td>Always metric in Quebec</td></tr>
<tr><td>Address</td><td>"J'habite au trois-mille-cinq-cents, rue Saint-Denis."</td><td>Addresses can have 4-5 digit numbers</td></tr>
<tr><td>Age</td><td>"Ma grand-mère a quatre-vingt-sept ans."</td><td>Same pattern as France</td></tr>
<tr><td>Time</td><td>"Y est trois heures et quart."</td><td>"et quart" / "et demie" / "moins quart"</td></tr>
</tbody>
</table>
<p><strong>Quebec Money Vocabulary:</strong></p>
<table>
<thead><tr><th>Term</th><th>Meaning</th><th>Note</th></tr></thead>
<tbody>
<tr><td>une piasse</td><td>a dollar (informal)</td><td>From old French "piastre"</td></tr>
<tr><td>une cenne</td><td>a cent</td><td>"J'ai pas une cenne!" (I'm broke!)</td></tr>
<tr><td>un trente sous</td><td>25 cents (a quarter)</td><td>Historical term, still used by older Quebecers</td></tr>
<tr><td>un deux piasses</td><td>a toonie ($2 coin)</td><td>"T'as-tu un deux piasses pour la machine?"</td></tr>
<tr><td>un huard</td><td>a loonie ($1 coin)</td><td>Named after the "huard" (loon) bird on the coin</td></tr>
<tr><td>le change</td><td>loose change / coins</td><td>"As-tu du change pour le parcomètre?"</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Paying at a Dépanneur:</strong></p>
<p><em>Vous achetez quelque chose au dépanneur du coin.</em></p>
<p>"Bonjour! Juste ces items-là, s'il vous plaît."<br>"D'accord. Ça va faire huit piasses et quarante-sept."<br>"Voici un dix."<br>"Merci. Votre change: un dollar et cinquante-trois cennes."<br>"Merci! Ah, attendez – avez-vous des billets de loterie?"<br>"Oui, on a le Lotto 6/49. C'est cinq piasses le billet."<br>"D'accord, j'en prends un. Souhaitez-moi bonne chance!"<br>"Bonne chance! Le gros lot est à quinze millions cette semaine!"</p>
<p><em>(You're buying something at the corner convenience store. "Hello! Just these items, please." "Okay. That'll be eight dollars and forty-seven." "Here's a ten." "Thank you. Your change: one dollar and fifty-three cents." "Thanks! Oh wait – do you have lottery tickets?" "Yes, we have Lotto 6/49. It's five dollars a ticket." "Okay, I'll take one. Wish me luck!" "Good luck! The jackpot is fifteen million this week!")</em></p>

"""
    html = insert_before(html, marker_5_7, new_5_7)

    # --- Remove the "NOTE: This textbook is extensive..." message ---
    old_note = '<p><strong>[NOTE: This textbook is extensive. To keep the file manageable while providing complete A1 coverage, I will summarize Units 15-20 with key content rather than full detailed treatment. Each unit would expand similarly if needed.]</strong></p>'
    html = html.replace(old_note, '')

    write_file(path, html)
    print("Part 1 done: Units 1-5 expanded successfully!")

if __name__ == '__main__':
    main()
