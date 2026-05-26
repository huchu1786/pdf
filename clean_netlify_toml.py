import re

def clean_toml():
    with open("netlify.toml", "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Remove force = true from any redirect that goes from /index.html to /
    # because that causes redirect loops in Netlify.
    # 2. Remove force = true from any redirect that goes from /tool/index.html to /tool/
    # 3. Remove force = true from any redirect that adds a trailing slash (e.g. /tool to /tool/)
    
    blocks = content.split("[[redirects]]")
    new_blocks = [blocks[0]] # the header
    
    for block in blocks[1:]:
        is_index_redirect = "/index.html" in block and "to = \"/\"" in block
        is_tool_index = "index.html\"" in block and "to = \"/" in block
        is_trailing_slash = re.search(r'from = "/([^/"]+)"\s+to = "/\1/"', block)
        
        if is_index_redirect or is_tool_index or is_trailing_slash:
            # We either remove force = true, or skip the block completely.
            # Let's remove these blocks entirely because Netlify's Pretty URLs handles ALL of these natively!
            # If we leave them with force=true, they cause Redirect Errors.
            continue
        
        new_blocks.append(block)
        
    with open("netlify.toml", "w", encoding="utf-8") as f:
        f.write("[[redirects]]".join(new_blocks))
        
    print(f"Cleaned netlify.toml. Reduced from {len(blocks)} to {len(new_blocks)} redirect blocks.")

if __name__ == "__main__":
    clean_toml()
