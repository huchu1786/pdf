#!/usr/bin/env python3
"""
Fix all tool pages in subdirectories:
1. Remove the duplicate <div class="tool-content"> block (old generic content)
2. Remove the entire <div class="seo-long-content"> block (duplicate sections + {tool_name} placeholder)
3. Fix OG/Twitter titles to match the page <title> tag
4. Report summary of all changes made
"""

import os
import re
import glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# Tool directories = any subdirectory that contains an index.html
# and is NOT a non-tool dir (scripts, blog-posts, __pycache__, etc.)
NON_TOOL_DIRS = {
    'scripts', 'blog-posts', '__pycache__', '.git', 'node_modules',
    'pdf-tools', 'image-tools', 'converter-tools', 'calculator-tools',
}

def get_tool_dirs():
    tool_dirs = []
    for entry in os.scandir(ROOT):
        if entry.is_dir() and entry.name not in NON_TOOL_DIRS and not entry.name.startswith('.'):
            idx = os.path.join(entry.path, 'index.html')
            if os.path.isfile(idx):
                tool_dirs.append((entry.name, idx))
    return sorted(tool_dirs)

def fix_tool_content_block(html):
    """Remove the <div class="tool-content"> ... </div> block that contains generic content."""
    # Pattern: matches from <div class="tool-content"> to its closing </div>
    # We need to match nested divs correctly using a simple stack approach
    pattern = r'(\s*<div class="tool-content">.*?</div>\s*)'
    result = re.sub(pattern, '\n', html, flags=re.DOTALL)
    return result

def fix_seo_long_content_block(html):
    """Remove the <div class="seo-long-content" ...> ... </div> block entirely."""
    # Find the opening tag (with any attributes)
    start_tag_pattern = r'<div class="seo-long-content"[^>]*>'
    start_match = re.search(start_tag_pattern, html)
    if not start_match:
        return html, False

    start_pos = start_match.start()
    # Count div nesting from this start position to find closing </div>
    depth = 0
    pos = start_match.start()
    content_after = html[pos:]
    
    i = 0
    end_pos = -1
    while i < len(content_after):
        if content_after[i:i+4] == '<div':
            depth += 1
            i += 4
        elif content_after[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end_pos = pos + i + 6
                break
            i += 6
        else:
            i += 1
    
    if end_pos == -1:
        return html, False
    
    # Remove the block + any surrounding whitespace/newlines
    before = html[:start_pos].rstrip('\n')
    after = html[end_pos:].lstrip('\n')
    return before + '\n' + after, True

def fix_tool_name_placeholder(html, tool_h1):
    """Replace {tool_name} with the actual tool name extracted from h1."""
    if '{tool_name}' in html:
        html = html.replace('{tool_name}', tool_h1)
        return html, True
    return html, False

def fix_og_twitter_titles(html):
    """Ensure OG title and Twitter title match the page <title> tag."""
    # Extract page title
    title_match = re.search(r'<title>(.*?)</title>', html)
    if not title_match:
        return html, False

    page_title = title_match.group(1)
    changed = False

    # Fix og:title
    def replace_og_title(m):
        nonlocal changed
        old = m.group(0)
        new = f'<meta property="og:title" content="{page_title}">'
        if old != new:
            changed = True
        return new
    html = re.sub(r'<meta property="og:title" content="[^"]*">', replace_og_title, html)

    # Fix twitter:title
    def replace_tw_title(m):
        nonlocal changed
        old = m.group(0)
        new = f'<meta name="twitter:title" content="{page_title}">'
        if old != new:
            changed = True
        return new
    html = re.sub(r'<meta name="twitter:title" content="[^"]*">', replace_tw_title, html)

    return html, changed

def extract_h1(html):
    """Extract the h1 text from the hero section."""
    # Look for the hero h1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if h1_match:
        text = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        return text
    return ''

def fix_file(tool_name, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    html = original
    changes = []

    # 1. Extract h1 for placeholder replacement
    tool_h1 = extract_h1(html)

    # 2. Remove tool-content block (old duplicate generic content)
    new_html = fix_tool_content_block(html)
    if new_html != html:
        changes.append('removed .tool-content block')
        html = new_html

    # 3. Remove seo-long-content block (duplicate How-to + Benefits + FAQ + {tool_name})
    new_html, removed = fix_seo_long_content_block(html)
    if removed:
        changes.append('removed .seo-long-content block')
        html = new_html

    # 4. Fix any remaining {tool_name} placeholders (belt-and-suspenders)
    new_html, fixed = fix_tool_name_placeholder(html, tool_h1)
    if fixed:
        changes.append(f'replaced {{tool_name}} with "{tool_h1}"')
        html = new_html

    # 5. Fix OG/Twitter titles to match page title
    new_html, fixed = fix_og_twitter_titles(html)
    if fixed:
        changes.append('updated og:title / twitter:title to match <title>')
        html = new_html

    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        return changes
    return []

def main():
    tool_dirs = get_tool_dirs()
    print(f"Found {len(tool_dirs)} tool directories.\n")

    total_fixed = 0
    total_skipped = 0

    for tool_name, filepath in tool_dirs:
        changes = fix_file(tool_name, filepath)
        if changes:
            print(f"✅ {tool_name}/index.html")
            for c in changes:
                print(f"   • {c}")
            total_fixed += 1
        else:
            print(f"   {tool_name}/index.html — no changes needed")
            total_skipped += 1

    print(f"\n{'='*60}")
    print(f"Done! Fixed: {total_fixed} files | Skipped: {total_skipped} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
