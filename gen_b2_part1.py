#!/usr/bin/env python3
"""Generate B2 HTML - Part 1: Template + TOC + Units 1-4"""
import os
DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(DIR, "b2.html")
A1 = os.path.join(DIR, "a1.html")

with open(A1, 'r', encoding='utf-8') as f:
    a1 = f.read()
css = a1[a1.index('<style>')+7:a1.index('</style>')]

toc = """
<li><a href="#h-b2-textbook" class="nav-link depth-1">Canadian French B2 Level</a></li>
<li><a href="#h-b2-guide" class="nav-link depth-2">A Comprehensive Guide</a></li>
<li><a href="#h-b2-toc" class="nav-link depth-2">TABLE OF CONTENTS</a></li>
<li><a href="#h-b2-part-i" class="nav-link depth-1">PART I: ADVANCED DISCOURSE</a></li>
<li><a href="#h-b2-u1" class="nav-link depth-2">UNIT 1: SUBJONCTIF PASSÉ</a></li>
<li><a href="#h-b2-1-1" class="nav-link depth-3">1.1 Introduction &amp; Formation</a></li>
<li><a href="#h-b2-1-2" class="nav-link depth-3">1.2 Usage and Concordance</a></li>
<li><a href="#h-b2-1-3" class="nav-link depth-3">1.3 Practice Examples</a></li>
<li><a href="#h-b2-1-4" class="nav-link depth-3">1.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u2" class="nav-link depth-2">UNIT 2: THE PASSIVE VOICE</a></li>
<li><a href="#h-b2-2-1" class="nav-link depth-3">2.1 Advanced Passive Structures</a></li>
<li><a href="#h-b2-2-2" class="nav-link depth-3">2.2 Avoiding the Passive (On, Se)</a></li>
<li><a href="#h-b2-2-3" class="nav-link depth-3">2.3 Use in Media and Formal Texts</a></li>
<li><a href="#h-b2-2-4" class="nav-link depth-3">2.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u3" class="nav-link depth-2">UNIT 3: DISCOURSE MARKERS</a></li>
<li><a href="#h-b2-3-1" class="nav-link depth-3">3.1 Structuring an Argument</a></li>
<li><a href="#h-b2-3-2" class="nav-link depth-3">3.2 Concession &amp; Opposition</a></li>
<li><a href="#h-b2-3-3" class="nav-link depth-3">3.3 Emphasizing a Point</a></li>
<li><a href="#h-b2-3-4" class="nav-link depth-3">3.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u4" class="nav-link depth-2">UNIT 4: NUANCED OPINIONS</a></li>
<li><a href="#h-b2-4-1" class="nav-link depth-3">4.1 Beyond Good and Bad</a></li>
<li><a href="#h-b2-4-2" class="nav-link depth-3">4.2 Expressing Certainty &amp; Doubt</a></li>
<li><a href="#h-b2-4-3" class="nav-link depth-3">4.3 Participating in Debates</a></li>
<li><a href="#h-b2-4-4" class="nav-link depth-3">4.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-part-ii" class="nav-link depth-1">PART II: PROFESSIONAL &amp; ACADEMIC</a></li>
<li><a href="#h-b2-u5" class="nav-link depth-2">UNIT 5: BUSINESS FRENCH</a></li>
<li><a href="#h-b2-5-1" class="nav-link depth-3">5.1 Corporate Vocabulary</a></li>
<li><a href="#h-b2-5-2" class="nav-link depth-3">5.2 Formal Emails</a></li>
<li><a href="#h-b2-5-3" class="nav-link depth-3">5.3 Running a Meeting</a></li>
<li><a href="#h-b2-5-4" class="nav-link depth-3">5.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u6" class="nav-link depth-2">UNIT 6: LAW &amp; RIGHTS</a></li>
<li><a href="#h-b2-6-1" class="nav-link depth-3">6.1 Legal Vocabulary</a></li>
<li><a href="#h-b2-6-2" class="nav-link depth-3">6.2 Understanding Contracts</a></li>
<li><a href="#h-b2-6-3" class="nav-link depth-3">6.3 Civil Rights &amp; Duties</a></li>
<li><a href="#h-b2-6-4" class="nav-link depth-3">6.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u7" class="nav-link depth-2">UNIT 7: SCIENCE &amp; TECH</a></li>
<li><a href="#h-b2-7-1" class="nav-link depth-3">7.1 Scientific Vocabulary</a></li>
<li><a href="#h-b2-7-2" class="nav-link depth-3">7.2 Information Technology</a></li>
<li><a href="#h-b2-7-3" class="nav-link depth-3">7.3 Discussing Innovation</a></li>
<li><a href="#h-b2-7-4" class="nav-link depth-3">7.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u8" class="nav-link depth-2">UNIT 8: HIGHER EDUCATION</a></li>
<li><a href="#h-b2-8-1" class="nav-link depth-3">8.1 Academic Research Terminology</a></li>
<li><a href="#h-b2-8-2" class="nav-link depth-3">8.2 Writing Essays (Dissertations)</a></li>
<li><a href="#h-b2-8-3" class="nav-link depth-3">8.3 Defending a Thesis</a></li>
<li><a href="#h-b2-8-4" class="nav-link depth-3">8.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-part-iii" class="nav-link depth-1">PART III: CULTURE &amp; IDENTITY</a></li>
<li><a href="#h-b2-u9" class="nav-link depth-2">UNIT 9: LITERATURE</a></li>
<li><a href="#h-b2-9-1" class="nav-link depth-3">9.1 Literary Analysis</a></li>
<li><a href="#h-b2-9-2" class="nav-link depth-3">9.2 Classic vs Modern Authors</a></li>
<li><a href="#h-b2-9-3" class="nav-link depth-3">9.3 The Passé Simple</a></li>
<li><a href="#h-b2-9-4" class="nav-link depth-3">9.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u10" class="nav-link depth-2">UNIT 10: CINEMA &amp; MEDIA</a></li>
<li><a href="#h-b2-10-1" class="nav-link depth-3">10.1 Advanced Media Critique</a></li>
<li><a href="#h-b2-10-2" class="nav-link depth-3">10.2 Analyzing Bias in News</a></li>
<li><a href="#h-b2-10-3" class="nav-link depth-3">10.3 Francophone Cinema</a></li>
<li><a href="#h-b2-10-4" class="nav-link depth-3">10.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u11" class="nav-link depth-2">UNIT 11: SOCIAL DEBATES</a></li>
<li><a href="#h-b2-11-1" class="nav-link depth-3">11.1 Immigration &amp; Integration</a></li>
<li><a href="#h-b2-11-2" class="nav-link depth-3">11.2 The Healthcare System</a></li>
<li><a href="#h-b2-11-3" class="nav-link depth-3">11.3 Urban Living vs Rural Life</a></li>
<li><a href="#h-b2-11-4" class="nav-link depth-3">11.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u12" class="nav-link depth-2">UNIT 12: QUEBEC IDENTITY</a></li>
<li><a href="#h-b2-12-1" class="nav-link depth-3">12.1 Language Laws (Loi 101)</a></li>
<li><a href="#h-b2-12-2" class="nav-link depth-3">12.2 The Sovereignist Movement</a></li>
<li><a href="#h-b2-12-3" class="nav-link depth-3">12.3 Cultural Protectionism</a></li>
<li><a href="#h-b2-12-4" class="nav-link depth-3">12.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-part-iv" class="nav-link depth-1">PART IV: MASTERING NUANCE</a></li>
<li><a href="#h-b2-u13" class="nav-link depth-2">UNIT 13: HUMOR &amp; SARCASM</a></li>
<li><a href="#h-b2-13-1" class="nav-link depth-3">13.1 Play on Words &amp; Puns</a></li>
<li><a href="#h-b2-13-2" class="nav-link depth-3">13.2 Irony and Sarcasm</a></li>
<li><a href="#h-b2-13-3" class="nav-link depth-3">13.3 Stand-up Comedy Conventions</a></li>
<li><a href="#h-b2-13-4" class="nav-link depth-3">13.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u14" class="nav-link depth-2">UNIT 14: IDIOMS &amp; SLANG</a></li>
<li><a href="#h-b2-14-1" class="nav-link depth-3">14.2 Advanced Idioms</a></li>
<li><a href="#h-b2-14-2" class="nav-link depth-3">14.3 Familiar and Slang Registers (Argot/Joual)</a></li>
<li><a href="#h-b2-14-3" class="nav-link depth-3">14.4 Swearing Appropriately</a></li>
<li><a href="#h-b2-14-4" class="nav-link depth-3">14.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u15" class="nav-link depth-2">UNIT 15: FORMAL WRITING</a></li>
<li><a href="#h-b2-15-1" class="nav-link depth-3">15.1 La Synthèse (Synthesis)</a></li>
<li><a href="#h-b2-15-2" class="nav-link depth-3">15.2 Le Compte-Rendu (Report)</a></li>
<li><a href="#h-b2-15-3" class="nav-link depth-3">15.3 Complex Sentence Structure</a></li>
<li><a href="#h-b2-15-4" class="nav-link depth-3">15.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u16" class="nav-link depth-2">UNIT 16: PRONUNCIATION</a></li>
<li><a href="#h-b2-16-1" class="nav-link depth-3">16.1 Liaisons (Obligatory vs Optional)</a></li>
<li><a href="#h-b2-16-2" class="nav-link depth-3">16.2 Intonation and Rhythm</a></li>
<li><a href="#h-b2-16-3" class="nav-link depth-3">16.3 Vowel Shifts</a></li>
<li><a href="#h-b2-16-4" class="nav-link depth-3">16.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-part-v" class="nav-link depth-1">PART V: REVIEW</a></li>
<li><a href="#h-b2-u17" class="nav-link depth-2">UNIT 17: GRAMMAR CAPSTONE</a></li>
<li><a href="#h-b2-17-1" class="nav-link depth-3">17.1 The Subjunctive vs Indicative Check</a></li>
<li><a href="#h-b2-17-2" class="nav-link depth-3">17.2 Preposition Pitfalls</a></li>
<li><a href="#h-b2-17-3" class="nav-link depth-3">17.3 Advanced Pronouns (y/en placement)</a></li>
<li><a href="#h-b2-17-4" class="nav-link depth-3">17.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u18" class="nav-link depth-2">UNIT 18: VOCAB CAPSTONE</a></li>
<li><a href="#h-b2-18-1" class="nav-link depth-3">18.1 False Friends (Faux Amis)</a></li>
<li><a href="#h-b2-18-2" class="nav-link depth-3">18.2 Anglicisms</a></li>
<li><a href="#h-b2-18-3" class="nav-link depth-3">18.3 Synonyms for Better Expression</a></li>
<li><a href="#h-b2-18-4" class="nav-link depth-3">18.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u19" class="nav-link depth-2">UNIT 19: EXAM STRATEGIES</a></li>
<li><a href="#h-b2-19-1" class="nav-link depth-3">19.1 Listening Comprehension (TEFAQ)</a></li>
<li><a href="#h-b2-19-2" class="nav-link depth-3">19.2 Oral Expression</a></li>
<li><a href="#h-b2-19-3" class="nav-link depth-3">19.3 Written Comprehension</a></li>
<li><a href="#h-b2-19-4" class="nav-link depth-3">19.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-b2-u20" class="nav-link depth-2">UNIT 20: THE FINAL TEST</a></li>
<li><a href="#h-b2-20-1" class="nav-link depth-3">20.1 Oral Debate Simulation</a></li>
<li><a href="#h-b2-20-2" class="nav-link depth-3">20.2 Written Synthesis Practice</a></li>
<li><a href="#h-b2-20-3" class="nav-link depth-3">20.3 Next Steps: Towards C1</a></li>
<li><a href="#h-b2-20-4" class="nav-link depth-3">20.4 Goodbye and Good Luck</a></li>
<li><a href="#h-b2-conclusion" class="nav-link depth-1">CONCLUSION</a></li>
"""

header = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canadian French B2 Level Complete Textbook</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
{css}
    </style>
</head>
<body>
    <button class="sidebar-toggle" id="sidebarToggle" title="Toggle Menu">
        <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
    </button>
    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <div class="app-container">
        <aside class="sidebar" id="sidebar">
            <div class="sidebar-header">
                <h2>📚 French Journey</h2>
            </div>
            <a href="index.html" class="home-btn">
                <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                    <polyline points="9 22 9 12 15 12 15 22"></polyline>
                </svg>
                Return to Home
            </a>
            <nav class="toc">
                <ul>{toc}</ul>
            </nav>
        </aside>
        <main class="content-area">
            <div class="content-wrapper">

<h1 id="h-b2-textbook">Canadian French B2 Level Complete Textbook</h1>
<h2 id="h-b2-guide">A Comprehensive Guide to Fluency &amp; Nuance</h2>
<hr>
<h2 id="h-b2-toc">TABLE OF CONTENTS</h2>
<p><strong>PART I: ADVANCED DISCOURSE</strong> – Subjonctif Passé, Passive Voice, Discourse Markers, Nuanced Opinions</p>
<p><strong>PART II: PROFESSIONAL &amp; ACADEMIC</strong> – Business, Law, Science, Higher Education</p>
<p><strong>PART III: CULTURE &amp; IDENTITY</strong> – Literature, Cinema, Social Debates, Quebec Identity</p>
<p><strong>PART IV: MASTERING NUANCE</strong> – Humor, Idioms, Formal Writing, Pronunciation</p>
<p><strong>PART V: REVIEW</strong> – Grammar/Vocab Capstone, Exam Strategies</p>
<hr>

