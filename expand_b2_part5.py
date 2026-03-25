#!/usr/bin/env python3
"""Expand B2 Units 17-20 with more Quebec French content."""

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
    path = r'e:\MyProjects\Web\Jason-French-Learning-Web\b2.html'
    html = read_file(path)

    # =========================================================================
    # UNIT 17: GRAMMAR CAPSTONE
    # =========================================================================
    marker_17_end = '<h2 id="h-b2-u18">'
    new_17 = """
<p><strong>Advanced Pronouns in Quebec (y/en) (🍁):</strong></p>
<p>In Quebec French, the pronouns "y" and "en" are used constantly and sometimes differently than in France.</p>
<ul>
<li><strong>"Y" replacing "lui/leur":</strong> In France, "I talk to him" is "Je <em>lui</em> parle". In casual Quebec French, it becomes "J'<em>y</em> parle". <em>"J'y ai dit de s'en aller." (I told him/her to leave).</em></li>
<li><strong>S'en aller:</strong> To leave. Very common. <em>"Bon, je m'en vais." (Alright, I'm leaving).</em></li>
<li><strong>En arracher:</strong> To have a hard time / struggle. <em>"Il en arrachait à l'école."</em></li>
<li><strong>En avoir ras le bol / plein mon cass' (QC):</strong> To be fed up.</li>
</ul>

<p><strong>Preposition Pitfalls in Spoken Quebec French:</strong></p>
<p>Common preposition shifts (faulty grammar, but widely used):</p>
<ul>
<li><em>Standard:</em> Je vais <strong>chez le</strong> médecin. / <em>Quebec spoken:</em> Je vais <strong>au</strong> médecin.</li>
<li><em>Standard:</em> La voiture <strong>de</strong> mon père. / <em>Quebec spoken:</em> Le char <strong>à</strong> mon père.</li>
</ul>

"""
    html = insert_before(html, marker_17_end, new_17)

    # =========================================================================
    # UNIT 18: VOCAB CAPSTONE
    # =========================================================================
    marker_18_end = '<h2 id="h-b2-u19">'
    new_18 = """
<p><strong>False Friends and Anglicisms (🍁):</strong></p>
<p>Quebec has a complex relationship with English. The government tries to ban anglicisms (e.g., using "courriel" instead of "email"), but colloquial speech is full of english loan words (structured with French grammar).</p>
<table>
<thead><tr><th>Anglicism used in QC</th><th>Standard French equivalent</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td><strong>Une job</strong> (feminine!)</td><td>Un emploi / un travail</td><td>A job</td></tr>
<tr><td><strong>Céduler</strong> (from schedule)</td><td>Planifier / programmer</td><td>To schedule (a meeting)</td></tr>
<tr><td><strong>Être dans le jus</strong></td><td>Être débordé</td><td>To be swamped/busy (in the juice)</td></tr>
<tr><td><strong>Un meeting</strong></td><td>Une réunion</td><td>A meeting (France uses this too)</td></tr>
<tr><td><strong>Canceller</strong></td><td>Annuler</td><td>To cancel</td></tr>
</tbody>
</table>

<p><strong>🇫🇷 Real-Life Scene – A Mixed-Register Conversation:</strong></p>
<p>"Je dois absolument canceller le meeting de ce soir, je suis dans le jus avec mon rapport final."<br>"T'inquiète, je vais céduler ça pour la semaine prochaine. Lâche pas!"<br>"Merci, j'en arrache aujourd'hui. Mon boss m'a donné de la job par-dessus la tête."</p>

"""
    html = insert_before(html, marker_18_end, new_18)

    # =========================================================================
    # UNIT 19: EXAM STRATEGIES
    # =========================================================================
    marker_19_end = '<h2 id="h-b2-u20">'
    new_19 = """
<p><strong>Preparing for the TEFAQ or TCFQ (Quebec Immigration Exams) (🍁):</strong></p>
<p>These exams specifically test your ability to comprehend the Quebec accent and cultural contexts.</p>
<ul>
<li><strong>Listen to different accents:</strong> The exams occasionally feature speakers from Lac-Saint-Jean or Gaspésie, where the accent is thicker and vocalic shifts are more pronounced than in Montreal.</li>
<li><strong>Understand the informal "tu":</strong> TEFAQ oral sections often simulate a conversation with a colleague using "tu" instead of "vous".</li>
<li><strong>Know the geography and institutions:</strong> Role-plays might ask you to convince a friend to visit the Charlevoix region, or explain how to renew a carte maladie at the RAMQ.</li>
</ul>

"""
    html = insert_before(html, marker_19_end, new_19)

    # =========================================================================
    # UNIT 20: THE FINAL TEST
    # =========================================================================
    marker_20_end = '<h1 id="h-b2-conclusion">'
    new_20 = """
<p><strong>B2 Final Test Simulation: The Oral Debate (🍁)</strong></p>
<p>In a DELF B2 or advanced TEFAQ, you will have to sustain a debate for 10-15 minutes.</p>
<p><strong>Prompt:</strong> <em>"Le télétravail devrait devenir la norme pour tous les employés de bureau au Québec afin de réduire la congestion routière et améliorer la conciliation travail-famille."</em></p>
<p><strong>Your Structural Roadmap:</strong></p>
<ol>
<li><strong>Introduction:</strong> Define the context (post-pandemic reality, inflation, traffic in Montreal).</li>
<li><strong>Concession (Certes / Il est vrai que):</strong> Acknowledge that remote work isolates some employees and hurts downtown businesses.</li>
<li><strong>Refutation (Cependant / Néanmoins):</strong> Argue that the environmental and psychological benefits outweigh the economic hit to downtown cores. Use the <em>Subjonctif Présent</em> ("Il est essentiel que le gouvernement s'adapte").</li>
<li><strong>Conclusion (En somme):</strong> Summarize and open a new question (e.g., the 4-day work week).</li>
</ol>

"""
    html = insert_before(html, marker_20_end, new_20)

    # =========================================================================
    # CONCLUSION
    # =========================================================================
    conclusion_marker = '<h1 id="h-b2-conclusion">'
    conclusion_idx = html.find(conclusion_marker)
    if conclusion_idx != -1:
        end_tag = html.find('</h1>', conclusion_idx)
        if end_tag != -1:
            insert_point = end_tag + len('</h1>')
            new_conclusion = """
<p><strong>Félicitations monumentales pour avoir complété le niveau B2 !</strong></p>
<p>At the B2 level, you are no longer just "getting by" in French; you are a fully functioning, independent speaker who can navigate the complexities of Quebec society. You understand the nuances between a formal email to a CEO and a casual hockey debate fueled by <em>Joual</em>. You grasp the significance of Loi 101, the impact of the Quiet Revolution, and the mechanics of the Quebec job market.</p>
<p>You have the linguistic tools to defend your opinions, complain to the OPC, and laugh at a local comedy show. The B2 level is the golden standard required for permanent residency and professional fluency in the province.</p>
<p><strong>Soyez fier/fière de vous ! Mettez votre français en pratique chaque jour. Le Québec vous ouvre les bras !</strong></p>
"""
            html = html[:insert_point] + new_conclusion + html[insert_point:]

    write_file(path, html)
    print("B2 Part 5 done: Units 17-20 and Conclusion expanded successfully!")

if __name__ == '__main__':
    main()
