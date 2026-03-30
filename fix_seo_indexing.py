import os
import re

ROOT_DIR = r"c:\Users\rmzsh\Downloads\pdf-main\pdf-main"
NETLIFY_TOML = os.path.join(ROOT_DIR, "netlify.toml")
BLOG_DIR = os.path.join(ROOT_DIR, "blog-posts")

def fix_netlify_redirects():
    print("Finding tool directories with index.html...")
    dirs_to_redirect = []
    
    # 1. Find directories to redirect
    for item in os.listdir(ROOT_DIR):
        item_path = os.path.join(ROOT_DIR, item)
        if os.path.isdir(item_path) and item not in ['.git', '__pycache__', 'scripts', 'blog-posts']:
            index_path = os.path.join(item_path, "index.html")
            if os.path.exists(index_path):
                dirs_to_redirect.append(item)
    
    print(f"Found {len(dirs_to_redirect)} directories.")
    
    # 2. Read netlify.toml
    with open(NETLIFY_TOML, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_blocks = []
    for d in sorted(dirs_to_redirect):
        # We want to redirect /dir/index.html to /dir/
        from_url = f"/{d}/index.html"
        to_url = f"/{d}/"
        
        # Check if already exists
        if f'from = "{from_url}"' not in content:
            block = f"""
[[redirects]]
  from = "{from_url}"
  to = "{to_url}"
  status = 301
  force = true
"""
            new_blocks.append(block)
            
    if new_blocks:
        with open(NETLIFY_TOML, "a", encoding="utf-8") as f:
            f.write("".join(new_blocks))
        print(f"Added {len(new_blocks)} redirect blocks to netlify.toml")
    else:
        print("No new redirect blocks needed in netlify.toml")

def fix_canonical_tags():
    print("Checking canonical tags in 2026-03-16 blog posts...")
    files = [f for f in os.listdir(BLOG_DIR) if f.startswith("2026-03-16") and f.endswith(".html")]
    print(f"Found {len(files)} blog posts from 2026-03-16.")
    
    fixed_count = 0
    for file in files:
        filepath = os.path.join(BLOG_DIR, file)
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        file_no_ext = file[:-5]
        expected_canonical = f'<link rel="canonical" href="https://lovepdfs.in/blog-posts/{file_no_ext}"/>'
        expected_canonical_alt = f'<link rel="canonical" href="https://lovepdfs.in/blog-posts/{file_no_ext}" />'
        
        # Check if it has the canonical tag
        if expected_canonical not in content and expected_canonical_alt not in content:
            # Maybe it has another canonical tag? Let's replace it.
            pattern = re.compile(r'<link rel="canonical" href="[^"]*"\s*/?>')
            if pattern.search(content):
                content = content.replace(pattern.search(content).group(), expected_canonical)
                print(f"[{file}] Replaced incorrect canonical tag.")
            else:
                # Add it before </head> or </title>
                if "</title>" in content:
                    content = content.replace("</title>", f"</title>\n{expected_canonical}")
                else:
                    content = content.replace("</head>", f"{expected_canonical}\n</head>")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            fixed_count += 1
            
    print(f"Fixed {fixed_count} canonical tags.")

if __name__ == "__main__":
    fix_netlify_redirects()
    fix_canonical_tags()
