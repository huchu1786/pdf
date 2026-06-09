import json
import re
from datetime import datetime

# Load blog post definitions
with open('blog_data.json', 'r', encoding='utf-8') as f:
    blog_data = json.load(f)

# Every blog post is now a premium root-level post.
def clean_excerpt(excerpt):
    # Remove HTML headings and paragraphs if any exist in the excerpt
    clean = re.sub(r'<[^>]+>', ' ', excerpt)
    
    # Remove repetitive phrases
    clean = re.sub(r'Learn how to use [^.]+ with our complete tutorial( and guide)?\.\s*', '', clean, flags=re.I)
    clean = re.sub(r'Learn (the )?best practices for [^.]+ and how to use our free online [^.]+ effectively\.\s*', '', clean, flags=re.I)
    
    # Clean whitespace
    clean = ' '.join(clean.split())
    
    if not clean:
        clean = "Get professional tips, step-by-step instructions, and optimization techniques for managing document tasks."
    return clean

posts_html = ""
for post in blog_data['posts']:
    date_str = datetime.strptime(post['date'], '%Y-%m-%d').strftime('%b %d, %Y')
    
    # Assign an emoji and styles based on category
    emoji = "📝"
    color = "rgba(232,50,26,"
    border_color = "var(--red)"
    if "Security" in post['category']:
        emoji = "🔒"
        color = "rgba(124,58,237,"
        border_color = "#7C3AED"
    elif "Image Tools" in post['category']:
        emoji = "🖼️"
        color = "rgba(236,72,153,"
        border_color = "#EC4899"
    elif "Tips" in post['category'] or "Tutorial" in post['category']:
        emoji = "🗜️"
        color = "rgba(22,163,74,"
        border_color = "#16A34A"
        
    href = f"{post['id']}.html"
        
    clean_ex = clean_excerpt(post['excerpt'])
    
    posts_html += f"""
      <div class="blog-card" onclick="window.location.href='{href}'">
        <div class="blog-thumb" style="background:linear-gradient(135deg,{color}0.08),{color}0.04))">
          <span style="font-size: 3rem;">{emoji}</span>
        </div>
        <div class="blog-body">
          <div class="blog-cat" style="color:{border_color}">{post['category']}</div>
          <div class="blog-title">{post['title']}</div>
          <div class="blog-excerpt">{clean_ex}</div>
          <div class="blog-meta">
            <span>{date_str}</span><span class="blog-meta-dot"></span><span>5 min read</span>
          </div>
          <br><a href="{href}" class="blog-read">Read More →</a>
        </div>
      </div>
"""

with open('blog.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything inside <div class="blog-grid">...</div>
start_tag = '<div class="blog-grid">'
end_tag = '</div>\n\n    <!-- Newsletter -->'

start_idx = content.find(start_tag) + len(start_tag)
end_idx = content.find(end_tag)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + "\n" + posts_html + "    " + content[end_idx:]
    with open('blog.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("blog.html updated successfully!")
else:
    print("Could not find blog-grid section in blog.html")
