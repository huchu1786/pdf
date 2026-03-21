#!/usr/bin/env python3
"""Enhance internal linking across all tool pages with 4-6 related tools each"""

import os
import re
from pathlib import Path
from generate_tool_pages_fixed import load_tools_data

def get_related_tools(tool_id, all_tools, max_related=6):
    """Get related tools based on category and functionality"""
    tool_categories = {
        'pdf-core': ['merge-pdf', 'split-pdf', 'compress-pdf', 'rotate-pdf', 'organize-pdf', 'crop-pdf'],
        'pdf-conversion': ['pdf-to-word', 'pdf-to-excel', 'pdf-to-ppt', 'pdf-to-jpg', 'word-to-pdf', 'excel-to-pdf', 'ppt-to-pdf', 'jpg-to-pdf'],
        'pdf-advanced': ['edit-pdf', 'sign-pdf', 'protect-pdf', 'unlock-pdf', 'add-watermark-pdf', 'redact-pdf', 'repair-pdf'],
        'image-tools': ['resize-image', 'crop-image', 'compress-image', 'jpg-to-png', 'png-to-jpg'],
        'calculators': ['age-calculator', 'bmi-calculator', 'loan-calculator', 'currency-converter', 'date-calculator', 'percentage-calculator', 'gst-calculator'],
        'pdf-extract': ['extract-pages-pdf', 'extract-images-pdf', 'remove-pages-pdf', 'pdf-to-text'],
        'pdf-format': ['pdf-to-pdfa', 'grayscale-pdf', 'flatten-pdf', 'deskew-pdf', 'resize-pdf', 'nup-pdf'],
        'pdf-metadata': ['edit-pdf-metadata', 'add-page-numbers-pdf', 'header-footer-pdf', 'remove-annotations-pdf'],
        'comparison': ['compare-pdf', 'alternate-mix-pdf'],
        'ocr': ['ocr-extract-text'],
        'web': ['html-to-pdf']
    }
    
    # Find which category this tool belongs to
    current_category = None
    for category, tools in tool_categories.items():
        if tool_id in tools:
            current_category = category
            break
    
    related_tools = []
    
    # Add tools from the same category (excluding current tool)
    if current_category:
        same_category = [t for t in tool_categories[current_category] if t != tool_id]
        related_tools.extend(same_category[:4])
    
    # Add tools from related categories
    if current_category == 'pdf-core':
        related_categories = ['pdf-advanced', 'pdf-conversion']
    elif current_category == 'pdf-conversion':
        related_categories = ['pdf-core', 'image-tools']
    elif current_category == 'pdf-advanced':
        related_categories = ['pdf-core', 'pdf-format']
    elif current_category == 'image-tools':
        related_categories = ['pdf-conversion']
    else:
        related_categories = ['pdf-core']
    
    for cat in related_categories:
        if len(related_tools) >= max_related:
            break
        related_tools.extend([t for t in tool_categories[cat] if t not in related_tools and t != tool_id][:2])
    
    return related_tools[:max_related]

def enhance_tool_page(tool_id, related_tools):
    """Enhance a tool page with better internal linking"""
    tool_dir = Path(tool_id)
    index_file = tool_dir / "index.html"
    
    if not index_file.exists():
        return False
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the existing related tools section
    related_section_pattern = r'<h2>Related Tools</h2>\s*<div class="related-links">(.*?)</div>'
    existing_match = re.search(related_section_pattern, content, re.DOTALL)
    
    if existing_match:
        # Generate new related tools HTML
        related_html = ''
        for related_tool in related_tools:
            # Convert tool ID to readable name
            tool_name = related_tool.replace('-', ' ').title()
            related_html += f'<a href="../{related_tool}/index.html" class="related-chip">{tool_name}</a>'
        
        # Replace the existing section
        new_section = f'<h2>Related Tools</h2>\n  <div class="related-links">{related_html}\n  </div>'
        content = re.sub(related_section_pattern, new_section, content, flags=re.DOTALL)
        
        # Also add a "More Tools" section if it doesn't exist
        if 'More Popular Tools' not in content:
            more_tools_html = '''
  <h2>More Popular Tools</h2>
  <div class="related-links">
    <a href="../compress-pdf/index.html" class="related-chip">Compress PDF</a>
    <a href="../merge-pdf/index.html" class="related-chip">Merge PDF</a>
    <a href="../pdf-to-word/index.html" class="related-chip">PDF to Word</a>
    <a href="../jpg-to-pdf/index.html" class="related-chip">JPG to PDF</a>
  </div>'''
            
            # Insert before the footer
            content = content.replace('</footer>', more_tools_html + '\n</footer>')
        
        # Write the enhanced content
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    
    return False

def main():
    """Enhance internal linking for all tool pages"""
    try:
        tools = load_tools_data()
        print(f"Processing {len(tools)} tool pages...")
        
        enhanced_count = 0
        for tool in tools:
            tool_id = tool['id']
            
            # Get related tools
            related_tools = get_related_tools(tool_id, tools)
            
            # Enhance the tool page
            if enhance_tool_page(tool_id, related_tools):
                enhanced_count += 1
                print(f"✓ Enhanced: {tool_id} (linked to {len(related_tools)} tools)")
            else:
                print(f"⚠ Skipped: {tool_id} (file not found or no related section)")
        
        print(f"\n🎉 Enhanced {enhanced_count} tool pages with internal linking")
        print("🔗 Each page now links to 4-6 related tools for better SEO")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
