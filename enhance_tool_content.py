#!/usr/bin/env python3
"""Add unique, high-quality content to major tools and noindex minor tools."""

import os
import re
from pathlib import Path
from generate_tool_pages_fixed import load_tools_data

# The 16 major tools that we want search engines to index.
MAJOR_TOOLS = {
    'merge-pdf', 'compress-pdf', 'split-pdf', 'pdf-to-word', 'word-to-pdf',
    'sign-pdf', 'protect-pdf', 'unlock-pdf', 'jpg-to-pdf', 'pdf-to-jpg',
    'edit-pdf', 'compress-image', 'png-to-jpg', 'jpg-to-png', 'image-to-pdf',
    'pdf-to-text'
}

def generate_tool_content(tool_id, tool_name):
    """Generate completely unique, non-boilerplate content for a major tool."""
    
    # 100% unique content data for each of the 16 major tools
    content_templates = {
        'merge-pdf': {
            'h2_1': "What is PDF Merging and How Does It Work?",
            'p_1': "Merging PDF files is a fundamental document management task. When you combine multiple files, our local processor stitches the page trees, resource dictionaries, and binary stream contents into a single unified file. This is highly useful for merging monthly reports, combining invoices, or organizing school notes.",
            'h2_2': "Crucial Benefits of Combining Your PDFs",
            'p_2': "Combining PDFs simplifies sharing and printing. It eliminates handling multiple loose files, reducing email clutter and avoiding errors when compiling research projects, portfolio items, or contract packages.",
            'h2_3': "Typical Use Cases",
            'p_3': "Students combine homework sheets and study drafts into one document. Account teams merge monthly bills and spreadsheets for archival. Legal teams compile legal briefs, forms, and evidence files.",
            'h2_4': "Technical Processing Mechanics",
            'p_4': "Our client-side tool runs PDF merging directly on your CPU via WebAssembly. It reads the local file objects in your browser, reorganizes the PDF catalog tree structure, and writes the output file. No document data is ever sent to our servers, keeping your records entirely secure and private."
        },
        'compress-pdf': {
            'h2_1': "How PDF Compression Reduces File Size",
            'p_1': "PDF compression works by optimizing elements inside the document. It downsamples high-resolution images, deletes unused font subsets, flattens form objects, and removes excessive metadata from the document structure.",
            'h2_2': "Key Advantages of Compressing Documents",
            'p_2': "Smaller PDFs load faster, consume less disk space, and bypass strict email attachment size limits. This helps you upload files quickly to government application portals, school boards, and corporate servers.",
            'h2_3': "When to Compress Your Files",
            'p_3': "Compress scanned files before submitting job applications, email agreements, passport forms, or tax returns. Web managers optimize documents to ensure fast loading times on digital resources.",
            'h2_4': "Client-Side Processing Security",
            'p_4': "Our tool optimizes the internal object streams locally using browser RAM. Since no data leaves your browser, you can safely compress sensitive payroll registers, medical forms, or proprietary trade secrets."
        },
        'split-pdf': {
            'h2_1': "Understanding PDF Splitting",
            'p_1': "Splitting a PDF lets you divide a large document into smaller files. You can choose to extract specific pages, separate page ranges, or split a document into single-page files based on your organizational needs.",
            'h2_2': "Why You Should Split Large Documents",
            'p_2': "Large PDF files often contain chapters or sections that are not relevant to every recipient. Splitting helps you isolate and share only the necessary pages, reducing file size and ensuring targeted communication.",
            'h2_3': "Common Applications",
            'p_3': "Teachers extract a single assignment chapter from a thick textbook. HR specialists separate individual employee reviews from a company-wide report. Legal teams isolate specific evidence pages for court filings.",
            'h2_4': "High-Fidelity Local Processing",
            'p_4': "Our browser tool extracts pages without rasterizing text or losing hyperlinks. The process runs locally via WebAssembly, preserving vectors, fonts, and catalog references while keeping your files private."
        },
        'pdf-to-word': {
            'h2_1': "Converting PDF to Editable Word Files",
            'p_1': "PDFs are designed to be static and read-only, which makes editing text difficult. Converting a PDF to a Microsoft Word document (.docx) translates the document's elements back into editable text boxes, paragraphs, and formatting.",
            'h2_2': "Benefits of Converting to Word Format",
            'p_2': "Once converted, you can easily modify text, adjust spacing, correct typos, and replace graphics using standard office processors. It eliminates the need to manually retype documents from scratch.",
            'h2_3': "Use Cases for PDF to DOCX Conversion",
            'p_3': "Professionals convert contracts to edit clause terms. Job seekers convert PDF portfolios to update their work history. Researchers transform published papers to quote passages and extract data lists.",
            'h2_4': "How Our Local Converter Works",
            'p_4': "Our tool scans the layout stream coordinates in your browser, groups letters into logical sentences, and formats them into a standard Word layout. No document data is sent to external servers."
        },
        'word-to-pdf': {
            'h2_1': "Converting Microsoft Word to PDF",
            'p_1': "Word documents are prone to formatting shifts when opened on different devices, operating systems, or office suites. Converting your DOCX files to PDF freezes the layout, fonts, and graphics exactly as you designed them.",
            'h2_2': "Why Convert Word to PDF?",
            'p_2': "PDF is the universal standard for business files. Converting to PDF makes your document read-only, professional, and readable on all platforms (mobiles, tablets, PCs) without requiring office software.",
            'h2_3': "When to Convert Your Documents",
            'p_3': "Convert invoices, business proposals, contracts, resumes, and ebooks before sharing them with clients, recruiters, or the public to ensure formatting remains pristine.",
            'h2_4': "Secure Local File Compilation",
            'p_4': "Our tool translates Word elements into vector structures directly within your web browser. All layout margins, borders, list settings, and image dimensions are compiled locally without data uploads."
        },
        'sign-pdf': {
            'h2_1': "Signing PDF Documents Online",
            'p_1': "Signing papers manually requires printing, signing, scanning, and emailing. Our online PDF signer lets you add secure electronic signatures directly to your PDF files from your browser in seconds.",
            'h2_2': "Advantages of Electronic Signatures",
            'p_2': "Signing digitally saves resources, accelerates document turnaround, and supports remote workflows. It provides a simple, modern way to finalize contracts and agreements.",
            'h2_3': "Typical Sign-PDF Scenarios",
            'p_3': "Freelancers sign project contracts and proposals. Business owners sign purchase agreements and invoices. Tenants sign rental applications and lease agreements.",
            'h2_4': "Vector Signature Integration",
            'p_4': "You can draw, type, or upload an image of your signature. Our tool renders the signature as a vector layer and embeds it directly into the PDF structure, compliant with digital standards. Processing is 100% local."
        },
        'protect-pdf': {
            'h2_1': "Securing PDFs with Password Protection",
            'p_1': "Unsecured PDFs can be opened and read by anyone who intercepts the file. Protecting your PDF with password encryption locks the file contents and prevents unauthorized access, viewing, copying, or printing.",
            'h2_2': "Why You Need Document Encryption",
            'p_2': "Encryption is essential for sending confidential records, personal identities, bank statements, or legal forms. It ensures only recipients with the correct password can view the contents.",
            'h2_3': "When to Encrypt Your Files",
            'p_3': "Protect financial reports, personal identification scans, tax documents, and legal agreements before sharing them over email or uploading to cloud storage drives.",
            'h2_4': "Local Encryption Protocols",
            'p_4': "We apply standard AES encryption directly inside your browser. Because your password and document files are processed locally, your credentials are never transmitted, ensuring absolute security."
        },
        'unlock-pdf': {
            'h2_1': "Unlocking Password-Protected PDFs",
            'p_1': "Protected PDFs prompt for a password every time they are opened. If you have the password, unlocking the PDF permanently removes the encryption, allowing instant access without password prompts.",
            'h2_2': "Benefits of Decrypting Your Documents",
            'p_2': "Decrypting files lets you merge them into other archives, print them, or share them without distributing the password. It simplifies routine access to your archived files.",
            'h2_3': "Typical Decryption Needs",
            'p_3': "Accountants unlock bank statements before combining them. Researchers remove security blocks from reference manuals. Administrative teams unlock corporate documents for collaborative editing.",
            'h2_4': "Safe Local Permission Removal",
            'p_4': "Our browser tool processes the PDF catalog structure and removes security flags from the file header. All decryption is done locally inside your browser; no server logs are created."
        },
        'jpg-to-pdf': {
            'h2_1': "Converting JPG Images to PDF",
            'p_1': "Images are often shared as separate files, which can get disorganized. Converting JPG, JPEG, or PNG images to a single PDF compiles all your scans or photos into a clean, paginated document.",
            'h2_2': "Why Convert Photos to PDF?",
            'p_2': "PDF files format photos into consistent page sizes (like A4 or Letter) with options to adjust orientation and margins. This makes printouts clean and documents highly presentable.",
            'h2_3': "Typical Conversion Scenarios",
            'p_3': "Students scan handwritten study sheets and compile them into a PDF. Designers compile project sketches into a portfolio. Freelancers merge receipt images for tax returns.",
            'h2_4': "Browser-Based Image Packaging",
            'p_4': "Our tool reads image dimensions, applies your layout preferences, and packages the binary image content into a PDF container locally. There are no server uploads, saving your bandwidth."
        },
        'pdf-to-jpg': {
            'h2_1': "Extracting PDF Pages as JPG Images",
            'p_1': "Many online platforms and social media channels do not support PDF uploads. Converting PDF pages to JPG images lets you extract visual versions of your document pages for general sharing.",
            'h2_2': "Advantages of Page-to-Image Conversion",
            'p_2': "JPG images are highly compatible and display instantly without external readers. Converting pages to images makes them easy to embed in web pages, blogs, and presentations.",
            'h2_3': "Common Extraction Scenarios",
            'p_3': "Publishers extract the cover page of a PDF book to display on their catalog. Business teams save PDF charts as JPGs for slide decks. Web designers export document pages for site portfolios.",
            'h2_4': "High-Resolution Image Rendering",
            'p_4': "Our tool renders PDF vector layers onto a high-definition browser canvas, converting the canvas stream into a downloadable JPG image file. The extraction is fast and runs entirely locally."
        },
        'edit-pdf': {
            'h2_1': "Editing PDF Documents in the Browser",
            'p_1': "Editing a PDF doesn't require expensive software suites. Our online PDF editor lets you add text, draw freehand, insert shapes, and place images onto your document directly inside your web browser.",
            'h2_2': "Why Use a Browser-Based PDF Editor?",
            'p_2': "Our tool is fast, free, and accessible from any device. It allows you to quickly fill out form fields, correct typos, write comments, and mark up layouts without software downloads.",
            'h2_3': "Use Cases for Document Editing",
            'p_3': "Contractors fill out PDF estimate sheets. Evaluators grade document submissions with checkmarks. Individuals add custom text blocks to secure forms and questionnaires.",
            'h2_4': "Vector Editing Technology",
            'p_4': "We load document pages as canvas vectors, capturing your edits on a separate overlay layer. When saving, the annotations are compiled back into the PDF metadata structure locally."
        },
        'compress-image': {
            'h2_1': "Optimizing Image File Sizes",
            'p_1': "Large images slow down web pages, consume mobile data, and overload storage boxes. Compressing images optimizes the byte size of PNG, JPG, or WebP files while maintaining clear details.",
            'h2_2': "Key Benefits of Image Compression",
            'p_2': "Optimized images load fast, which improves website page-speed scores and user satisfaction. It compresses images by up to 80% with minimal visible degradation.",
            'h2_3': "When to Compress Your Photos",
            'p_3': "Web editors optimize graphics before uploading them. Photographers shrink photos for client previews. System users compress image files to upload to restricted portals.",
            'h2_4': "Local Image Scale Optimization",
            'p_4': "The compression process runs directly in your browser. It uses HTML5 canvas layers to adjust quality rates and compress the file locally, keeping your family and business photos private."
        },
        'png-to-jpg': {
            'h2_1': "Converting PNG to JPG Format",
            'p_1': "PNG files are lossless and support transparency, but they are often extremely large. Converting PNG to JPG format flattens the transparency and compresses the pixel data, reducing file sizes.",
            'h2_2': "Why Convert PNG to JPG?",
            'p_2': "JPGs are highly compressed and load much faster on web servers. If your image doesn't require transparency (like screenshots or product photos), JPG is the superior format for web speed.",
            'h2_3': "Common PNG to JPG Tasks",
            'p_3': "Webmasters convert PNG screenshots to JPG to reduce bandwidth cost. Digital editors optimize graphics for email campaigns. Mobile users compress storage footprints.",
            'h2_4': "Flattening & Encoding Locally",
            'p_4': "Our converter reads PNG pixel values, replaces transparent pixels with white backdrops, and encodes the binary matrix into standard JPEG byte blocks. The process is instant and run locally."
        },
        'jpg-to-png': {
            'h2_1': "Converting JPG to Lossless PNG",
            'p_1': "JPG files use lossy compression, which introduces pixel artifacts when saved repeatedly. Converting JPG to PNG converts the image to a lossless format, preserving quality for future edits.",
            'h2_2': "Benefits of PNG Output Format",
            'p_2': "PNG format is ideal for graphic design, print layout preparation, and editing. It maintains sharp lines, text boundaries, and solid color blocks without creating artifacts.",
            'h2_3': "When to Use JPG to PNG Conversion",
            'p_3': "Graphic designers convert JPG logos to PNG before editing. Web developers convert assets to prepare icons. Artists convert compressed drafts to save lossless final versions.",
            'h2_4': "Lossless Byte Stream Writing",
            'p_4': "The script reads your JPEG image coordinates and writes them into a standard PNG pixel grid locally in your browser tab. No compression artifacts are added during this local operation."
        },
        'image-to-pdf': {
            'h2_1': "Converting Diverse Image Formats to PDF",
            'p_1': "Sharing multiple individual image files can look unprofessional. Converting images (PNG, JPG, BMP, WebP) to a single PDF packages all graphic sheets into a structured, printable booklet.",
            'h2_2': "Advantages of Compilation to PDF",
            'p_2': "Image-to-PDF compilation creates a single, clean document with standard page dimensions. It formats receipts, documents, or photos in sequence, which is ideal for billing or archives.",
            'h2_3': "Typical Compiler Scenarios",
            'p_3': "Office managers compile scanned paper invoices into single report PDFs. Creatives compile sketches for review. Individuals package identification documents for records.",
            'h2_4': "Vector Compilation Engine",
            'p_4': "Our local WebAssembly tool loads image streams, aligns them to page margins, and exports them as standard PDF page structures. The compilation is done entirely in your browser."
        },
        'pdf-to-text': {
            'h2_1': "Extracting Plain Text from PDF Files",
            'p_1': "PDF files are visual formats, which makes copying text blocks difficult. A PDF-to-Text converter extracts the embedded character streams, removing all styling and giving you clean, editable text.",
            'h2_2': "Benefits of Plain Text Extraction",
            'p_2': "Plain text is easy to edit, translate, search, and import into other database applications. It simplifies scraping data from reports or copying passages from books.",
            'h2_3': "Common Extraction Tasks",
            'p_3': "Researchers extract text from digital reports to search keywords. Programmers extract details from documentation databases. Writers copy draft contents for edits.",
            'h2_4': "Client-Side Font Coordinate Mapping",
            'p_4': "We run PDF.js character extraction algorithms locally. The tool parses font dictionaries and mappings directly in your browser tab, returning plain text without sending files to any server."
        }
    }
    
    # Check if we have unique content defined
    template = content_templates.get(tool_id)
    if not template:
        return ""
        
    # Generate unique layout for major tools
    content = f"""
    <div class="tool-content">
        <h2>{template['h2_1']}</h2>
        <p>{template['p_1']}</p>
        
        <h2>{template['h2_2']}</h2>
        <p>{template['p_2']}</p>
        
        <h2>{template['h2_3']}</h2>
        <p>{template['p_3']}</p>
        
        <h2>{template['h2_4']}</h2>
        <p>{template['p_4']}</p>
    </div>
    """
    return content

