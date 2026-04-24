#!/usr/bin/env python3
import re

def count_occ(filepath, pattern):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return len(re.findall(pattern, content, re.IGNORECASE))

files = ['compress-pdf/index.html', 'merge-pdf/index.html']
patterns = [
    ('How to Use This Tool', 'How-to section'),
    ('Key Benefits', 'Key Benefits section'),
    ('Frequently Asked Questions', 'FAQ section'),
    (r'\{tool_name\}', '{tool_name} placeholder'),
    ('class="seo-long-content"', 'seo-long-content div'),
]

for fp in files:
    print(f'--- {fp} ---')
    for pat, label in patterns:
        n = count_occ(fp, pat)
        if 'tool_name' in pat or 'seo-long' in pat:
            status = 'FIXED' if n == 0 else 'STILL PRESENT!'
        else:
            status = 'GOOD (no dupe)' if n <= 1 else 'DUPLICATE!'
        print(f'  {label}: {n} occurrence(s) => {status}')
    print()
