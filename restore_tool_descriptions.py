#!/usr/bin/env python3
"""
Restore tool-specific 'About' explanation sections to every tool page.
Injects a clean <div class="tool-about"> block at the TOP of the <section class="seo-content"> section.
Does NOT duplicate steps, benefits, or FAQs — those already exist in the section below.
Safe to re-run: checks for existing tool-about block and skips if already present.
"""

import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

NON_TOOL_DIRS = {
    'scripts', 'blog-posts', '__pycache__', '.git', 'node_modules',
    'pdf-tools', 'image-tools', 'converter-tools', 'calculator-tools',
}

# Per-tool rich descriptions: (what_is, use_cases, advanced, privacy_note)
TOOL_DATA = {
    'compress-pdf': (
        "PDF compression reduces file sizes without compromising document quality. Large PDFs cause problems with email attachments, cloud storage limits, and slow upload speeds. Compressing your PDF shrinks it down — sometimes by up to 80% — while keeping text crisp and images readable.",
        "Graphic designers compress high-resolution portfolios before sending to clients. Students reduce thesis and assignment sizes for online submission portals. Businesses compress invoices, reports, and presentations to stay within email attachment limits. Anyone sharing documents via WhatsApp, Drive, or Dropbox benefits from smaller files.",
        "Our browser-based compressor uses pdf-lib and canvas re-rendering to strip unnecessary metadata, optimize embedded images, and reduce font overhead. All processing happens on your device — no server upload, no file size cap, no waiting in queues.",
        "compress PDF without uploading"
    ),
    'merge-pdf': (
        "Merging PDFs combines multiple separate files into a single, unified document. Whether you're assembling a report from multiple chapters, combining scanned pages, or packaging documents for a client, a merged PDF is easier to share, print, and archive.",
        "Students merge lecture notes, references, and assignments into one study pack. Lawyers compile contracts, exhibits, and affidavits into a single case file. HR professionals bundle offer letters, forms, and policies into employee onboarding packets. Businesses combine vendor quotes and purchase orders for procurement records.",
        "Our merger preserves the original page order, bookmarks, and links from each source file. Drag-and-drop reordering lets you arrange files before combining. Everything runs in your browser using WebAssembly — your documents never leave your device.",
        "merge PDF files without uploading"
    ),
    'split-pdf': (
        "Splitting a PDF lets you extract specific pages or sections from a larger document. Instead of sharing a whole 200-page report when someone only needs pages 5–12, you can split out exactly what's needed — saving time and avoiding information overload.",
        "Teachers extract individual chapters from textbooks for assignments. Lawyers separate individual exhibits from large case files. HR departments pull individual employee records from bulk exports. Publishers split book manuscripts into chapters for editorial review.",
        "Choose from three split modes: by page range, every N pages, or extract individual pages. The original document stays untouched — you're always working with a copy. Processing is instant and happens entirely in your browser.",
        "split PDF without uploading"
    ),
    'rotate-pdf': (
        "Rotating PDF pages fixes orientation issues caused by scanned documents, phone cameras, or incorrectly exported files. A single misaligned page in a report can look unprofessional — rotating it takes seconds and makes your document presentation-ready.",
        "Scanned documents often come out sideways or upside down. Rotate individual pages or the entire PDF to fix orientation before sharing. Useful for architects rotating blueprint pages, photographers correcting portrait vs. landscape scans, and students fixing scanned notes.",
        "Rotate by 90°, 180°, or 270° clockwise or counter-clockwise. Apply rotation to all pages at once or select specific pages. Changes are applied client-side — the output file is ready to download immediately with no quality loss.",
        "rotate PDF pages without uploading"
    ),
    'organize-pdf': (
        "Organizing a PDF lets you reorder, delete, or rearrange pages to get your document exactly how you want it. When you receive a multi-page scan in the wrong order, or need to remove blank pages from a document, this tool gives you full control.",
        "Business professionals reorder sections of long reports before final distribution. Students rearrange chapters in compiled study guides. Administrators remove blank filler pages from scanned government forms. Anyone who works with long documents benefits from being able to organize pages visually.",
        "Drag page thumbnails to reorder them. Click to select and delete unwanted pages. Preview each page before finalizing. All operations are done locally in your browser — changes are non-destructive until you download the result.",
        "organize PDF pages without uploading"
    ),
    'edit-pdf': (
        "Editing a PDF lets you add text, draw annotations, highlight passages, and make corrections directly on the document — without needing to convert it first. PDFs are often the final format for contracts, forms, and reports, so being able to edit them in place saves a lot of back-and-forth.",
        "Freelancers annotate client contracts before signing. Students highlight and add margin notes to study materials. Managers add comments and corrections to draft reports. Anyone filling out a PDF form benefits from direct text editing rather than printing and scanning.",
        "Add freeform text anywhere on the page. Draw rectangles, circles, or freehand paths. Insert sticky note annotations. Highlight existing text. All edits are layered on top of the original PDF non-destructively and saved into the output file.",
        "edit PDF online without uploading"
    ),
    'sign-pdf': (
        "Signing a PDF digitally lets you add your signature to contracts, agreements, and forms without printing a single page. A legally valid e-signature on a PDF is accepted by most institutions, governments, and businesses worldwide.",
        "Freelancers sign client agreements before starting projects. Employees sign offer letters and HR forms. Students sign scholarship applications and enrollment forms. Anyone who regularly deals with contracts or official paperwork benefits from browser-based PDF signing.",
        "Draw your signature with a mouse or trackpad, type it in a signature font, or upload an image of your handwritten signature. Drag it to the correct position on the page, resize it, and download the signed PDF instantly.",
        "sign PDF without uploading"
    ),
    'protect-pdf': (
        "Password-protecting a PDF adds a layer of security that prevents unauthorized access to sensitive documents. Whether it's a legal contract, financial report, or personal record, a password ensures only the intended recipient can open and read the file.",
        "Lawyers protect confidential client documents before sharing via email. Accountants lock financial statements sent to clients or auditors. HR managers secure offer letters and salary information. Anyone sharing sensitive information in PDF format benefits from password protection.",
        "Choose an owner password to restrict editing, copying, and printing — or a user password that requires a code to open the file at all. Encryption happens locally in your browser using pdf-lib — no password is ever transmitted to a server.",
        "protect PDF with password without uploading"
    ),
    'unlock-pdf': (
        "Unlocking a PDF removes the password restriction so you can open, read, copy, and edit the document normally again. If you've lost the password to a PDF you own, or received an unlocked PDF that you need to work with, this tool lifts those restrictions.",
        "Professionals who created password-protected PDFs but lost the password can recover access. Users who received locked PDFs from clients or institutions can unlock them for local editing. Anyone archiving old protected PDFs for long-term storage benefits from removing password requirement.",
        "Enter the current password to authorize the unlock, then download the restriction-free version. The unlocking process runs entirely in your browser — your password and file content are never transmitted anywhere.",
        "unlock PDF without uploading"
    ),
    'pdf-to-word': (
        "Converting a PDF to Word (DOCX) lets you edit the document's text and layout in Microsoft Word or Google Docs. PDFs are great for sharing but terrible for editing — converting to Word gives you back full control over the content.",
        "Students edit PDF lecture slides for note-taking in Word. Professionals revise contracts received in PDF into editable Word documents. Writers convert published PDF articles back to editable text for reference. Anyone who needs to make changes to a finalized document benefits from PDF-to-Word conversion.",
        "Our converter preserves paragraph structure, headings, and text formatting as closely as possible. Complex layouts with tables and columns are handled intelligently. All conversion happens client-side — your document never leaves your device.",
        "convert PDF to Word without uploading"
    ),
    'word-to-pdf': (
        "Converting a Word document to PDF ensures your document looks identical on every device — no font substitutions, no layout shifts, no version compatibility issues. PDFs are the standard for sharing finalized documents professionally.",
        "Job seekers convert their Word resumes to PDF before submitting applications. Students convert assignments for online submission portals that require PDF format. Businesses convert reports and proposals to PDF before sending to clients. Anyone sharing a finalized document should convert to PDF first.",
        "Upload your DOCX file and convert it to a high-fidelity PDF that preserves fonts, images, tables, and page layout. The conversion runs in your browser using a client-side rendering engine — no server upload required.",
        "convert Word to PDF without uploading"
    ),
    'jpg-to-pdf': (
        "Converting JPG images to PDF lets you create a single, shareable document from one or multiple photos. A PDF file is universally readable, maintains image quality, and is far more professional than attaching a zip of photos.",
        "Students photograph handwritten notes and convert them to a single PDF for submission. Real estate agents convert property photos to a PDF presentation. Travelers create digital albums in PDF format for easy sharing. Anyone who needs to compile images into a document format benefits from JPG-to-PDF conversion.",
        "Upload one or multiple JPG images and choose the output page size (A4, Letter, etc.) and orientation. Images are embedded at maximum quality. Multiple images are arranged one per page in the order you upload them.",
        "convert JPG to PDF without uploading"
    ),
    'pdf-to-jpg': (
        "Converting a PDF to JPG extracts each page as a high-quality image file. This is essential when you need to embed a PDF page in a presentation, share a document preview on social media, or use a specific page as an image in another design.",
        "Marketers extract PDF report pages to share as images on social media. Designers pull individual pages for use in presentations or mockups. Developers need page screenshots for documentation or testing. Educators extract textbook pages as images for online course materials.",
        "Each page of your PDF is rendered as a high-resolution JPG. Choose the output quality level to balance image clarity against file size. All rendering is done client-side using PDF.js — no server upload required.",
        "convert PDF to JPG without uploading"
    ),
    'pdf-to-excel': (
        "Converting a PDF to Excel extracts tabular data from your document into editable spreadsheet cells. When you receive financial reports, data tables, or statistics in PDF format, converting to Excel lets you analyze, sort, and chart the data properly.",
        "Accountants extract financial tables from PDF bank statements for reconciliation. Researchers pull data tables from PDF reports into Excel for statistical analysis. Business analysts convert PDF dashboards into editable spreadsheets. Anyone who needs to work with numeric data trapped in a PDF benefits from this conversion.",
        "Our tool identifies table structures within the PDF and maps them to Excel rows and columns. Text, numbers, and formatting are preserved as faithfully as possible. Processing is entirely browser-based and private.",
        "convert PDF to Excel without uploading"
    ),
    'excel-to-pdf': (
        "Converting an Excel spreadsheet to PDF creates a print-ready, universally readable version of your data. PDFs preserve your column widths, formatting, and formulas (as values) exactly as they appear — no more layout surprises when sharing with others.",
        "Accountants share financial reports in PDF format for non-editable distribution. Managers send formatted data tables to clients in PDF rather than raw Excel files. Researchers publish data appendices in PDF alongside academic papers. Anyone sharing finalized tabular data benefits from Excel-to-PDF conversion.",
        "Upload your XLSX or CSV file and convert it to a clean, formatted PDF. Your column headers, row data, and basic cell formatting are preserved in the output. Processing happens locally in your browser.",
        "convert Excel to PDF without uploading"
    ),
    'pdf-to-ppt': (
        "Converting a PDF to PowerPoint extracts the content of each page into editable slides. If you received a presentation as a PDF and need to edit or re-present the slides, converting to PPT gives you full control over the content again.",
        "Teachers receive PDF lectures and convert them to editable PowerPoint for classroom customization. Consultants convert delivered PDF proposals back to slides for internal review. Students convert study material PDFs into slide decks for presentation practice.",
        "Each PDF page becomes a slide in the output PPTX file. Text blocks, images, and layout are mapped to PowerPoint elements as closely as possible. Conversion runs client-side — your document stays on your device.",
        "convert PDF to PowerPoint without uploading"
    ),
    'ppt-to-pdf': (
        "Converting a PowerPoint to PDF locks in your presentation design — fonts, colors, transitions, and animations are fixed as static slides. A PDF presentation looks identical on every device and can be read without PowerPoint installed.",
        "Speakers share their deck as a PDF handout after presentations. Students submit PDF versions of presentations for grading. Professionals send presentation PDFs to clients who may not have Office installed. Anyone distributing finalized slides should convert to PDF first.",
        "Upload your PPTX file and convert it to PDF with each slide on its own page. Fonts, images, and layout are rendered faithfully. The conversion runs client-side in your browser.",
        "convert PowerPoint to PDF without uploading"
    ),
    'html-to-pdf': (
        "Converting HTML to PDF captures a webpage or HTML file as a static, printable document. This is useful for archiving web content, creating reports from HTML templates, or generating PDFs from dynamic content for distribution.",
        "Developers generate PDF reports from HTML invoice templates. Archivists save website content as PDF for offline reference. Designers export HTML email templates as PDF previews. Anyone building document generation workflows benefits from HTML-to-PDF conversion.",
        "Paste an HTML snippet or upload an HTML file and convert it to PDF with preserved layout, fonts, and images. CSS styles are applied during rendering. Conversion runs in your browser using a client-side rendering engine.",
        "convert HTML to PDF without uploading"
    ),
    'compress-image': (
        "Image compression reduces file sizes of JPG, PNG, and WebP images without visible quality degradation. Smaller images load faster on websites, take up less storage, and are easier to share — making compression a must for web optimization and email attachments.",
        "Web developers compress hero images and product photos to improve page load speed. Bloggers reduce image file sizes before uploading to their CMS. Email marketers compress images to stay within attachment size limits. Social media managers optimize photos before scheduling posts.",
        "Our compressor uses canvas-based rendering to re-encode images at your chosen quality setting. Adjust the compression slider to find the perfect balance between file size and visual quality. All processing happens in your browser — no upload required.",
        "compress images without uploading"
    ),
    'resize-image': (
        "Resizing an image changes its pixel dimensions while preserving aspect ratio or allowing custom width×height. Whether you need a specific resolution for a website, a certain size for a print layout, or a smaller image for faster loading, resizing is the first step.",
        "Social media managers resize photos to the exact pixel dimensions required by each platform. Web developers resize thumbnails and hero images to fit their layout grid. E-commerce sellers resize product images to meet marketplace requirements. Designers prepare assets at multiple resolutions for responsive sites.",
        "Enter target dimensions in pixels or a percentage scale. Choose whether to maintain aspect ratio or stretch to fit. Our tool resizes instantly in the browser using the canvas API — no server upload, no watermark, no size limit.",
        "resize images without uploading"
    ),
    'crop-image': (
        "Cropping an image removes unwanted outer areas and focuses on the most important part of the photo. Whether you're removing a distracting background, changing aspect ratio, or zooming into a subject, cropping is one of the most fundamental photo edits.",
        "Photographers crop portraits to remove distracting backgrounds. Social media managers crop images to the exact aspect ratios platforms require (1:1 for Instagram, 16:9 for Twitter). E-commerce sellers crop product photos to a clean square format. Web designers crop hero images to focus on key content.",
        "Drag the crop handles to select the area you want to keep. Enter exact dimensions or choose from preset aspect ratios. The crop is applied instantly and you can download the result immediately — all without leaving your browser.",
        "crop images without uploading"
    ),
    'jpg-to-png': (
        "Converting JPG to PNG changes the image format from a lossy, compressed format to a lossless one. PNG files support transparency (alpha channel) which JPG doesn't — essential for logos, icons, and images that need a transparent background.",
        "Graphic designers convert JPG logos to PNG to use them on differently colored backgrounds. Web developers convert product photos to PNG for transparent overlays. UI designers prepare icons and illustrations in PNG for use in apps and websites. Anyone who needs a transparent background must use PNG format.",
        "Upload your JPG and instantly receive a PNG file with the same visual quality. If the original JPG has no transparent areas, the output PNG will have a white background. Conversion is instant and runs entirely in your browser.",
        "convert JPG to PNG without uploading"
    ),
    'png-to-jpg': (
        "Converting PNG to JPG significantly reduces file size at the cost of some quality — perfect for web images, email attachments, and scenarios where transparency is not needed. JPG files are typically 60–80% smaller than equivalent PNG files.",
        "Web developers convert PNG screenshots and images to JPG for faster website loading. Bloggers convert product and feature images from PNG to JPG to reduce page weight. Anyone sharing images via email or social media benefits from smaller JPG files.",
        "Upload your PNG file, choose an output quality level (higher = better quality, larger file), and download the converted JPG. Background transparency in the PNG is filled with white in the JPG output. Conversion runs entirely in your browser.",
        "convert PNG to JPG without uploading"
    ),
    'crop-pdf': (
        "Cropping a PDF trims the visible page area to remove white margins, cut out unwanted content, or resize pages to a specific dimension. This is particularly useful for scanned documents with large borders, or for extracting a specific region of a page.",
        "Researchers crop PDF papers to remove oversized margins before printing. Designers crop PDF artwork proofs to focus on the design area. Students crop scanned textbook pages to remove headers and footers. Administrators crop large A3-format documents to A4 for standard printing.",
        "Define the crop box by entering margin values or dragging handles on the page preview. Apply the crop to all pages at once or specific pages. The original content outside the crop box is hidden but not deleted — another crop can restore it.",
        "crop PDF pages without uploading"
    ),
    'resize-pdf': (
        "Resizing a PDF changes the physical page dimensions — for example, scaling an A3 document to A4, or changing a letter-size PDF to a custom size. This is different from compression — it changes the page geometry rather than the file encoding.",
        "Print shops resize submitted PDF artwork to match their standard paper sizes. Architects scale A1 blueprint PDFs down to A4 for email distribution. Teachers resize oversized presentation PDFs to standard A4 for printing handouts. Anyone preparing documents for specific paper sizes benefits from PDF resizing.",
        "Choose from preset page sizes (A4, A3, Letter, Legal) or enter a custom width and height in millimetres. Content is scaled to fit the new dimensions while maintaining aspect ratio. Processing runs locally in your browser.",
        "resize PDF pages without uploading"
    ),
    'rotate-pdf': (
        "Rotating PDF pages fixes orientation issues caused by scanned documents, phone cameras, or incorrectly exported files. A single misaligned page in a report looks unprofessional — rotating it takes seconds.",
        "Scanned documents often come out sideways. Rotate individual pages or the whole PDF in 90° increments. Architects rotate blueprint pages, photographers fix portrait/landscape orientation, and students correct scanned notes.",
        "Select specific pages or apply to all. Choose 90°, 180°, or 270° rotation. Changes happen in the browser — no server upload needed.",
        "rotate PDF pages without uploading"
    ),
    'add-watermark-pdf': (
        "Adding a watermark to a PDF stamps a visible text or image overlay on your document pages — used for branding, marking documents as drafts, confidential, or copyrighted, or simply adding ownership information.",
        "Legal firms watermark draft contracts with 'DRAFT' before sending for review. Photographers watermark portfolio PDFs with their studio name. Businesses mark sensitive reports as 'CONFIDENTIAL'. Publishers add copyright watermarks to preview PDFs.",
        "Enter your watermark text, choose font size, opacity, rotation angle, and position. The watermark is rendered on every page and baked into the PDF. Processing is local — your document never leaves your device.",
        "add watermark to PDF without uploading"
    ),
    'add-page-numbers-pdf': (
        "Adding page numbers to a PDF inserts automatic numbering into the header or footer of each page. Multi-page reports, manuals, and academic papers all benefit from page numbers to help readers navigate and reference content.",
        "Report writers add page numbers before submitting to clients or managers. Students add numbering to thesis documents for academic submission. Publishers add page numbers to book layouts before printing. Legal professionals number court submissions for easy reference during proceedings.",
        "Choose the position (top-left, top-center, top-right, bottom-left, bottom-center, bottom-right), start number, and format. Page numbers are added by pdf-lib rendering — processing is entirely local and private.",
        "add page numbers to PDF without uploading"
    ),
    'extract-pages-pdf': (
        "Extracting pages from a PDF lets you pull out specific pages from a large document and save them as a new, standalone PDF. Instead of sharing a 100-page report when someone needs only 3 pages, extract just what's needed.",
        "Researchers extract specific chapters from long academic PDFs. Lawyers extract individual witness statements from large case file documents. Publishers extract chapter previews for marketing use. Managers extract executive summary pages from full reports for quick sharing.",
        "Enter the page numbers or ranges you want to extract. The resulting PDF contains only the extracted pages in the order specified. Processing is instant and browser-based — nothing is uploaded to a server.",
        "extract PDF pages without uploading"
    ),
    'remove-pages-pdf': (
        "Removing pages from a PDF lets you delete unwanted content — blank pages, confidential appendices, cover sheets, or anything else you don't want in the final document — without touching the rest.",
        "HR professionals remove salary appendices before sharing policy documents. Editors remove placeholder pages from book drafts. Students remove irrelevant reference pages before submitting assignment PDFs. Anyone simplifying or curating a long document benefits from page removal.",
        "Select individual pages or ranges to delete. The output PDF contains all remaining pages in their original order. Processing runs entirely in your browser — the original file is never modified.",
        "remove PDF pages without uploading"
    ),
    'extract-images-pdf': (
        "Extracting images from a PDF saves all embedded photos and graphics as individual image files. If you received a PDF with images you need to reuse — product photos, charts, diagrams — this tool pulls them out at their original quality.",
        "Designers extract product images from supplier PDF catalogs for use in marketing materials. Researchers extract figures and charts from academic PDFs for presentations. Publishers extract artwork from submitted PDF manuscripts. Anyone needing the raw image assets from a PDF document benefits.",
        "All detected images in the PDF are extracted and offered as individual JPG or PNG downloads. Resolution is preserved from the original embedded image. Everything runs in your browser — no server upload required.",
        "extract images from PDF without uploading"
    ),
    'ocr-extract-text': (
        "OCR (Optical Character Recognition) reads scanned or image-based PDFs and extracts the text content, making it searchable and copyable. A scanned invoice or photograph of a document is unreadable as text — OCR converts it into real, selectable characters.",
        "Businesses digitize paper invoices and contracts by scanning and running OCR. Researchers extract text from scanned academic papers for citation. Administrators convert scanned government forms into editable text. Anyone dealing with old paper documents that have been scanned to PDF benefits from OCR.",
        "Our browser-based OCR uses Tesseract.js to recognize text in images embedded in your PDF. Supported languages include English plus many others. The extracted text is displayed and available for copy-paste — all processed locally, privately.",
        "extract text from PDF without uploading"
    ),
    'edit-pdf-metadata': (
        "PDF metadata includes the document's title, author, subject, keywords, and creation date stored invisibly inside the file. Editing metadata is important for document management, SEO for web-published PDFs, and removing personal information before sharing.",
        "Businesses update author and title metadata in PDFs before publishing to their website for SEO benefit. Professionals remove personal author names before sharing documents externally. Archivists set correct creation dates and keywords for document management systems. Publishers update title and subject fields across released PDF editions.",
        "Edit title, author, subject, keywords, and other metadata fields. Clear existing values or update them to new ones. Changes are applied non-destructively and the updated file is downloaded immediately. Processing is browser-based and private.",
        "edit PDF metadata without uploading"
    ),
    'flatten-pdf': (
        "Flattening a PDF merges all interactive form fields, annotations, and layers into the static page content. Once flattened, form fields can no longer be edited — but the data is permanently preserved in the visual layout, which is important for archiving completed forms.",
        "Businesses flatten completed intake forms before archiving or sharing. Legal departments flatten annotation layers from reviewed contracts before final distribution. Accountants flatten completed tax forms before long-term filing. Anyone who needs to permanently lock in filled form data before sharing benefits from flattening.",
        "Flattening removes all interactive layers (form fields, checkboxes, text annotations) and merges them into the static page background. The resulting PDF is smaller and compatible with older PDF viewers that don't support forms. Runs entirely in your browser.",
        "flatten PDF without uploading"
    ),
    'grayscale-pdf': (
        "Converting a PDF to grayscale removes all color from the document, rendering everything in shades of grey. This reduces file size, reduces print ink usage, and makes documents readable on black-and-white printers without color loss artifacts.",
        "Students convert color lecture slides to grayscale for cheaper black-and-white printing. Offices reduce printing costs by greyscaling color reports before printing. Publishers prepare grayscale versions of PDFs for print-on-demand services that charge extra for color pages. Anyone printing at scale benefits from grayscale conversion.",
        "Every page is rendered into greyscale using a luminance conversion formula that preserves readability of text and image detail. The output PDF is typically 20–40% smaller than the color original. Processing runs locally in your browser.",
        "convert PDF to grayscale without uploading"
    ),
    'deskew-pdf': (
        "Deskewing a PDF corrects pages that were scanned at a slight angle — the most common problem with flatbed scanner output. Even a 2-degree tilt makes a document look sloppy and can interfere with OCR accuracy.",
        "Office administrators deskew batches of scanned contracts and letters before archiving. Researchers deskew scanned academic papers before running OCR. Legal clerks deskew court document scans before electronic filing. Anyone processing large volumes of scanned documents benefits from automatic deskewing.",
        "Our deskew algorithm detects the rotation angle of each page and corrects it automatically. Pages are rotated by the detected amount and the result is a straight, professional-looking document. All processing is done in your browser.",
        "deskew PDF without uploading"
    ),
    'repair-pdf': (
        "Repairing a PDF attempts to fix structural errors and corruption in damaged PDF files. A corrupt PDF may fail to open, show blank pages, or display garbled content — the repair tool tries to reconstruct the file structure and recover as much content as possible.",
        "Users whose PDFs were interrupted during download or email transfer can attempt repair to recover the file. Database exports that produce malformed PDFs can be repaired before use. Legacy PDF files with deprecated encoding sometimes need repair to open in modern viewers.",
        "Our repair tool attempts to parse and reconstruct the cross-reference table, object streams, and page tree of the PDF. It uses pdf-lib's repair mode to salvage damaged files. Success depends on the nature of the corruption — partial recovery is common.",
        "repair PDF without uploading"
    ),
    'redact-pdf': (
        "Redacting a PDF permanently blacks out sensitive information before sharing. Unlike highlighting or drawing black boxes on a layer, true redaction removes the underlying text data so it cannot be uncovered by copy-paste or PDF extraction tools.",
        "Law firms redact confidential client information from court submissions. Healthcare providers redact patient names from case study documents. Government agencies redact classified information from FOIA request responses. Any professional sharing documents that contain sensitive data they need to conceal uses redaction.",
        "Select areas on each page to redact using a rectangular selection tool. The selected regions are filled with solid black and the underlying text data is removed from the PDF structure. Processing is browser-based — your sensitive document never leaves your device.",
        "redact PDF without uploading"
    ),
    'sign-pdf': (
        "Signing a PDF digitally lets you add your signature to contracts, agreements, and forms without printing. E-signatures are accepted by most institutions, governments, and businesses worldwide as legally binding.",
        "Freelancers sign client agreements. Employees sign offer letters. Students sign scholarship applications. Anyone dealing with contracts or official forms benefits from digital signing.",
        "Draw your signature, type it, or upload a handwritten image. Drag and position it on the page, then download the signed PDF instantly.",
        "sign PDF without uploading"
    ),
    'compare-pdf': (
        "Comparing two PDFs side-by-side highlights differences between versions — changed text, added or removed content, shifted formatting. Instead of manually scanning two documents, the comparison tool marks changes automatically.",
        "Legal teams compare contract drafts to identify clause changes between versions. Writers compare edited versions of documents to review revision history. Developers compare exported PDF reports to catch rendering regressions. Accountants compare financial statement versions to spot discrepancies.",
        "Upload the original and revised PDFs and the comparison engine highlights text that has been added, removed, or changed. Differences are shown with color coding. Processing is browser-based and private.",
        "compare PDF files without uploading"
    ),
    'alternate-mix-pdf': (
        "Alternate-mix interleaving merges two PDFs by alternating their pages — page 1 from doc A, page 1 from doc B, page 2 from doc A, page 2 from doc B, and so on. This is used when a double-sided document has been scanned as two separate single-side runs.",
        "Office workers combine front-side and back-side scans of double-sided documents into a single correctly ordered PDF. Archivists interleave odd and even page batches from duplex scanning operations. Anyone who scans documents one side at a time benefits from alternate mixing.",
        "Upload the two PDFs (front pages and back pages) and the tool merges them in alternating page order. Optionally reverse the second document's order if it was scanned last-page-first. Processing runs in your browser.",
        "interleave PDF pages without uploading"
    ),
    'header-footer-pdf': (
        "Adding headers and footers to a PDF places repeating text at the top or bottom of every page — useful for company names, document titles, page numbers, dates, or confidentiality notices.",
        "Legal firms add matter numbers and client names to document footers. Businesses add company name and date to report headers. Publishers add chapter titles and page numbers to book PDFs. Academic writers add thesis title and student ID to submission headers.",
        "Define separate header and footer text, choose alignment (left, center, right), set font size, and optionally include auto page numbering. Applied to all pages simultaneously. Output is immediately downloadable.",
        "add header and footer to PDF without uploading"
    ),
    'nup-pdf': (
        "N-up PDF printing places multiple pages from your document onto a single sheet — 2-up means two pages per sheet, 4-up means four pages per sheet, and so on. This is the digital equivalent of 'booklet printing' and significantly reduces paper and printing costs.",
        "Students print 4-up lecture slides to save paper in revision sessions. Businesses print 2-up handouts for meetings. Event organizers print agendas 4-up for larger attendee groups. Anyone printing multi-page documents benefits from N-up layouts.",
        "Choose 2-up, 4-up, 6-up, or 8-up layout. Pages are arranged left-to-right then top-to-bottom in reading order. The output is a new PDF with the multi-page layout ready for printing on standard paper.",
        "combine PDF pages for printing without uploading"
    ),
    'pdf-to-text': (
        "Extracting text from a PDF saves all the document's readable text as a plain .txt file. This is useful for searching, analysis, language processing, importing into other software, or simply copying content without needing to read a PDF viewer.",
        "Journalists extract text from PDF reports for word-frequency analysis. Developers extract PDF invoice text for parsing and data entry. Researchers extract article text for plagiarism checking or sentiment analysis. Anyone who needs to work with the text content of a PDF document programmatically benefits.",
        "Text is extracted page-by-page using PDF.js's text layer renderer, which preserves reading order as faithfully as the PDF encoding allows. The output is a UTF-8 plain text file. Processing happens entirely in your browser.",
        "extract text from PDF without uploading"
    ),
    'pdf-to-pdfa': (
        "PDF/A is an ISO-standardized archival format designed for long-term preservation. Converting to PDF/A embeds all fonts, color profiles, and resources into the file — ensuring it can be rendered correctly decades from now without any external dependencies.",
        "Government agencies require PDF/A format for official document submissions. Libraries and archives convert PDFs to PDF/A for permanent digital preservation. Legal departments archive contracts and agreements in PDF/A to ensure long-term readability. Academic journals accept PDF/A submissions for archival purposes.",
        "The conversion embeds all fonts, sets a color profile, and removes features not permitted in PDF/A (like JavaScript, encryption, or external references). The resulting PDF/A file is fully compliant for archival submission.",
        "convert PDF to PDF/A without uploading"
    ),
    'remove-annotations-pdf': (
        "Removing annotations from a PDF deletes all sticky notes, highlights, comments, underlines, and drawing markup that reviewers have added — giving you a clean, annotation-free version of the document.",
        "Document reviewers share their annotated version for input, then produce a clean final copy without markups. Publishers strip editor comments before releasing final PDFs. Legal teams remove internal review notes before submitting court documents. Teachers remove their draft feedback before returning student papers.",
        "All annotation objects in the PDF are identified and removed from the page content and object tree. The underlying text and images remain untouched. Processing runs entirely in your browser.",
        "remove PDF annotations without uploading"
    ),
    'password-generator': (
        "A password generator creates random, cryptographically strong passwords instantly. Human-invented passwords are predictable — common words, keyboard walks, or personal dates. A generated password is truly random and exponentially harder to crack.",
        "IT administrators generate temporary passwords for new employee accounts. Developers generate API keys and secrets for application configuration. Security-conscious individuals generate unique passwords for each new website registration. Anyone setting up a new account should use a generated password rather than a memorable one.",
        "Choose your desired length, and which character sets to include — uppercase, lowercase, numbers, and symbols. Copy the generated password directly to your clipboard. Generation happens entirely in your browser — no password is ever transmitted anywhere.",
        "generate strong passwords privately"
    ),
    'qr-code-generator': (
        "A QR code encodes text, URLs, contact information, or any data into a scannable 2D barcode. Scanning with a phone camera instantly opens the encoded URL, displays the text, or saves the contact — no typing required.",
        "Business owners add QR codes to business cards, menus, and signage for instant mobile access. Event organizers print QR codes for registration check-in. Teachers share resource links as QR codes in printed handouts. Marketers add QR codes to print advertisements to drive online traffic.",
        "Type or paste any text or URL, generate the QR code instantly, and download as PNG. All generation happens in your browser using a client-side QR library — your data is never sent to a server.",
        "generate QR codes without uploading"
    ),
    'color-picker': (
        "A color picker lets you select colors visually or enter HEX, RGB, or HSL values and convert between formats. It also helps you identify and copy the exact color code you need for design work, web development, or brand style guides.",
        "Web designers pick brand colors and copy their HEX codes for use in CSS. Graphic designers identify color values from reference images. Developers convert between HEX, RGB, and HSL formats for different coding contexts. Brand managers specify exact color codes for consistency across materials.",
        "The color picker shows a real-time preview of your selected color and displays all equivalent values — HEX, RGB, and HSL — simultaneously. Click any value to copy it to your clipboard instantly. Works entirely in your browser.",
        "pick colors privately"
    ),
    'json-formatter': (
        "A JSON formatter takes raw, minified, or poorly indented JSON data and reformats it with proper indentation, line breaks, and syntax highlighting — making it human-readable and easy to debug.",
        "Developers paste API response JSON to inspect structure before writing parsing code. Backend engineers debug malformed JSON by formatting and validating it. Data analysts format JSON exports for readability. Anyone working with JSON data in any context benefits from a quick formatting tool.",
        "Paste your JSON, click Format, and instantly see a properly indented, colored version. The tool also validates your JSON and highlights syntax errors. Formatting and validation run entirely in your browser — your data is never transmitted.",
        "format JSON privately"
    ),
    'email-validator': (
        "An email validator checks whether an email address has valid syntax — correctly formatted local part, @ symbol, and domain. It catches typos and formatting errors before you send to an address or add it to a database.",
        "Developers validate email fields in form submissions before accepting registrations. Marketers clean email lists by removing malformed addresses. Customer support teams validate emails before adding contacts to CRM systems. Anyone who collects email addresses benefits from validation.",
        "Enter one or multiple email addresses and get an instant pass/fail result based on RFC 5322 syntax rules. The tool checks for common errors: missing @, invalid characters, bad TLD format, and more. Validation runs locally in your browser.",
        "validate email addresses privately"
    ),
    'csv-to-excel': (
        "Converting a CSV to Excel (XLSX) transforms a plain comma-separated text file into a properly formatted spreadsheet with cells, columns, and optional data type detection. CSVs open correctly in Excel but lose formatting — converting produces a native XLSX file.",
        "Data analysts convert database CSV exports to Excel for further analysis with formulas and charts. Finance teams convert accounting software exports to Excel for reporting. Operations teams convert bulk data exports to Excel for sorting and filtering. Anyone receiving data in CSV format benefits from converting to Excel.",
        "Upload your CSV file and download a properly formatted XLSX with each field in its own column. Column headers from the first row are preserved. Conversion happens entirely in your browser using SheetJS.",
        "convert CSV to Excel without uploading"
    ),
    'loan-calculator': (
        "A loan calculator computes your monthly payment, total interest paid, and total repayment amount for any loan — mortgage, car loan, personal loan, or student loan — based on the principal, interest rate, and loan term.",
        "Home buyers calculate mortgage payments before applying to ensure affordability. Car buyers compare loan terms from different lenders. Students estimate monthly repayment obligations before accepting education loans. Anyone considering taking on debt benefits from understanding the numbers upfront.",
        "Enter the loan amount, annual interest rate, and term in months or years. The calculator instantly shows monthly payment, total interest, and total repayment using the standard amortization formula. Everything runs in your browser.",
        "calculate loan payments privately"
    ),
    'currency-converter': (
        "A currency converter calculates the equivalent value of one currency in another using up-to-date exchange rates. Whether you're planning travel, making international payments, or comparing prices abroad, quick conversion is essential.",
        "Travelers check exchange rates before converting cash or making purchases abroad. Online shoppers compare prices in foreign currencies against their local equivalent. Businesses convert invoice amounts between billing and payment currencies. Importers and exporters track exchange rate impacts on their costs.",
        "Select source and target currencies, enter an amount, and get the converted value instantly. Rates are fetched from a public exchange rate API. Conversion logic runs in your browser.",
        "convert currencies privately"
    ),
    'date-calculator': (
        "A date calculator finds the difference between two dates in days, weeks, months, and years — or adds/subtracts a number of days from a date to find a future or past date. Essential for deadline planning, contract durations, and milestone tracking.",
        "Project managers calculate exactly how many days until a deadline. HR professionals calculate employment durations for payroll or benefits. Lawyers calculate contract expiry dates. Students plan revision schedules by counting days until exams.",
        "Enter a start date and end date to see the difference in multiple units. Or enter a date and a number of days to find the resulting date. All calculation runs in your browser — no server needed.",
        "calculate date differences privately"
    ),
    'bmi-calculator': (
        "A BMI (Body Mass Index) calculator computes your BMI score from your height and weight, and shows how it falls within standard health classification ranges — underweight, healthy, overweight, or obese. BMI is a widely used screening metric for health risk assessment.",
        "Individuals track their BMI as part of personal health monitoring. Healthcare professionals quickly screen patients during check-ins. Fitness coaches use BMI as a baseline metric when creating training plans. Anyone interested in understanding their weight relative to height uses BMI as a starting point.",
        "Enter your height and weight in metric or imperial units. The BMI is calculated instantly using the formula Weight(kg) ÷ Height(m)². Your score is displayed with its WHO classification category. All calculation runs locally in your browser.",
        "calculate BMI privately"
    ),
    'age-calculator': (
        "An age calculator computes your exact age from your date of birth to today — or to any target date — in years, months, weeks, and days. It handles leap years and varying month lengths for precise results.",
        "People check their exact age for legal documents like passport applications and official forms. HR departments calculate employee tenure for benefits milestones. Parents track their child's age in weeks and months during early development. Planners use it to calculate ages at a future date.",
        "Enter your date of birth and an optional 'as of' date. The calculator displays age in years, months, and days — plus total weeks and total days. All calculation runs in your browser.",
        "calculate age privately"
    ),
    'percentage-calculator': (
        "A percentage calculator performs the three most common percentage operations: finding X% of Y, finding what percentage X is of Y, and calculating the percentage change between two numbers. No mental math required.",
        "Students calculate exam score percentages. Shoppers calculate discounts and sale savings. Business analysts calculate growth rates and year-over-year percentage changes. Accountants calculate tax amounts as percentages of income or sales.",
        "Three independent calculators are shown side-by-side. Enter the values for whichever operation you need and get the result instantly. All calculations run in your browser.",
        "calculate percentages privately"
    ),
    'word-counter': (
        "A word counter counts words, characters, sentences, paragraphs, and estimated reading time from any text you paste or type. Essential for writers, students, and content creators who have strict word count requirements.",
        "Students check essay and assignment word counts against academic requirements. Bloggers ensure articles hit the minimum word count for good SEO. Copywriters hit character limits for ad copy in Google Ads or Twitter. Authors track daily writing progress against chapter targets.",
        "Paste or type text in the input area. Word, character, sentence, and paragraph counts update in real time as you type. Reading time is estimated at 200 words per minute. Everything runs in your browser — your text never leaves your device.",
        "count words privately"
    ),
    'gst-calculator': (
        "A GST calculator computes Goods and Services Tax amounts for India's 5%, 12%, 18%, and 28% slab rates. Enter an exclusive or inclusive amount and instantly get the base price, GST amount, and total — with CGST/SGST breakdown.",
        "Small business owners calculate GST on sales invoices and purchase bills. Freelancers add correct GST to client invoices. Consumers check how much GST they're paying on a purchase. Accountants verify GST calculations during tax filing.",
        "Enter an amount, choose the GST rate and whether the amount is GST-exclusive or GST-inclusive. The calculator instantly shows base amount, GST, total, and the CGST/SGST split for intra-state transactions. Runs entirely in your browser.",
        "calculate GST privately"
    ),
    'organize-pdf': (
        "Organizing a PDF lets you visually reorder, delete, or rearrange pages to structure your document exactly how you want. When you receive a multi-page scan in the wrong order or need to remove blank pages, this tool gives you full page-level control.",
        "Business professionals reorder report sections before distribution. Students rearrange chapters in compiled study guides. Administrators remove blank filler pages from scanned government forms. Anyone working with long documents benefits from page-by-page organization.",
        "Drag page thumbnails to reorder. Click to select and delete unwanted pages. Preview each page before finalizing. All operations are done locally in your browser.",
        "organize PDF pages without uploading"
    ),
}

