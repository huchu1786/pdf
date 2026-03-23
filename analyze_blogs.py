import json
import os
from collections import defaultdict

# Load blog data
with open('blog_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

posts = data['posts']
print(f"Total posts: {len(posts)}")

# Group by category
categories = defaultdict(list)
for post in posts:
    cat = post.get('category', 'Uncategorized')
    categories[cat].append(post)

print("\nCategories:")
for cat, posts_list in categories.items():
    print(f"  {cat}: {len(posts_list)} posts")

# Create interlinking groups based on topic
topic_groups = {
    "PDF Manipulation": ["merge-pdf", "split-pdf", "compress-pdf", "rotate-pdf", "organize-pdf", "crop-pdf", "extract-pages-pdf", "remove-pages-pdf"],
    "PDF Security": ["protect-pdf", "unlock-pdf", "sign-pdf", "redact-pdf", "remove-annotations-pdf"],
    "PDF Conversion": ["convert-pdf-to-word", "convert-pdf-to-excel", "pdf-to-powerpoint", "convert-pdf-to-jpg", "convert-word-to-pdf", "convert-excel-to-pdf", "convert-powerpoint-to-pdf", "convert-pdf-to-text", "convert-html-to-pdf", "convert-pdf-to-pdfa", "convert-pdf-to-grayscale"],
    "Image Tools": ["compress-image", "crop-image", "resize-image", "convert-jpg-to-png", "convert-png-to-jpg", "convert-jpg-to-pdf"],
    "PDF Enhancement": ["add-watermark-pdf", "add-page-numbers-pdf", "add-header-footer-pdf", "flatten-pdf", "edit-pdf-metadata", "extract-images-pdf", "resize-pdf-page-size", "alternate-mix-pdf", "deskew-pdf", "repair-pdf"],
    "OCR & Text": ["ocr-extract-text", "edit-pdf"],
    "Comparison": ["compare-pdf"]
}

# Map slugs to post titles
slug_to_post = {}
for post in posts:
    slug = post['slug']
    slug_to_post[slug] = post['title']

print("\n=== Interlinking Plan ===")
print("For each blog post, we'll add contextual links to related posts in the same topic group.")
print("\nExample implementation:")
print("1. Identify the main tool/topic of each blog")
print("2. Find 3-5 related posts from the same topic group")
print("3. Add contextual links within the content (not just at the end)")
print("4. Update 'Related Articles' section with actual links")

# Create a mapping for each post
print("\n\nSample interlinking for key posts:")
for group_name, tools in topic_groups.items():
    print(f"\n{group_name}:")
    for tool in tools[:3]:  # Show first 3 as example
        # Find matching post
        matching = [p for p in posts if tool.replace('-', ' ') in p['title'].lower() or tool in p['slug']]
        if matching:
            post = matching[0]
            related = [p for p in posts if p['slug'] != post['slug'] and any(t in p['slug'] for t in tools)]
            print(f"  {post['title']}")
            if related:
                print(f"    → Related: {', '.join(r['title'][:30] + '...' for r in related[:3])}")

# Also check for existing scripts
print("\n\nChecking for existing enhancement scripts...")
if os.path.exists('enhance_internal_links.py'):
    print("Found enhance_internal_links.py")
if os.path.exists('add_blog_interlinks.py'):
    print("Found add_blog_interlinks.py (in temp)")