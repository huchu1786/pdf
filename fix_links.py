import glob, os

files = glob.glob('*/*.html') + glob.glob('*.html')
count = 0
for f in files:
    if 'pdf_tools_app' in f or 'blog-posts' in f: continue
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception:
        continue
    orig = content
    content = content.replace('href="../index.html#tools"', 'href="../all-tools.html"')
    content = content.replace('href="../#tools"', 'href="../all-tools.html"')
    content = content.replace('href="index.html#tools"', 'href="all-tools.html"')
    content = content.replace('href="/sitemap.xml"', 'href="../sitemap.xml"')
    
    # Fix the brand name mismatch while we are at it
    content = content.replace('i<span>Love</span>PDFs', 'LovePDFs')
    content = content.replace('ilovepdfs', 'LovePDFs')
    content = content.replace('iLovePDFs', 'LovePDFs')
    
    if content != orig:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1

print(f'Fixed links and branding in {count} pages.')
