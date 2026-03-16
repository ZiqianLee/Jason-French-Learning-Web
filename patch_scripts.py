import os
import re

scripts = ["expand_a2.py", "expand_b1.py", "expand_b2.py"]

for script in scripts:
    with open(script, "r", encoding="utf-8") as f:
        code = f.read()
        
    # We want to replace the logic that finds the insertion point
    # Search for the block that defines the loop and the regex search
    
    new_loop = """modified_content = content
for u, block in additions.items():
    # Remove the <h4> title to blend in seamlessly
    block = re.sub(r'<h4>.*?</h4>\\n', '', block)
    
    # Target the h2 tag for the unit in the main content
    # This avoids matching the sidebar TOC link
    pattern_h2 = re.compile(rf'<h2[^>]* id="h-[^>]*">.*?{re.escape(u)}.*?</h2>', re.IGNORECASE)
    match_h2 = pattern_h2.search(modified_content)
    
    if match_h2:
        u_header_end = match_h2.end()
        # Search for the next boundary (<hr>, next h2, or conclusion)
        search_pattern = re.compile(r'(<hr>|<h2 id="h-unit|<h1|<h2 id="h-a2-conclusion|<h2 id="h-b1-conclusion|<h2 id="h-b2-conclusion)')
        match_boundary = search_pattern.search(modified_content[u_header_end:])
        
        if match_boundary:
            insert_pos = u_header_end + match_boundary.start()
            modified_content = modified_content[:insert_pos] + "\\n" + block + "\\n\\n" + modified_content[insert_pos:]
        else:
            print(f"Failed to find boundary for {u}")
    else:
        print(f"Could not find header for {u}")"""

    # Replace from 'modified_content = content' up to the write logic
    idx = code.find("modified_content = content")
    if idx != -1:
        head = code[:idx]
        tail = code[idx:]
        
        write_idx = tail.find('with open("')
        if write_idx != -1:
            write_logic = tail[write_idx:]
            new_code = head + new_loop + "\n\n" + write_logic
            
            with open(script, "w", encoding="utf-8") as fw:
                fw.write(new_code)
            print(f"Patched {script}")
        else:
            print(f"Could not find write logic in {script}")
    else:
        print(f"Could not find loop start in {script}")
