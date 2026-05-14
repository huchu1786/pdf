import os
import re

TOOLS_CONTENT = {
    "merge-pdf": {
        "steps": """
  <ol class="steps-list">
    <li><strong>Upload Your PDFs:</strong> Click the 'Choose Files' button to select two or more PDF documents from your device, or simply drag and drop them directly into the designated workspace area.</li>
    <li><strong>Arrange the Order:</strong> Once uploaded, you will see a visual thumbnail representation of your files. You can click and drag these thumbnails to arrange them in the exact order you want them to appear in the final merged document.</li>
    <li><strong>Review and Finalize:</strong> Double-check the sequence of your files. If you added a file by mistake, you can remove it by clicking the 'x' icon on its thumbnail.</li>
    <li><strong>Merge and Download:</strong> Click the 'Merge PDFs' button. Our client-side WebAssembly engine will instantly combine the files without uploading them to any server. Your consolidated PDF will download automatically.</li>
  </ol>
  
  <div style="background: var(--bg2); padding: 1.5rem; border-radius: 12px; margin-top: 2rem; margin-bottom: 2rem; border-left: 4px solid var(--red);">
    <h3 style="margin-top: 0; font-family: 'Fraunces', serif;">Why Merge PDFs Locally?</h3>
    <p style="margin-bottom: 0;">Most online PDF mergers require you to upload your sensitive documents (like legal contracts or financial reports) to a remote server. LovePDFs processes everything directly inside your browser. This means zero upload time, zero risk of data breaches, and instant results.</p>
  </div>
""",
        "faqs": """
  <div class="faq-list">
      <div class="faq-item">
        <div class="faq-q">Is there a limit to how many PDFs I can merge at once?</div>
        <p class="faq-a">Because LovePDFs processes files locally using your device's memory rather than a remote server, there are no hard limits. You can merge dozens of large PDFs, provided your computer has sufficient RAM to handle the process. We recommend merging batches of up to 50 files for optimal browser performance.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Will merging PDFs change their original formatting?</div>
        <p class="faq-a">Absolutely not. Our merge engine performs a binary-level combination of the documents. All original fonts, formatting, embedded images, and vector graphics are perfectly preserved in the final output file.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Are my merged files safe and secure?</div>
        <p class="faq-a">Yes. Unlike traditional online tools that upload your files to cloud servers, LovePDFs utilizes advanced WebAssembly technology to process your files entirely within your web browser. Your data never leaves your device, guaranteeing 100% privacy and GDPR compliance.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can I merge PDFs on my mobile phone?</div>
        <p class="faq-a">Yes, our platform is fully responsive and optimized for mobile browsers. You can select PDFs directly from your iOS or Android file manager and merge them on the go.</p>
      </div>
  </div>
"""
    },
    "compress-pdf": {
        "steps": """
  <ol class="steps-list">
    <li><strong>Select Your Document:</strong> Drag and drop your large PDF file into the upload area or click to browse your device's storage.</li>
    <li><strong>Choose Compression Level:</strong> Select from three intelligent compression tiers:
        <ul style="margin-top: 0.5rem; margin-bottom: 0.5rem; color: var(--text2);">
            <li><em>Low Compression:</em> Best for printing. Minor size reduction, unnoticeable quality change.</li>
            <li><em>Medium Compression:</em> Ideal for email and web sharing. Great balance of size and clarity.</li>
            <li><em>High Compression:</em> Maximum size reduction. Best for text-heavy documents where image sharpness is secondary.</li>
        </ul>
    </li>
    <li><strong>Process Locally:</strong> Hit the 'Compress PDF' button. Our tool will analyze your file, optimize embedded images, and remove unnecessary metadata directly in your browser.</li>
    <li><strong>Download Optimized File:</strong> Instantly download your new, smaller PDF. You'll see a summary showing exactly how much space you saved.</li>
  </ol>
  
  <div style="background: var(--bg2); padding: 1.5rem; border-radius: 12px; margin-top: 2rem; margin-bottom: 2rem; border-left: 4px solid var(--red);">
    <h3 style="margin-top: 0; font-family: 'Fraunces', serif;">The Secret to High-Quality Compression</h3>
    <p style="margin-bottom: 0;">PDFs often become bloated due to unoptimized high-resolution images and hidden metadata. Our client-side compressor smartly targets these specific areas, downscaling DPI where appropriate and stripping redundant data, without touching your text vectors. The result is a dramatically smaller file that looks virtually identical to the original.</p>
  </div>
""",
        "faqs": """
  <div class="faq-list">
      <div class="faq-item">
        <div class="faq-q">How does PDF compression actually work?</div>
        <p class="faq-a">Our tool reduces file size through several methods: it compresses embedded raster images (like JPEGs and PNGs) by reducing their DPI, it removes unused fonts and hidden metadata (like author info and software tracking), and it optimizes the internal document structure to eliminate redundant code.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can I compress a PDF to exactly 100KB or 1MB?</div>
        <p class="faq-a">While you cannot specify an exact target size in kilobytes, selecting the "High" compression setting will aggressively optimize the file, often reducing sizes by 70% to 90%. If your file contains mostly text, it will easily drop below 100KB.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Is the compression process secure?</div>
        <p class="faq-a">Completely. Most "free" compression tools make you upload your file to their servers, exposing your private data. LovePDFs runs the compression algorithm directly in your browser using JavaScript and WebAssembly. Your file is never uploaded.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Will my text become blurry after compression?</div>
        <p class="faq-a">No. Text in PDFs is typically stored as vector data, which is completely unaffected by our compression engine. Only rasterized images (photos, scanned pages) will undergo optimization.</p>
      </div>
  </div>
"""
    },
    "jpg-to-pdf": {
        "steps": """
  <ol class="steps-list">
    <li><strong>Upload Images:</strong> Click the file selection area or drag and drop your JPG, PNG, or WebP images. You can select multiple images simultaneously.</li>
    <li><strong>Order Your Pages:</strong> The images will appear as thumbnails. Drag these thumbnails to arrange them in the precise order you want them to appear in your final PDF document.</li>
    <li><strong>Customize Page Settings:</strong> (Optional) Adjust the output settings to fit your needs. You can set the page size (A4, Letter, Auto), define page margins, and choose the orientation (Portrait or Landscape).</li>
    <li><strong>Convert and Save:</strong> Click the 'Convert to PDF' button. Our system will embed your images into a structured PDF document locally and trigger an instant download.</li>
  </ol>
  
  <div style="background: var(--bg2); padding: 1.5rem; border-radius: 12px; margin-top: 2rem; margin-bottom: 2rem; border-left: 4px solid var(--red);">
    <h3 style="margin-top: 0; font-family: 'Fraunces', serif;">Perfect for Compiling Scanned Documents</h3>
    <p style="margin-bottom: 0;">If you've taken photos of your lecture notes, receipts, or legal documents with your phone, sharing them as a bunch of loose JPG files is messy and unprofessional. Converting them into a single, paginated PDF ensures they are viewed in the correct order, on any device, without requiring specialized photo-viewing software.</p>
  </div>
""",
        "faqs": """
  <div class="faq-list">
      <div class="faq-item">
        <div class="faq-q">Does converting JPG to PDF reduce the image quality?</div>
        <p class="faq-a">By default, our tool embeds your images into the PDF structure exactly as they are, without applying additional lossy compression. This ensures your final document looks just as crisp as the original photos.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can I add PNG or WebP images as well?</div>
        <p class="faq-a">Yes! Despite the tool's name, our engine seamlessly accepts JPG, JPEG, PNG, WebP, and BMP image formats. You can mix and match different image types in the same conversion batch.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Are my personal photos uploaded to a server?</div>
        <p class="faq-a">No. We respect your privacy. The conversion from image to PDF happens entirely inside your browser's memory using local processing. We do not have access to your files, and nothing is ever stored on our servers.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">How do I make the images fit the whole page?</div>
        <p class="faq-a">In the tool settings before converting, you can set the margins to "None". This will stretch or scale your image to cover the entire selected paper size (e.g., A4), edge to edge.</p>
      </div>
  </div>
"""
    },
    "pdf-to-word": {
        "steps": """
  <ol class="steps-list">
    <li><strong>Upload the PDF:</strong> Select the PDF document you wish to convert to a Word file by clicking the upload button or dragging the file into the browser window.</li>
    <li><strong>Wait for Analysis:</strong> The tool immediately begins analyzing the document structure. It identifies text blocks, paragraphs, headers, and tabular data using a sophisticated client-side extraction engine.</li>
    <li><strong>Review Conversion:</strong> The process is usually instantaneous. Our engine works to reconstruct the layout so that it matches the original PDF as closely as possible within the constraints of the DOCX format.</li>
    <li><strong>Download Word Document:</strong> Click 'Download Word' to save your new, fully editable .docx file to your device. You can now open it in Microsoft Word, Google Docs, or LibreOffice.</li>
  </ol>
  
  <div style="background: var(--bg2); padding: 1.5rem; border-radius: 12px; margin-top: 2rem; margin-bottom: 2rem; border-left: 4px solid var(--red);">
    <h3 style="margin-top: 0; font-family: 'Fraunces', serif;">Regain Control of Your Content</h3>
    <p style="margin-bottom: 0;">PDFs are designed to be "digital paper" — perfect for viewing, but terrible for editing. Our PDF to Word converter bridges this gap by intelligently reverse-engineering the text positioning data in the PDF and rebuilding it as flowing, editable paragraphs in a Word document, saving you hours of manual re-typing.</p>
  </div>
""",
        "faqs": """
  <div class="faq-list">
      <div class="faq-item">
        <div class="faq-q">Will my converted Word document look exactly like the PDF?</div>
        <p class="faq-a">Our converter strives for high visual fidelity. It reconstructs paragraphs, lists, and basic layouts effectively. However, because PDFs use absolute coordinate positioning and Word uses flow layout, highly complex graphical designs may require minor manual adjustments after conversion.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can this tool convert scanned PDFs?</div>
        <p class="faq-a">This specific tool extracts digital text layers. If your PDF is a flat scanned image (like a photograph of a page), you will need to use our OCR tool first to recognize the text before converting it to an editable format.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Is it safe to convert confidential business documents?</div>
        <p class="faq-a">Yes. Unlike standard online converters that upload your contracts or financial reports to remote servers, our conversion runs securely within your local browser environment. Your confidential data is fully protected from interception or unauthorized storage.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">What software do I need to open the resulting file?</div>
        <p class="faq-a">The tool generates a standard OpenXML (.docx) file. This can be opened natively in Microsoft Word (2007 or newer), Apple Pages, Google Docs, or free alternatives like OpenOffice and LibreOffice.</p>
      </div>
  </div>
"""
    },
    "split-pdf": {
        "steps": """
  <ol class="steps-list">
    <li><strong>Select Document:</strong> Upload the large PDF file you wish to split by dragging it into the drop zone or browsing your computer.</li>
    <li><strong>Choose Splitting Method:</strong> Select how you want to divide the file:
        <ul style="margin-top: 0.5rem; margin-bottom: 0.5rem; color: var(--text2);">
            <li><em>Extract Pages:</em> Select specific individual pages to pull out into a new document.</li>
            <li><em>Custom Ranges:</em> Define specific page ranges (e.g., 1-5, 8-12) to create separate documents for each range.</li>
            <li><em>Fixed Intervals:</em> Split the document automatically every 'X' number of pages.</li>
        </ul>
    </li>
    <li><strong>Visual Selection:</strong> If using the visual mode, simply click the thumbnails of the pages you want to extract. Selected pages will be highlighted.</li>
    <li><strong>Split and Download:</strong> Click 'Split PDF'. Our local processor will instantly separate the pages and download them to your device, often packaged in a ZIP file if multiple documents are generated.</li>
  </ol>
  
  <div style="background: var(--bg2); padding: 1.5rem; border-radius: 12px; margin-top: 2rem; margin-bottom: 2rem; border-left: 4px solid var(--red);">
    <h3 style="margin-top: 0; font-family: 'Fraunces', serif;">Share Only What Matters</h3>
    <p style="margin-bottom: 0;">Sending a 200-page report to a client when they only need to review the 3-page executive summary is unprofessional and wastes bandwidth. Splitting your PDF allows you to extract precise sections, ensuring your recipient gets exactly what they need without the clutter.</p>
  </div>
""",
        "faqs": """
  <div class="faq-list">
      <div class="faq-item">
        <div class="faq-q">Does splitting a PDF damage the original file?</div>
        <p class="faq-a">No, your original file is completely safe. Our tool creates new, independent PDF documents from the pages you select, leaving your source file untouched on your device.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Can I extract just one single page?</div>
        <p class="faq-a">Absolutely. You can use the visual page selector to click a single page, or type a single page number into the custom range box, and hit extract.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">How are multiple split files delivered?</div>
        <p class="faq-a">If your splitting criteria results in multiple separate PDF documents (e.g., splitting every 2 pages), our tool will automatically package them into a single, compressed ZIP file for easy, one-click downloading.</p>
      </div>
      <div class="faq-item">
        <div class="faq-q">Is the splitting process secure and private?</div>
        <p class="faq-a">Yes. We use client-side processing, meaning the splitting logic runs directly in your browser. Unlike other services, we never upload your large, potentially sensitive documents to external servers.</p>
      </div>
  </div>
"""
    }
}

for tool, content in TOOLS_CONTENT.items():
    filepath = os.path.join(tool, 'index.html')
    if not os.path.exists(filepath):
        print(f"Skipping {tool}, file not found.")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace steps
    steps_match = re.search(r'<ol class="steps-list">.*?</ol>', html, re.DOTALL)
    if steps_match:
        html = html[:steps_match.start()] + content['steps'] + html[steps_match.end():]
    
    # Replace FAQs
    faq_match = re.search(r'<div class="faq-list">.*?</div>', html, re.DOTALL)
    if faq_match:
        html = html[:faq_match.start()] + content['faqs'] + html[faq_match.end():]
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Updated {tool} successfully.")