<h1 id="h-b2-part-i">PART I: ADVANCED DISCOURSE</h1>

<h2 id="h-b2-u1">UNIT 1: LE SUBJONCTIF PASSÉ (PAST SUBJUNCTIVE)</h2>

<h3 id="h-b2-1-1">1.1 Introduction &amp; Formation</h3>
<p>At the B2 level, expressing emotion or doubt about an event that occurred <em>in the past</em> requires the <strong>subjonctif passé</strong>.</p>
<p><strong>Formation:</strong> Subjonctif présent of être or avoir + past participle.</p>
<ul>
<li><strong>Avoir:</strong> que j'aie parlé, que tu aies fini, qu'il ait vendu.</li>
<li><strong>Être:</strong> que je sois allé(e), qu'elle se soit lavée, que nous soyons partis.</li>
</ul>

<h3 id="h-b2-1-2">1.2 Usage and Concordance</h3>
<p>Use the past subjunctive when the main clause (trigger) is in the present, but the dependent clause refers to a completed past action.</p>
<ul>
<li><strong>Je suis déçu qu'ils n'aient pas gagné le match hier.</strong> (I am disappointed that they did not win the game yesterday.)</li>
<li><strong>Il est dommage que tu sois tombé malade pendant tes vacances.</strong> (It is a shame that you fell sick during your vacation.)</li>
<li><strong>Bien qu'elle ait beaucoup étudié, elle a échoué à l'examen.</strong> (Although she studied a lot, she failed the exam.)</li>
</ul>

