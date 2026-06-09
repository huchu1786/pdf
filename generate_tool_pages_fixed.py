#!/usr/bin/env python3
"""Generate individual tool pages for all tools in tools-data.js - Fixed version"""

import os
import re
from pathlib import Path

def load_tools_data():
    """Load tools data from tools-data.js"""
    with open('tools-data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the entire TOOLS_SEO array content
    tools_match = re.search(r'const TOOLS_SEO = (\[.*?\]);', content, re.DOTALL)
    if not tools_match:
        raise ValueError("Could not find TOOLS_SEO array")
    
    array_content = tools_match.group(1)
    
    # Split by object boundaries (look for }, followed by optional whitespace and { or ])
    objects = re.split(r'\}\s*,\s*\n', array_content)
    
    tools = []
    for obj in objects:
        # Skip empty objects or the closing bracket
        if not obj.strip() or obj.strip() == ']':
            continue
            
        # Add back the closing brace that was removed by split
        if not obj.rstrip().endswith('}'):
            obj += '}'
        
        # Extract ID
        id_match = re.search(r"id:\s*'([^']+)'", obj)
        if not id_match:
            continue
            
        tool_id = id_match.group(1)
        
        # Parse individual fields
        tool_data = {'id': tool_id}
        
        # Extract title
        title_match = re.search(r"title:\s*'([^']+)'", obj)
        if title_match:
            tool_data['title'] = title_match.group(1)
        
        # Extract meta
        meta_match = re.search(r"meta:\s*'([^']+)'", obj)
        if meta_match:
            tool_data['meta'] = meta_match.group(1)
        
        # Extract h1
        h1_match = re.search(r"h1:\s*'([^']+)'", obj)
        if h1_match:
            tool_data['h1'] = h1_match.group(1)
        
        # Extract desc
        desc_match = re.search(r"desc:\s*'([^']+)'", obj)
        if desc_match:
            tool_data['desc'] = desc_match.group(1)
        
        # Extract toolId
        toolid_match = re.search(r"toolId:\s*'([^']+)'", obj)
        if toolid_match:
            tool_data['toolId'] = toolid_match.group(1)
        
        # Extract instructions
        instructions_match = re.search(r"instructions:\s*\[(.*?)\]", obj, re.DOTALL)
        if instructions_match:
            instructions_text = instructions_match.group(1)
            instructions = re.findall(r"'([^']+)'", instructions_text)
            tool_data['instructions'] = instructions
        
        # Extract benefits
        benefits_match = re.search(r"benefits:\s*\[(.*?)\]", obj, re.DOTALL)
        if benefits_match:
            benefits_text = benefits_match.group(1)
            benefits = []
            benefit_objects = re.findall(r"{title:\s*'([^']+)',\s*desc:\s*'([^']+)'}", benefits_text)
            for title, desc in benefit_objects:
                benefits.append({'title': title, 'desc': desc})
            tool_data['benefits'] = benefits
        
        # Extract faqs
        faqs_match = re.search(r"faqs:\s*\[(.*?)\]", obj, re.DOTALL)
        if faqs_match:
            faqs_text = faqs_match.group(1)
            faqs = []
            faq_objects = re.findall(r"{q:\s*'([^']+)',\s*a:\s*'([^']+)'}", faqs_text)
            for q, a in faq_objects:
                faqs.append({'q': q, 'a': a})
            tool_data['faqs'] = faqs
        
        # Extract related tools
        related_match = re.search(r"related:\s*\[([^\]]*)\]", obj)
        if related_match:
            related_text = related_match.group(1)
            related = re.findall(r"'([^']+)'", related_text)
            tool_data['related'] = related
        
        # Only add if we have basic required fields
        if 'title' in tool_data and 'h1' in tool_data:
            tools.append(tool_data)
    
    return tools

def generate_tool_page(tool_data):
    """Generate HTML page for a single tool"""
    tool_id = tool_data['id']
    tool_dir = Path(tool_id)
    
    # Create directory if it doesn't exist
    tool_dir.mkdir(exist_ok=True)
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
    <title>{tool_data['title']}</title>
    <meta name="description" content="{tool_data['meta']}"/>
    <link rel="icon" type="image/png" sizes="512x512" href="../favicon.png">
    <link rel="apple-touch-icon" href="../favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,900&family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../shared.css">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4413784450447798" crossorigin="anonymous"></script>
</head>
<body>
    <nav class="site-nav" id="siteNav">
        <a href="../" class="nav-logo"><div class="nav-logo-heart">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
    </div>
    love<span>pdfs</span></a>
        <div class="nav-mid">
            <a href="../all-tools.html" class="nav-link">All Tools</a>
            <a href="../all-tools.html" class="nav-link">PDF Tools</a>
            <a href="../all-tools.html" class="nav-link">Image Tools</a>
        </div>
        <div class="nav-right">
            
            <a href="../contact.html" class="nav-btn-o">Contact</a>
            <a href="../" class="nav-btn-f">← All Tools</a>
        </div>
    </nav>

    <main class="tool-page">
        <div class="tool-hero">
            <h1 class="tool-title">{tool_data['h1']}</h1>
            <p class="tool-description">{tool_data['desc']}</p>
        </div>

        <div class="tool-container">
            <div class="tool-workspace">
                <div class="drop-area" id="dropArea">
                    <div class="drop-icon">📁</div>
                    <p class="drop-text">Click to upload or drag and drop</p>
                    <p class="drop-subtext">Supports multiple files</p>
                    <input type="file" id="fileInput" multiple accept=".pdf,.jpg,.jpeg,.png,.webp">
                </div>
                
                <div class="tool-options" id="toolOptions" style="display: none;">
                    <div class="file-list" id="fileList"></div>
                    <div class="tool-controls">
                        <button class="btn-primary" id="processBtn">Process Files</button>
                        <button class="btn-secondary" id="clearBtn">Clear All</button>
                    </div>
                </div>
                
                <div class="tool-result" id="toolResult" style="display: none;">
                    <div class="result-preview" id="resultPreview"></div>
                    <div class="result-actions">
                        <button class="btn-primary" id="downloadBtn">Download Result</button>
                        <button class="btn-secondary" id="startOverBtn">Start Over</button>
                    </div>
                </div>
            </div>

            <div class="tool-sidebar">
                <div class="info-card">
                    <h3>How to Use</h3>
                    <ol class="instructions">
                        {''.join([f'<li>{step}</li>' for step in tool_data.get('instructions', ['Upload your files', 'Configure options', 'Process files', 'Download result'])])}
                    </ol>
                </div>

                <div class="info-card">
                    <h3>Benefits</h3>
                    <div class="benefits">
                        {''.join([f'<div class="benefit"><h4>{benefit["title"]}</h4><p>{benefit["desc"]}</p></div>' for benefit in tool_data.get('benefits', [{'title': 'Fast Processing', 'desc': 'Quick and efficient processing of your files.'}])])}
                    </div>
                </div>

                <div class="info-card">
                    <h3>Frequently Asked Questions</h3>
                    <div class="faqs">
                        {''.join([f'<div class="faq"><h4>{faq["q"]}</h4><p>{faq["a"]}</p></div>' for faq in tool_data.get('faqs', [{'q': 'Is it free?', 'a': 'Yes, this tool is completely free to use.'}])])}
                    </div>
                </div>
            </div>
        </div>

        <div class="related-tools">
            <h3>Related Tools</h3>
            <div class="tools-grid">
                {''.join([f'<div class="tool-card" onclick="window.location.href=\'../{related}/\'"><div class="tool-icon">🔧</div><h4>{related.replace("-", " ").title()}</h4></div>' for related in tool_data.get('related', ['compress-pdf', 'split-pdf', 'merge-pdf'])[:6]])}
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="footer-grid">
            <div class="footer-brand">
                <div class="footer-logo"><div class="nav-logo-heart">
      <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>
    </div>
    love<span>pdfs</span></div>
                <div class="footer-tagline">Every PDF & Image tool you'll ever need — 100% free, private, running entirely in your browser.</div>
                <div class="footer-contact"><a href="../contact.html">Contact us</a></div>
                <div class="footer-badges"><span class="fbadge">&#128274; SSL</span><span class="fbadge">&#9889; WebAssembly</span><span class="fbadge">&#10022; Always Free</span></div>
            </div>
            <div><div class="footer-col-title">Product</div><div class="footer-links"><a href="../">Home</a><a href="../features.html">Features</a><a href="../pricing.html">Pricing</a><a href="../all-tools.html">Tools</a><a href="../faq.html">FAQ</a></div></div>
            <div><div class="footer-col-title">Solutions</div><div class="footer-links"><a href="../business.html">Business</a><a href="../education.html">Education</a></div></div>
            <div><div class="footer-col-title">Legal</div><div class="footer-links"><a href="../security.html">Security</a><a href="../privacy.html">Privacy policy</a><a href="../terms.html">Terms & conditions</a><a href="../cookies.html">Cookies</a></div></div>
            <div><div class="footer-col-title">Company</div><div class="footer-links"><a href="../about.html">About us</a><a href="../contact.html">Contact us</a><a href="../blog.html">Blog</a><a href="../press.html">Press</a></div></div>
        </div>
        <div class="footer-bottom" style="max-width:1240px;margin:2rem auto 0;padding-top:1.5rem;border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem">
            <div class="footer-copy" style="font-size:0.8rem;color:var(--muted)">&copy; LovePDFs 2026 &reg; · Private & Local Processing</div>
            <div class="footer-sitemap"><a href="../sitemap.xml" style="color:var(--muted);font-size:0.82rem;text-decoration:none;transition:color 0.2s">Sitemap</a></div>
        </div>
    </footer>

    <script src="../app.js"></script>
    <script>
        // Tool-specific functionality will be loaded based on toolId
        const toolId = '{tool_data.get('toolId', tool_data['id'])}';
        document.addEventListener('DOMContentLoaded', () => {{
            // Initialize tool-specific functionality
            if (typeof window.initializeTool === 'function') {{
                window.initializeTool(toolId);
            }}
        }});
    </script>
</body>
</html>"""
    
    # Write to file
    output_file = tool_dir / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return output_file

def main():
    """Generate all tool pages"""
    try:
        tools = load_tools_data()
        print(f"Found {len(tools)} tools in tools-data.js")
        
        generated_count = 0
        for tool in tools:
            tool_id = tool['id']
            tool_dir = Path(tool_id)
            
            # Check if page already exists
            if tool_dir.exists() and (tool_dir / "index.html").exists():
                print(f"[OK] {tool_id} - page already exists")
                continue
            
            # Generate page
            output_file = generate_tool_page(tool)
            generated_count += 1
            print(f"[NEW] Generated: {output_file}")
        
        print(f"\nGenerated {generated_count} new tool pages")
        print(f"Total tools: {len(tools)}")
        
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
