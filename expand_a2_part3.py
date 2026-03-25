#!/usr/bin/env python3
"""Expand A2 Units 11-16 with more Quebec French content."""

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
    # UNIT 11: GIVING INSTRUCTIONS & ADVICE
    # =========================================================================

    marker_11_end = '<h2 id="h-unit-12-comparisons">'
    new_11 = """
<p><strong>The Impératif – Extended Conjugation (🍁):</strong></p>
<p>The imperative is essential for recipes, instructions, and giving advice. Here's a comprehensive review:</p>
<table>
<thead><tr><th>Verb</th><th>Tu form</th><th>Nous form</th><th>Vous form</th><th>Example</th></tr></thead>
<tbody>
<tr><td>parler</td><td>Parle!</td><td>Parlons!</td><td>Parlez!</td><td>"Parle plus fort!" (Speak louder!)</td></tr>
<tr><td>finir</td><td>Finis!</td><td>Finissons!</td><td>Finissez!</td><td>"Finis tes devoirs!" (Finish your homework!)</td></tr>
<tr><td>venir</td><td>Viens!</td><td>Venons!</td><td>Venez!</td><td>"Viens icitte!" (Come here! – QC)</td></tr>
<tr><td>prendre</td><td>Prends!</td><td>Prenons!</td><td>Prenez!</td><td>"Prends ton manteau!" (Take your coat!)</td></tr>
<tr><td>aller</td><td>Va!</td><td>Allons!</td><td>Allez!</td><td>"Va-t'en!" (Go away!)</td></tr>
<tr><td>être</td><td>Sois!</td><td>Soyons!</td><td>Soyez!</td><td>"Sois patient!" (Be patient!)</td></tr>
<tr><td>avoir</td><td>Aie!</td><td>Ayons!</td><td>Ayez!</td><td>"Aie pas peur!" (Don't be afraid! – QC drops "n'aie")</td></tr>
<tr><td>savoir</td><td>Sache!</td><td>Sachons!</td><td>Sachez!</td><td>"Sache que c'est important." (Know that it's important.)</td></tr>
</tbody>
</table>
<p><strong>Imperative with Pronouns:</strong></p>
<table>
<thead><tr><th>Positive</th><th>Translation</th><th>Negative</th><th>Translation</th></tr></thead>
<tbody>
<tr><td>Donne-le-moi!</td><td>Give it to me!</td><td>Ne me le donne pas!</td><td>Don't give it to me!</td></tr>
<tr><td>Dis-lui!</td><td>Tell him/her!</td><td>Ne lui dis pas!</td><td>Don't tell him/her!</td></tr>
<tr><td>Fais-le!</td><td>Do it!</td><td>Fais-le pas! (QC)</td><td>Don't do it!</td></tr>
<tr><td>Vas-y!</td><td>Go for it!</td><td>Vas-y pas!</td><td>Don't go!</td></tr>
</tbody>
</table>
<p><strong>Quebec Advice Expressions (🍁):</strong></p>
<table>
<thead><tr><th>Quebec Expression</th><th>English</th><th>When to Use</th></tr></thead>
<tbody>
<tr><td>Tu devrais...</td><td>You should...</td><td>"Tu devrais apprendre le français." (You should learn French.)</td></tr>
<tr><td>Si j'étais toi, je...</td><td>If I were you, I would...</td><td>"Si j'étais toi, j'irais au CLSC." (If I were you, I'd go to the CLSC.)</td></tr>
<tr><td>Faudrait que tu...</td><td>You'd need to...</td><td>"Faudrait que tu voies un docteur." (You should see a doctor.)</td></tr>
<tr><td>Je te conseille de...</td><td>I advise you to...</td><td>"Je te conseille de prendre un manteau." (I advise you to take a coat.)</td></tr>
<tr><td>À ta place, je...</td><td>In your place, I would...</td><td>"À ta place, je changerais de job." (In your place, I'd change jobs.)</td></tr>
<tr><td>C'est mieux de...</td><td>It's better to...</td><td>"C'est mieux de pas sortir quand y fait tempête." (It's better not to go out when there's a storm.)</td></tr>
</tbody>
</table>
<p><strong>Quebec Recipe – La Tourtière (Step-by-Step Instructions) (🍁):</strong></p>
<p>Here's a traditional Quebec tourtière recipe using imperative and instructional French:</p>
<ol>
<li><strong>Mélangez</strong> une livre de porc haché, une demi-livre de bœuf haché et une demi-livre de veau haché dans un grand chaudron. (Mix one pound of ground pork, half a pound of ground beef, and half a pound of ground veal in a large pot.)</li>
<li><strong>Ajoutez</strong> un oignon haché finement, deux gousses d'ail, du sel, du poivre, du clou de girofle et de la cannelle. (Add a finely chopped onion, two garlic cloves, salt, pepper, cloves, and cinnamon.)</li>
<li><strong>Versez</strong> une tasse d'eau et <strong>faites cuire</strong> à feu moyen pendant trente minutes en brassant souvent. (Pour in one cup of water and cook over medium heat for thirty minutes, stirring often.)</li>
<li><strong>Ajoutez</strong> deux pommes de terre râpées pour épaissir le mélange. <strong>Laissez refroidir.</strong> (Add two grated potatoes to thicken the mixture. Let cool.)</li>
<li><strong>Préchauffez</strong> le four à 200°C (400°F). (Preheat the oven to 200°C/400°F.)</li>
<li><strong>Remplissez</strong> une croûte à tarte avec la viande et <strong>couvrez</strong> avec la croûte du dessus. (Fill a pie crust with the meat and cover with the top crust.)</li>
<li><strong>Faites cuire</strong> au four pendant quarante-cinq minutes ou jusqu'à ce que la croûte soit dorée. (Bake for forty-five minutes or until the crust is golden.)</li>
<li><strong>Servez</strong> avec du ketchup aux fruits maison! (Serve with homemade fruit ketchup!)</li>
</ol>
<p><strong>Important Recipe Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>mélanger / brasser (QC)</td><td>to mix / to stir</td></tr>
<tr><td>ajouter</td><td>to add</td></tr>
<tr><td>verser</td><td>to pour</td></tr>
<tr><td>faire cuire / cuire</td><td>to cook</td></tr>
<tr><td>hacher</td><td>to chop / to mince</td></tr>
<tr><td>râper</td><td>to grate</td></tr>
<tr><td>couper</td><td>to cut</td></tr>
<tr><td>préchauffer le four</td><td>to preheat the oven</td></tr>
<tr><td>laisser refroidir</td><td>to let cool</td></tr>
<tr><td>servir</td><td>to serve</td></tr>
<tr><td>assaisonner</td><td>to season</td></tr>
<tr><td>le chaudron (QC) / la casserole</td><td>pot</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – A Mother Giving Instructions Before Leaving:</strong></p>
<p><em>Maman part travailler et donne des instructions aux enfants.</em></p>
<p>"Bon, j'pars travailler. Écoutez bien! D'abord, finissez vos devoirs avant de jouer aux jeux vidéo. Deuxièmement, faites pas de dégât dans la cuisine. Si vous avez faim, mangez les fruits sur le comptoir."<br>"Oui maman!"<br>"Pis fais attention au poêle, touche pas ça! Si vous avez besoin de quelque chose, appelez-moi au bureau. Le numéro est sur le frigo."<br>"D'accord, on va être sages!"<br>"J'espère bien! Pis sortez pas dehors, y fait trop frette. Je reviens vers cinq heures. Soyez gentils, lâchez pas!"</p>
<p><em>(Mom is leaving for work and giving instructions to the kids. "Okay, I'm going to work. Listen carefully! First, finish your homework before playing video games. Second, don't make a mess in the kitchen. If you're hungry, eat the fruit on the counter." "Yes Mom!" "And be careful with the stove, don't touch it! If you need something, call me at the office. The number is on the fridge." "Okay, we'll be good!" "I hope so! And don't go outside, it's too cold. I'll be back around five. Be good, hang in there!")</em></p>

"""
    html = insert_before(html, marker_11_end, new_11)

    # =========================================================================
    # UNIT 12: COMPARISONS & SUPERLATIVES
    # =========================================================================

    marker_12_end = '<h1 id="h-part-iv-health">'
    new_12 = """
<p><strong>Comparison Structures – Complete Guide:</strong></p>
<table>
<thead><tr><th>Type</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>More... than</td><td>plus + adj. + que</td><td>"Montréal est plus grande que Québec." (Montreal is bigger than Quebec City.)</td></tr>
<tr><td>Less... than</td><td>moins + adj. + que</td><td>"L'été est moins long que je voudrais." (Summer is shorter than I'd like.)</td></tr>
<tr><td>As... as</td><td>aussi + adj. + que</td><td>"Le sirop d'érable est aussi bon qu'avant." (Maple syrup is as good as before.)</td></tr>
<tr><td>More (quantity)</td><td>plus de + noun + que</td><td>"Y'a plus de neige à Québec qu'à Montréal." (There's more snow in QC City than Montreal.)</td></tr>
<tr><td>Less (quantity)</td><td>moins de + noun + que</td><td>"Y'a moins de trafic qu'hier." (There's less traffic than yesterday.)</td></tr>
<tr><td>As much/many</td><td>autant de + noun + que</td><td>"Y'a autant de restaurants qu'à Paris!" (There are as many restaurants as in Paris!)</td></tr>
</tbody>
</table>
<p><strong>Superlatives – Complete Guide:</strong></p>
<table>
<thead><tr><th>Type</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>The most</td><td>le/la/les plus + adj.</td><td>"C'est la plus belle ville du Québec." (It's the most beautiful city in Quebec.)</td></tr>
<tr><td>The least</td><td>le/la/les moins + adj.</td><td>"C'est le mois le moins froid." (It's the least cold month.)</td></tr>
<tr><td>The best</td><td>le/la/les meilleur(e)(s)</td><td>"C'est la meilleure poutine en ville!" (It's the best poutine in town!)</td></tr>
<tr><td>The worst</td><td>le/la/les pire(s)</td><td>"C'est la pire tempête de l'hiver." (It's the worst storm of the winter.)</td></tr>
</tbody>
</table>
<p><strong>Comparing Quebec's Regions:</strong></p>
<table>
<thead><tr><th>Comparison</th><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>Size</td><td>Montréal est plus peuplée que Québec, mais Québec est plus ancienne.</td><td>Montreal is more populated than Quebec City, but Quebec City is older.</td></tr>
<tr><td>Weather</td><td>Il fait plus froid à Québec qu'à Montréal en hiver.</td><td>It's colder in Quebec City than Montreal in winter.</td></tr>
<tr><td>Nature</td><td>La Gaspésie est la plus belle région pour la nature.</td><td>The Gaspé is the most beautiful region for nature.</td></tr>
<tr><td>Cost</td><td>Montréal est moins chère que Toronto mais plus chère que Sherbrooke.</td><td>Montreal is cheaper than Toronto but more expensive than Sherbrooke.</td></tr>
<tr><td>Bilingualism</td><td>Montréal est plus bilingue que Québec ou Saguenay.</td><td>Montreal is more bilingual than Quebec City or Saguenay.</td></tr>
<tr><td>Food</td><td>Le Lac-Saint-Jean a les meilleurs bleuets du monde!</td><td>Lac-Saint-Jean has the best blueberries in the world!</td></tr>
</tbody>
</table>
<p><strong>Quebec Comparison Expressions (🍁):</strong></p>
<table>
<thead><tr><th>Expression</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>C'est ben mieux!</td><td>It's much better!</td><td>"Le nouveau resto est ben mieux que l'ancien."</td></tr>
<tr><td>C'est pas mal pire.</td><td>It's quite a bit worse.</td><td>"La météo est pas mal pire que prévu."</td></tr>
<tr><td>Y'a rien de mieux que...</td><td>There's nothing better than...</td><td>"Y'a rien de mieux qu'une poutine à trois heures du matin!"</td></tr>
<tr><td>C'est pas comparable!</td><td>There's no comparison!</td><td>"Le sirop d'érable du Québec pis celui des É.-U.? C'est pas comparable!"</td></tr>
<tr><td>De loin...</td><td>By far...</td><td>"C'est de loin le meilleur restaurant en ville."</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Debating the Best Poutine in Montreal:</strong></p>
<p><em>Vous et vos amis débattez sur la meilleure poutine à Montréal.</em></p>
<p>"La meilleure poutine à Montréal, c'est chez La Banquise! Y'a rien de mieux!"<br>"Ben voyons! La Banquise, c'est bon, mais c'est touristique. La poutine chez Patati Patata est ben meilleure, pis c'est moins cher."<br>"Moins cher, peut-être, mais les portions sont plus petites!"<br>"Moi, je trouve que la poutine au Dirty Dogs est aussi bonne que La Banquise, pis y'a moins d'attente."<br>"En tout cas, la pire poutine, c'est celle de la cafétéria du bureau. C'est même pas des vrais fromages en grains!"<br>"C'est vrai! Le fromage en grains, c'est le plus important. Si y fait pas 'squick-squick', c'est pas une vraie poutine!"<br>"Mettons qu'on est tous d'accord pour dire que la poutine québécoise est la meilleure au monde!"<br>"Mets-en!"</p>
<p><em>(You and your friends debate the best poutine in Montreal. "The best poutine in Montreal is at La Banquise! Nothing's better!" "Come on! La Banquise is good, but it's touristy. The poutine at Patati Patata is much better, and it's cheaper." "Cheaper, maybe, but the portions are smaller!" "I think the poutine at Dirty Dogs is as good as La Banquise, and there's less of a wait." "Anyway, the worst poutine is the one from the office cafeteria. They don't even use real cheese curds!" "True! The cheese curds are the most important. If they don't squeak, it's not real poutine!" "Let's say we all agree that Quebec poutine is the best in the world!" "Absolutely!")</em></p>

"""
    html = insert_before(html, marker_12_end, new_12)

    # =========================================================================
    # UNIT 13: BODY & HEALTH
    # =========================================================================

    marker_13_end = '<h2 id="h-unit-14-doctor">'
    new_13 = """
<p><strong>Extended Body Parts Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>la tête</td><td>head</td><td>le cou</td><td>neck</td></tr>
<tr><td>les cheveux</td><td>hair</td><td>l'épaule (f.)</td><td>shoulder</td></tr>
<tr><td>le front</td><td>forehead</td><td>le bras</td><td>arm</td></tr>
<tr><td>l'œil (m.) / les yeux</td><td>eye / eyes</td><td>le coude</td><td>elbow</td></tr>
<tr><td>le nez</td><td>nose</td><td>le poignet</td><td>wrist</td></tr>
<tr><td>la bouche</td><td>mouth</td><td>la main</td><td>hand</td></tr>
<tr><td>les lèvres</td><td>lips</td><td>le doigt</td><td>finger</td></tr>
<tr><td>les dents</td><td>teeth</td><td>le pouce</td><td>thumb</td></tr>
<tr><td>la langue</td><td>tongue</td><td>l'ongle (m.)</td><td>nail</td></tr>
<tr><td>l'oreille (f.)</td><td>ear</td><td>la poitrine</td><td>chest</td></tr>
<tr><td>la joue</td><td>cheek</td><td>le ventre</td><td>belly/stomach</td></tr>
<tr><td>le menton</td><td>chin</td><td>le dos</td><td>back</td></tr>
<tr><td>la jambe</td><td>leg</td><td>la hanche</td><td>hip</td></tr>
<tr><td>le genou</td><td>knee</td><td>la cuisse</td><td>thigh</td></tr>
<tr><td>la cheville</td><td>ankle</td><td>le pied</td><td>foot</td></tr>
<tr><td>l'orteil (m.)</td><td>toe</td><td>le talon</td><td>heel</td></tr>
</tbody>
</table>
<p><strong>Describing Symptoms – Complete Guide:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>J'ai mal à la tête.</td><td>I have a headache.</td><td>"J'ai mal à la tête depuis ce matin."</td></tr>
<tr><td>J'ai mal au ventre.</td><td>I have a stomachache.</td><td>"J'ai mal au ventre, j'ai trop mangé."</td></tr>
<tr><td>J'ai mal à la gorge.</td><td>I have a sore throat.</td><td>"J'ai mal à la gorge pis j'tousse."</td></tr>
<tr><td>J'ai mal au dos.</td><td>My back hurts.</td><td>"J'ai mal au dos parce que j'ai pelleté."</td></tr>
<tr><td>J'ai de la fièvre.</td><td>I have a fever.</td><td>"J'ai de la fièvre, trente-neuf degrés."</td></tr>
<tr><td>Je tousse.</td><td>I'm coughing.</td><td>"Je tousse depuis trois jours."</td></tr>
<tr><td>J'éternue.</td><td>I'm sneezing.</td><td>"J'arrête pas d'éternuer."</td></tr>
<tr><td>J'ai le nez bouché.</td><td>My nose is blocked.</td><td>"J'ai le nez bouché, je respire mal."</td></tr>
<tr><td>J'ai le nez qui coule.</td><td>My nose is running.</td><td>"J'ai le nez qui coule tout le temps."</td></tr>
<tr><td>J'ai des nausées.</td><td>I'm nauseous.</td><td>"J'ai des nausées depuis hier."</td></tr>
<tr><td>J'ai des frissons.</td><td>I have chills.</td><td>"J'ai des frissons, je pense que j'ai la grippe."</td></tr>
<tr><td>Je suis étourdi(e).</td><td>I'm dizzy.</td><td>"Je suis étourdie quand je me lève vite."</td></tr>
<tr><td>Je me suis blessé(e).</td><td>I injured myself.</td><td>"Je me suis blessé au genou en jouant au hockey."</td></tr>
<tr><td>Je me suis foulé la cheville.</td><td>I sprained my ankle.</td><td>"Je me suis foulé la cheville sur la glace."</td></tr>
</tbody>
</table>
<p><strong>Quebec Healthcare System – Essential Information (🍁):</strong></p>
<table>
<thead><tr><th>Term</th><th>Full Name</th><th>Description</th></tr></thead>
<tbody>
<tr><td>RAMQ</td><td>Régie de l'assurance maladie du Québec</td><td>Quebec's public health insurance. Every resident must have a carte d'assurance maladie (health card).</td></tr>
<tr><td>CLSC</td><td>Centre local de services communautaires</td><td>Community health clinic – first stop for non-emergency care, vaccinations, mental health.</td></tr>
<tr><td>Urgence</td><td>L'urgence de l'hôpital</td><td>Emergency room. Warning: wait times can be very long (4-12+ hours)!</td></tr>
<tr><td>Clinique sans rendez-vous</td><td>Walk-in clinic</td><td>"J'ai été à la clinique sans rendez-vous." (I went to the walk-in clinic.)</td></tr>
<tr><td>Médecin de famille</td><td>Family doctor</td><td>Many Quebecers don't have one. You can register on a waiting list at the GAMF.</td></tr>
<tr><td>Info-Santé 811</td><td>Health info line</td><td>"Appelle le 811 si t'es pas sûr." (Call 811 if you're not sure.)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Feeling Sick and Calling Info-Santé:</strong></p>
<p><em>Vous vous sentez mal et vous appelez Info-Santé 811.</em></p>
<p>"Info-Santé, bonjour!"<br>"Bonjour, j'appelle parce que je file pas ben pantoute depuis hier soir."<br>"D'accord. Quels sont vos symptômes?"<br>"J'ai mal à la gorge, j'tousse beaucoup, pis j'ai de la fièvre. Je pense que c'est la grippe."<br>"Avez-vous pris votre température?"<br>"Oui, trente-neuf degrés."<br>"Avez-vous des difficultés à respirer?"<br>"Non, juste le nez bouché, mais je respire correct par la bouche."<br>"D'accord. Je vous conseille de rester à la maison, de boire beaucoup de liquides, de prendre du Tylenol pour la fièvre et de vous reposer."<br>"Est-ce que je devrais aller à l'urgence?"<br>"Pas pour l'instant. Mais si votre fièvre monte au-dessus de quarante degrés ou si vous avez de la difficulté à respirer, allez à l'urgence. Autrement, essayez de voir un médecin dans les prochains jours."<br>"Merci beaucoup! Bonne soirée!"</p>
<p><em>(You're feeling sick and call Info-Santé 811. "Hello, I'm calling because I haven't been feeling well at all since yesterday evening." "Okay. What are your symptoms?" "I have a sore throat, I'm coughing a lot, and I have a fever. I think it's the flu." "Did you take your temperature?" "Yes, 39 degrees." "Are you having difficulty breathing?" "No, just a stuffy nose, but I can breathe fine through my mouth." "Okay. I advise you to stay home, drink plenty of fluids, take Tylenol for the fever, and rest." "Should I go to the emergency room?" "Not right now. But if your fever goes above 40 degrees or if you have difficulty breathing, go to the ER. Otherwise, try to see a doctor in the next few days.")</em></p>

"""
    html = insert_before(html, marker_13_end, new_13)

    # =========================================================================
    # UNIT 14: AT THE DOCTOR & PHARMACY
    # =========================================================================

    marker_14_end = '<h2 id="h-unit-15-banking">'
    new_14 = """
<p><strong>At the Doctor – Complete Dialogue Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Who Says It</th></tr></thead>
<tbody>
<tr><td>Qu'est-ce qui vous amène aujourd'hui?</td><td>What brings you in today?</td><td>Doctor</td></tr>
<tr><td>Depuis quand avez-vous ces symptômes?</td><td>How long have you had these symptoms?</td><td>Doctor</td></tr>
<tr><td>Où avez-vous mal exactement?</td><td>Where does it hurt exactly?</td><td>Doctor</td></tr>
<tr><td>Est-ce que vous prenez des médicaments?</td><td>Are you taking any medication?</td><td>Doctor</td></tr>
<tr><td>Avez-vous des allergies?</td><td>Do you have any allergies?</td><td>Doctor</td></tr>
<tr><td>Ouvrez la bouche et dites "Ah".</td><td>Open your mouth and say "Ah".</td><td>Doctor</td></tr>
<tr><td>Respirez profondément.</td><td>Breathe deeply.</td><td>Doctor</td></tr>
<tr><td>Je vais vous prescrire...</td><td>I'm going to prescribe you...</td><td>Doctor</td></tr>
<tr><td>Prenez deux comprimés trois fois par jour.</td><td>Take two tablets three times a day.</td><td>Doctor</td></tr>
<tr><td>Revenez me voir si ça ne s'améliore pas.</td><td>Come back to see me if it doesn't improve.</td><td>Doctor</td></tr>
</tbody>
</table>
<p><strong>At the Pharmacy – Essential Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>une ordonnance / une prescription</td><td>a prescription</td><td>"J'ai une ordonnance du docteur."</td></tr>
<tr><td>un médicament</td><td>a medication</td><td>"C'est un médicament sur ordonnance."</td></tr>
<tr><td>un comprimé / une pilule</td><td>a tablet / a pill</td><td>"Prenez un comprimé le matin."</td></tr>
<tr><td>un sirop</td><td>a syrup</td><td>"Un sirop contre la toux."</td></tr>
<tr><td>les gouttes</td><td>drops</td><td>"Des gouttes pour les yeux."</td></tr>
<tr><td>une crème</td><td>a cream</td><td>"Une crème pour les mains sèches."</td></tr>
<tr><td>un pansement</td><td>a bandage</td><td>"J'ai besoin de pansements."</td></tr>
<tr><td>du Tylenol / de l'acétaminophène</td><td>Tylenol / acetaminophen</td><td>"Tu peux prendre du Tylenol."</td></tr>
<tr><td>de l'Advil / de l'ibuprofène</td><td>Advil / ibuprofen</td><td>"L'Advil, c'est bon pour l'inflammation."</td></tr>
<tr><td>un thermomètre</td><td>a thermometer</td><td>"On a-tu un thermomètre à la maison?"</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – At the Doctor's Office (CLSC):</strong></p>
<p><em>Vous avez rendez-vous au CLSC pour votre enfant qui est malade.</em></p>
<p>"Bonjour madame! Qu'est-ce qui amène le petit aujourd'hui?"<br>"Bonjour docteur. Mon garçon tousse depuis quatre jours pis y a de la fièvre par moments."<br>"D'accord. Quel âge a-t-il?"<br>"Y a six ans."<br>"Bon, je vais regarder ça. Ouvre la bouche, mon bonhomme, et dis 'Ah'."<br>[Le docteur examine l'enfant.]<br>"Ses amygdales sont un peu enflées. C'est probablement une infection virale. C'est pas une angine bactérienne."<br>"Est-ce qu'y a besoin d'antibiotiques?"<br>"Non, les antibiotiques ne fonctionnent pas contre les virus. Donnez-lui du Tylenol pour enfants pour la fièvre, beaucoup de liquides, et laissez-le se reposer."<br>"Combien de Tylenol?"<br>"Selon son poids... il pèse combien?"<br>"Vingt-deux kilos."<br>"Alors, cinq millilitres de Tylenol liquide, aux quatre à six heures si nécessaire. Revenez si la fièvre dure plus d'une semaine ou s'il a de la difficulté à avaler."<br>"Merci beaucoup, docteur!"</p>

"""
    html = insert_before(html, marker_14_end, new_14)

    # =========================================================================
    # UNIT 15: BANKING & ADMINISTRATIVE TASKS
    # =========================================================================

    marker_15_end = '<h2 id="h-unit-16-emergencies">'
    new_15 = """
<p><strong>Quebec Banking – Desjardins & the Caisse Populaire (🍁):</strong></p>
<p>Desjardins is Quebec's cooperative financial institution, deeply embedded in Quebec culture:</p>
<table>
<thead><tr><th>French</th><th>English</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>la caisse populaire / la caisse Desjardins</td><td>credit union</td><td>The most common financial institution in QC (outside Montreal)</td></tr>
<tr><td>un compte chèques</td><td>a chequing account</td><td>"J'ai ouvert un compte chèques chez Desjardins."</td></tr>
<tr><td>un compte épargne</td><td>a savings account</td><td>"Je mets de l'argent dans mon compte épargne chaque mois."</td></tr>
<tr><td>un REER</td><td>RRSP (registered retirement savings plan)</td><td>"Faut que je cotise à mon REER avant le premier mars."</td></tr>
<tr><td>un CELI</td><td>TFSA (tax-free savings account)</td><td>"Le CELI, c'est bon pour épargner sans payer d'impôt."</td></tr>
<tr><td>un prêt hypothécaire</td><td>a mortgage</td><td>"Notre hypothèque est de trois cent mille."</td></tr>
<tr><td>le taux d'intérêt</td><td>the interest rate</td><td>"Le taux d'intérêt est à combien?"</td></tr>
<tr><td>un virement</td><td>a transfer</td><td>"J'ai fait un virement Interac."</td></tr>
<tr><td>un chèque</td><td>a cheque</td><td>"J'ai déposé mon chèque au guichet."</td></tr>
<tr><td>un relevé de compte</td><td>a bank statement</td><td>"J'ai vérifié mon relevé de compte en ligne."</td></tr>
</tbody>
</table>
<p><strong>Quebec Government Administrative Tasks (🍁):</strong></p>
<table>
<thead><tr><th>Task</th><th>Where</th><th>Key Vocabulary</th></tr></thead>
<tbody>
<tr><td>Get/renew driver's license</td><td>SAAQ</td><td>"Renouveler mon permis de conduire à la SAAQ"</td></tr>
<tr><td>Get health insurance card</td><td>RAMQ</td><td>"Demander ma carte d'assurance maladie"</td></tr>
<tr><td>File income taxes</td><td>Revenu Québec + ARC</td><td>"Faire mes impôts avant le 30 avril"</td></tr>
<tr><td>Register to vote</td><td>DGEQ (Directeur général des élections)</td><td>"M'inscrire sur la liste électorale"</td></tr>
<tr><td>Apply for a SIN</td><td>Service Canada</td><td>"Obtenir mon numéro d'assurance sociale (NAS)"</td></tr>
<tr><td>Register a car</td><td>SAAQ</td><td>"Immatriculer mon véhicule"</td></tr>
<tr><td>French course (immigrants)</td><td>MIFI</td><td>"M'inscrire en francisation"</td></tr>
<tr><td>Apply for citizenship</td><td>IRCC</td><td>"Faire ma demande de citoyenneté"</td></tr>
</tbody>
</table>
<p><strong>Tax Season Vocabulary (🍁):</strong></p>
<table>
<thead><tr><th>French</th><th>English</th></tr></thead>
<tbody>
<tr><td>les impôts</td><td>taxes / income tax</td></tr>
<tr><td>la déclaration de revenus</td><td>tax return</td></tr>
<tr><td>le remboursement d'impôt</td><td>tax refund</td></tr>
<tr><td>le feuillet T4 / Relevé 1</td><td>T4 slip / RL-1 slip (employment income)</td></tr>
<tr><td>un comptable</td><td>an accountant</td></tr>
<tr><td>la date limite</td><td>the deadline</td></tr>
<tr><td>Revenu Québec</td><td>Quebec tax agency</td></tr>
<tr><td>l'Agence du revenu du Canada (ARC)</td><td>Canada Revenue Agency (CRA)</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Opening a Bank Account at Desjardins:</strong></p>
<p><em>Vous ouvrez un compte chez Desjardins.</em></p>
<p>"Bonjour! Je voudrais ouvrir un compte, s'il vous plaît."<br>"Bien sûr! Bienvenue chez Desjardins. Est-ce votre premier compte ici?"<br>"Oui, j'suis nouveau au Québec. J'ai besoin d'un compte chèques et d'un compte épargne."<br>"Parfait! J'aurais besoin de deux pièces d'identité. Avez-vous votre passeport et une preuve d'adresse?"<br>"Oui, voici mon passeport et ma facture d'Hydro-Québec."<br>"Excellent! On va ouvrir un forfait Bon Départ, c'est gratuit pour les nouveaux arrivants. Ça inclut un compte chèques avec une carte de débit Interac, un compte épargne, et l'accès en ligne."<br>"Est-ce que je peux aussi avoir une carte de crédit?"<br>"Avec Desjardins, on peut vous offrir une carte de crédit garantie pour commencer. Après six mois, on pourra évaluer votre dossier pour une carte régulière."<br>"Merci! C'est vraiment utile!"</p>

"""
    html = insert_before(html, marker_15_end, new_15)

    # =========================================================================
    # UNIT 16: EMERGENCY SITUATIONS
    # =========================================================================

    marker_16_end = '<h1 id="h-part-v-travel">'
    new_16 = """
<p><strong>Emergency Numbers in Quebec (🍁):</strong></p>
<table>
<thead><tr><th>Number</th><th>Service</th><th>When to Call</th></tr></thead>
<tbody>
<tr><td>911</td><td>Police, Fire, Ambulance</td><td>Immediate danger, fire, medical emergency, crime in progress</td></tr>
<tr><td>811</td><td>Info-Santé / Info-Social</td><td>Health advice, non-emergency health questions</td></tr>
<tr><td>310-4141</td><td>SQ (Sûreté du Québec)</td><td>Provincial police for highways and rural areas</td></tr>
<tr><td>1-800-361-5813</td><td>Centre antipoison</td><td>Poison control</td></tr>
<tr><td>1-866-APPELLE</td><td>Suicide prevention line</td><td>Crisis support</td></tr>
<tr><td>511</td><td>Road conditions</td><td>Highway info, closures, construction</td></tr>
</tbody>
</table>
<p><strong>Calling 911 in French – What to Say:</strong></p>
<table>
<thead><tr><th>Situation</th><th>What to Say</th></tr></thead>
<tbody>
<tr><td>Identify the emergency</td><td>"J'ai besoin d'une ambulance / de la police / des pompiers."</td></tr>
<tr><td>Give your location</td><td>"Je suis au [adresse]. C'est au coin de [rue] et [rue]."</td></tr>
<tr><td>Describe what happened</td><td>"Y'a eu un accident de voiture." / "Quelqu'un est tombé." / "Y'a un feu."</td></tr>
<tr><td>Number of people involved</td><td>"Y'a deux personnes blessées."</td></tr>
<tr><td>Person's condition</td><td>"Y est conscient mais y saigne beaucoup." / "A respire pas."</td></tr>
<tr><td>Stay on the line</td><td>"Oui, je reste en ligne." (Yes, I'll stay on the line.)</td></tr>
</tbody>
</table>
<p><strong>Accident & Emergency Vocabulary:</strong></p>
<table>
<thead><tr><th>French</th><th>English</th><th>Example</th></tr></thead>
<tbody>
<tr><td>un accident de voiture</td><td>a car accident</td><td>"Y'a eu un accident sur l'autoroute 15."</td></tr>
<tr><td>une blessure</td><td>an injury</td><td>"C'est une blessure grave."</td></tr>
<tr><td>un incendie / un feu</td><td>a fire</td><td>"Y'a un feu dans l'immeuble!"</td></tr>
<tr><td>une inondation</td><td>a flood</td><td>"Le sous-sol est inondé."</td></tr>
<tr><td>un vol / un cambriolage</td><td>a theft / a break-in</td><td>"Quelqu'un a volé mon vélo."</td></tr>
<tr><td>perdu(e)</td><td>lost</td><td>"Je suis perdu dans le bois."</td></tr>
<tr><td>coincé(e) / pogné(e) (QC)</td><td>stuck / trapped</td><td>"Mon char est pogné dans la neige!"</td></tr>
<tr><td>une panne de courant</td><td>a power outage</td><td>"Y'a une panne de courant dans tout le quartier."</td></tr>
<tr><td>glisser / tomber</td><td>to slip / to fall</td><td>"J'ai glissé sur la glace pis je suis tombé."</td></tr>
<tr><td>saigner</td><td>to bleed</td><td>"Y saigne du nez."</td></tr>
</tbody>
</table>
<p><strong>🇫🇷 Real-Life Scene – Car Stuck in Snow:</strong></p>
<p><em>Votre voiture est prise dans un banc de neige.</em></p>
<p>"Ayoye! Mon char est pogné dans le banc de neige!"<br>"Essaie de reculer pis avancer doucement."<br>"Ça marche pas, les roues tournent dans le vide."<br>"Attends, j'ai une pelle dans le coffre. Je vais pelleter autour des roues."<br>"Merci! Pis mets de la petite roche sous les pneus, ça va donner de la traction."<br>"Okay, essaie asteure."<br>"Ça bouge un petit peu... Pousse!"<br>[Avec l'aide de voisins]<br>"Merci tout le monde! Au Québec, on s'entraide dans la neige, hein!"<br>"C'est normal! M'a t'avertir : gare pas ton char dans le chemin quand y'a une opération de déneigement."<br>"T'as ben raison. La prochaine fois, je vais écouter la météo avant de sortir!"</p>
<p><em>(Your car is stuck in a snowbank. "Ow! My car is stuck in the snowbank!" "Try to go back and forth gently." "It's not working, the wheels are spinning." "Wait, I have a shovel in the trunk. I'll shovel around the wheels." "Thanks! And put some gravel under the tires, that'll give traction." "Okay, try now." "It's moving a little... Push!" [With help from neighbors] "Thanks everyone! In Quebec, we help each other in the snow, right!" "It's normal! I'll warn you: don't park your car on the street during snow removal." "You're absolutely right. Next time, I'll check the weather before going out!")</em></p>

"""
    html = insert_before(html, marker_16_end, new_16)

    write_file(path, html)
    print("A2 Part 3 done: Units 11-16 expanded successfully!")

if __name__ == '__main__':
    main()
