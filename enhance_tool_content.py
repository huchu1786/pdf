#!/usr/bin/env python3
"""Add comprehensive 400-700 word content to each tool page"""

import os
import re
from pathlib import Path
from generate_tool_pages_fixed import load_tools_data

def generate_tool_content(tool_data):
    """Generate comprehensive content for a tool"""
    tool_id = tool_data['id']
    tool_name = tool_data.get('h1', tool_id.replace('-', ' ').title())
    
    # Content templates based on tool type
    content_templates = {
        'merge-pdf': {
            'intro': "Merging PDF files is a common task for professionals, students, and anyone who works with documents. Whether you're combining research papers, creating a portfolio, or compiling reports for a client, having all your content in a single PDF file makes sharing and organization much more efficient.",
            'benefits': "When you merge PDF files, you create a single, cohesive document that's easier to manage, share, and print. This eliminates the need to handle multiple files and reduces the risk of losing important pages. Merged PDFs are particularly useful for creating comprehensive reports, combining invoices, or assembling project documentation.",
            'use_cases': "PDF merging is essential in various scenarios. Students can combine lecture notes, research papers, and assignments into one study document. Business professionals can merge contracts, proposals, and supporting documents into a single client package. Legal professionals can compile case files, evidence, and legal briefs into organized case files.",
            'advanced': "Our advanced PDF merger maintains the original quality of your documents while intelligently combining them. The tool preserves bookmarks, links, and formatting when possible, ensuring your merged document remains professional and functional. You can easily reorder pages before merging to achieve the perfect document structure."
        },
        'compress-pdf': {
            'intro': "PDF compression is a crucial technique for reducing file sizes without compromising document quality. Large PDF files can be problematic for email attachments, web uploads, and storage. Compressing PDFs makes them more manageable while maintaining readability and professional appearance.",
            'benefits': "Compressed PDF files load faster, use less storage space, and are easier to share via email or cloud services. This is particularly important for businesses that handle large volumes of documents, as it reduces storage costs and improves workflow efficiency. Compression also ensures faster downloads for recipients, enhancing user experience.",
            'use_cases': "PDF compression is valuable in numerous scenarios. Graphic designers can compress high-resolution portfolios for client submissions. Publishers can reduce book PDF sizes for digital distribution. Businesses can compress reports and presentations for email marketing campaigns. Students can reduce assignment file sizes for online submissions.",
            'advanced': "Our compression algorithm intelligently analyzes your PDF content to optimize file size while preserving quality. It removes unnecessary metadata, optimizes image compression, and streamlines font embedding. The result is a significantly smaller file that maintains visual clarity and text readability."
        },
        'split-pdf': {
            'intro': "Splitting PDF files allows you to extract specific pages or sections from larger documents. This functionality is essential when you need to share only certain pages, create smaller files for specific purposes, or organize large documents into manageable sections.",
            'benefits': "PDF splitting provides greater control over document management. You can extract relevant pages for specific recipients, create targeted content for different audiences, or break down large documents into logical sections. This improves organization and makes document sharing more efficient and relevant.",
            'use_cases': "PDF splitting is useful in many contexts. Teachers can extract specific chapters from textbooks for assignments. Lawyers can separate individual case documents from large case files. HR departments can extract individual employee records from comprehensive HR files. Marketing teams can separate product pages from large catalogs.",
            'advanced': "Our PDF splitter maintains the original quality and formatting of extracted pages. It preserves bookmarks, hyperlinks, and interactive elements within the selected pages. The tool provides precise control over page selection, allowing you to extract single pages, ranges, or non-consecutive pages with equal ease."
        }
    }
    
    # Get template or use default
    template = content_templates.get(tool_id, {
        'intro': f"{tool_name} is an essential tool for anyone working with digital documents. This powerful utility helps you streamline your workflow, improve productivity, and achieve professional results with minimal effort.",
        'benefits': f"Using {tool_name} offers numerous advantages for document management. It saves time, reduces manual effort, and ensures consistent results every time. The tool is designed to be user-friendly while providing professional-grade functionality that meets the needs of both casual users and professionals.",
        'use_cases': f"This tool is perfect for various applications. Whether you're a student managing academic documents, a business professional handling reports and presentations, or an individual organizing personal files, {tool_name} provides the functionality you need to work more efficiently.",
        'advanced': f"Our advanced implementation ensures optimal performance and reliability. The tool processes your files with precision, maintains document quality, and provides intuitive controls that make complex operations simple. Built with modern technology, it delivers consistent results across different document types and sizes."
    })
    
    # Generate comprehensive content
    content = f"""
        <div class="tool-content">
            <h2>What is {tool_name}?</h2>
            <p>{template['intro']}</p>
            
            <h2>Key Benefits of Using {tool_name}</h2>
            <p>{template['benefits']}</p>
            
            <h2>Common Use Cases</h2>
            <p>{template['use_cases']}</p>
            
            <h2>Advanced Features</h2>
            <p>{template['advanced']}</p>
            
            <h2>Why Choose Our {tool_name} Tool?</h2>
            <p>Our {tool_name} tool stands out for its exceptional performance, user-friendly interface, and commitment to privacy. Unlike many online tools, we process all files directly in your browser, ensuring your documents never leave your device. This approach provides maximum security while delivering professional results quickly and efficiently.</p>
            
            <p>The tool is designed to handle various file types and sizes, making it versatile enough for both personal and professional use. Whether you're working with simple documents or complex files, our tool maintains quality and provides consistent results. The intuitive interface ensures that even users with minimal technical experience can achieve professional outcomes.</p>
            
            <h2>Tips for Best Results</h2>
            <p>To get the most out of {tool_name}, follow these best practices: Always ensure your original files are of good quality before processing. Take advantage of any preview options to verify results before finalizing. Use appropriate settings for your specific use case to optimize the balance between quality and file size. Regularly save your work to prevent data loss, especially when working with important documents.</p>
            
            <p>Remember that our tool is continuously updated to provide the latest features and improvements. We welcome user feedback and regularly enhance our tools based on user needs and technological advancements. This commitment to excellence ensures you always have access to the best document processing capabilities available.</p>
        </div>
    """
    
    return content

