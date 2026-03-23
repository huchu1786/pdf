#!/usr/bin/env python3
"""
Create interlink sections for blog posts with related tools.
"""

import os
import re
from pathlib import Path

# Mapping of blog topics to related tools
TOOL_CATEGORIES = {
    'pdf-manipulation': {
        'title': 'Essential PDF Manipulation Tools',
        'tools': [
            {'name': 'Merge PDF', 'url': 'https://lovepdfs.in/merge-pdf/', 'desc': 'Combine multiple PDFs into one'},
            {'name': 'Split PDF', 'url': 'https://lovepdfs.in/split-pdf/', 'desc': 'Divide PDF into separate files'},
            {'name': 'Compress PDF', 'url': 'https://lovepdfs.in/compress-pdf/', 'desc': 'Reduce PDF file size'},
            {'name': 'Rotate PDF', 'url': 'https://lovepdfs.in/rotate-pdf/', 'desc': 'Rotate pages in PDF'},
            {'name': 'Organize PDF', 'url': 'https://lovepdfs.in/organize-pdf/', 'desc': 'Reorder, delete pages'},
            {'name': 'Crop PDF', 'url': 'https://lovepdfs.in/crop-pdf/', 'desc': 'Trim PDF page margins'},
        ]
    },
    'pdf-conversion': {
        'title': 'PDF Conversion Tools',
        'tools': [
            {'name': 'PDF to Word', 'url': 'https://lovepdfs.in/pdf-to-word/', 'desc': 'Convert PDF to editable Word'},
            {'name': 'PDF to Excel', 'url': 'https://lovepdfs.in/pdf-to-excel/', 'desc': 'Extract tables to Excel'},
            {'name': 'PDF to JPG', 'url': 'https://lovepdfs.in/pdf-to-jpg/', 'desc': 'Convert PDF pages to images'},
            {'name': 'Word to PDF', 'url': 'https://lovepdfs.in/word-to-pdf/', 'desc': 'Convert Word to PDF'},
            {'name': 'Excel to PDF', 'url': 'https://lovepdfs.in/excel-to-pdf/', 'desc': 'Convert Excel to PDF'},
            {'name': 'JPG to PDF', 'url': 'https://lovepdfs.in/jpg-to-pdf/', 'desc': 'Convert images to PDF'},
        ]
    },
    'pdf-security': {
        'title': 'PDF Security & Protection',
        'tools': [
            {'name': 'Protect PDF', 'url': 'https://lovepdfs.in/protect-pdf/', 'desc': 'Add password encryption'},
            {'name': 'Unlock PDF', 'url': 'https://lovepdfs.in/unlock-pdf/', 'desc': 'Remove PDF passwords'},
            {'name': 'Sign PDF', 'url': 'https://lovepdfs.in/sign-pdf/', 'desc': 'Add digital signatures'},
            {'name': 'Redact PDF', 'url': 'https://lovepdfs.in/redact-pdf/', 'desc': 'Permanently remove sensitive info'},
            {'name': 'Remove Annotations', 'url': 'https://lovepdfs.in/remove-annotations-pdf/', 'desc': 'Delete comments'},
            {'name': 'Watermark PDF', 'url': 'https://lovepdfs.in/add-watermark-pdf/', 'desc': 'Add watermarks'},
        ]
    },
    'image-tools': {
        'title': 'Image Tools',
        'tools': [
            {'name': 'Compress Image', 'url': 'https://lovepdfs.in/compress-image/', 'desc': 'Reduce image file size'},
            {'name': 'Resize Image', 'url': 'https://lovepdfs.in/resize-image/', 'desc': 'Change image dimensions'},
            {'name': 'Crop Image', 'url': 'https://lovepdfs.in/crop-image/', 'desc': 'Trim image edges'},
            {'name': 'JPG to PNG', 'url': 'https://lovepdfs.in/jpg-to-png/', 'desc': 'Convert JPG to PNG'},
            {'name': 'PNG to JPG', 'url': 'https://lovepdfs.in/png-to-jpg/', 'desc': 'Convert PNG to JPG'},
            {'name': 'Image to PDF', 'url': 'https://lovepdfs.in/jpg-to-pdf/', 'desc': 'Convert images to PDF'},
        ]
    },
    'pdf-advanced': {
        'title': 'Advanced PDF Tools',
        'tools': [
            {'name': 'Edit PDF', 'url': 'https://lovepdfs.in/edit-pdf/', 'desc': 'Edit text and images in PDF'},
            {'name': 'OCR Extract Text', 'url': 'https://lovepdfs.in/ocr-extract-text/', 'desc': 'Extract text from scans'},
            {'name': 'Compare PDF', 'url': 'https://lovepdfs.in/compare-pdf/', 'desc': 'Find differences between PDFs'},
            {'name': 'Repair PDF', 'url': 'https://lovepdfs.in/repair-pdf/', 'desc': 'Fix corrupted PDF files'},
            {'name': 'Deskew PDF', 'url': 'https://lovepdfs.in/deskew-pdf/', 'desc': 'Straighten scanned pages'},
            {'name': 'Flatten PDF', 'url': 'https://lovepdfs.in/flatten-pdf/', 'desc': 'Make forms non-editable'},
        ]
    }
}