# Default template for tools not specifically listed
DEFAULT_TEMPLATE = (
    "{h1} is a powerful, privacy-first utility that helps you manage and process your files directly in the browser. Without needing to upload anything to a server, you get instant, professional results — securely and for free.",
    "Students, professionals, and individuals use {h1} for a wide range of everyday document and image tasks. Whether you're preparing files for work, study, or personal projects, this tool saves time and eliminates the need for expensive desktop software.",
    "All processing uses modern WebAssembly and JavaScript libraries running entirely in your browser tab. Your files never leave your device. There are no file size limits imposed by a server, and no queues — results are instant.",
    "use {h1} without uploading"
)

# Style block to inject once into <head>
ABOUT_CSS = """
  <style>
    /* ── TOOL ABOUT SECTION ── */
    .tool-about {
      background: var(--card);
      border: 2px solid var(--border);
      border-radius: 20px;
      padding: 2.25rem 2.5rem;
      margin-bottom: 3.5rem;
      position: relative;
      overflow: hidden;
    }
    .tool-about::before {
      content: '';
      position: absolute; top: 0; left: 0; right: 0; height: 3px;
      background: linear-gradient(90deg, var(--red), #FF9A3A);
    }
    .tool-about h2 {
      font-family: 'Fraunces', serif !important;
      font-size: clamp(1.8rem, 4vw, 2.4rem) !important;
      font-weight: 900 !important;
      color: var(--text) !important;
      margin: 0 0 1.25rem !important;
      letter-spacing: -0.02em;
    }
    .tool-about-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 1.25rem;
      margin: 1.5rem 0 0;
    }
    .tool-about-card {
      background: var(--bg2);
      border: 1.5px solid var(--border);
      border-radius: 14px;
      padding: 1.25rem 1.4rem;
      transition: border-color 0.2s;
    }
    .tool-about-card:hover { border-color: rgba(232,50,26,0.3); }
    .tool-about-card h3 {
      font-family: 'Fraunces', serif;
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--red);
      margin: 0 0 0.5rem;
      display: flex; align-items: center; gap: 0.5rem;
    }
    .tool-about-card p {
      margin: 0;
      font-size: 1.05rem;
      line-height: 1.7;
      color: var(--text2);
    }
    .tool-about-intro {
      font-size: 1.2rem;
      line-height: 1.85;
      color: var(--text2);
      margin: 0;
    }
  </style>"""


