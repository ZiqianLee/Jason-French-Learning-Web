import os
import re

file_path = "a1.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# I want to replace the huge <ul> list inside <nav class="toc"> with a simplified one.
# It should ONLY show the depth-1 links (the Parts and the general titles).

# Simplified TOC string
new_toc = """<ul>
<li><a href="#h-canadian-french-a1-level-complete-textbook" class="nav-link depth-1">Canadian French A1 Level Complete Textbook</a></li>
<li><a href="#h-part-i-foundations" class="nav-link depth-1">PART I: FOUNDATIONS</a></li>
<li><a href="#h-part-ii-personal-information" class="nav-link depth-1">PART II: PERSONAL INFORMATION</a></li>
<li><a href="#h-part-iii-everyday-grammar" class="nav-link depth-1">PART III: EVERYDAY GRAMMAR</a></li>
<li><a href="#h-part-iv-daily-communication" class="nav-link depth-1">PART IV: DAILY COMMUNICATION</a></li>
<li><a href="#h-part-v-important-structures" class="nav-link depth-1">PART V: IMPORTANT STRUCTURES</a></li>
<li><a href="#h-conclusion-study-tips" class="nav-link depth-1">CONCLUSION & STUDY TIPS</a></li>
</ul>"""

# Find the exact portion and replace it
# The original nav class="toc" might look like:
# <nav class="toc">
#   <ul>...</ul>
# </nav>

pattern = r'<nav class="toc">\s*<ul>.*?</ul>\s*</nav>'
replacement = f'<nav class="toc">\n                {new_toc}\n            </nav>'

# Use re.sub with DOTALL
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Updated TOC in {file_path}")