def detect_blog_topic(filename):
    """Detect the main topic of a blog post from its filename."""
    filename_lower = filename.lower()
    
    if 'merge' in filename_lower or 'split' in filename_lower:
        return 'pdf-manipulation'
    elif 'compress' in filename_lower:
        return 'pdf-manipulation'
    elif 'convert' in filename_lower or 'to-word' in filename_lower or 'to-excel' in filename_lower or 'to-jpg' in filename_lower:
        return 'pdf-conversion'
    elif 'protect' in filename_lower or 'unlock' in filename_lower or 'sign' in filename_lower or 'password' in filename_lower:
        return 'pdf-security'
    elif 'image' in filename_lower or 'jpg' in filename_lower or 'png' in filename_lower:
        return 'image-tools'
    elif 'edit' in filename_lower or 'ocr' in filename_lower or 'compare' in filename_lower:
        return 'pdf-advanced'
    elif 'watermark' in filename_lower or 'page-numbers' in filename_lower or 'header' in filename_lower:
        return 'pdf-advanced'
    else:
        return 'pdf-manipulation'  # default

def generate_interlink_section(topic):
    """Generate HTML for interlink section based on topic."""
    if topic not in TOOL_CATEGORIES:
        topic = 'pdf-manipulation'
    
    category = TOOL_CATEGORIES[topic]
    
    html = f'''
<div class="interlink-section" style="margin: 3rem 0; padding: 2rem; background: var(--surface); border-radius: 12px; border: 1px solid var(--border);">
    <h3 style="margin-top: 0; margin-bottom: 1.5rem; font-size: 1.4rem; color: var(--text);">{category['title']}</h3>
    <p style="margin-bottom: 1.5rem; color: var(--muted);">Explore these related tools to enhance your PDF workflow:</p>
    
    <div class="interlink-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1rem;">
'''
    
    for tool in category['tools']:
        html += f'''
        <a href="{tool['url']}" class="interlink-card" style="display: block; padding: 1rem; background: var(--background); border-radius: 8px; border: 1px solid var(--border); text-decoration: none; color: var(--text); transition: all 0.2s;">
            <div style="font-weight: 700; margin-bottom: 0.5rem; color: var(--primary);">{tool['name']}</div>
            <div style="font-size: 0.9rem; color: var(--muted);">{tool['desc']}</div>
        </a>
'''
    
    html += '''
    </div>
    
    <div style="margin-top: 1.5rem; padding-top: 1rem; border-top: 1px solid var(--border);">
        <a href="https://lovepdfs.in/all-tools.html" style="color: var(--primary); font-weight: 600; text-decoration: none;">
            View all 40+ tools →
        </a>
    </div>
</div>
'''
    
    return html

def main():
    print("Generating interlink section templates...")
    
    # Test with different topics
    for topic in TOOL_CATEGORIES.keys():
        print(f"\n=== {topic.upper()} ===")
        print(generate_interlink_section(topic)[:200] + "...")
    
    # Example usage
    print("\n=== EXAMPLE USAGE ===")
    test_files = [
        '2026-03-15-how-to-merge-pdf-files-like-a-pro-in-2024.html',
        '2026-03-16-convert-pdf-to-word-complete-guide-and-tutorial.html',
        '2026-03-16-protect-pdf-complete-guide-and-tutorial.html',
        '2026-03-16-compress-image-complete-guide-and-tutorial.html',
    ]
    
    for file in test_files:
        topic = detect_blog_topic(file)
        print(f"\n{file} → Topic: {topic}")
    
    print("\nTo add interlink sections to blogs:")
    print("1. Detect the blog topic using detect_blog_topic()")
    print("2. Generate HTML with generate_interlink_section()")
    print("3. Insert the HTML before the conclusion section")

if __name__ == '__main__':
    main()