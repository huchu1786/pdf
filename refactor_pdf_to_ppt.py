import re
import os

FILE_PATH = "pdf-to-ppt/index.html"

def read_file():
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(content):
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

def get_compare_pdf_blocks():
    """Extract standard Nav and Footer from compare-pdf"""
    with open("compare-pdf/index.html", 'r', encoding='utf-8') as f:
        comp = f.read()
    
    nav = re.search(r'<!-- NAV -->(.*?)</nav>', comp, re.DOTALL).group(0)
    footer = re.search(r'<!-- FOOTER -->(.*?)</footer>', comp, re.DOTALL).group(0)
    return nav, footer

def process():
    html = read_file()
    nav, footer = get_compare_pdf_blocks()
    
    # 1. Fix standard Head imports
    html = re.sub(r'<link href="https://fonts.googleapis.com/css2.*?rel="stylesheet">', 
                  """<link rel="icon" type="image/png" href="../favicon.png"/>
<link rel="apple-touch-icon" href="../favicon.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,700;9..144,900&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="../shared.css"/>""", html, flags=re.DOTALL)
                  
    # 2. Extract specifically needed inline styles and nuke the rest of the style block
    custom_css = """<style>
/* SLIDE PREVIEW */
.preview-section { margin-top: 20px; display: none; }
.preview-section.visible { display: block !important; }
.preview-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; }
.preview-title { font-family: 'Fraunces', serif; font-weight: 700; font-size: 1.2rem; }
.preview-count { font-size: 0.9rem; color: var(--muted); }
.slides-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 14px; }
.slide-thumb { background: var(--card); border: 1px solid var(--border); border-radius: 10px; overflow: hidden; box-shadow: var(--shadow-xs); transition: transform 0.2s, box-shadow 0.2s; }
.slide-thumb:hover { transform: translateY(-2px); box-shadow: var(--shadow-sm); }
.slide-canvas-wrap { aspect-ratio: 4/3; overflow: hidden; background: var(--bg2); display: flex; align-items: center; justify-content: center; }
.slide-canvas-wrap canvas { width: 100%; height: 100%; object-fit: contain; border-bottom: 1px solid var(--border); }
.slide-num { padding: 6px 10px; font-size: 11px; color: var(--muted); font-weight: 500; background: var(--bg); text-align:center; }
.visible { display: block !important; }
.file-info { display: none; background: var(--bg2); border: 1.5px solid var(--border); border-radius: 12px; padding: 0.75rem 1rem; align-items: center; justify-content: space-between; margin-bottom: 1.25rem; }
.file-info.visible { display: flex !important; }
.file-name { font-weight: 700; font-size: 0.9rem; }
.file-meta { font-size: 0.8rem; color: var(--muted); }
.btn-clear { background: none; border: none; color: var(--muted); cursor: pointer; font-size: 1.1rem; }
.btn-clear:hover { color: var(--red); }
</style>"""

    html = re.sub(r'<style>.*?</style>', custom_css, html, flags=re.DOTALL)
    
    # 3. Replace Nav
    html = re.sub(r'<nav>.*?</nav>', nav, html, flags=re.DOTALL)
    
    # 4. Replace Hero
    hero_pattern = r'<div class="hero">.*?<h1>(.*?)</h1>.*?<p>(.*?)</p>.*?</div>'
    match = re.search(hero_pattern, html, flags=re.DOTALL)
    if match:
        h1 = match.group(1)
        p = match.group(2)
        new_hero = f"""<section class="tool-hero page-wrap">
  <a href="../all-tools.html" class="tool-hero-eyebrow">Back to All Tools</a>
  <h1>{h1}</h1>
  <p>{p}</p>
  <div class="tool-trust-row">
    <div class="tool-trust-item"><span class="check">✓</span> 100% Free</div>
    <div class="tool-trust-item"><span class="check">✓</span> No Signup</div>
    <div class="tool-trust-item"><span class="check">✓</span> Files Stay Private</div>
    <div class="tool-trust-item"><span class="check">✓</span> Browser-Powered</div>
  </div>
</section>"""
        html = re.sub(hero_pattern, new_hero, html, flags=re.DOTALL)
        
    # 5. Main Wrapper -> tool-workspace wrapper
    html = html.replace('<div class="main">', '<div class="tool-workspace" id="toolWorkspace">')
    
    # Drop zone styling mapping
    html = html.replace('<div class="drop-zone" id="dropZone">', '<div class="dzone" id="dropZone">')
    html = html.replace('<div class="drop-icon">📄</div>', '<span class="dzone-icon">📄</span>')
    html = html.replace('<h2>Drop your PDF here</h2>', '<h3>Drop your PDF here</h3>')
    html = html.replace('class="btn-primary" onclick="document.getElementById(\'fileInput\').click()"', 'class="btn-go" style="margin:0 auto; max-width:250px" onclick="document.getElementById(\'fileInput\').click()"')
    
    # UI panel mappings
    html = html.replace('<div class="options-panel" id="optionsPanel">', '<div class="panel" id="optionsPanel">')
    html = html.replace('<div class="options-title">⚙️ Conversion Options</div>', '<div class="panel-head"><h3>⚙️ Conversion Options</h3></div>')
    html = html.replace('class="select-group"', 'style="display:flex; flex-direction:column; gap:4px;"')
    html = html.replace('<select ', '<select class="tool-select" ')
    html = html.replace('class="option-item"', 'class="cb-row"')
    html = html.replace('class="select-row"', 'class="options-row" style="margin-bottom:1rem;"')
    html = html.replace('class="options-grid"', 'class="options-row" style="margin-bottom:1.5rem;"')
    html = html.replace('<button class="btn-primary" id="convertBtn">', '<div class="act-row"><button class="btn-go" id="convertBtn">')
    html = html.replace('🔄 Convert to PowerPoint</button>', '🔄 Convert to PowerPoint</button></div>')

    # Progress Section mappings to shared.css footprint
    prog = """<div class="prog" id="progressSection" style="margin-top:1.5rem">
    <div class="prog-hd"><span class="prog-l" id="progressLabel">Reading PDF...</span><span class="prog-p" id="progressSub">Please wait</span></div>
    <div class="prog-track"><div class="prog-bar" id="progressBar"></div></div>
  </div>"""
    html = re.sub(r'<div class="progress-section" id="progressSection">.*?</div>\s*</div>', prog, html, flags=re.DOTALL)
    
    # Result Box mappings
    result_html = """<div class="result-box" id="resultSection" style="flex-direction:column; text-align:center; padding:2rem 1rem;">
    <div class="result-ic" style="margin:0 auto; width:64px; height:64px; font-size:2rem;">🎉</div>
    <div class="result-t" style="font-size:1.4rem;">Your PowerPoint is Ready!</div>
    <div class="result-m" id="resultMeta" style="margin-bottom:1.5rem; font-size:1rem;">0 slides created from 0 pages</div>
    <div class="act-row" style="justify-content:center;">
        <a id="downloadBtn" class="btn-go" download style="background:var(--green); box-shadow:0 6px 20px var(--green-glow);">⬇ Download PPTX File</a>
        <button class="btn-rst" id="againBtn">Convert another PDF</button>
    </div>
  </div>"""
    html = re.sub(r'<div class="result-section" id="resultSection">.*?</div>\s*</div>', result_html, html, flags=re.DOTALL)

    # SEO Sections Formatting
    html = html.replace('<!-- About -->', '</div><!-- /tool-workspace -->\n\n<section class="seo-content">')
    html = html.replace('class="content-section"', 'style="margin-bottom: 2rem;"')
    html = html.replace('<div class="use-case-grid">', '<div class="benefits-grid">')
    html = html.replace('<div class="use-case-card">', '<div class="benefit-card">')
    html = html.replace('<strong>', '<h4>')
    html = html.replace('</strong>', '</h4>')
    html = html.replace('<div class="faq-item">', '<div class="faq-list" style="margin-bottom:2rem;"><div class="faq-item">')
    html = html.replace('</div>\n    <div class="faq-item">', '</div><div class="faq-item">')
    html = html.replace('<!-- Related Tools -->', '</div>') # Close faq list wrapper
    html = html.replace('class="faq-q"', 'class="faq-q" style="cursor:default;"') # Disabled toggle for static standard
    html = html.replace('class="faq-a"', 'class="faq-a" style="display:block;"')

    # Fix related chips
    html = html.replace('class="related-tool"', 'class="related-chip"')

    # Replace Footer
    html = re.sub(r'<footer>.*?</footer>', footer, html, flags=re.DOTALL)
    
    # We opened <section class="seo-content"> but didn't close it before footer. 
    # The footer replace usually covers it, but let's insert </section> right before the footer.
    html = html.replace('<!-- FOOTER -->', '</section>\n\n<!-- FOOTER -->')

    write_file(html)
    print("Refactor Complete.")

if __name__ == '__main__':
    process()
