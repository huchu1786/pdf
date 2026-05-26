import os
import re

ROOT_DIR = r"c:\Users\rmzsh\Downloads\pdf-main\pdf-main"

def fix_links():
    fixed = 0
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if d not in ('.git', 'node_modules', '__pycache__', 'backups')]
        for file in filenames:
            if not file.endswith(('.html', '.js')):
                continue
                
            filepath = os.path.join(dirpath, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original = content
            
            # Replace href="../tool/index.html" with href="../tool/"
            content = re.sub(r'href=(["\'])\.\./([^/]+)/index\.html\1', r'href=\1../\2/\1', content)
            
            # Replace href="tool/index.html" with href="tool/"
            content = re.sub(r'href=(["\'])([^/]+)/index\.html\1', r'href=\1\2/\1', content)
            
            # Replace href="index.html" with href="/" or "../index.html" with "../"
            # Actually, for "../index.html", we can just replace with "../"
            content = re.sub(r'href=(["\'])\.\./index\.html(#.*?)?\1', r'href=\1../\2\1', content)
            content = re.sub(r'href=(["\'])index\.html(#.*?)?\1', r'href=\1/\2\1', content)
            
            # Fix links to root pages missing .html
            pages = ['features', 'pricing', 'about', 'contact', 'faq', 'blog', 'privacy', 'terms', 'cookies', 'security', 'business', 'education', 'press']
            for page in pages:
                content = re.sub(rf'href=(["\'])\.\./{page}\1', rf'href=\1../{page}.html\1', content)
                content = re.sub(rf'href=(["\'])/{page}\1', rf'href=\1/{page}.html\1', content)
                content = re.sub(rf'href=(["\']){page}\1', rf'href=\1{page}.html\1', content)
                
            # Clean up blog post links
            content = re.sub(r'href=(["\'])(/?)blog-posts/([^/"]+)(?<!\.html)\1', r'href=\1\2blog-posts/\3.html\1', content)
            
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed += 1
                
    print(f"Fixed links in {fixed} files.")

if __name__ == '__main__':
    fix_links()
