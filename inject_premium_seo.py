import os
import re
from pathlib import Path

# The highly targeted, premium SEO profiles given by the user
PREMIUM_SEO_PROFILES = {
    "compare-pdf": {
        "title": "Compare Legal PDF Documents Online Free | Secure Difference Checker",
        "h1": "Compare Legal PDF Documents Online Free",
        "description": "Secure and professional PDF comparison tool for business. Compare contracts, audit changes, and detect differences between two PDFs instantly. US & UK compliant.",
        "keywords": "compare pdf online free, compare legal documents pdf online, contract comparison software pdf, business document version comparison tool, compliance document comparison pdf, secure pdf tools online, pdf tools for business, pdf difference checker online, audit pdf changes online, secure pdf tools for US businesses"
    },
    "merge-pdf": {
        "title": "Merge PDF Files Securely for Business | Batch PDF Combine Tool",
        "h1": "Secure PDF Merger for Companies & Professionals",
        "description": "Merge multiple PDF files securely for business. Combine invoices, legal documents, and reports into one high-quality PDF. Enterprise-grade cloud PDF merge tool.",
        "keywords": "merge pdf online free, combine pdf files securely, merge multiple pdf files for business, batch pdf merge tool, merge invoices pdf online, merge pdf for legal documents, enterprise pdf tools online, merge pdf for business use, gdpr compliant pdf tools"
    },
    "split-pdf": {
        "title": "Split Confidential PDF Documents Online | Extract Pages Securely",
        "h1": "Securely Split PDF Documents for Business",
        "description": "Extract pages from large PDF files online. Securely split confidential documents, manage accounting invoices, and separate PDF pages for email size optimization.",
        "keywords": "split pdf online free, split confidential pdf documents, extract pages from pdf, split invoices pdf for accounting, bulk pdf page extraction tool, document workflow automation tools, secure document sharing pdf, secure pdf tools online, pdf tools online USA"
    },
    "organize-pdf": {
        "title": "Enterprise PDF Organizer Online | Reorder PDF Pages Securely",
        "h1": "Professional PDF Workflow Management Tool",
        "description": "Arrange and organize legal PDF documents. Reorder PDF pages online with our professional document management software. Fast, secure, and business-ready.",
        "keywords": "organize pdf pages online, document management pdf organizer, organize legal pdf documents, pdf workflow management tool, enterprise pdf organizer online, digital document management tools, business productivity tools pdf, online document processing tools, gdpr compliant pdf tools"
    },
    "pdf-to-ppt": {
        "title": "Convert PDF to Powerpoint Presentation | High Quality PPT Converter",
        "h1": "Convert PDF to PPT for Client Presentations",
        "description": "Convert report PDFs to editable PPT slides for corporate use. Secure business presentation converter. High quality PDF to PowerPoint online without losing formatting.",
        "keywords": "pdf to ppt converter, convert pdf to powerpoint presentation, business presentation pdf to ppt, pdf to ppt high quality converter, pdf to powerpoint for corporate use, edit pdf for professional use, secure file conversion tools, pdf converter UK free"
    },
    "resize-image": {
        "title": "Optimize Images for Shopify & SEO | Bulk Image Resizer",
        "h1": "High Quality Image Optimizer for Digital Marketing",
        "description": "Resize image for ecommerce websites. Compress images for faster websites without losing quality. Optimize photos for Shopify, marketing, and professional SEO.",
        "keywords": "resize image for website, optimize images for shopify, image compression for faster website, resize images for digital marketing, bulk image resizer for business, image optimizer for seo, file conversion tools online secure, online document processing platform"
    }
}

def inject_premium_seo(tool_id, data):
    index_path = Path(tool_id) / "index.html"
    if not index_path.exists():
        print(f"ERROR: {index_path} not found.")
        return False
        
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Replace <title>
    html = re.sub(
        r'<title>.*?</title>',
        f'<title>{data["title"]}</title>',
        html,
        flags=re.DOTALL | re.IGNORECASE
    )

    # 2. Replace <meta name="description">
    html = re.sub(
        r'<meta\s+name="description"\s+content="[^"]*"\s*/?>',
        f'<meta name="description" content="{data["description"]}"/>',
        html,
        flags=re.IGNORECASE
    )

    # 3. Replace <meta name="keywords">
    html = re.sub(
        r'<meta\s+name="keywords"\s+content="[^"]*"\s*/?>',
        f'<meta name="keywords" content="{data["keywords"]}"/>',
        html,
        flags=re.IGNORECASE
    )

    # 4. Replace <h1>
    html = re.sub(
        r'<h1[^>]*>.*?</h1>',
        f'<h1>{data["h1"]}</h1>',
        html,
        count=1,
        flags=re.DOTALL | re.IGNORECASE
    )

    # 5. Sync OpenGraph & Twitter titles
    html = re.sub(
        r'<meta\s+property="og:title"\s+content="[^"]*"\s*/?>',
        f'<meta property="og:title" content="{data["title"]}"/>',
        html,
        flags=re.IGNORECASE
    )
    html = re.sub(
        r'<meta\s+property="og:description"\s+content="[^"]*"\s*/?>',
        f'<meta property="og:description" content="{data["description"]}"/>',
        html,
        flags=re.IGNORECASE
    )
    # Target Twitter tags if they exist
    if 'twitter:title' in html:
        html = re.sub(
            r'<meta\s+name="twitter:title"\s+content="[^"]*"\s*/?>',
            f'<meta name="twitter:title" content="{data["title"]}"/>',
            html,
            flags=re.IGNORECASE
        )
    if 'twitter:description' in html:
        html = re.sub(
            r'<meta\s+name="twitter:description"\s+content="[^"]*"\s*/?>',
            f'<meta name="twitter:description" content="{data["description"]}"/>',
            html,
            flags=re.IGNORECASE
        )

    # 6. Update internal Schema.org name attribute
    html = re.sub(
        r'"name"\s*:\s*"[^"]*",\s*"url"',
        f'"name": "{data["h1"]}",\n  "url"',
        html,
        flags=re.IGNORECASE
    )
    html = re.sub(
        r'"description"\s*:\s*"[^"]*",\s*"applicationCategory"',
        f'"description": "{data["description"]}",\n  "applicationCategory"',
        html,
        flags=re.IGNORECASE
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f"SUCCESS: Injected Premium SEO into {tool_id}")
    return True

if __name__ == "__main__":
    for tool_id, data in PREMIUM_SEO_PROFILES.items():
        inject_premium_seo(tool_id, data)