def enhance_tool_page_content(tool_data):
    """Clean up and conditionally enhance tool pages based on index scoping."""
    tool_id = tool_data['id']
    tool_name = tool_data.get('h1', tool_id.replace('-', ' ').title())
    tool_dir = Path(tool_id)
    index_file = tool_dir / "index.html"
    
    if not index_file.exists():
        return False
    
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Strip out old tool-content and associated injected CSS styles
    content = re.sub(r'<div class="tool-content">.*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<style>\s*\.tool-content\s*\{.*?</style>', '', content, flags=re.DOTALL)
    
    # 2. Scope indexing and inject content
    is_major = tool_id in MAJOR_TOOLS
    robots_val = "index, follow" if is_major else "noindex, follow"
    
    # Replace or insert robots meta tag
    if 'name="robots"' in content:
        content = re.sub(r'<meta name="robots" content="[^"]+">', f'<meta name="robots" content="{robots_val}">', content)
    else:
        # Insert right after head tag
        content = re.sub(r'<head>', f'<head>\n    <meta name="robots" content="{robots_val}">', content)
        
    # If it is a major tool, generate and insert unique text and styles
    if is_major:
        new_content = generate_tool_content(tool_id, tool_name)
        if new_content:
            # Find a good place to insert content (after workspace)
            insertion_patterns = [
                r'<div class="tool-workspace">.*?</div>',
                r'<main class="tool-page">.*?<div class="tool-container">',
                r'<div class="tool-hero">.*?</div>'
            ]
            
            for pattern in insertion_patterns:
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    insertion_point = match.end()
                    content = content[:insertion_point] + new_content + content[insertion_point:]
                    break
            else:
                if '<h2>Related Tools</h2>' in content:
                    content = content.replace('<h2>Related Tools</h2>', new_content + '\n  <h2>Related Tools</h2>')
            
            # Re-inject tool-specific CSS styles
            styles = """
    <style>
    .tool-content {
        max-width: 800px;
        margin: 3rem auto;
        padding: 2.5rem;
        background: var(--card);
        border: 2px solid var(--border);
        border-radius: 20px;
        box-shadow: var(--shadow-sm);
    }
    .tool-content h2 {
        font-family: 'Fraunces', serif;
        font-size: 1.6rem;
        font-weight: 800;
        color: var(--text);
        margin: 2rem 0 1rem 0;
        border-bottom: 2px solid var(--border);
        padding-bottom: 0.5rem;
    }
    .tool-content h2:first-child {
        margin-top: 0;
    }
    .tool-content p {
        font-size: 1.05rem;
        line-height: 1.75;
        color: var(--text2);
        margin-bottom: 1.5rem;
    }
    </style>"""
            
            if '</head>' in content:
                content = content.replace('</head>', styles + '\n</head>')
                
    # Save the updated page back to the file
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True

def main():
    try:
        tools = load_tools_data()
        print(f"Auditing and rewriting {len(tools)} tool pages...")
        
        updated_count = 0
        major_count = 0
        minor_count = 0
        
        for tool in tools:
            tool_id = tool['id']
            is_major = tool_id in MAJOR_TOOLS
            
            if enhance_tool_page_content(tool):
                updated_count += 1
                if is_major:
                    major_count += 1
                    print(f"[MAJOR] INDEX & ENHANCE: {tool_id}")
                else:
                    minor_count += 1
                    print(f"[MINOR] NOINDEX & CLEAN: {tool_id}")
            else:
                print(f"[SKIP] Skipped (not found): {tool_id}")
                
        print(f"\nCompleted tool pages scope audit and enhancement!")
        print(f"Total processed: {updated_count}")
        print(f"Indexable (Major): {major_count}")
        print(f"Noindexed (Minor): {minor_count}")
        
    except Exception as e:
        print(f"[ERROR] Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