<h3 id="h-b2-1-3">1.3 Practice Examples</h3>
<ul>
<li><strong>Je doute qu'il ait lu ce rapport avant la réunion.</strong> (I doubt he read this report before the meeting.)</li>
<li><strong>Le professeur exige que le devoir ait été soumis avant minuit.</strong> (The professor demands that the assignment have been submitted before midnight. - <em>Note the passive past subjunctive here!</em>)</li>
<li><strong>C'est le meilleur film québécois que j'aie jamais vu.</strong> (It is the best Québécois film I have ever seen.) - <em>Superlatives often trigger the subjunctive.</em></li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Discussing a Concluded Project:</strong></p>
<p><em>Deux cadres analysent les résultats décevants du dernier trimestre.</em></p>
<p>"Je suis vraiment contrarié que notre campagne marketing n'ait pas généré les ventes escomptées."<br>"Moi aussi. Je suis étonné que les consommateurs n'aient pas réagi à la promotion."<br>"Il est possible que nous ayons mal ciblé notre clientèle. Bien que l'équipe ait travaillé sans relâche, les résultats ne sont pas là."<br>"Je propose qu'on révise la stratégie. Il faut absolument que nous ayons corrigé le tir avant le mois prochain."</p>
<p><em>(Two executives analyze the disappointing results of the last quarter. "I am really upset that our marketing campaign did not generate the anticipated sales." "Me too. I am surprised that consumers did not react to the promotion." "It is possible that we wrongly targeted our clientele. Although the team worked relentlessly, the results are not there." "I propose we revise the strategy. We absolutely must have corrected our course before next month.")</em></p>

