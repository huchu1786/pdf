import os
import re

ROOT_DIR = r"c:\Users\rmzsh\Downloads\pdf-main\pdf-main"

def fix_html_files():
    fixed_canonicals = 0
    fixed_links = 0

    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '__pycache__', 'backups')]
        
        for file in filenames:
            if not file.endswith('.html'):
                continue
                
            filepath = os.path.join(dirpath, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {filepath}: {e}")
                continue
                
            original_content = content
            
            # --- 1. Fix Canonical Tags ---
            rel_path = os.path.relpath(filepath, ROOT_DIR).replace('\\', '/')
            
            # Determine correct canonical URL
            if rel_path == 'index.html':
                canonical_url = "https://lovepdfs.in/"
            elif file == 'index.html' and os.path.dirname(rel_path):
                # It's a tool directory like /merge-pdf/index.html
                folder = os.path.dirname(rel_path)
                canonical_url = f"https://lovepdfs.in/{folder}/"
            else:
                # It's a root level or blog-posts level html file, like /features.html
                # Remove .html for clean URLs (canonical best practice under Netlify)
                clean_path = rel_path
                if clean_path.endswith('.html'):
                    clean_path = clean_path[:-5]
                canonical_url = f"https://lovepdfs.in/{clean_path}"
                
            expected_tag = f'<link rel="canonical" href="{canonical_url}" />'
            expected_tag_alt = f'<link rel="canonical" href="{canonical_url}"/>'
            
            if expected_tag not in content and expected_tag_alt not in content:
                # Replace existing canonical or add new one
                canonical_pattern = re.compile(r'<link\s+rel=["\']canonical["\']\s+href=["\'][^"\']*["\']\s*/?>')
                if canonical_pattern.search(content):
                    content = canonical_pattern.sub(expected_tag, content)
                else:
                    if '</head>' in content:
                        content = content.replace('</head>', f'    {expected_tag}\n</head>')
                fixed_canonicals += 1

            # --- 2. Fix Internal Links ---
            # Fix links pointing to /index.html to just /
            # This uses a regex to find href="something/index.html"
            
            def replacer(match):
                nonlocal fixed_links
                full_href = match.group(0)
                url = match.group(1)
                
                # Skip external links
                if url.startswith('http') or url.startswith('mailto:') or url.startswith('javascript:'):
                    return full_href
                
                new_url = url
                
                # Fix links ending in /index.html
                if new_url.endswith('/index.html'):
                    new_url = new_url[:-10]
                elif new_url == 'index.html':
                    new_url = '/'
                    
                # Fix missing .html for known root pages if they are linked without it
                root_pages = ['features', 'pricing', 'about', 'contact', 'faq', 'blog', 'privacy', 'terms', 'cookies', 'security', 'business', 'education', 'press']
                for page in root_pages:
                    if new_url == f'/{page}':
                        new_url = f'/{page}.html'
                    elif new_url == page:
                        new_url = f'{page}.html'
                        
                if new_url != url:
                    fixed_links += 1
                    # Return the reconstructed href attribute
                    quote = match.group(0)[5] # get the quote character used (' or ")
                    return f'href={quote}{new_url}{quote}'
                
                return full_href

            content = re.sub(r'href\s*=\s*(["\'])(.*?)\1', replacer, content)
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

    print(f"Fixed {fixed_canonicals} canonical tags.")
    print(f"Fixed {fixed_links} internal links.")

if __name__ == "__main__":
    fix_html_files()
