#!/usr/bin/env python3
"""Generate A2 HTML - Part 1: Template + Units 1-5"""
import os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a2.html")
A1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "a1.html")

with open(A1, 'r', encoding='utf-8') as f:
    a1_content = f.read()

css_start = a1_content.index('<style>') + len('<style>')
css_end = a1_content.index('</style>')
css_block = a1_content[css_start:css_end]

js_start = a1_content.index('<script>') + len('<script>')
js_end = a1_content.index('</script>')
js_block = a1_content[js_start:js_end]

toc = """
<li><a href="#h-a2-textbook" class="nav-link depth-1">Canadian French A2 Level</a></li>
<li><a href="#h-a2-guide" class="nav-link depth-2">A Comprehensive Guide</a></li>
<li><a href="#h-a2-toc" class="nav-link depth-2">TABLE OF CONTENTS</a></li>
<li><a href="#h-part-i-reviewing" class="nav-link depth-1">PART I: REVIEWING &amp; DEEPENING</a></li>
<li><a href="#h-unit-1-a1-review" class="nav-link depth-2">UNIT 1: REVIEW OF A1 ESSENTIALS</a></li>
<li><a href="#h-1-1-key-verbs-review" class="nav-link depth-3">1.1 Key Verbs Review</a></li>
<li><a href="#h-1-2-essential-vocabulary" class="nav-link depth-3">1.2 Essential Vocabulary Recap</a></li>
<li><a href="#h-1-3-sentence-building" class="nav-link depth-3">1.3 Building Longer Sentences</a></li>
<li><a href="#h-1-4-cdn-french-a1-review" class="nav-link depth-3">1.4 Canadian French Review (🍁)</a></li>
<li><a href="#h-unit-2-imparfait" class="nav-link depth-2">UNIT 2: THE IMPARFAIT</a></li>
<li><a href="#h-2-1-intro-imparfait" class="nav-link depth-3">2.1 Introduction to the Imparfait</a></li>
<li><a href="#h-2-2-forming-imparfait" class="nav-link depth-3">2.2 Forming the Imparfait</a></li>
<li><a href="#h-2-3-uses-imparfait" class="nav-link depth-3">2.3 Uses of the Imparfait</a></li>
<li><a href="#h-2-4-imparfait-vs-pc" class="nav-link depth-3">2.4 Imparfait vs. Passé Composé</a></li>
<li><a href="#h-2-5-cdn-imparfait" class="nav-link depth-3">2.5 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-3-futur-simple" class="nav-link depth-2">UNIT 3: FUTUR SIMPLE</a></li>
<li><a href="#h-3-1-intro-futur" class="nav-link depth-3">3.1 Introduction to Futur Simple</a></li>
<li><a href="#h-3-2-regular-futur" class="nav-link depth-3">3.2 Regular Verb Conjugations</a></li>
<li><a href="#h-3-3-irregular-futur" class="nav-link depth-3">3.3 Irregular Stems</a></li>
<li><a href="#h-3-4-uses-futur" class="nav-link depth-3">3.4 Uses of Futur Simple</a></li>
<li><a href="#h-3-5-cdn-futur" class="nav-link depth-3">3.5 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-4-recent-past-near-future" class="nav-link depth-2">UNIT 4: PASSÉ RÉCENT &amp; VENIR DE</a></li>
<li><a href="#h-4-1-passe-recent" class="nav-link depth-3">4.1 Passé Récent</a></li>
<li><a href="#h-4-2-etre-en-train-de" class="nav-link depth-3">4.2 Être en train de</a></li>
<li><a href="#h-4-3-timeline-expressions" class="nav-link depth-3">4.3 Timeline Expressions</a></li>
<li><a href="#h-4-4-cdn-recent" class="nav-link depth-3">4.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-part-ii-daily-life" class="nav-link depth-1">PART II: EXPANDING DAILY LIFE</a></li>
<li><a href="#h-unit-5-shopping" class="nav-link depth-2">UNIT 5: SHOPPING &amp; MONEY</a></li>
<li><a href="#h-5-1-store-vocabulary" class="nav-link depth-3">5.1 Store Vocabulary</a></li>
<li><a href="#h-5-2-asking-prices" class="nav-link depth-3">5.2 Asking About Prices</a></li>
<li><a href="#h-5-3-clothing" class="nav-link depth-3">5.3 Clothing &amp; Sizes</a></li>
<li><a href="#h-5-4-paying" class="nav-link depth-3">5.4 Paying &amp; Transactions</a></li>
<li><a href="#h-5-5-cdn-shopping" class="nav-link depth-3">5.5 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-6-housing" class="nav-link depth-2">UNIT 6: HOUSING &amp; HOME</a></li>
<li><a href="#h-6-1-rooms" class="nav-link depth-3">6.1 Rooms &amp; Furniture</a></li>
<li><a href="#h-6-2-describing-home" class="nav-link depth-3">6.2 Describing Your Home</a></li>
<li><a href="#h-6-3-renting" class="nav-link depth-3">6.3 Renting an Apartment</a></li>
<li><a href="#h-6-4-cdn-housing" class="nav-link depth-3">6.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-7-transport" class="nav-link depth-2">UNIT 7: TRANSPORTATION</a></li>
<li><a href="#h-7-1-transport-vocab" class="nav-link depth-3">7.1 Transportation Vocabulary</a></li>
<li><a href="#h-7-2-giving-directions" class="nav-link depth-3">7.2 Giving &amp; Asking Directions</a></li>
<li><a href="#h-7-3-public-transit" class="nav-link depth-3">7.3 Public Transit in Quebec</a></li>
<li><a href="#h-7-4-cdn-transport" class="nav-link depth-3">7.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-8-weather" class="nav-link depth-2">UNIT 8: WEATHER &amp; CLIMATE</a></li>
<li><a href="#h-8-1-weather-vocab" class="nav-link depth-3">8.1 Weather Vocabulary</a></li>
<li><a href="#h-8-2-describing-weather" class="nav-link depth-3">8.2 Describing the Weather</a></li>
<li><a href="#h-8-3-seasons-quebec" class="nav-link depth-3">8.3 Seasons in Quebec</a></li>
<li><a href="#h-8-4-cdn-weather" class="nav-link depth-3">8.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-part-iii-social" class="nav-link depth-1">PART III: SOCIAL INTERACTIONS</a></li>
<li><a href="#h-unit-9-invitations" class="nav-link depth-2">UNIT 9: INVITATIONS &amp; EVENTS</a></li>
<li><a href="#h-9-1-inviting" class="nav-link depth-3">9.1 Inviting Someone</a></li>
<li><a href="#h-9-2-accepting-declining" class="nav-link depth-3">9.2 Accepting &amp; Declining</a></li>
<li><a href="#h-9-3-event-vocab" class="nav-link depth-3">9.3 Event Vocabulary</a></li>
<li><a href="#h-9-4-cdn-invitations" class="nav-link depth-3">9.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-10-phone" class="nav-link depth-2">UNIT 10: PHONE CALLS &amp; MESSAGES</a></li>
<li><a href="#h-10-1-phone-vocab" class="nav-link depth-3">10.1 Phone Vocabulary</a></li>
<li><a href="#h-10-2-making-calls" class="nav-link depth-3">10.2 Making &amp; Receiving Calls</a></li>
<li><a href="#h-10-3-texting" class="nav-link depth-3">10.3 Text Messages &amp; Email</a></li>
<li><a href="#h-10-4-cdn-phone" class="nav-link depth-3">10.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-11-instructions" class="nav-link depth-2">UNIT 11: GIVING INSTRUCTIONS</a></li>
<li><a href="#h-11-1-imperatif" class="nav-link depth-3">11.1 The Impératif</a></li>
<li><a href="#h-11-2-giving-advice" class="nav-link depth-3">11.2 Giving Advice</a></li>
<li><a href="#h-11-3-recipes" class="nav-link depth-3">11.3 Recipes &amp; Instructions</a></li>
<li><a href="#h-11-4-cdn-instructions" class="nav-link depth-3">11.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-12-comparisons" class="nav-link depth-2">UNIT 12: COMPARISONS &amp; SUPERLATIVES</a></li>
<li><a href="#h-12-1-comparatif" class="nav-link depth-3">12.1 The Comparatif</a></li>
<li><a href="#h-12-2-superlatif" class="nav-link depth-3">12.2 The Superlatif</a></li>
<li><a href="#h-12-3-irregular-comparisons" class="nav-link depth-3">12.3 Irregular Comparisons</a></li>
<li><a href="#h-12-4-cdn-comparisons" class="nav-link depth-3">12.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-part-iv-health" class="nav-link depth-1">PART IV: HEALTH &amp; SERVICES</a></li>
<li><a href="#h-unit-13-body-health" class="nav-link depth-2">UNIT 13: BODY &amp; HEALTH</a></li>
<li><a href="#h-13-1-body-parts" class="nav-link depth-3">13.1 Body Parts</a></li>
<li><a href="#h-13-2-symptoms" class="nav-link depth-3">13.2 Describing Symptoms</a></li>
<li><a href="#h-13-3-health-expressions" class="nav-link depth-3">13.3 Health Expressions</a></li>
<li><a href="#h-13-4-cdn-health" class="nav-link depth-3">13.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-14-doctor" class="nav-link depth-2">UNIT 14: AT THE DOCTOR</a></li>
<li><a href="#h-14-1-appointment" class="nav-link depth-3">14.1 Making an Appointment</a></li>
<li><a href="#h-14-2-consultation" class="nav-link depth-3">14.2 The Consultation</a></li>
<li><a href="#h-14-3-pharmacy" class="nav-link depth-3">14.3 At the Pharmacy</a></li>
<li><a href="#h-14-4-cdn-doctor" class="nav-link depth-3">14.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-15-banking" class="nav-link depth-2">UNIT 15: BANKING &amp; ADMIN</a></li>
<li><a href="#h-15-1-bank-vocab" class="nav-link depth-3">15.1 Banking Vocabulary</a></li>
<li><a href="#h-15-2-transactions" class="nav-link depth-3">15.2 Common Transactions</a></li>
<li><a href="#h-15-3-admin-tasks" class="nav-link depth-3">15.3 Administrative Tasks</a></li>
<li><a href="#h-15-4-cdn-banking" class="nav-link depth-3">15.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-16-emergencies" class="nav-link depth-2">UNIT 16: EMERGENCY SITUATIONS</a></li>
<li><a href="#h-16-1-emergency-vocab" class="nav-link depth-3">16.1 Emergency Vocabulary</a></li>
<li><a href="#h-16-2-calling-help" class="nav-link depth-3">16.2 Calling for Help</a></li>
<li><a href="#h-16-3-describing-problems" class="nav-link depth-3">16.3 Describing Problems</a></li>
<li><a href="#h-16-4-cdn-emergencies" class="nav-link depth-3">16.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-part-v-travel" class="nav-link depth-1">PART V: TRAVEL &amp; CULTURE</a></li>
<li><a href="#h-unit-17-travel" class="nav-link depth-2">UNIT 17: TRAVEL PLANNING</a></li>
<li><a href="#h-17-1-travel-vocab" class="nav-link depth-3">17.1 Travel Vocabulary</a></li>
<li><a href="#h-17-2-booking" class="nav-link depth-3">17.2 Booking &amp; Reservations</a></li>
<li><a href="#h-17-3-packing" class="nav-link depth-3">17.3 Packing &amp; Preparation</a></li>
<li><a href="#h-17-4-cdn-travel" class="nav-link depth-3">17.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-18-hotel-airport" class="nav-link depth-2">UNIT 18: HOTEL &amp; AIRPORT</a></li>
<li><a href="#h-18-1-hotel" class="nav-link depth-3">18.1 Hotel Vocabulary</a></li>
<li><a href="#h-18-2-checking-in" class="nav-link depth-3">18.2 Checking In &amp; Out</a></li>
<li><a href="#h-18-3-airport" class="nav-link depth-3">18.3 At the Airport</a></li>
<li><a href="#h-18-4-cdn-hotel" class="nav-link depth-3">18.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-19-quebec-culture" class="nav-link depth-2">UNIT 19: QUEBEC CULTURE</a></li>
<li><a href="#h-19-1-festivals" class="nav-link depth-3">19.1 Major Quebec Festivals</a></li>
<li><a href="#h-19-2-traditions" class="nav-link depth-3">19.2 Traditions &amp; Customs</a></li>
<li><a href="#h-19-3-cuisine" class="nav-link depth-3">19.3 Québécois Cuisine</a></li>
<li><a href="#h-19-4-cdn-culture" class="nav-link depth-3">19.4 Canadian French Notes (🍁)</a></li>
<li><a href="#h-unit-20-review-b1" class="nav-link depth-2">UNIT 20: REVIEW &amp; B1 PREP</a></li>
<li><a href="#h-20-1-grammar-review" class="nav-link depth-3">20.1 Grammar Review</a></li>
<li><a href="#h-20-2-vocab-review" class="nav-link depth-3">20.2 Vocabulary Review</a></li>
<li><a href="#h-20-3-b1-preview" class="nav-link depth-3">20.3 What to Expect at B1</a></li>
<li><a href="#h-20-4-study-tips" class="nav-link depth-3">20.4 Study Tips</a></li>
<li><a href="#h-a2-conclusion" class="nav-link depth-1">CONCLUSION</a></li>
"""

header = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Canadian French A2 Level Complete Textbook</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
{css_block}
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
"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(header)

print(f"Part 1 done. File: {OUTPUT}, Size: {os.path.getsize(OUTPUT)} bytes")
