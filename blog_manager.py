#!/usr/bin/env python3
"""Blog management system for LovePDFs - Create and manage daily blog posts"""

import os
import json
from datetime import datetime, date
from pathlib import Path

class BlogManager:
    def __init__(self, base_dir="/home/rameez/Downloads/ilovepdfs"):
        self.base_dir = Path(base_dir)
        self.blog_dir = self.base_dir / "blog-posts"
        self.blog_data_file = self.base_dir / "blog_data.json"
        self.ensure_blog_structure()
    
    def ensure_blog_structure(self):
        """Create blog directory structure if it doesn't exist"""
        self.blog_dir.mkdir(exist_ok=True)
        
        # Create blog data file if it doesn't exist
        if not self.blog_data_file.exists():
            initial_data = {
                "posts": [],
                "categories": ["PDF Tips", "Image Tools", "Workflow", "Security", "Tutorials"],
                "tags": ["PDF", "Images", "Productivity", "Security", "Tutorial", "Tips"]
            }
            with open(self.blog_data_file, 'w') as f:
                json.dump(initial_data, f, indent=2)
    
    def create_daily_post(self, title, content, category="PDF Tips", tags=None, excerpt=None):
        """Create a new daily blog post"""
        if tags is None:
            tags = ["PDF", "Tips"]
        
        # Generate slug from title
        slug = title.lower().replace(' ', '-').replace('?', '').replace('!', '').replace('.', '')
        slug = ''.join(c for c in slug if c.isalnum() or c == '-')
        
        # Get today's date
        today = date.today()
        date_str = today.strftime("%Y-%m-%d")
        
        # Create blog post metadata
        post_data = {
            "id": f"{date_str}-{slug}",
            "title": title,
            "slug": slug,
            "date": date_str,
            "author": "LovePDFs Team",
            "category": category,
            "tags": tags,
            "excerpt": excerpt or content[:150] + "..." if len(content) > 150 else content,
            "published": True,
            "featured": False
        }
        
        # Create blog post HTML file
        blog_html = self.generate_blog_html(post_data, content)
        blog_file = self.blog_dir / f"{post_data['id']}.html"
        
        with open(blog_file, 'w', encoding='utf-8') as f:
            f.write(blog_html)
        
        # Update blog data
        self.update_blog_data(post_data)
        
        return post_data
    
    def generate_blog_html(self, post_data, content):
        """Generate HTML for a blog post"""
        template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
    <title>{post_data['title']} | LovePDFs Blog</title>
    <meta name="description" content="{post_data['excerpt']}"/>
    <meta name="keywords" content="{', '.join(post_data['tags'])}"/>
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
            <a href="../blog.html" class="nav-btn-f">← Blog</a>
        </div>
    </nav>

    <main class="blog-post-container">
        <article class="blog-post">
            <div class="blog-header">
                <div class="blog-meta">
                    <span class="blog-category">{post_data['category']}</span>
                    <span class="blog-date">{datetime.strptime(post_data['date'], '%Y-%m-%d').strftime('%B %d, %Y')}</span>
                </div>
                <h1 class="blog-title">{post_data['title']}</h1>
                <div class="blog-tags">
                    {' '.join([f'<span class="tag">{tag}</span>' for tag in post_data['tags']])}
                </div>
            </div>
            
            <div class="blog-content">
                {content}
            </div>
            
            <div class="blog-footer">
                <div class="author-info">
                    <div class="author-avatar">P</div>
                    <div class="author-details">
                        <div class="author-name">{post_data['author']}</div>
                        <div class="author-bio">Helping you work smarter with PDFs and images every day.</div>
                    </div>
                </div>
                
                <div class="related-posts">
                    <h3>Related Articles</h3>
                    <div class="related-grid">
                        <!-- Related posts will be dynamically added -->
                    </div>
                </div>
            </div>
        </article>
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
</body>
</html>"""
        return template
    
    def update_blog_data(self, post_data):
        """Update the blog data JSON file with new post"""
        with open(self.blog_data_file, 'r') as f:
            blog_data = json.load(f)
        
        blog_data['posts'].insert(0, post_data)  # Add to beginning
        
        with open(self.blog_data_file, 'w') as f:
            json.dump(blog_data, f, indent=2)
    
    def update_main_blog_page(self):
        """Update the main blog.html page with latest posts"""
        with open(self.blog_data_file, 'r') as f:
            blog_data = json.load(f)
        
        # Generate blog cards HTML
        posts_html = ""
        for post in blog_data['posts'][:12]:  # Show latest 12 posts
            posts_html += f"""
            <div class="blog-card" onclick="window.location.href='blog-posts/{post['id']}.html'">
                <div class="blog-thumb">📄</div>
                <div class="blog-body">
                    <div class="blog-cat">{post['category']}</div>
                    <div class="blog-title">{post['title']}</div>
                    <div class="blog-excerpt">{post['excerpt']}</div>
                    <div class="blog-meta">
                        <span>{datetime.strptime(post['date'], '%Y-%m-%d').strftime('%b %d, %Y')}</span>
                        <span class="blog-meta-dot"></span>
                        <span>{post['author']}</span>
                    </div>
                    <a href="blog-posts/{post['id']}.html" class="blog-read">Read More →</a>
                </div>
            </div>"""
        
        # Update blog.html (you'll need to modify this to insert the posts)
        return posts_html

def main():
    """Example usage of BlogManager"""
    blog = BlogManager()
    
    # Example: Create a daily blog post
    today_post = blog.create_daily_post(
        title="How to Merge PDF Files Like a Pro in 2024",
        content="""
        <h2>Why Merge PDF Files?</h2>
        <p>Merging PDF files is a common task for professionals and students alike. Whether you're combining research papers, creating a portfolio, or compiling documents for a client, having all your content in one PDF file makes sharing and organization much easier.</p>
        
        <h2>Best Practices for PDF Merging</h2>
        <ul>
            <li>Always check the order of files before merging</li>
            <li>Ensure consistent page orientations</li>
            <li>Remove any duplicate or unnecessary pages</li>
            <li>Test the merged file before sharing</li>
        </ul>
        
        <h2>Using Our Free PDF Merger</h2>
        <p>Our online PDF merger makes combining files simple and secure. Here's how to use it:</p>
        <ol>
            <li>Upload all the PDF files you want to merge</li>
            <li>Drag and drop to reorder them if needed</li>
            <li>Click "Merge PDFs" to combine them</li>
            <li>Download your merged file instantly</li>
        </ol>
        
        <p>Best of all, everything happens right in your browser - your files never leave your device!</p>
        """,
        category="PDF Tips",
        tags=["PDF", "Merge", "Tutorial", "Productivity"],
        excerpt="Learn the best practices for merging PDF files and how to use our free online PDF merger tool effectively."
    )
    
    print(f"Created blog post: {today_post['id']}")
    print(f"File saved: blog-posts/{today_post['id']}.html")

if __name__ == "__main__":
    main()
