#!/usr/bin/env python3
"""
Check internal links in HTML files for existence.
"""
import os
import re
from urllib.parse import urljoin, urlparse
import sys

def find_html_files(root_dir):
    html_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # skip node_modules, .git, __pycache__
        dirnames[:] = [d for d in dirnames if d not in ('node_modules', '.git', '__pycache__', 'blog-posts')]
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(dirpath, f))
    return html_files

def extract_links(html_content, base_path):
    """Extract href and src attributes."""
    links = []
    # href
    for match in re.finditer(r'href\s*=\s*["\']([^"\']+)["\']', html_content, re.IGNORECASE):
        link = match.group(1)
        links.append(link)
    # src
    for match in re.finditer(r'src\s*=\s*["\']([^"\']+)["\']', html_content, re.IGNORECASE):
        link = match.group(1)
        links.append(link)
    return links

def is_internal(link):
    # skip external URLs, mailto, tel, javascript, anchors
    if link.startswith('http://') or link.startswith('https://'):
        return False
    if link.startswith('mailto:') or link.startswith('tel:') or link.startswith('javascript:'):
        return False
    if link.startswith('#'):
        return False
    if link.startswith('data:'):
        return False
    return True

def resolve_path(link, base_dir, html_file_path):
    """Resolve relative link to absolute file path."""
    # If link is absolute from root (starts with /), treat as relative to base_dir
    if link.startswith('/'):
        link = link[1:]
    # Compute directory of the HTML file
    html_dir = os.path.dirname(html_file_path)
    # Join with link
    target = os.path.normpath(os.path.join(html_dir, link))
    # If target is outside base_dir, still check existence
    return target

def main():
    root_dir = '.'
    html_files = find_html_files(root_dir)
    print(f"Found {len(html_files)} HTML files.")
    
    broken = []
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {html_file}: {e}")
            continue
        
        links = extract_links(content, html_file)
        for link in links:
            if not is_internal(link):
                continue
            target = resolve_path(link, root_dir, html_file)
            if not os.path.exists(target):
                # Check if it's a directory with index.html
                if os.path.isdir(target):
                    index = os.path.join(target, 'index.html')
                    if os.path.exists(index):
                        continue
                broken.append((html_file, link, target))
    
    if broken:
        print("\nBroken internal links found:")
        for file, link, target in broken:
            print(f"  {file} -> {link} (resolved: {target})")
        print(f"\nTotal broken links: {len(broken)}")
    else:
        print("\nNo broken internal links found.")
    
    # Also check for orphaned files (files not linked from index?)
    # Not implemented for now.

if __name__ == '__main__':
    main()