<h3 id="h-b2-1-4">1.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In everyday spoken Quebec French, the subjonctif passé is often replaced by a simpler construction, such as using the indicative: <strong>"Je suis fâché que t'as pas fait la vaisselle."</strong> (Instead of the correct: "que tu n'aies pas fait"). However, at the B2 level, particularly in writing or formal situations, mastering the proper subjunctive is crucial.</li>
</ul>
<hr>

<h2 id="h-b2-u2">UNIT 2: THE PASSIVE VOICE IN DEPTH</h2>

<h3 id="h-b2-2-1">2.1 Advanced Passive Structures</h3>
<p>In B2, you will encounter the passive voice across all tenses, particularly in bureaucratic texts and journalism. <br>
<strong>Formation:</strong> Conjugate <strong>être</strong> in the desired tense + past participle (agreed with the subject).</p>
<ul>
<li><strong>Imparfait:</strong> L'immeuble <strong>était rénové</strong> par la ville. (The building was being renovated by the city.)</li>
<li><strong>Futur:</strong> La décision <strong>sera prise</strong> la semaine prochaine. (The decision will be made next week.)</li>
<li><strong>Conditionnel:</strong> Des mesures plus strictes <strong>seraient adoptées</strong>. (Stricter measures would be adopted.)</li>
<li><strong>Passé Composé:</strong> Le suspect <strong>a été arrêté</strong>. (The suspect was arrested.)</li>
</ul>

<h3 id="h-b2-2-2">2.2 Avoiding the Passive (On, Se)</h3>
<p>French strongly prefers the active voice. Instead of the passive, B2 speakers often use <strong>"On"</strong> or reflexive verbs (la voix pronominale).</p>
<ul>
<li><em>Passive:</em> Cette porte est fermée à 18h.</li>
<li><em>With "On":</em> <strong>On</strong> ferme cette porte à 18h. (They close this door at 6pm.)</li>
<li><em>With "Se":</em> Cette porte <strong>se ferme</strong> à 18h. (This door closes [itself] at 6pm.)</li>
</ul>
<p>Another example:</p>
<ul>
<li><em>Passive:</em> Le français est parlé au Québec.</li>
<li><em>Reflexive:</em> Le français <strong>se parle</strong> au Québec.</li>
</ul>