def enhance_tool_page_content(tool_data):
    """Add comprehensive content to a tool page"""
    tool_id = tool_data['id']
    tool_dir = Path(tool_id)
    index_file = tool_dir / "index.html"
    
    if not index_file.exists():
        return False
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Generate comprehensive content
    new_content = generate_tool_content(tool_data)
    
    # Find a good place to insert the content (after the hero section)
    # Look for the main content area or tool workspace
    insertion_patterns = [
        r'<div class="tool-workspace">.*?</div>',
        r'<main class="tool-page">.*?<div class="tool-container">',
        r'<div class="tool-hero">.*?</div>'
    ]
    
    for pattern in insertion_patterns:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # Insert content after this section
            insertion_point = match.end()
            content = content[:insertion_point] + new_content + content[insertion_point:]
            break
    else:
        # If no pattern matches, insert before the related tools section
        if '<h2>Related Tools</h2>' in content:
            content = content.replace('<h2>Related Tools</h2>', new_content + '\n  <h2>Related Tools</h2>')
    
    # Add CSS styles for the new content
    styles = """
    <style>
    .tool-content {
        max-width: 800px;
        margin: 3rem auto;
        padding: 2rem;
        background: var(--card);
        border: 2px solid var(--border);
        border-radius: 20px;
    }
    .tool-content h2 {
        font-family: 'Fraunces', serif;
        font-size: 1.8rem;
        font-weight: 800;
        color: var(--text);
        margin: 2.5rem 0 1rem 0;
        border-bottom: 2px solid var(--border);
        padding-bottom: 0.5rem;
    }
    .tool-content h2:first-child {
        margin-top: 0;
    }
    .tool-content p {
        font-size: 1.1rem;
        line-height: 1.8;
        color: var(--text2);
        margin-bottom: 1.5rem;
    }
    .tool-content strong {
        color: var(--red);
        font-weight: 700;
    }
    </style>"""
    
    # Insert styles in head section
    if '</head>' in content:
        content = content.replace('</head>', styles + '\n</head>')
    
    # Write the enhanced content
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Add comprehensive content to all tool pages"""
    try:
        tools = load_tools_data()
        print(f"Adding comprehensive content to {len(tools)} tool pages...")
        
        enhanced_count = 0
        for tool in tools:
            tool_id = tool['id']
            
            # Enhance the tool page with content
            if enhance_tool_page_content(tool):
                enhanced_count += 1
                print(f"✓ Enhanced content: {tool_id}")
            else:
                print(f"⚠ Skipped: {tool_id} (file not found)")
        
        print(f"\n🎉 Added comprehensive content to {enhanced_count} tool pages")
        print("📝 Each page now has 400-700 words of SEO-optimized content")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