def get_tool_about_html(tool_id, h1):
    """Return the about section HTML for a given tool."""
    h1_clean = h1.strip()
    if tool_id in TOOL_DATA:
        intro, use_cases, advanced, privacy = TOOL_DATA[tool_id]
    else:
        t = DEFAULT_TEMPLATE
        intro = t[0].format(h1=h1_clean)
        use_cases = t[1].format(h1=h1_clean)
        advanced = t[2].format(h1=h1_clean)
        privacy = t[3].format(h1=h1_clean)

    return f"""
  <!-- TOOL ABOUT SECTION -->
  <div class="tool-about">
    <h2>About {h1_clean}</h2>
    <p class="tool-about-intro">{intro}</p>
    <div class="tool-about-grid">
      <div class="tool-about-card">
        <h3>🎯 Who Uses This</h3>
        <p>{use_cases}</p>
      </div>
      <div class="tool-about-card">
        <h3>⚡ How It Works</h3>
        <p>{advanced}</p>
      </div>
      <div class="tool-about-card">
        <h3>🔒 100% Private</h3>
        <p>Your files never leave your browser. No account required, no server uploads — just fast, local processing. This is what it means to {privacy}.</p>
      </div>
    </div>
  </div>
"""


def extract_h1(html):
    """Extract the h1 text from the tool-hero section."""
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
    if m:
        return re.sub(r'<[^>]+>', '', m.group(1)).strip()
    return ''