<h3 id="h-b2-2-3">2.3 Use in Media and Formal Texts</h3>
<p>In news, the passive emphasizes the action rather than the doer:</p>
<ul>
<li><strong>Une entente a été conclue entre le gouvernement et le syndicat tard hier soir. Les détails seront dévoilés demain matin.</strong> (An agreement was reached between the government and the union late last night. The details will be revealed tomorrow morning.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Listening to the Traffic Report:</strong></p>
<p><em>Vous écoutez le bulletin de circulation à ICI Première.</em></p>
<p>"Et maintenant, la circulation: L'autoroute 40 en direction est <strong>a été complètement bloquée</strong> à la hauteur du boulevard Saint-Michel à cause d'un carambolage. Plusieurs véhicules <strong>sont impliqués</strong>. Il <strong>est conseillé</strong> de prendre l'avenue Papineau, bien que celle-ci <strong>soit également congestionnée</strong>."</p>
<p><em>(You are listening to the traffic report on ICI Première. "And now, traffic: Highway 40 Eastbound has been completely blocked near Saint-Michel Boulevard because of a pile-up. Several vehicles are involved. It is advised to take Papineau Avenue, although it is also congested.")</em></p>

<h3 id="h-b2-2-4">2.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>In Quebec journalism, the passive voice is as common as in France. However, pay attention to specific administrative vocabulary. For example, a contract might be <strong>"octroyé"</strong> (granted/awarded) rather than just "donné".</li>
<li><strong>"À la hauteur de"</strong> is a very common spatial expression in Quebec meaning "at the level of" or "near" (often used when giving directions on a highway).</li>
</ul>
<hr>

<h2 id="h-b2-u3">UNIT 3: COMPLEX DISCOURSE MARKERS</h2>

<h3 id="h-b2-3-1">3.1 Structuring a Nuanced Argument</h3>
<p>To pass a B2 exam (like the DELF or TEFAQ), you must string ideas together logically.</p>
<ul>
<li><strong>Pour commencer:</strong> En premier lieu, tout d'abord, à première vue.</li>
<li><strong>Pour ajouter une idée:</strong> De plus, par ailleurs, en outre.</li>
<li><strong>Pour illustrer:</strong> À titre d'exemple, notamment, en d'autres termes.</li>
<li><strong>Pour conclure:</strong> En définitive, tout bien considéré, en somme.</li>
</ul>

<h3 id="h-b2-3-2">3.2 Concession &amp; Opposition</h3>
<p>Concession allows you to acknowledge a counter-argument before refuting it, a hallmark of advanced speech.</p>
<ul>
<li><strong>Bien que / Quoique (+ subjonctif):</strong> Although. <em>Bien qu'il soit cher, ce quartier est idéal.</em></li>
<li><strong>Cependant / Néanmoins / Toutefois:</strong> However / Nevertheless. <em>Il pleuvait; néanmoins, nous sommes sortis.</em></li>
<li><strong>En revanche / Par contre:</strong> On the other hand.</li>
<li><strong>Malgré (+ nom):</strong> Despite. <em>Malgré la grève, les cours ont eu lieu.</em></li>
<li><strong>Certes..., mais...:</strong> Admittedly..., but... <em>Certes, l'intelligence artificielle présente des risques, mais elle offre aussi des opportunités immenses.</em></li>
</ul>

<h3 id="h-b2-3-3">3.3 Emphasizing a Point</h3>
<ul>
<li><strong>Il va de soi que...</strong> (It goes without saying that...)</li>
<li><strong>Il n'en reste pas moins que...</strong> (The fact remains that...)</li>
<li><strong>Quoi qu'il en soit,</strong> (Be that as it may, / Anyway,)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – Defending an Urban Planning Choice:</strong></p>
<p><em>Lors d'une assemblée citoyenne, un élu défend un nouveau parc.</em></p>
<p>"<strong>Certes</strong>, ce projet de réaménagement coûtera cher aux contribuables. <strong>Cependant</strong>, il faut voir cela comme un investissement à long terme. <strong>En effet</strong>, l'ajout d'espaces verts réduira les îlots de chaleur. <strong>Bien que</strong> certains commerçants craignent une perte de stationnement, <strong>il n'en reste pas moins que</strong> la majorité des résidents réclament un milieu de vie plus sain. <strong>En définitive</strong>, l'amélioration de la qualité de vie compensera largement les inconvénients initiaux."</p>
<p><em>(During a town hall meeting, an elected official defends a new park. "Admittedly, this redevelopment project will be expensive for taxpayers. However, we must see this as a long-term investment. Indeed, the addition of green spaces will reduce heat islands. Although some merchants fear a loss of parking, the fact remains that the majority of residents are demanding a healthier living environment. Ultimately, the improvement in quality of life will largely compensate for the initial inconveniences.")</em></p>

<h3 id="h-b2-3-4">3.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li><strong>"Dans le fond"</strong> is widely used in spoken Quebec French as a filler or a concluding discourse marker, meaning "basically," "essentially," or "in the end."</li>
<li><strong>"Par contre"</strong> is used much more frequently than "en revanche" in Quebec.</li>
</ul>
<hr>

<h2 id="h-b2-u4">UNIT 4: EXPRESSING NUANCED OPINIONS</h2>

<h3 id="h-b2-4-1">4.1 Beyond Good and Bad</h3>
<p>At B2, you must evaluate situations with nuance rather than simple approval or disapproval.</p>
<ul>
<li><strong>Je suis partagé(e) sur la question.</strong> (I have mixed feelings on the issue.)</li>
<li><strong>Cette mesure soulève plusieurs interrogations essentielles.</strong> (This measure raises several essential questions.)</li>
<li><strong>D'un côté..., mais de l'autre...</strong> (On one hand..., but on the other...)</li>
<li><strong>Il faut nuancer ce propos.</strong> (We must add nuance to this statement.)</li>
<li><strong>Ce n'est ni tout blanc ni tout noir.</strong> (It's not black and white.)</li>
</ul>

