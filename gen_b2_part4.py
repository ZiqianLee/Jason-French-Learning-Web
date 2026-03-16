#!/usr/bin/env python3
"""Generate B2 HTML - Part 4: Units 17-20 + Footer/JS"""
import os
DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(DIR, "b2.html")
A1 = os.path.join(DIR, "a1.html")

with open(A1, 'r', encoding='utf-8') as f:
    a1_content = f.read()
js_start = a1_content.index('<script>') + len('<script>')
js_end = a1_content.index('</script>')
js_block = a1_content[js_start:js_end]

content = """
<h1 id="h-b2-part-v">PART V: REVIEW &amp; B2 EXAM PREP</h1>

<h2 id="h-b2-u17">UNIT 17: GRAMMAR CAPSTONE</h2>

<h3 id="h-b2-17-1">17.1 The Subjunctive vs. Indicative Check</h3>
<p>In B2, you are expected to switch effortlessly between moods based on the trigger phrase.</p>
<ul>
<li><strong>Indicatif (Certainty):</strong> Je pense que, je crois que, j'espère que, il est clair que.
<ul><li><em>Je pense qu'il vient ce soir.</em> (I think he is coming tonight.)</li></ul></li>
<li><strong>Subjonctif (Doubt/Emotion/Necessity):</strong> Je ne pense pas que, il faut que, je suis content que, bien que.
<ul><li><em>Je ne pense pas qu'il vienne ce soir.</em> (I don't think he is coming tonight.)</li></ul></li>
</ul>

<h3 id="h-b2-17-2">17.2 Preposition Pitfalls</h3>
<ul>
<li><strong>À vs. De:</strong> Continuer <strong>à</strong> faire qch, vs. Essayer <strong>de</strong> faire qch.
<ul><li><em>J'ai réussi à le convaincre de venir.</em> (I succeeded in convincing him to come.)</li></ul></li>
<li><strong>Pour vs. Pendant:</strong> Use <em>pour</em> for planned future duration; use <em>pendant</em> for completed past duration.
<ul><li><em>Je pars au Québec pour deux abs.</em> (I am leaving for Quebec for two years.)</li>
<li><em>J'ai habité à Montréal pendant cinq ans.</em> (I lived in Montreal for five years.)</li></ul></li>
</ul>

<h3 id="h-b2-17-3">17.3 Advanced Pronouns (Y / En placement)</h3>
<ul>
<li><strong>Y</strong> replaces <em>à + noun</em> (ideas/places). <em>Tu penses à ton avenir? Oui, j'<strong>y</strong> pense.</em></li>
<li><strong>En</strong> replaces <em>de + noun</em> (quantities/ideas). <em>Tu as besoin de ce dossier? Oui, j'<strong>en</strong> ai besoin.</em></li>
<li><strong>Order:</strong> Subject + (me/te/se/nous/vous) + (le/la/les) + (lui/leur) + (y) + (en) + Verb.
<ul><li><em>Il y a des pommes? Donne-m'<strong>en</strong> deux.</em> (Are there apples? Give me two of them.)</li></ul></li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Correcting a Colleague:</strong></p>
<p><em>Correction bienveillante entre collègues.</em></p>
<p>"J'ai dit au client qu'il faut qu'il est patient."<br>"Attention! Après 'il faut que', tu dois utiliser le subjonctif. Tu devrais dire : il faut qu'il <strong>soit</strong> patient."<br>"Ah oui, c'est vrai. Et pour le contrat, je lui ai demandé de m'y envoyer."<br>"Presque! Tu demandes à envoyer <em>le contrat</em> (le) <em>à toi</em> (me). Donc: Tu lui as demandé de <strong>te l'envoyer</strong>."</p>
<p><em>(Kind correction between colleagues. "I told the client that he must is patient." "Careful! After 'il faut que', you must use the subjunctive. You should say: he must *be* patient." "Ah yes, it's true. And for the contract, I asked him to send there to me." "Almost! You ask to send *the contract* (it) *to you* (me). So: You asked him to send *it to you*.")</em></p>

<h3 id="h-b2-17-4">17.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In spoken Quebec French, prepositions are often mashed together or skipped entirely. "Je vais <strong>à la</strong> maison" often sounds like "j'va <strong>a'</strong> maison" or even "m'a aller chez nous."</li>
</ul>
<hr>

<h2 id="h-b2-u18">UNIT 18: VOCABULARY CAPSTONE</h2>

<h3 id="h-b2-18-1">18.1 False Friends (Faux Amis)</h3>
<p>Watch out for words that look like English but mean something completely different.</p>
<table>
<thead><tr><th>French Word</th><th>Does NOT mean...</th><th>Actually means...</th><th>How to say the English word</th></tr></thead>
<tbody>
<tr><td>Actuellement</td><td>Actually</td><td>Currently</td><td>En fait / En réalité</td></tr>
<tr><td>Éventuellement</td><td>Eventually</td><td>Possibly / Perhaps</td><td>Finalement / Tôt ou tard</td></tr>
<tr><td>Une location</td><td>A location</td><td>A rental</td><td>Un endroit / Un lieu</td></tr>
<tr><td>Assister à (un événement)</td><td>To assist someone</td><td>To attend (an event)</td><td>Aider qqn</td></tr>
<tr><td>Une librairie</td><td>A library</td><td>A bookstore</td><td>Une bibliothèque</td></tr>
<tr><td>Formidable</td><td>Formidable (scary)</td><td>Wonderful / Great</td><td>Redoutable</td></tr>
</tbody></table>

<h3 id="h-b2-18-2">18.2 Anglicisms to Avoid in Writing</h3>
<p>While anglicisms are common in spoken Quebec French, you must avoid them in B2 writing.</p>
<ul>
<li><em>Avoid:</em> Prendre pour acquis. <em>Use:</em> <strong>Tenir pour acquis</strong> (To take for granted).</li>
<li><em>Avoid:</em> Faire du sens. <em>Use:</em> <strong>Avoir du sens / Être logique</strong> (To make sense).</li>
<li><em>Avoid:</em> Céduler une rencontre. <em>Use:</em> <strong>Planifier une réunion</strong> (To schedule a meeting).</li>
</ul>

<h3 id="h-b2-18-3">18.3 Synonyms for Better Expression</h3>
<p>Stop using "bon," "mauvais," "très," and "beaucoup." Upgrade your vocabulary!</p>
<ul>
<li><strong>Bon →</strong> Excellent, remarquable, pertinent, efficace.</li>
<li><strong>Mauvais →</strong> Médiocre, néfaste, désastreux, défectueux.</li>
<li><strong>Très →</strong> Extrêmement, profondément, particulièrement.</li>
<li><strong>Beaucoup de →</strong> Une multitude de, un grand nombre de, abondamment.</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Revising an Essay:</strong></p>
<p><em>Un professeur corrige le texte d'un étudiant.</em></p>
<p>"Dans votre introduction, vous écrivez : 'Les téléphones intelligents ont beaucoup de mauvais effets.' C'est grammaticalement correct, mais trop simple pour le niveau B2. Essayez plutôt : 'Les téléphones intelligents ont des répercussions néfastes sur la santé mentale.'"<br>"Je comprends. C'est plus précis. Et pour ma transition, est-ce que je peux dire 'actuellement, les jeunes...'"<br>"Seulement si vous voulez dire 'en ce moment' (currently). Si vous vouliez dire 'in fact', vous devez utiliser 'en réalité' ou 'de fait'."</p>
<p><em>(A teacher corrects a student's text. "In your introduction, you write: 'Smartphones have a lot of bad effects.' It is grammatically correct, but too simple for the B2 level. Try instead: 'Smartphones have detrimental repercussions on mental health.'" "I understand. It is more precise. And for my transition, can I say 'actuellement, young people...'" "Only if you mean 'currently'. If you meant 'in fact', you must use 'en réalité' or 'de fait'.")</em></p>

<h3 id="h-b2-18-4">18.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec, there is a strong linguistic effort to replace English tech terms with French ones to fight anglicisms. For example, <em>un courriel</em> (email), <em>le clavardage</em> (chat), <em>un mot-clic</em> (hashtag), <em>un balado</em> (podcast). The OQLF (Office québécois de la langue française) is responsible for this.</li>
</ul>
<hr>

<h2 id="h-b2-u19">UNIT 19: EXAM STRATEGIES (DELF/TEFAQ)</h2>

<h3 id="h-b2-19-1">19.1 Listening Comprehension (TEFAQ)</h3>
<p>If you are applying for Quebec immigration, the TEFAQ (Test d'évaluation de français pour l'accès au Québec) is your goal. A B2 score earns you maximum points.</p>
<ul>
<li><strong>Strategy:</strong> Read the questions <em>before</em> the audio starts to anticipate the topic.</li>
<li><strong>Trap:</strong> The audio will often mention numbers or names that are in the wrong answers just to trick you. Listen for synonyms, not exact matches.</li>
</ul>

<h3 id="h-b2-19-2">19.2 Oral Expression</h3>
<p>The DELF B2 involves a 20-minute monologue and debate based on an article.</p>
<ul>
<li><strong>Strategy 1: Plan your structure.</strong> Introduction (hook, source, thesis), Body (2-3 arguments clearly separated by discourse markers), Conclusion.</li>
<li><strong>Strategy 2: Self-correction.</strong> If you make a grammar mistake, correct yourself immediately! (e.g., "Il faut que je fais... pardon, il faut que je fasse"). Examiners reward self-awareness.</li>
<li><strong>Strategy 3: Engage the examiner.</strong> When they challenge you, use concession ("Je comprends votre point de vue, cependant...").</li>
</ul>

<h3 id="h-b2-19-3">19.3 Written Comprehension &amp; Expression</h3>
<ul>
<li><strong>Expression:</strong> You will usually write a formal letter (e.g., to a mayor to complain about a city project). Use formal greetings (Veuillez agréer...), structure your paragraphs, and use the conditional for politeness (Je souhaiterais vous faire part de...).</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Before the Exam:</strong></p>
<p><em>Deux candidats stressent avant l'épreuve orale du TEFAQ.</em></p>
<p>"Je suis tellement nerveux. Et s'ils me posent des questions sur un sujet que je ne connais pas, comme la politique étrangère?"<br>"Ne t'inquiète pas. Ils n'évaluent pas tes connaissances générales, mais ta capacité à argumenter. Si tu manques d'idées, structure bien tes phrases. Utilise des mots de liaison : d'une part, d'autre part..."<br>"Tu as raison. Je vais essayer de placer quelques subjonctifs et un conditionnel passé pour montrer que je maîtrise la grammaire complexe."<br>"Exactement! Et surtout, n'oublie pas de respirer et de parler lentement. Bonne chance!"</p>
<p><em>(Two candidates stress before the TEFAQ oral exam. "I am so nervous. What if they ask me questions on a subject I don't know, like foreign policy?" "Don't worry. They are not evaluating your general knowledge, but your ability to argue. If you lack ideas, structure your sentences well. Use linking words: on the one hand, on the other hand..." "You are right. I will try to throw in a few subjunctives and a past conditional to show that I master complex grammar." "Exactly! And above all, don't forget to breathe and speak slowly. Good luck!")</em></p>

<h3 id="h-b2-19-4">19.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>The TEFAQ audio specifically features <strong>accents from Quebec and France</strong>. You must be comfortable hearing both. Do not rely solely on Parisian audio materials to prepare.</li>
</ul>
<hr>

<h2 id="h-b2-u20">UNIT 20: THE FINAL TEST</h2>

<h3 id="h-b2-20-1">20.1 Oral Debate Simulation</h3>
<p><em>Exercise:</em> Imagine you are arguing with a municipal councilor who wants to cut funding for public libraries. Defend the libraries using:</p>
<ol>
<li>Une concession (Certes...)</li>
<li>Un subjonctif (Il est indispensable que...)</li>
<li>Une phrase passive (Les bibliothèques sont fréquentées par...)</li>
</ol>
<p><em>(Example answer: Certes, le budget de la ville est serré, mais il est indispensable que ces espaces de culture restent ouverts. Elles sont fréquentées quotidiennement par les étudiants et les aînés, et une coupure serait catastrophique pour la cohésion sociale.)</em></p>

<h3 id="h-b2-20-2">20.2 Written Synthesis Practice</h3>
<p>Review the themes we've covered (Education, Environment, Tech, Immigration). Ensure you can write a 250-word letter taking a clear stance on any of these issues using B2-level transitions (En outre, Néanmoins, En définitive).</p>

<h3 id="h-b2-20-3">20.3 Next Steps: Towards C1</h3>
<p>What separates a B2 from a C1 (Advanced)?</p>
<ul>
<li><strong>B2:</strong> You can communicate clearly, argue effectively, and understand most of the news. You make occasional errors but can self-correct.</li>
<li><strong>C1:</strong> You have fluid, spontaneous expression. You understand cultural references, humor, idioms, and fast-paced slang seamlessly. You can read complex literary or academic texts without a dictionary.</li>
</ul>

<h3 id="h-b2-20-4">20.4 Goodbye and Good Luck</h3>
<p>You have reached the end of the Canadian French textbook series! To progress further, you no longer need textbooks. You need immersion. Watch Quebec television (Tou.tv), read La Presse, listen to Radio-Canada, and most importantly, speak with francophones every day.</p>
<hr>

<h1 id="h-b2-conclusion">CONCLUSION</h1>
<p><strong>Félicitations! Toutes nos félicitations!</strong></p>
<p>Reaching the B2 level is the holy grail of language learning. You are now officially fluent enough to immigrate to Quebec, study at a francophone university like l'UdeM or l'UQAM, and hold a professional job entirely in French.</p>
<p>Soyez fiers de votre parcours. Le français est une langue riche, complexe, et parfois frustrante, mais elle ouvre les portes de toute une culture vibrante en Amérique du Nord.</p>
<p><strong>Merci, bravo, et à la prochaine!</strong></p>

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

print(f"B2 COMPLETE. Final file size: {os.path.getsize(OUTPUT)} bytes")
