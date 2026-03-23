#!/usr/bin/env python3
"""
Script to update remaining blog posts with quality content and interlinking.
This script identifies blog posts with repetitive content and provides recommendations.
"""

import os
import re
from pathlib import Path

def analyze_blog_content(filepath):
    """Analyze a blog post for repetitive content patterns."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for repetitive phrases
    repetitive_phrases = [
        "Navigating government websites like the EPF portal",
        "In today's digital landscape",
        "knowing the best hacks to manipulate, compress, and edit",
        "absolute superpower",
        "Modern workflows—whether you are working remotely from Pune",
        "filing extensive income tax returns",
        "scrambling to upload college assignments",
        "midnight portal deadline",
        "Whether you are uploading forms to DigiLocker",
        "applying for UPSC exams online",
        "The Portable Document Format (PDF) remains the gold standard",
        "Instead of downloading massive software suites like Adobe Acrobat",
        "Everything happens entirely within your web browser",
        "This means absolutely no processing is done on external servers",
        "This represents a massive shift in how we handle data securely",
        "In the past, compressing a PDF meant uploading",
        "mysterious cloud server somewhere overseas",
        "Because there is strictly no server upload involved",
        "you immediately bypass annoying internet upload speed bottlenecks",
        "massive 100MB documents can be heavily processed",
        "fraction of a second",
        "Mastering your everyday digital files",
        "finding the exact right tools",
        "thoroughly utilizing completely free",
        "inherently secure browser-based platforms",
        "gracefully cut down on tedious administrative friction",
        "We highly recommend you boldly start by heavily exploring",
        "massive library of utilities",
        "Visit the homepage",
        "read more extensive tutorials on our central blog"
    ]
    
    issues = []
    for phrase in repetitive_phrases:
        if phrase in content:
            issues.append(phrase)
    
    return {
        'file': os.path.basename(filepath),
        'size': len(content),
        'repetitive_count': len(issues),
        'issues': issues[:5]  # Show first 5 issues
    }

def get_blog_posts():
    """Get all blog post files."""
    blog_dir = Path('blog-posts')
    posts = list(blog_dir.glob('*.html'))
    return posts

def main():
    print("Analyzing blog posts for repetitive content...")
    posts = get_blog_posts()
    print(f"Found {len(posts)} blog posts")
    
    # Analyze each post
    problematic = []
    for post in posts:
        analysis = analyze_blog_content(post)
        if analysis['repetitive_count'] > 0:
            problematic.append(analysis)
    
    print(f"\nFound {len(problematic)} posts with repetitive content:")
    for p in problematic[:10]:  # Show first 10
        print(f"  {p['file']}: {p['repetitive_count']} repetitive phrases")
        if p['issues']:
            print(f"    Sample: {p['issues'][0][:60]}...")
    
    # Create update plan
    print("\n=== UPDATE PLAN ===")
    print("1. High priority (5+ repetitive phrases):")
    high_priority = [p for p in problematic if p['repetitive_count'] >= 5]
    for p in high_priority:
        print(f"   - {p['file']}")
    
    print("\n2. Medium priority (1-4 repetitive phrases):")
    medium_priority = [p for p in problematic if 1 <= p['repetitive_count'] < 5]
    for p in medium_priority[:10]:  # Limit output
        print(f"   - {p['file']}")
    
    print(f"\nTotal to update: {len(problematic)} posts")
    
    # Generate interlinking suggestions
    print("\n=== INTERLINKING SUGGESTIONS ===")
    print("Create contextual links between related posts:")
    
    # Group by topic
    topic_groups = {
        'PDF Manipulation': ['merge', 'split', 'compress', 'rotate', 'organize', 'crop'],
        'PDF Security': ['protect', 'unlock', 'sign', 'redact', 'password'],
        'PDF Conversion': ['convert', 'to-word', 'to-excel', 'to-jpg', 'word-to', 'excel-to'],
        'Image Tools': ['image', 'jpg', 'png', 'resize', 'crop-image'],
        'PDF Editing': ['edit', 'watermark', 'page-numbers', 'header-footer', 'metadata']
    }
    
    # Map files to topics
    for post in posts[:5]:  # Just show examples
        filename = post.name.lower()
        topics = []
        for topic, keywords in topic_groups.items():
            if any(keyword in filename for keyword in keywords):
                topics.append(topic)
        
        if topics:
            print(f"  {post.name}")
            print(f"    Topics: {', '.join(topics)}")
            print(f"    Could link to other posts in: {topics[0] if topics else 'General'}")
    
    # Recommendations
    print("\n=== RECOMMENDATIONS ===")
    print("1. Update high-priority posts first (listed above)")
    print("2. Create unique, topic-specific content for each post")
    print("3. Add 3-5 contextual internal links to related posts")
    print("4. Update meta descriptions and titles for better SEO")
    print("5. Consider creating a batch update script for similar posts")

if __name__ == '__main__':
    main()