<h3 id="h-b2-4-2">4.2 Expressing Certainty &amp; Doubt</h3>
<p><strong>Certainty (Indicatif):</strong></p>
<ul>
<li>Il est indéniable que (It is undeniable that)</li>
<li>Il est évident que (It is obvious that)</li>
<li>Je suis persuadé(e) que (I am convinced that)</li>
</ul>
<p><strong>Doubt (Subjonctif):</strong></p>
<ul>
<li>Il est peu probable que (It is unlikely that)</li>
<li>Je ne suis pas certain(e) que (I am not sure that)</li>
<li>Il se peut que (It is possible that)</li>
</ul>

<h3 id="h-b2-4-3">4.3 Participating in Debates</h3>
<ul>
<li><strong>Interrupting politely:</strong> <em>Si je peux me permettre, je voudrais ajouter que...</em> (If I may, I would like to add that...)</li>
<li><strong>Asking for clarification:</strong> <em>Pouvez-vous préciser votre pensée?</em> (Can you clarify your thought?)</li>
<li><strong>Refuting an argument:</strong> <em>Je comprends l'idée, mais force est de constater que la réalité est bien différente.</em> (I understand the idea, but it must be noted that reality is quite different.)</li>
</ul>

<p><strong>🇫🇷 Real-Life Scene – A Radio Talk Show (Ligne Ouverte):</strong></p>
<p><em>Un auditeur appelle à la radio pour débattre d'une loi sur la langue.</em></p>
<p>"Bonjour. Écoutez, je suis assez partagé sur ce nouveau projet de loi. <strong>D'un côté</strong>, il est indéniable qu'il faut protéger la langue française au Québec. C'est notre identité. <strong>Mais de l'autre côté</strong>, je ne suis pas certain que contraindre les petites entreprises soit la bonne approche."<br>"Vous pensez donc que le gouvernement va trop loin?" (Animateur)<br>"<strong>Il faut nuancer.</strong> Le gouvernement a raison d'agir, mais <strong>il se pourrait que</strong> cette loi nuise à l'attraction de talents internationaux. <strong>Quoi qu'il en soit</strong>, nous avons besoin d'un vrai débat de société sur la question et non de lois précipitées."</p>
<p><em>(A listener calls the radio to debate a language law. "Hello. Listen, I have mixed feelings about this new bill. On one hand, it is undeniable that we must protect the French language in Quebec. It is our identity. But on the other hand, I am not certain that constraining small businesses is the right approach." "So you think the government is going too far?" (Host) "We must nuance this. The government is right to act, but it could be that this law harms the attraction of international talent. Be that as it may, we need a real societal debate on the issue and not rushed laws.")</em></p>

<h3 id="h-b2-4-4">4.4 Canadian French Notes (🍁)</h3>
<p><strong>Canadian French Note (🍁):</strong></p>
<ul>
<li>Talk radio, or <strong>"les radios d'opinion"</strong> (sometimes critically called "les radios poubelles" if they are sensationalist), is a massive part of Quebec culture, especially in Quebec City.</li>
<li>Debating politics and language rights is a favorite pastime in Quebec society. Being able to formulate balanced, nuanced arguments (using "d'un côté," "de l'autre") is the key to participating in these passionate discussions effectively.</li>
</ul>
"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(header)

print(f"B2 Part 1 (Template + Units 1-4) done. File size: {os.path.getsize(OUTPUT)} bytes")
