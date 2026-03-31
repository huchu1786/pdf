import os
import re
import json
from pathlib import Path

def main():
    base_dir = Path(r"c:\Users\rmzsh\Downloads\pdf-main\pdf-main")
    seo_file = base_dir / "viral_seo_data.json"
    
    with open(seo_file, "r", encoding="utf-8") as f:
        seo_data = json.load(f)
        
    updated_count = 0
    
    for tool_folder, data in seo_data.items():
        index_path = base_dir / tool_folder / "index.html"
        if not index_path.exists():
            print(f"Skipping {tool_folder}, index.html not found.")
            continue
            
        with open(index_path, "r", encoding="utf-8") as f:
            html = f.read()
            
        primary = data["primary"]
        keyword_list = [primary.lower()] + data["long_tails"]
        keywords_str = ", ".join(keyword_list)
        
        # 1. Update <title>
        # e.g., <title>Convert PDF to Word Free Online | LovePDFs</title>
        html = re.sub(r'<title>.*?</title>', f'<title>{primary} | LovePDFs</title>', html, flags=re.IGNORECASE)
        
        # Update OpenGraph and Twitter Titles to match the <title>
        html = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{primary} | LovePDFs">', html)
        html = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{primary} | LovePDFs">', html)
        
        # 2. Update <h1>
        # Usually it is <h1>Title</h1>
        html = re.sub(r'<h1>.*?</h1>', f'<h1>{primary}</h1>', html, flags=re.IGNORECASE)
        
        # 3. Inject or update <meta name="keywords">
        # If exists, replace content
        if '<meta name="keywords"' in html:
            html = re.sub(r'<meta\s+name="keywords"\s+content="[^"]*">', f'<meta name="keywords" content="{keywords_str}">', html, flags=re.IGNORECASE)
        else:
            # Inject right below <meta name="description">
            html = re.sub(r'(<meta\s+name="description"\s+content="[^"]*"/>)', f'\\1\n<meta name="keywords" content="{keywords_str}">', html, flags=re.IGNORECASE)
            
        # 4. Optional: If application/ld+json exists, update its name.
        # "name": "..."
        json_ld_matches = re.finditer(r'("@context":\s*"https://schema\.org",\s*"@type":\s*"WebApplication",\s*"name":\s*")([^"]+)(")', html)
        for match in json_ld_matches:
            old_name = match.group(2)
            html = html.replace(match.group(0), f'{match.group(1)}{primary}{match.group(3)}')
        
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(html)
            
        print(f"Updated {tool_folder}/index.html with primary keyword: {primary}")
        updated_count += 1
        
    print(f"\nSuccessfully injected SEO into {updated_count} tool pages.")

if __name__ == "__main__":
    main()