def get_tool_dirs():
    dirs = []
    for entry in os.scandir(ROOT):
        if entry.is_dir() and entry.name not in NON_TOOL_DIRS and not entry.name.startswith('.'):
            idx = os.path.join(entry.path, 'index.html')
            if os.path.isfile(idx):
                dirs.append((entry.name, idx))
    return sorted(dirs)


def process_file(tool_id, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has tool-about section
    if 'class="tool-about"' in html:
        return 'already has about section'

    h1 = extract_h1(html)
    if not h1:
        return 'could not find h1'

    about_html = get_tool_about_html(tool_id, h1)

    # --- Insert the about section at the top of <section class="seo-content"> ---
    # Right after the opening <section class="seo-content"> tag
    seo_open = '<section class="seo-content">'
    if seo_open in html:
        insertion_idx = html.index(seo_open) + len(seo_open)
        html = html[:insertion_idx] + about_html + html[insertion_idx:]
    else:
        # Fallback: inject before the first <h2>How to Use This Tool</h2>
        target = '<h2>How to Use This Tool</h2>'
        if target in html:
            html = html.replace(target, about_html + '\n  ' + target, 1)
        else:
            return 'could not find injection point'

    # --- Inject CSS into <head> once ---
    if 'tool-about' not in html.split('</head>')[0]:
        html = html.replace('</head>', ABOUT_CSS + '\n</head>', 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    return 'ok'


def main():
    tool_dirs = get_tool_dirs()
    print(f"Processing {len(tool_dirs)} tool directories...\n")
    ok = skipped = errors = 0
    for tool_id, filepath in tool_dirs:
        result = process_file(tool_id, filepath)
        if result == 'ok':
            print(f"  ✅ {tool_id}")
            ok += 1
        elif result == 'already has about section':
            print(f"  ⏭  {tool_id} — skipped (already done)")
            skipped += 1
        else:
            print(f"  ⚠  {tool_id} — {result}")
            errors += 1
    print(f"\n{'='*55}")
    print(f"Injected: {ok}  |  Skipped: {skipped}  |  Errors: {errors}")
    print(f"{'='*55}")


if __name__ == '__main__':
    main()
