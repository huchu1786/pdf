import json
import os
import re
from blog_manager import BlogManager

def main():
    with open('tmp_tools.json', 'r', encoding='utf-8') as f:
        tools = json.load(f)

    with open('blog_data.json', 'r', encoding='utf-8') as f:
        blog_data = json.load(f)

    # get slugs of existing blogs from blog_data.json
    existing_slugs = [post['slug'] for post in blog_data['posts']]

    # check existing files in blog-posts
    if os.path.exists('blog-posts'):
        existing_files = set(os.listdir('blog-posts'))
    else:
        existing_files = set()

    blog_manager = BlogManager(base_dir='c:/Users/rmzsh/Downloads/Downloads/ilovepdfs')
    
    # We also see some blog-*.html in the root dir. Let's find those too.
    root_blog_files = [f for f in os.listdir('.') if f.startswith('blog-') and f.endswith('.html')]

    created_count = 0
    for tool in tools:
        tool_id = tool['id']
        tool_title = tool['title']
        tool_desc = tool['desc']
        tool_h1 = tool['h1']
        faqs = tool.get('faqs', [])
        benefits = tool.get('benefits', [])
        instructions = tool.get('instructions', [])

        # Create a title for the blog
        blog_title = f"{tool_h1}: Complete Guide and Tutorial"
        blog_slug = blog_title.lower().replace(' ', '-').replace(':', '').replace('|', '').replace('?', '').replace('!', '').replace('.', '')
        blog_slug = ''.join(c for c in blog_slug if c.isalnum() or c == '-')

        # Check if already exists in blog_data
        if blog_slug in existing_slugs:
            continue
        
        # Check if tool_id is in any root blog file
        if f"blog-{tool_id}.html" in root_blog_files:
            continue

        instruction_html = "<h3>How to Use It</h3><ol>"
        for inst in instructions:
            instruction_html += f"<li>{inst}</li>"
        instruction_html += "</ol>"

        benefits_html = "<h3>Benefits</h3><ul>"
        for ben in benefits:
            benefits_html += f"<li><strong>{ben['title']}:</strong> {ben['desc']}</li>"
        benefits_html += "</ul>"

        faqs_html = "<h3>Frequently Asked Questions</h3>"
        for faq in faqs:
            faqs_html += f"<h4>{faq['q']}</h4><p>{faq['a']}</p>"

        content = f"""
        <h2>Understanding {tool_h1}</h2>
        <p>{tool_desc} This detailed guide will explain everything you need to know about using our free online {tool_h1} tool effectively.</p>
        
        {benefits_html}
        {instruction_html}
        {faqs_html}
        
        <h3>Conclusion</h3>
        <p>Using the {tool_h1} tool is quick, easy, and completely free. Start optimizing your workflow today!</p>
        """

        try:
            category = "Tools Tutorial"
            if "pdf" in tool_id:
                category = "PDF Tips"
            elif "image" in tool_id or "jpg" in tool_id or "png" in tool_id:
                category = "Image Tools"

            post = blog_manager.create_daily_post(
                title=blog_title,
                content=content,
                category=category,
                tags=[tool_h1, "Tutorial", "Guide"],
                excerpt=f"Learn how to use {tool_h1} with our complete tutorial and guide. {tool_desc}"
            )
            existing_slugs.append(post['slug'])
            print(f"Created: {post['id']}")
            created_count += 1
        except Exception as e:
            print(f"Error creating for {tool_id}: {e}")

    print(f"Total created: {created_count}")

if __name__ == '__main__':
    main()
