import re

def test():
    content = '    <a href="../split-pdf/index.html" class="related-chip">Split PDF</a>'
    fixed_links = 0
    def replacer(match):
        nonlocal fixed_links
        url = match.group(2)
        print("Found URL:", url)
        new_url = url
        if new_url.endswith('/index.html'):
            new_url = new_url[:-10]
            print("Changed to:", new_url)
        if new_url != url:
            fixed_links += 1
            quote = match.group(1)
            return f'href={quote}{new_url}{quote}'
        return match.group(0)

    content = re.sub(r'href\s*=\s*(["\'])(.*?)\1', replacer, content)
    print("New content:", content)
    print("Fixed links:", fixed_links)

if __name__ == '__main__':
    test()
