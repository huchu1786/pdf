#!/usr/bin/env python3
"""Generate individual tool pages for all tools in tools-data.js"""

import os
import json
import re
from pathlib import Path

def load_tools_data():
    """Load tools data from tools-data.js"""
    with open('tools-data.js', 'r') as f:
        content = f.read()
    
    # Extract all tool objects by finding each { id: '...' } pattern
    tools = []
    
    # Find all tool IDs first
    tool_ids = re.findall(r"id:\s*'([^']+)'", content)
    
    for tool_id in tool_ids:
        # Find the start of this tool object
        tool_start_pattern = fr"id:\s*'{re.escape(tool_id)}'"
        tool_start = content.find(tool_start_pattern)
        if tool_start == -1:
            continue
        
        # Go back to find the opening {
        tool_start = content.rfind('{', 0, tool_start)
        if tool_start == -1:
            continue
        
        # Find the end of this object (next object or end of array)
        tool_end = content.find('\n  },', tool_start)
        if tool_end == -1:
            tool_end = content.find('\n];', tool_start)
        
        if tool_end == -1:
            continue
        
        tool_content = content[tool_start:tool_end + 3]
        
        # Parse individual fields
        tool_data = {'id': tool_id}
        
        # Extract title
        title_match = re.search(r"title:\s*'([^']+)'", tool_content)
        if title_match:
            tool_data['title'] = title_match.group(1)
        
        # Extract meta
        meta_match = re.search(r"meta:\s*'([^']+)'", tool_content)
        if meta_match:
            tool_data['meta'] = meta_match.group(1)
        
        # Extract h1
        h1_match = re.search(r"h1:\s*'([^']+)'", tool_content)
        if h1_match:
            tool_data['h1'] = h1_match.group(1)
        
        # Extract desc
        desc_match = re.search(r"desc:\s*'([^']+)'", tool_content)
        if desc_match:
            tool_data['desc'] = desc_match.group(1)
        
        # Extract toolId
        toolid_match = re.search(r"toolId:\s*'([^']+)'", tool_content)
        if toolid_match:
            tool_data['toolId'] = toolid_match.group(1)
        
        # Extract instructions
        instructions_match = re.search(r"instructions:\s*\[(.*?)\]", tool_content, re.DOTALL)
        if instructions_match:
            instructions_text = instructions_match.group(1)
            instructions = re.findall(r"'([^']+)'", instructions_text)
            tool_data['instructions'] = instructions
        
        # Extract benefits
        benefits_match = re.search(r"benefits:\s*\[(.*?)\]", tool_content, re.DOTALL)
        if benefits_match:
            benefits_text = benefits_match.group(1)
            benefits = []
            benefit_objects = re.findall(r"{title:\s*'([^']+)',\s*desc:\s*'([^']+)'}", benefits_text)
            for title, desc in benefit_objects:
                benefits.append({'title': title, 'desc': desc})
            tool_data['benefits'] = benefits
        
        # Extract faqs
        faqs_match = re.search(r"faqs:\s*\[(.*?)\]", tool_content, re.DOTALL)
        if faqs_match:
            faqs_text = faqs_match.group(1)
            faqs = []
            faq_objects = re.findall(r"{q:\s*'([^']+)',\s*a:\s*'([^']+)'}", faqs_text)
            for q, a in faq_objects:
                faqs.append({'q': q, 'a': a})
            tool_data['faqs'] = faqs
        
        # Extract related tools
        related_match = re.search(r"related:\s*\[([^\]]*)\]", tool_content)
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
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,900&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../shared.css">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1303178479491171" crossorigin="anonymous"></script>
</head>
<body>
    <nav class="site-nav" id="siteNav">
        <a href="../index.html" class="nav-logo"><div class="nav-logo-ic">P</div>i<span>Love</span>PDFs</a>
        <div class="nav-mid">
            <a href="../index.html#tools" class="nav-link">All Tools</a>
            <a href="../features.html" class="nav-link">Features</a>
            <a href="../blog.html" class="nav-link">Blog</a>
        </div>
        <div class="nav-right">
            <button class="theme-btn" id="themeBtn">🌙</button>
            <a href="mailto:huchusim@gmail.com" class="nav-btn-o">✉️ Contact</a>
            <a href="../index.html" class="nav-btn-f">← Tools</a>
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
                        {''.join([f'<li>{step}</li>' for step in tool_data['instructions']])}
                    </ol>
                </div>

                <div class="info-card">
                    <h3>Benefits</h3>
                    <div class="benefits">
                        {''.join([f'<div class="benefit"><h4>{benefit["title"]}</h4><p>{benefit["desc"]}</p></div>' for benefit in tool_data['benefits']])}
                    </div>
                </div>

                <div class="info-card">
                    <h3>Frequently Asked Questions</h3>
                    <div class="faqs">
                        {''.join([f'<div class="faq"><h4>{faq["q"]}</h4><p>{faq["a"]}</p></div>' for faq in tool_data['faqs']])}
                    </div>
                </div>
            </div>
        </div>

        <div class="related-tools">
            <h3>Related Tools</h3>
            <div class="tools-grid">
                {''.join([f'<div class="tool-card" onclick="window.location.href=\'../{related}.html\'"><div class="tool-icon">🔧</div><h4>{related.replace("-", " ").title()}</h4></div>' for related in tool_data['related']])}
            </div>
        </div>
    </main>

    <footer class="site-footer">
        <div class="footer-grid">
            <div class="footer-brand">
                <div class="footer-logo"><div class="nav-logo-ic" style="width:30px;height:30px;font-size:0.9rem">P</div>i<span>Love</span>PDFs</div>
                <div class="footer-tagline">Every PDF & Image tool you'll ever need — 100% free, private, running entirely in your browser.</div>
            </div>
            <div><div class="footer-col-title">Product</div><div class="footer-links"><a href="../index.html">Home</a><a href="../features.html">Features</a><a href="../all-tools.html">Tools</a></div></div>
            <div><div class="footer-col-title">Resources</div><div class="footer-links"><a href="../blog.html">Blog</a><a href="../faq.html">FAQ</a></div></div>
            <div><div class="footer-col-title">Legal</div><div class="footer-links"><a href="../privacy.html">Privacy</a><a href="../terms.html">Terms</a></div></div>
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
                print(f"✓ {tool_id} - page already exists")
                continue
            
            # Generate page
            output_file = generate_tool_page(tool)
            generated_count += 1
            print(f"✓ Generated: {output_file}")
        
        print(f"\n🎉 Generated {generated_count} new tool pages")
        print(f"📁 Total tools: {len(tools)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
