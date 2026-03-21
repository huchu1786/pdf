const fs = require('fs');

// ════════════════════════════════════════════════════════════════
//  LOVEPDFS — FULLY SEO-UPGRADED TOOLS DATA
//  Updated: March 2026
//  Strategy: Worldwide high-volume + low-competition long-tail
//  + India-specific govt exam keywords + privacy/no-upload trend
// ════════════════════════════════════════════════════════════════

const TOOLS_SEO = [

  // ── CORE PDF TOOLS ──

  {
    id: 'merge-pdf',
    toolId: 'merge',
    title: 'Merge PDF Files Online Free — No Signup, No Watermark | LovePDFs',
    meta: 'Merge PDF files free online with no watermark and no signup. Combine multiple PDFs into one document in your browser — files never uploaded to any server.',
    h1: 'Merge PDF Files Online Free',
    desc: 'Combine PDFs in the order you want. No watermarks, no signup, no file uploads — 100% private and browser-based.',
    instructions: [
      'Click "Choose Files" or drag your PDFs into the drop area.',
      'Reorder the files by dragging them into the correct sequence.',
      'Click "Merge PDFs" to combine them into one document.',
      'Download your merged PDF file instantly — no email required.'
    ],
    benefits: [
      { title: 'No watermark ever', desc: 'Unlike other free tools, LovePDFs never adds a watermark to your merged document.' },
      { title: 'Completely private', desc: 'All merging happens in your browser. Your files are never uploaded to any server.' },
      { title: 'Works on mobile', desc: 'Merge PDFs on iPhone or Android directly from your browser — no app required.' }
    ],
    faqs: [
      { q: 'How to merge PDF without watermark free?', a: 'LovePDFs merges PDF files completely free without adding any watermarks. Upload your files, arrange them, and download the merged result instantly.' },
      { q: 'How to merge PDF files on iPhone for free?', a: 'Open LovePDFs in Safari on your iPhone, select the Merge PDF tool, upload your files from Files app, and tap Merge PDFs. No app download needed.' },
      { q: 'How to combine PDF files on Android free?', a: 'Open LovePDFs in Chrome on Android, tap Choose Files, select your PDFs from storage, and hit Merge PDFs. Works on all modern Android browsers.' },
      { q: 'How to merge PDF without uploading to server?', a: 'LovePDFs processes everything locally in your browser using WebAssembly technology. Your PDF files never leave your device.' },
      { q: 'Can I merge more than two PDF files at once?', a: 'Yes, you can merge unlimited PDF files in a single operation with no restrictions on the number of files or total size.' },
      { q: 'Is there a file size limit for merging PDFs?', a: 'Since everything runs in your browser locally, there are no server-imposed file size limits. Very large files may depend on your device memory.' }
    ],
    related: ['split-pdf', 'compress-pdf', 'pdf-to-word', 'organize-pdf']
  },

  {
    id: 'compress-pdf',
    toolId: 'compress',
    title: 'Compress PDF Online Free — Reduce Size Without Uploading | LovePDFs',
    meta: 'Compress PDF without uploading to any server. Reduce PDF file size free — compress below 1MB, 500KB or 100KB while keeping quality. No signup, no watermark.',
    h1: 'Compress PDF Online — No Upload Required',
    desc: 'Reduce PDF file size instantly in your browser. Files never leave your device — perfect for government forms, email attachments, and secure documents.',
    instructions: [
      'Click to upload or drag and drop your PDF file into the tool.',
      'Select your desired compression level: Low, Medium, or High.',
      'Click "Compress PDF" to start the local compression process.',
      'Download your optimized, smaller PDF file immediately.'
    ],
    benefits: [
      { title: 'No file upload — 100% private', desc: 'Unlike other compressors, your PDF never leaves your device. Perfect for sensitive documents and GDPR compliance.' },
      { title: 'Compress for government portals', desc: 'Reduce PDFs to under 1MB or 500KB for UPSC, SSC, bank, and other government application portals that reject large files.' },
      { title: 'Up to 80% size reduction', desc: 'Smart compression removes unnecessary metadata and optimizes images while maintaining readable quality.' }
    ],
    faqs: [
      { q: 'How to compress PDF below 1MB for government website?', a: 'Upload your PDF to LovePDFs and select High compression. The tool reduces your file to under 1MB instantly in your browser — perfect for government exam portals.' },
      { q: 'How to compress PDF to 100KB free online?', a: 'Select the highest compression level to compress your PDF to 100KB or less. Works entirely in your browser with no upload required.' },
      { q: 'How to compress PDF without losing quality?', a: 'Select Medium compression for the best balance of file size and visual quality. Text remains sharp and images stay readable.' },
      { q: 'How to compress PDF without uploading to server?', a: 'LovePDFs compresses PDFs entirely in your browser using WebAssembly. Your file is never sent to any external server — 100% private.' },
      { q: 'How to compress PDF for email attachment free?', a: 'Use Medium compression to bring your PDF under the typical 10MB email attachment limit while preserving professional appearance.' },
      { q: 'How to compress PDF on iPhone or Android free?', a: 'Open LovePDFs on your phone browser, upload your PDF, choose compression level, and download. No app needed — works on all mobile browsers.' }
    ],
    related: ['merge-pdf', 'split-pdf', 'edit-pdf', 'repair-pdf']
  },

  {
    id: 'split-pdf',
    toolId: 'split',
    title: 'Split PDF Online Free — Extract Pages Instantly | LovePDFs',
    meta: 'Split PDF into individual pages free. Extract one page or a range from any PDF instantly in your browser — no software, no signup, no upload.',
    h1: 'Split PDF Into Pages Free',
    desc: 'Extract exactly the pages you need. Split one PDF into multiple files or extract a single page — all in your browser with no uploads.',
    instructions: [
      'Upload the PDF document you want to split.',
      'Choose your split method: by page range, fixed intervals, or extract all pages.',
      'Define custom ranges (e.g. 1-5, 8, 11-13) or select pages visually.',
      'Click "Split PDF" and download your separated files instantly.'
    ],
    benefits: [
      { title: 'Extract any single page', desc: 'Pull out one specific page from a large PDF document in seconds.' },
      { title: 'Custom range splitting', desc: 'Define exactly which page ranges you want — split a 100-page report into chapters.' },
      { title: 'Browser-based, no upload', desc: 'Your confidential documents never leave your device during splitting.' }
    ],
    faqs: [
      { q: 'How to split one PDF into multiple files free?', a: 'Upload your PDF to LovePDFs, choose Split by Range or Extract All Pages, define your ranges, and click Split PDF. All files download in a ZIP.' },
      { q: 'How to extract one page from a PDF free?', a: 'Use the Custom Range option, enter the single page number you need, and click Split. You will get just that page as a separate PDF.' },
      { q: 'How to save one page of a PDF as a separate file?', a: 'Open the Split PDF tool, enter the page number in the custom range box, and click Split PDF to extract it as its own standalone document.' },
      { q: 'How to split PDF without Adobe Acrobat?', a: 'LovePDFs is a free browser-based alternative to Adobe Acrobat. Just upload, define your split, and download — no software installation needed.' },
      { q: 'Can I split a PDF into single individual pages?', a: 'Yes — select the Extract All Pages option to get every page as its own separate PDF file in a single ZIP download.' }
    ],
    related: ['merge-pdf', 'remove-pages-pdf', 'extract-pages-pdf', 'organize-pdf']
  },

  {
    id: 'rotate-pdf',
    toolId: 'rotate',
    title: 'Rotate PDF Pages Free — Save Permanently Online | LovePDFs',
    meta: 'Rotate PDF pages free and save permanently. Fix upside-down scanned pages or change orientation from portrait to landscape with LovePDFs — no software needed.',
    h1: 'Rotate PDF Pages and Save Permanently',
    desc: 'Fix upside-down or sideways PDF pages in seconds. Rotate all pages, odd pages, or even pages — changes saved permanently in the downloaded file.',
    instructions: [
      'Select or drag and drop your PDF file into the tool.',
      'Choose the rotation angle: 90°, 180°, or 270°.',
      'Select which pages to rotate: All, Odd, or Even pages.',
      'Click "Rotate PDF" and download your corrected document.'
    ],
    benefits: [
      { title: 'Permanent rotation', desc: 'The downloaded file has the rotation permanently saved — not just a display fix.' },
      { title: 'Fix scanned documents', desc: 'Correct pages that were scanned sideways or upside down in one click.' },
      { title: 'Selective page rotation', desc: 'Apply different rotations to odd and even pages for double-sided scan fixes.' }
    ],
    faqs: [
      { q: 'How to rotate PDF and save permanently free?', a: 'Upload your PDF to LovePDFs, choose the rotation angle, and download. The orientation is permanently saved in the new file — not just a viewer fix.' },
      { q: 'How to rotate a PDF page on iPhone free?', a: 'Open LovePDFs in Safari on your iPhone, upload the PDF, select rotation angle, and tap Rotate PDF. The fixed file downloads to your device.' },
      { q: 'How to fix a sideways PDF scan?', a: 'Upload the scanned PDF, select 90° or 270° rotation depending on which way it tilted, choose All Pages, and download the corrected version.' },
      { q: 'Can I rotate just specific pages?', a: 'Currently the tool rotates by page pattern (All, Odd, Even). To rotate specific individual pages, use our Organize PDF tool for granular control.' }
    ],
    related: ['organize-pdf', 'edit-pdf', 'crop-pdf', 'flatten-pdf']
  },

  {
    id: 'unlock-pdf',
    toolId: 'unlock',
    title: 'Remove PDF Password Free Online — Unlock PDF Instantly | LovePDFs',
    meta: 'Unlock PDF online free. Remove PDF password and restrictions instantly in your browser — no software, no upload to server. 100% private with LovePDFs.',
    h1: 'Remove PDF Password Free Online',
    desc: 'Remove password protection and print/copy/edit restrictions from any PDF file. Works entirely in your browser — your document stays private.',
    instructions: [
      'Upload your password-protected PDF file.',
      'If prompted, enter the password to authorize the removal.',
      'Click "Unlock PDF" to remove all restrictions instantly.',
      'Download your fully unlocked, restriction-free PDF.'
    ],
    benefits: [
      { title: 'Remove edit and print restrictions', desc: 'Enable printing, copying text, and editing on previously locked PDF documents.' },
      { title: 'Completely private', desc: 'Unlocking happens locally in your browser — your sensitive documents never reach any server.' },
      { title: 'Instant results', desc: 'No waiting — unlock any PDF in seconds directly from your browser.' }
    ],
    faqs: [
      { q: 'How to remove password from PDF free?', a: 'Upload your PDF to LovePDFs, enter the password when prompted, and click Unlock PDF. The tool removes all password protection and restrictions instantly.' },
      { q: 'How to unlock a PDF without uploading to server?', a: 'LovePDFs processes everything locally in your browser. Your confidential document is never sent to any external server.' },
      { q: 'Can I unlock a PDF I forgot the password to?', a: 'If the PDF has an open password (required just to view it), you need the password to unlock it. LovePDFs can remove owner restrictions (print/edit/copy locks) without a password.' },
      { q: 'Is it legal to remove PDF password restrictions?', a: 'Yes, provided you own the document or have permission to access it. Removing restrictions from your own documents is perfectly legal.' }
    ],
    related: ['protect-pdf', 'sign-pdf', 'edit-pdf', 'redact-pdf']
  },

  {
    id: 'protect-pdf',
    toolId: 'protect',
    title: 'Password Protect PDF Free Online — Lock PDF Securely | LovePDFs',
    meta: 'Password protect PDF free online. Lock a PDF with a strong password in your browser — files never uploaded, 100% private. No signup required with LovePDFs.',
    h1: 'Password Protect PDF Online Free',
    desc: 'Encrypt and lock your PDF with a password to keep sensitive data confidential. Encryption happens locally — your document never leaves your device.',
    instructions: [
      'Upload the PDF you want to password protect.',
      'Enter a strong password and confirm it in the second field.',
      'Click "Protect PDF" to apply AES encryption instantly.',
      'Download your password-secured document.'
    ],
    benefits: [
      { title: 'Client-side encryption', desc: 'The password and document are processed entirely in your browser — never sent to our servers.' },
      { title: 'Secure sensitive documents', desc: 'Protect contracts, invoices, medical records, and personal documents before sharing.' },
      { title: 'Instant protection', desc: 'Apply strong password encryption to any PDF in seconds, no software required.' }
    ],
    faqs: [
      { q: 'How to lock a PDF with password free?', a: 'Upload your PDF to LovePDFs, enter your chosen password, and click Protect PDF. The encryption happens in your browser — your document is never uploaded.' },
      { q: 'How to password protect a PDF without Adobe?', a: 'LovePDFs is a completely free Adobe Acrobat alternative for PDF password protection. Works in any browser, on any device, with no software needed.' },
      { q: 'What type of encryption is used to protect the PDF?', a: 'LovePDFs applies standard PDF encryption. For maximum security, use a strong unique password with mixed characters.' },
      { q: 'What if I forget my PDF password?', a: 'There is no way to recover a lost password. Always store your password securely before protecting the document.' }
    ],
    related: ['unlock-pdf', 'redact-pdf', 'sign-pdf', 'edit-pdf']
  },

  {
    id: 'add-watermark-pdf',
    toolId: 'watermark',
    title: 'Add Watermark to PDF Free — No Adobe Needed | LovePDFs',
    meta: 'Add text watermark to PDF free online without Adobe Acrobat. Stamp CONFIDENTIAL, DRAFT or your brand on any PDF in your browser — private and instant.',
    h1: 'Add Watermark to PDF Free Online',
    desc: 'Stamp custom text over your PDF pages. Choose font, opacity, position, and which pages to watermark — all free, all in your browser.',
    instructions: [
      'Upload your PDF document to the tool.',
      'Enter the watermark text (e.g. CONFIDENTIAL, DRAFT, your company name).',
      'Choose position, color, font size, and which pages to apply it to.',
      'Click "Apply Watermark" and download the watermarked result.'
    ],
    benefits: [
      { title: 'No Adobe Acrobat needed', desc: 'Add professional watermarks entirely for free, directly in your browser.' },
      { title: 'Fully customizable', desc: 'Control transparency, position (diagonal, centered, header/footer), color, and page selection.' },
      { title: 'Brand your documents', desc: 'Easily add company names, CONFIDENTIAL, or DRAFT stamps to any document before sharing.' }
    ],
    faqs: [
      { q: 'How to add watermark to PDF without Adobe Acrobat?', a: 'LovePDFs provides a free browser-based way to add custom text watermarks to any PDF without needing Adobe Acrobat or any paid software.' },
      { q: 'How to add CONFIDENTIAL stamp to PDF free?', a: 'Enter "CONFIDENTIAL" as your watermark text, choose diagonal placement, adjust opacity to around 30%, and click Apply Watermark.' },
      { q: 'Can I add watermark to specific pages only?', a: 'Yes — choose to apply the watermark to All Pages, First Page Only, Last Page Only, or Odd/Even pages.' },
      { q: 'Can I add an image watermark or logo?', a: 'Currently the tool supports text watermarks. Image/logo watermarks will be added in an upcoming update.' }
    ],
    related: ['edit-pdf', 'add-page-numbers-pdf', 'protect-pdf', 'redact-pdf']
  },

  {
    id: 'remove-pages-pdf',
    toolId: 'removepg',
    title: 'Remove Pages from PDF Free Online — Delete PDF Pages | LovePDFs',
    meta: 'Remove pages from PDF free online. Delete specific pages from any PDF without Adobe Acrobat — works in browser, no upload, no signup with LovePDFs.',
    h1: 'Remove Pages from PDF Free Online',
    desc: 'Delete specific pages from any PDF document in seconds. Visual thumbnail grid shows exactly which pages you are removing before you confirm.',
    instructions: [
      'Upload your PDF file to the Remove Pages tool.',
      'Click on the page thumbnails you want to delete — selected pages are highlighted.',
      'Click "Remove Pages" to delete all selected pages.',
      'Download the updated PDF with those pages permanently removed.'
    ],
    benefits: [
      { title: 'Visual page selection', desc: 'See thumbnail previews of every page so you know exactly what you are deleting.' },
      { title: 'No Adobe Acrobat needed', desc: 'Delete PDF pages completely free in your browser without any paid software.' },
      { title: 'Fast cleanup', desc: 'Strip blank pages, cover letters, or confidential sections before sharing documents.' }
    ],
    faqs: [
      { q: 'How to delete a page from PDF without Adobe?', a: 'LovePDFs is a free Adobe Acrobat alternative. Upload your PDF, click the pages you want deleted, and hit Remove Pages. Done in seconds, no software needed.' },
      { q: 'How to remove blank pages from PDF free?', a: 'Upload your PDF, identify blank pages in the visual thumbnail grid, select them all, and click Remove Pages to strip them out permanently.' },
      { q: 'How to delete multiple pages from PDF at once?', a: 'Click multiple page thumbnails to select them all before clicking Remove Pages. There is no limit on how many pages you can delete.' },
      { q: 'Is removing pages from PDF permanent?', a: 'Yes. When you download the resulting file, the selected pages are permanently removed from the document.' }
    ],
    related: ['split-pdf', 'extract-pages-pdf', 'organize-pdf', 'merge-pdf']
  },

  {
    id: 'organize-pdf',
    toolId: 'organize',
    title: 'Rearrange PDF Pages Online Free — Reorder Without Acrobat | LovePDFs',
    meta: 'Rearrange and reorder PDF pages free online. Drag and drop to reorganize pages without Adobe Acrobat — browser-based, private, no signup with LovePDFs.',
    h1: 'Rearrange PDF Pages Online Free',
    desc: 'Drag and drop to reorder pages in any PDF. Fix scanning order mistakes, reorganize chapters, or build your document exactly how you need it.',
    instructions: [
      'Upload your PDF to the Organize tool.',
      'Drag and drop the page thumbnails to your desired order.',
      'Rotate individual pages if needed using the rotation icon.',
      'Click "Organize PDF" and download the reordered document.'
    ],
    benefits: [
      { title: 'Intuitive drag-and-drop', desc: 'Visually rearrange pages by dragging thumbnails — no page number guessing needed.' },
      { title: 'Fix scan order mistakes', desc: 'Correct documents that were scanned or assembled out of order.' },
      { title: 'Combine with rotation', desc: 'Rotate and reorder pages in the same step before downloading.' }
    ],
    faqs: [
      { q: 'How to reorder pages in PDF without Adobe Acrobat?', a: 'LovePDFs offers a free drag-and-drop page organizer that works in any browser. Upload, drag pages to the right order, and download — no Acrobat needed.' },
      { q: 'How to move pages in a PDF free?', a: 'Open the Organize PDF tool, drag the page thumbnail to its new position, and click Organize PDF to save the new order.' },
      { q: 'Can I both reorder and rotate pages at the same time?', a: 'Yes — you can drag pages to a new position and also rotate individual pages using the rotation icon on each thumbnail, all before downloading.' }
    ],
    related: ['split-pdf', 'remove-pages-pdf', 'merge-pdf', 'crop-pdf']
  },

  {
    id: 'crop-pdf',
    toolId: 'crop',
    title: 'Crop PDF Pages Free Online — Remove Margins | LovePDFs',
    meta: 'Crop PDF pages free online. Remove white borders and margins from PDF, resize page content area — browser-based, private, no Adobe needed with LovePDFs.',
    h1: 'Crop PDF Pages Online Free',
    desc: 'Remove white borders, margins, and excess whitespace from PDF pages. Adjust the crop area precisely and download the trimmed result instantly.',
    instructions: [
      'Upload your PDF to the Crop tool.',
      'Adjust the crop margins (top, bottom, left, right) using the sliders.',
      'Preview the result to confirm the crop area looks correct.',
      'Click "Crop PDF" and download your trimmed document.'
    ],
    benefits: [
      { title: 'Remove unwanted margins', desc: 'Make text appear larger by cropping away excessive white space around pages.' },
      { title: 'Standardize page sizes', desc: 'Make all pages in a scanned document consistent in their visible content area.' },
      { title: 'Fast and private', desc: 'Cropping is processed in your browser — your document is never uploaded.' }
    ],
    faqs: [
      { q: 'How to remove white border from PDF pages free?', a: 'Upload your PDF to the Crop tool, drag the margin sliders inward until the white borders disappear, and click Crop PDF.' },
      { q: 'How to crop a scanned PDF to remove black edges?', a: 'Use the crop sliders to trim away the black scanner borders on all sides. Apply to all pages for a consistent professional result.' },
      { q: 'Will cropping change the actual PDF content?', a: 'Cropping adjusts the visible area (crop box) of each page. The underlying content is unchanged — just the visible portion is modified.' }
    ],
    related: ['rotate-pdf', 'edit-pdf', 'resize-pdf', 'organize-pdf']
  },

  // ── CONVERTERS ──

  {
    id: 'pdf-to-word',
    toolId: 'pdf2word',
    title: 'PDF to Word Converter Free — Keep Formatting | LovePDFs',
    meta: 'Convert PDF to Word free without losing formatting. Free PDF to Word converter — no email required, no signup, files processed in your browser with LovePDFs.',
    h1: 'Convert PDF to Word Free — Keep Your Formatting',
    desc: 'Convert PDF to editable Word document (.docx) with layout preserved. No email, no signup, no upload to server — runs entirely in your browser.',
    instructions: [
      'Upload your PDF file to the PDF to Word converter.',
      'The tool automatically analyses the layout and text positioning.',
      'Click "Convert to Word" to generate the .docx file.',
      'Download your editable Word document instantly.'
    ],
    benefits: [
      { title: 'Preserves formatting', desc: 'Advanced layout analysis retains text position, headings, paragraphs, and tables from the original PDF.' },
      { title: 'No email required', desc: 'Unlike most converters that email you the result, LovePDFs downloads directly — no personal data needed.' },
      { title: '100% private', desc: 'Your document is never uploaded to an external conversion server — all processing happens locally.' }
    ],
    faqs: [
      { q: 'How to convert PDF to Word without losing formatting?', a: 'LovePDFs uses advanced layout analysis to group text by position, detect headings, and preserve paragraph structure when converting PDF to Word.' },
      { q: 'How to convert PDF to Word without email or signup?', a: 'Open LovePDFs PDF to Word tool, upload your file, click Convert, and download directly. No email, no account, no personal data required.' },
      { q: 'How to convert scanned PDF to Word free?', a: 'First use our OCR tool to extract text from the scanned PDF, then use the PDF to Word converter to create an editable document.' },
      { q: 'How to convert PDF to editable Word free?', a: 'Our converter creates a fully editable .docx file that opens in Microsoft Word, Google Docs, LibreOffice, and any other word processor.' },
      { q: 'How to convert PDF to Word on iPhone or Android?', a: 'Open LovePDFs on your mobile browser, upload from your Files app or Google Drive, convert, and download — no desktop needed.' }
    ],
    related: ['word-to-pdf', 'edit-pdf', 'pdf-to-excel', 'ocr-extract-text']
  },

  {
    id: 'pdf-to-excel',
    toolId: 'pdf2xls',
    title: 'Convert PDF to Excel Free Online — Extract Tables | LovePDFs',
    meta: 'PDF to Excel converter free. Extract data and tables from PDF to Excel or CSV for free — no software, no upload, browser-based with LovePDFs.',
    h1: 'Convert PDF to Excel Free Online',
    desc: 'Extract tables and data from any PDF into an Excel-compatible CSV file. Perfect for financial reports, invoices, and data sheets — all processed locally.',
    instructions: [
      'Upload your PDF containing data or tables.',
      'The tool analyses text positioning to detect table structures.',
      'Click "Convert to Excel" to extract all data.',
      'Download the CSV file — open it in Excel, Google Sheets, or any spreadsheet app.'
    ],
    benefits: [
      { title: 'Precise table extraction', desc: 'Detects row and column structure using text coordinates for accurate data extraction.' },
      { title: 'Universal CSV format', desc: 'The exported CSV opens in Excel, Google Sheets, LibreOffice Calc, and any spreadsheet software.' },
      { title: 'Secure financial data', desc: 'Sensitive financial or personal data in the PDF never leaves your device.' }
    ],
    faqs: [
      { q: 'How to extract data from PDF to Excel for free?', a: 'Upload your PDF to LovePDFs PDF to Excel tool. It analyses column and row structure and exports the data as a CSV file compatible with Excel.' },
      { q: 'How to convert PDF table to Excel without software?', a: 'LovePDFs runs entirely in your browser — no Excel, no Adobe, no installed software needed to extract tables from PDFs.' },
      { q: 'Can I open the converted file in Google Sheets?', a: 'Yes — the exported CSV file can be uploaded directly to Google Sheets or Opened with Microsoft Excel, LibreOffice, or Numbers on Mac.' }
    ],
    related: ['pdf-to-word', 'excel-to-pdf', 'ocr-extract-text', 'pdf-to-text']
  },

  {
    id: 'pdf-to-ppt',
    toolId: 'pdf2ppt',
    title: 'Convert PDF to PowerPoint Free Online | LovePDFs',
    meta: 'PDF to PPT converter free. Extract text from PDF presentations into an editable format for free — browser-based, private, no upload with LovePDFs.',
    h1: 'Convert PDF to PowerPoint Free',
    desc: 'Extract and retrieve text content from PDF slide documents. Get slide text out of any PDF presentation quickly, privately, in your browser.',
    instructions: [
      'Upload your PDF presentation file.',
      'The tool extracts all text content from the PDF pages.',
      'Click "Convert to PPT" to generate the output.',
      'Download the extracted content for use in your presentation.'
    ],
    benefits: [
      { title: 'Fast text retrieval', desc: 'Quickly extract all text from slide-based PDF documents.' },
      { title: 'Private and secure', desc: 'Confidential business presentations never leave your browser.' },
      { title: 'No software needed', desc: 'Works entirely in your browser — no PowerPoint or Adobe installation required.' }
    ],
    faqs: [
      { q: 'How to convert PDF to PowerPoint free?', a: 'Upload your PDF to LovePDFs PDF to PPT tool to extract the text content. For full slide recreation with layouts, a desktop app like LibreOffice Impress may give better results.' },
      { q: 'How to edit a PDF presentation without PowerPoint?', a: 'Use our PDF to PPT converter to extract the text content, then edit it in Google Slides or LibreOffice Impress for free.' }
    ],
    related: ['pdf-to-word', 'pdf-to-excel', 'edit-pdf', 'ocr-extract-text']
  },

  {
    id: 'pdf-to-jpg',
    toolId: 'pdf2jpg',
    title: 'Convert PDF to JPG Free — High Quality Page Images | LovePDFs',
    meta: 'PDF to JPG converter free. Save each PDF page as a high-quality JPG image online for free — no upload to server, no signup with LovePDFs.',
    h1: 'Convert PDF to JPG Images Free',
    desc: 'Convert every page of a PDF into a high-quality JPG image. Choose your DPI quality setting and download all images instantly in a ZIP file.',
    instructions: [
      'Upload your PDF file to the PDF to JPG converter.',
      'Choose your output quality: Standard (96 DPI), High (192 DPI), or Ultra (288 DPI).',
      'Click "Convert to JPG" to render each page as an image.',
      'Download all page images in a ZIP file instantly.'
    ],
    benefits: [
      { title: 'Up to 288 DPI quality', desc: 'Choose ultra-sharp 288 DPI for print-quality images or standard 96 DPI for smaller file sizes.' },
      { title: 'All pages at once', desc: 'Convert an entire multi-page PDF to JPG images in a single operation.' },
      { title: 'Private processing', desc: 'Your PDF is rendered to images entirely in your browser — never sent to an external server.' }
    ],
    faqs: [
      { q: 'How to save each PDF page as an image free?', a: 'Upload your PDF to LovePDFs PDF to JPG tool, choose your quality setting, and click Convert. Each page downloads as a separate JPG in a ZIP file.' },
      { q: 'How to convert PDF to JPG without losing quality?', a: 'Select the Ultra (288 DPI) setting for maximum quality image output from your PDF pages.' },
      { q: 'How to convert PDF to image on iPhone free?', a: 'Open LovePDFs in Safari, upload your PDF from Files, choose quality, and tap Convert to JPG. Images download directly to your iPhone.' },
      { q: 'Can I convert just one page of a PDF to JPG?', a: 'Use the Split PDF tool first to extract the single page, then run it through PDF to JPG to get that specific page as an image.' }
    ],
    related: ['jpg-to-pdf', 'image-to-pdf', 'compress-image', 'pdf-to-word']
  },

  {
    id: 'word-to-pdf',
    toolId: 'word2pdf',
    title: 'Convert Word to PDF Free Online — DOCX to PDF | LovePDFs',
    meta: 'Word to PDF converter free. Convert Word document to PDF without Microsoft Office — DOCX to PDF free online, no signup, no watermark with LovePDFs.',
    h1: 'Convert Word to PDF Free Online',
    desc: 'Convert any Word .docx file to a professional PDF document entirely in your browser. No Microsoft Office required — free, private, instant.',
    instructions: [
      'Upload your Word (.docx) file to the converter.',
      'The tool processes your document structure and formatting.',
      'Click "Convert to PDF" to generate your PDF file.',
      'Download the finished PDF document immediately.'
    ],
    benefits: [
      { title: 'No Microsoft Office needed', desc: 'Convert Word documents to PDF without having Office installed — works in any browser.' },
      { title: 'No watermark', desc: 'Your converted PDF is completely clean — no watermarks or branding added.' },
      { title: 'Preserves formatting', desc: 'Fonts, headings, tables, and layout are preserved in the converted PDF output.' }
    ],
    faqs: [
      { q: 'How to convert Word to PDF without Microsoft Office?', a: 'Upload your .docx file to LovePDFs Word to PDF tool and click Convert. No Office subscription or installation needed — works entirely in the browser.' },
      { q: 'How to convert DOCX to PDF free no watermark?', a: 'LovePDFs converts Word to PDF completely free with no watermarks added. Just upload, convert, and download a clean PDF.' },
      { q: 'How to convert Word to PDF on Android or iPhone?', a: 'Open LovePDFs in your mobile browser, upload the .docx from your device storage, and tap Convert to PDF. No app needed.' },
      { q: 'Does Word to PDF conversion preserve images and tables?', a: 'Yes — the converter preserves text formatting, embedded images, tables, and the overall document layout in the output PDF.' }
    ],
    related: ['pdf-to-word', 'excel-to-pdf', 'compress-pdf', 'protect-pdf']
  },

  {
    id: 'excel-to-pdf',
    toolId: 'xls2pdf',
    title: 'Convert Excel to PDF Free Online — Spreadsheet to PDF | LovePDFs',
    meta: 'Excel to PDF converter free. Convert spreadsheet to PDF without Excel — XLSX and CSV to PDF free online, no signup, browser-based with LovePDFs.',
    h1: 'Convert Excel to PDF Free Online',
    desc: 'Convert Excel spreadsheets (.xlsx) and CSV files to clean PDF documents. No Excel installation needed — runs entirely in your browser.',
    instructions: [
      'Upload your Excel (.xlsx) or CSV file.',
      'The tool renders your spreadsheet data as a formatted PDF.',
      'Click "Convert to PDF" to generate the output.',
      'Download your PDF spreadsheet document.'
    ],
    benefits: [
      { title: 'No Excel required', desc: 'Convert spreadsheets to PDF without Microsoft Excel — works in any browser on any device.' },
      { title: 'CSV and XLSX support', desc: 'Supports both .xlsx Excel files and .csv spreadsheet formats.' },
      { title: 'Share-ready PDFs', desc: 'PDF format is universally readable — perfect for sharing financial reports with clients.' }
    ],
    faqs: [
      { q: 'How to convert Excel to PDF without Microsoft Excel?', a: 'Upload your .xlsx or .csv file to LovePDFs and click Convert to PDF. No Excel installation or Office subscription required.' },
      { q: 'How to convert spreadsheet to PDF for free online?', a: 'LovePDFs converts both Excel and CSV files to PDF for free in your browser. Just upload, convert, and download.' },
      { q: 'Can I convert a Google Sheets file to PDF?', a: 'Download your Google Sheet as an .xlsx or .csv file first, then upload it to LovePDFs to convert it to PDF.' }
    ],
    related: ['word-to-pdf', 'pdf-to-excel', 'compress-pdf', 'protect-pdf']
  },

  {
    id: 'ppt-to-pdf',
    toolId: 'ppt2pdf',
    title: 'Convert PowerPoint to PDF Free Online — PPT to PDF | LovePDFs',
    meta: 'PPT to PDF converter free. Convert PowerPoint presentation to PDF without Microsoft Office — PPTX to PDF free online, no signup with LovePDFs.',
    h1: 'Convert PowerPoint to PDF Free',
    desc: 'Convert PowerPoint .pptx presentations to PDF documents without needing Microsoft Office. Fast, free, and private in your browser.',
    instructions: [
      'Upload your PowerPoint (.pptx) presentation file.',
      'The tool processes each slide and converts it to a PDF page.',
      'Click "Convert to PDF" to generate your presentation PDF.',
      'Download the PDF version of your presentation.'
    ],
    benefits: [
      { title: 'No PowerPoint needed', desc: 'Convert presentations to PDF without any Microsoft Office license or software.' },
      { title: 'Universal sharing', desc: 'PDFs are readable on every device — share presentations without compatibility worries.' },
      { title: 'Preserves slide layout', desc: 'Slide designs, text, and images are preserved in the PDF output.' }
    ],
    faqs: [
      { q: 'How to convert PowerPoint to PDF without Microsoft Office?', a: 'Upload your .pptx to LovePDFs PPT to PDF tool and click Convert. No Office subscription or desktop app needed.' },
      { q: 'How to send a PowerPoint as PDF for free?', a: 'Convert your PPT to PDF using LovePDFs for free, then attach the PDF to your email. PDFs are universally compatible and cannot be accidentally edited.' }
    ],
    related: ['pdf-to-ppt', 'word-to-pdf', 'compress-pdf', 'protect-pdf']
  },

  {
    id: 'jpg-to-pdf',
    toolId: 'jpg2pdf',
    title: 'Convert JPG to PDF Free Online — Multiple Images to One PDF | LovePDFs',
    meta: 'JPG to PDF converter free. Combine multiple JPG images into one PDF online free — no signup, no watermark, works on mobile with LovePDFs.',
    h1: 'Convert JPG to PDF Free — Multiple Images',
    desc: 'Turn one or multiple JPG images into a single PDF document. Perfect for scanning notes, combining photos, and creating shareable documents from images.',
    instructions: [
      'Click to upload or drag multiple JPG images into the tool.',
      'Reorder the images if needed by dragging thumbnails.',
      'Choose page orientation and margin settings.',
      'Click "Convert to PDF" and download your multi-page PDF.'
    ],
    benefits: [
      { title: 'Multiple images to one PDF', desc: 'Combine unlimited JPG photos into a single organized PDF document.' },
      { title: 'Works on mobile', desc: 'Convert photos on your phone directly from the browser — great for scanning and submitting documents.' },
      { title: 'No watermark', desc: 'Your converted PDF is completely clean — no stamps, branding, or limitations.' }
    ],
    faqs: [
      { q: 'How to combine multiple JPG images into one PDF free?', a: 'Upload all your JPG images at once to LovePDFs JPG to PDF tool, arrange them in order, and click Convert to PDF. All images become pages in one PDF.' },
      { q: 'How to convert JPG to PDF on iPhone free?', a: 'Open LovePDFs in Safari on iPhone, tap Choose Files, select your photos from the Photos app or Files, and tap Convert to PDF.' },
      { q: 'How to convert photos to PDF on Android free?', a: 'Open LovePDFs in Chrome on Android, upload your photos from your Gallery, and tap Convert to PDF. No app installation needed.' },
      { q: 'How to convert JPG to PDF for government form submission?', a: 'Upload your photo JPG to LovePDFs, convert to PDF, then use our Compress PDF tool if the file needs to meet a size requirement.' }
    ],
    related: ['image-to-pdf', 'pdf-to-jpg', 'compress-pdf', 'png-to-jpg']
  },

  {
    id: 'image-to-pdf',
    toolId: 'img2pdf',
    title: 'Convert Image to PDF Free — JPG PNG to PDF Online | LovePDFs',
    meta: 'Image to PDF converter free. Turn any photo or image (JPG, PNG, WEBP) into a PDF online for free — no upload, mobile friendly with LovePDFs.',
    h1: 'Convert Image to PDF Free Online',
    desc: 'Convert any image format — JPG, PNG, WEBP — into a PDF document. Works on phone, tablet, and desktop. No uploads, no signup, completely private.',
    instructions: [
      'Upload your image file (JPG, PNG, or WEBP).',
      'Adjust page size and orientation if needed.',
      'Click "Convert to PDF" to create your PDF document.',
      'Download your image as a PDF instantly.'
    ],
    benefits: [
      { title: 'All major image formats', desc: 'Supports JPG, JPEG, PNG, and WEBP image conversion to PDF.' },
      { title: 'Perfect for mobile photos', desc: 'Turn photos taken on your phone into PDF documents — great for document submissions.' },
      { title: 'Instant download', desc: 'No server processing wait — conversion happens in your browser and downloads immediately.' }
    ],
    faqs: [
      { q: 'How to turn a photo into a PDF on iPhone free?', a: 'Open LovePDFs in Safari on your iPhone, choose the Image to PDF tool, select your photo from Photos or Files, and tap Convert to PDF.' },
      { q: 'How to convert a PNG screenshot to PDF free?', a: 'Upload your PNG to the Image to PDF tool and click Convert. PNG files including screenshots are fully supported.' },
      { q: 'How to convert image to PDF for government form?', a: 'Upload your photo, convert it to PDF, then use our Compress PDF tool to reduce the file size to meet the portal requirements.' }
    ],
    related: ['jpg-to-pdf', 'compress-image', 'png-to-jpg', 'compress-pdf']
  },

  // ── IMAGE TOOLS ──

  {
    id: 'resize-image',
    toolId: 'resizeimg',
    title: 'Resize Image Online Free — Without Losing Quality | LovePDFs',
    meta: 'Resize image online free without losing quality. Resize photo to passport size, Instagram, LinkedIn or any custom dimensions — browser-based with LovePDFs.',
    h1: 'Resize Image Online Free',
    desc: 'Resize any image to exact pixel dimensions or percentage. Passport size, social media sizes, or custom dimensions — all processed locally in your browser.',
    instructions: [
      'Upload your image (JPG, PNG, or WEBP).',
      'Enter the desired width and height in pixels, or choose a preset size.',
      'Select whether to maintain the original aspect ratio.',
      'Click "Resize Image" and download your resized photo.'
    ],
    benefits: [
      { title: 'Passport and ID photo sizes', desc: 'Resize photos to exact passport dimensions (35x45mm, 2x2 inch) for visa and government applications.' },
      { title: 'Social media presets', desc: 'Instant resize to Instagram, LinkedIn, Facebook, Twitter/X, and YouTube thumbnail sizes.' },
      { title: 'No quality loss', desc: 'High-quality resampling algorithm preserves sharpness when resizing down.' }
    ],
    faqs: [
      { q: 'How to resize image to passport size free online?', a: 'Upload your photo, select the Passport Size preset (or enter 35x45mm / 413x531px), and click Resize. Download your passport-ready photo instantly.' },
      { q: 'How to resize image for Aadhar card photo free?', a: 'Aadhar requires a 35x45mm photo. Upload your image, choose the 35x45mm preset, and download. Use Compress Image to meet KB requirements.' },
      { q: 'How to resize image without losing quality?', a: 'LovePDFs uses high-quality bicubic resampling to maintain sharpness. Avoid enlarging images significantly — resizing down preserves quality best.' },
      { q: 'How to resize image for Instagram free?', a: 'Select the Instagram preset (1080x1080 square or 1080x1350 portrait) to instantly resize your image for Instagram posts or profile.' },
      { q: 'How to resize image for LinkedIn banner free?', a: 'Select the LinkedIn Banner preset (1584x396px) to resize your image perfectly for your LinkedIn profile cover.' }
    ],
    related: ['compress-image', 'crop-image', 'png-to-jpg', 'jpg-to-pdf']
  },

  {
    id: 'crop-image',
    toolId: 'cropimg',
    title: 'Crop Image Online Free — Cut and Trim Photos | LovePDFs',
    meta: 'Crop image online free. Cut, trim and crop photos to any size or aspect ratio — browser-based, no upload to server, instant download with LovePDFs.',
    h1: 'Crop Image Online Free',
    desc: 'Crop and trim any image to a custom area or fixed aspect ratio. Draw your crop region visually and download the result — all in your browser.',
    instructions: [
      'Upload your image to the crop tool.',
      'Drag the crop handles to select the area you want to keep.',
      'Choose a fixed aspect ratio (square, 4:3, 16:9) or freeform.',
      'Click "Crop Image" and download the cropped result.'
    ],
    benefits: [
      { title: 'Visual crop selector', desc: 'Drag handles to precisely define your crop area with a live preview.' },
      { title: 'Fixed aspect ratios', desc: 'Crop to Square, 4:3, 16:9, or freeform for different use cases.' },
      { title: 'Instant browser processing', desc: 'Cropping happens in your browser — no server upload, no wait time.' }
    ],
    faqs: [
      { q: 'How to crop an image online free without software?', a: 'Upload your image to LovePDFs Crop tool, drag the selection handles to your desired area, and click Crop Image. No software installation required.' },
      { q: 'How to crop a photo to square for Instagram free?', a: 'Select the 1:1 Square aspect ratio preset, adjust the crop position, and click Crop. Your photo is trimmed to a perfect square for Instagram.' },
      { q: 'How to remove background from image by cropping?', a: 'Use the freeform crop to trim away unwanted background areas. For full background removal, pair with an image editing tool.' }
    ],
    related: ['resize-image', 'compress-image', 'png-to-jpg', 'image-to-pdf']
  },

  {
    id: 'compress-image',
    toolId: 'compressimg',
    title: 'Compress Image Online Free — Reduce Size to 50KB, 20KB | LovePDFs',
    meta: 'Compress image online free without losing quality. Reduce image to 100KB, 50KB or 20KB for government forms, email, WhatsApp — no upload needed with LovePDFs.',
    h1: 'Compress Image Free — Reduce to Any Size',
    desc: 'Reduce image file size to any target KB without visible quality loss. Perfect for government exam portals, email attachments, and WhatsApp sharing.',
    instructions: [
      'Upload your JPG or PNG image.',
      'Enter your target file size in KB (e.g. 50KB, 100KB, 200KB).',
      'Click "Compress Image" to reduce the file to your target size.',
      'Download your compressed image — check the size before sending.'
    ],
    benefits: [
      { title: 'Target any KB size', desc: 'Compress to exactly 50KB, 20KB, 100KB or any other size needed for forms and portals.' },
      { title: 'Government exam ready', desc: 'Meet strict photo size requirements for SSC, UPSC, Railways, bank jobs, and visa applications worldwide.' },
      { title: 'No upload — 100% private', desc: 'Image compression runs entirely in your browser. Your personal photo never leaves your device.' }
    ],
    faqs: [
      { q: 'How to compress image to 50KB free online?', a: 'Upload your image, enter 50 in the target size field, and click Compress Image. Perfect for government exam photo requirements.' },
      { q: 'How to compress image to 20KB for government form?', a: 'Set the target to 20KB and click Compress. The tool reduces quality gradually until the file meets your exact size requirement.' },
      { q: 'How to reduce image file size without losing quality?', a: 'LovePDFs uses progressive compression — it finds the highest quality setting that still meets your target size, minimizing visible quality loss.' },
      { q: 'How to compress image for WhatsApp without blurring?', a: 'Set a target of 200-500KB to reduce file size while keeping WhatsApp-quality sharpness. Avoid compressing below 50KB for photos.' },
      { q: 'How to compress image for email attachment free?', a: 'Set target to 500KB or 1MB to bring your image under typical email size limits while keeping it looking professional.' },
      { q: 'How to compress image without uploading to server?', a: 'LovePDFs compresses images entirely in your browser using JavaScript canvas processing. Your photo is never sent to any external server.' }
    ],
    related: ['resize-image', 'crop-image', 'png-to-jpg', 'compress-pdf']
  },

  {
    id: 'jpg-to-png',
    toolId: 'jpg2png',
    title: 'Convert JPG to PNG Free Online — Transparent Background | LovePDFs',
    meta: 'Convert JPG to PNG free online. Turn JPG images into PNG with transparent background support — browser-based, no upload, instant download with LovePDFs.',
    h1: 'Convert JPG to PNG Free Online',
    desc: 'Convert JPG images to PNG format. PNG supports transparent backgrounds — perfect for logos, icons, and design work. Processed locally in your browser.',
    instructions: [
      'Upload your JPG or JPEG image file.',
      'Optionally enable transparent background (replaces white with transparency).',
      'Click "Convert to PNG" to process the image.',
      'Download your PNG file immediately.'
    ],
    benefits: [
      { title: 'Transparent background support', desc: 'Convert white backgrounds to transparency — ideal for logos and overlay graphics.' },
      { title: 'Lossless PNG quality', desc: 'PNG uses lossless compression — no quality degradation unlike repeated JPEG saves.' },
      { title: 'Browser-based conversion', desc: 'No upload required — your image is converted locally on your device.' }
    ],
    faqs: [
      { q: 'How to convert JPG to PNG with transparent background free?', a: 'Upload your JPG, enable the transparent background option to replace white areas with transparency, and click Convert to PNG.' },
      { q: 'Why convert JPG to PNG?', a: 'PNG is better for logos, graphics, and images that need transparent backgrounds. JPG uses lossy compression that degrades quality with each save.' },
      { q: 'How to remove white background from image free?', a: 'Upload your JPG, enable the "Replace white with transparency" option, and convert to PNG. White areas become fully transparent.' }
    ],
    related: ['png-to-jpg', 'compress-image', 'resize-image', 'crop-image']
  },

  {
    id: 'png-to-jpg',
    toolId: 'png2jpg',
    title: 'Convert PNG to JPG Free Online — No Quality Loss | LovePDFs',
    meta: 'Convert PNG to JPG free online. PNG to JPEG converter — no software needed, no upload, instant browser-based conversion without quality loss with LovePDFs.',
    h1: 'Convert PNG to JPG Free — Instant Online',
    desc: 'Convert PNG images to JPG format instantly. Reduce file size while maintaining quality — perfect when a form or portal only accepts JPG.',
    instructions: [
      'Upload your PNG image file.',
      'Adjust the JPG quality slider (90% recommended for best balance).',
      'Click "Convert to JPG" to process.',
      'Download your converted JPG image.'
    ],
    benefits: [
      { title: 'Smaller file sizes', desc: 'JPG files are typically 5-10x smaller than PNG for the same image — ideal for web and email.' },
      { title: 'Form compatibility', desc: 'Many government and business portals only accept JPG — convert your PNG instantly.' },
      { title: 'Quality control', desc: 'Adjust the quality slider to find the perfect balance between file size and image clarity.' }
    ],
    faqs: [
      { q: 'How to convert PNG to JPG without losing quality?', a: 'Set the quality slider to 90-95% for near-lossless conversion. LovePDFs uses high-quality rendering for maximum sharpness.' },
      { q: 'How to convert PNG to JPG for government form?', a: 'Government portals often only accept JPG photos. Upload your PNG, set quality to 85-90%, and convert to get a submission-ready JPG.' },
      { q: 'How to convert PNG screenshot to JPG free?', a: 'Upload your PNG screenshot to the converter, adjust quality if needed, and click Convert to JPG. Downloads instantly in your browser.' },
      { q: 'How to bulk convert PNG to JPG free?', a: 'Currently LovePDFs converts one image at a time. For bulk conversion, process each file individually using the tool.' }
    ],
    related: ['jpg-to-png', 'compress-image', 'resize-image', 'jpg-to-pdf']
  },

  // ── EDIT TOOLS ──

  {
    id: 'edit-pdf',
    toolId: 'edit',
    title: 'Edit PDF Online Free — Add Text, Draw, Highlight | LovePDFs',
    meta: 'Edit PDF online free without Adobe Acrobat. Add text, draw, highlight, annotate any PDF in your browser — no watermark, no signup, private with LovePDFs.',
    h1: 'Edit PDF Online Free — No Adobe Needed',
    desc: 'Add text, draw shapes, highlight content, and annotate any PDF. Full editor runs in your browser — nothing uploaded, completely private.',
    instructions: [
      'Upload your PDF to the editor.',
      'Select a tool: Text, Draw, Highlight, or Shapes.',
      'Click or draw on any part of the PDF to add your annotations.',
      'Click "Save PDF" to download your edited document.'
    ],
    benefits: [
      { title: 'Full annotation toolkit', desc: 'Add text boxes, freehand drawings, highlights in multiple colors, shapes, and sticky notes.' },
      { title: 'No Adobe Acrobat required', desc: 'LovePDFs is a completely free browser-based alternative to Adobe Acrobat for PDF editing.' },
      { title: 'No watermark on download', desc: 'Your edited PDF downloads completely clean — no branding or stamps added.' }
    ],
    faqs: [
      { q: 'How to edit PDF without Adobe Acrobat free?', a: 'LovePDFs is a free online PDF editor that works in any browser. Upload your PDF and use the toolbar to add text, draw, or highlight — no Adobe needed.' },
      { q: 'How to edit PDF text online free without watermark?', a: 'Upload your PDF to LovePDFs editor, add or modify annotations, and download. The result has absolutely no watermarks.' },
      { q: 'How to fill in a PDF form online free?', a: 'Open your PDF form in LovePDFs editor, use the Text tool to click on form fields and type your answers, then download the filled form.' },
      { q: 'How to highlight text in a PDF free online?', a: 'Select the Highlight tool in LovePDFs editor, choose your highlight color, and drag over the text you want to highlight. Multiple colors supported.' },
      { q: 'How to edit a PDF on iPhone free?', a: 'Open LovePDFs in Safari on your iPhone, upload the PDF, use the editor toolbar to add annotations, and tap Save PDF to download.' }
    ],
    related: ['sign-pdf', 'add-watermark-pdf', 'redact-pdf', 'pdf-to-word']
  },

  {
    id: 'extract-pages-pdf',
    toolId: 'extractpg',
    title: 'Extract Pages from PDF Free — Save as Separate File | LovePDFs',
    meta: 'Extract pages from PDF free online. Save one page or a range of PDF pages as a separate file — no software, no upload, instant download with LovePDFs.',
    h1: 'Extract Pages from PDF Free',
    desc: 'Pull out specific pages or page ranges from any PDF and save them as a new document. No uploads, no software — runs in your browser.',
    instructions: [
      'Upload your PDF to the Extract Pages tool.',
      'Select the pages you want to extract by clicking their thumbnails.',
      'Or enter a page range manually (e.g. 2-5, 8, 12).',
      'Click "Extract Pages" and download your new PDF.'
    ],
    benefits: [
      { title: 'Extract any page range', desc: 'Get exactly the pages you need as a standalone PDF — no manual cutting needed.' },
      { title: 'Visual selection', desc: 'Click page thumbnails to select exactly what to extract — see before you confirm.' },
      { title: 'Private browser processing', desc: 'Your original document and the extracted pages never leave your device.' }
    ],
    faqs: [
      { q: 'How to extract one page from PDF free?', a: 'Upload your PDF, click the single page thumbnail you need, and click Extract Pages. That page downloads as its own PDF file.' },
      { q: 'How to save specific pages of a PDF as a new file?', a: 'Select multiple page thumbnails or enter a range like "3-7" to extract those pages into a new PDF document.' },
      { q: 'What is the difference between Split PDF and Extract Pages?', a: 'Split PDF divides a document into multiple files. Extract Pages lets you select and save specific pages as a single new document.' }
    ],
    related: ['split-pdf', 'remove-pages-pdf', 'organize-pdf', 'merge-pdf']
  },

  {
    id: 'repair-pdf',
    toolId: 'repair',
    title: 'Repair Corrupted PDF Free Online — Fix Damaged PDF | LovePDFs',
    meta: 'Repair PDF online free. Fix corrupted, damaged or broken PDF files for free in your browser — no software, no upload to server with LovePDFs.',
    h1: 'Repair Corrupted PDF File Free',
    desc: 'Recover and fix damaged, corrupted, or broken PDF files. The repair engine rebuilds document structure to restore readable content from problematic PDFs.',
    instructions: [
      'Upload your corrupted or damaged PDF file.',
      'The tool analyses the file structure and detects errors.',
      'Click "Repair PDF" to attempt structural repair.',
      'Download the recovered PDF and check the result.'
    ],
    benefits: [
      { title: 'Recovers unreadable PDFs', desc: 'Rebuilds PDF document structure to restore content from files that fail to open.' },
      { title: 'No data sent to servers', desc: 'Your confidential documents are processed locally — no external server sees your data.' },
      { title: 'Free recovery attempt', desc: 'Try repairing your damaged PDF at no cost before seeking paid recovery options.' }
    ],
    faqs: [
      { q: 'How to fix a corrupted PDF file free?', a: 'Upload your damaged PDF to LovePDFs Repair tool. It analyses the file structure and attempts to rebuild it. Download the repaired version.' },
      { q: 'Why is my PDF corrupted?', a: 'PDFs can become corrupted due to incomplete downloads, storage errors, virus damage, or interrupted file transfers. The repair tool can fix many common corruption types.' },
      { q: 'Will the repair tool recover all my content?', a: 'Recovery success depends on the type and extent of corruption. The tool can fix structural errors but may not recover severely damaged files.' }
    ],
    related: ['compress-pdf', 'edit-pdf', 'flatten-pdf', 'ocr-extract-text']
  },

  {
    id: 'ocr-extract-text',
    toolId: 'ocr',
    title: 'OCR PDF Free — Extract Text from Scanned PDF Online | LovePDFs',
    meta: 'OCR PDF online free. Extract text from scanned PDF, make PDF searchable, convert image PDF to text — free, browser-based, private with LovePDFs.',
    h1: 'OCR PDF — Extract Text from Scanned Documents Free',
    desc: 'Use optical character recognition to extract text from scanned PDF pages. Make any image-based PDF searchable and copy-able — free and private.',
    instructions: [
      'Upload your scanned PDF or image-based PDF.',
      'Select the language of the document for best accuracy.',
      'Click "Run OCR" to extract text from all pages.',
      'Download the text-searchable PDF or copy the extracted text.'
    ],
    benefits: [
      { title: 'Makes scanned PDFs searchable', desc: 'After OCR, you can search, copy, and select text in previously image-only PDF pages.' },
      { title: 'Multi-language support', desc: 'Recognizes text in English, Hindi, and many other languages for accurate extraction.' },
      { title: 'Private processing', desc: 'OCR runs locally using browser-based technology — your scanned documents are never uploaded.' }
    ],
    faqs: [
      { q: 'How to extract text from scanned PDF free?', a: 'Upload your scanned PDF to LovePDFs OCR tool, select the document language, and click Run OCR. Download the searchable PDF or copy the extracted text.' },
      { q: 'How to make a scanned PDF searchable free?', a: 'Run the OCR tool on your scanned document. It adds a text layer to the PDF so you can search, highlight, and copy text from previously image-only pages.' },
      { q: 'How to convert image PDF to text free?', a: 'Upload your image-based PDF to the OCR tool and it will recognize all text characters in the scanned images and make them selectable.' },
      { q: 'How accurate is the OCR text extraction?', a: 'Accuracy depends on scan quality. Clean, high-resolution scans of printed text achieve very high accuracy. Handwritten text may have lower accuracy.' }
    ],
    related: ['pdf-to-word', 'edit-pdf', 'repair-pdf', 'pdf-to-text']
  },

  {
    id: 'sign-pdf',
    toolId: 'sign',
    title: 'Sign PDF Online Free — Add Digital Signature Without Printing | LovePDFs',
    meta: 'Sign PDF online free without printing or scanning. Add digital signature to any PDF — draw, type, or upload signature — private, no signup with LovePDFs.',
    h1: 'Sign PDF Online Free — No Printing Needed',
    desc: 'Add your signature to any PDF digitally. Draw with mouse or touch, type your name, or upload a signature image — fully private, never uploaded.',
    instructions: [
      'Upload the PDF you need to sign.',
      'Click "Add Signature" and choose Draw, Type, or Upload.',
      'Draw, type, or upload your signature image.',
      'Position and resize the signature on the page, then download.'
    ],
    benefits: [
      { title: 'Three signature methods', desc: 'Draw with mouse/touch, type your name in a signature font, or upload an image of your real signature.' },
      { title: 'No printing or scanning', desc: 'Sign documents entirely digitally — no need to print, physically sign, scan, and re-upload.' },
      { title: 'Works on phone', desc: 'Sign PDFs on iPhone or Android using your finger — perfect for contracts on the go.' }
    ],
    faqs: [
      { q: 'How to add signature to PDF free without printing?', a: 'Open LovePDFs Sign PDF tool, upload your document, draw or type your signature, position it on the page, and download the signed PDF — no printing needed.' },
      { q: 'How to sign PDF on iPhone for free?', a: 'Open LovePDFs in Safari, upload the PDF, use your finger to draw your signature in the Draw mode, position it, and download the signed document.' },
      { q: 'How to sign PDF without Adobe Acrobat?', a: 'LovePDFs is a completely free alternative to Adobe Acrobat Sign. Upload, sign, and download — no subscription or software needed.' },
      { q: 'Is a digital signature from LovePDFs legally valid?', a: 'Electronic signatures are legally valid in most countries for most document types. For legally binding contracts, ensure you comply with your jurisdiction\'s e-signature laws (eIDAS in EU, ESIGN in US).' },
      { q: 'How to sign PDF on Android free?', a: 'Open LovePDFs in Chrome on Android, upload your PDF, draw your signature using touch, place it on the signature line, and download.' }
    ],
    related: ['edit-pdf', 'protect-pdf', 'redact-pdf', 'unlock-pdf']
  },

  {
    id: 'redact-pdf',
    toolId: 'redact',
    title: 'Redact PDF Free — Permanently Black Out Text Online | LovePDFs',
    meta: 'Redact PDF online free. Permanently remove and black out sensitive text from any PDF — private, browser-based, no upload to server with LovePDFs.',
    h1: 'Redact PDF Free — Permanently Remove Sensitive Text',
    desc: 'Permanently black out sensitive information in any PDF. Redaction is irreversible — the hidden text cannot be recovered. Runs entirely in your browser.',
    instructions: [
      'Upload your PDF to the Redact tool.',
      'Draw black redaction boxes over the text you want to remove permanently.',
      'Click "Apply Redactions" to permanently black out the selected areas.',
      'Download the redacted PDF — the covered content is gone forever.'
    ],
    benefits: [
      { title: 'Permanent redaction', desc: 'Unlike adding a black rectangle on top, true redaction permanently removes the underlying text data.' },
      { title: 'GDPR and privacy compliance', desc: 'Redact personal data, addresses, account numbers, and sensitive information before sharing documents.' },
      { title: 'Browser-based and private', desc: 'Your sensitive documents are never uploaded to any server — all redaction happens locally.' }
    ],
    faqs: [
      { q: 'How to black out text in PDF permanently free?', a: 'Upload your PDF to LovePDFs Redact tool, draw over the text you want to hide, and click Apply Redactions. The text is permanently removed — not just covered.' },
      { q: 'What is the difference between redacting and drawing a black box on PDF?', a: 'Drawing a black rectangle only visually hides text — the underlying text is still in the file and can be copied. True redaction permanently removes the text data itself.' },
      { q: 'How to remove personal information from PDF before sharing?', a: 'Use the Redact tool to draw over names, addresses, account numbers, or any personal data. Apply the redactions and the information is permanently deleted from the PDF.' },
      { q: 'Is PDF redaction in LovePDFs truly permanent?', a: 'Yes — the redact tool permanently removes the underlying text and image data in the redacted areas, not just adds a visual overlay.' }
    ],
    related: ['edit-pdf', 'protect-pdf', 'sign-pdf', 'remove-annotations-pdf']
  },

  {
    id: 'compare-pdf',
    toolId: 'compare',
    title: 'Compare Two PDF Files Free Online — Find Differences | LovePDFs',
    meta: 'Compare PDF files free online. Find differences between two PDF documents side by side for free — no upload to server, browser-based with LovePDFs.',
    h1: 'Compare Two PDF Files Free Online',
    desc: 'View two PDF documents side by side to spot differences in text and layout. Perfect for reviewing contract revisions, document versions, and edits.',
    instructions: [
      'Upload your first PDF (original version).',
      'Upload your second PDF (revised version).',
      'The tool displays both documents side by side for comparison.',
      'Differences are highlighted for easy identification.'
    ],
    benefits: [
      { title: 'Side-by-side comparison', desc: 'View both document versions simultaneously with synchronized scrolling.' },
      { title: 'Difference highlighting', desc: 'Changed text and content differences are visually highlighted for quick review.' },
      { title: 'No upload required', desc: 'Both documents are loaded and compared locally in your browser — sensitive documents stay private.' }
    ],
    faqs: [
      { q: 'How to find differences between two PDF documents free?', a: 'Upload both PDFs to LovePDFs Compare tool. The documents are displayed side by side with differences highlighted — no server upload needed.' },
      { q: 'How to compare two versions of a contract PDF?', a: 'Upload the original and revised contract versions. The comparison highlights text changes, additions, and deletions between the two documents.' },
      { q: 'Can I compare PDFs without uploading them to a server?', a: 'Yes — LovePDFs PDF comparison runs entirely in your browser. Both documents are loaded locally and never sent to any external server.' }
    ],
    related: ['edit-pdf', 'split-pdf', 'ocr-extract-text', 'pdf-to-word']
  },

  {
    id: 'html-to-pdf',
    toolId: 'html2pdf',
    title: 'Convert HTML to PDF Free Online | LovePDFs',
    meta: 'HTML to PDF converter free. Convert any webpage or HTML file to PDF online for free — browser-based, no upload, instant download with LovePDFs.',
    h1: 'Convert HTML to PDF Free Online',
    desc: 'Convert HTML files or web page code into a PDF document. Paste HTML content or upload an HTML file — convert and download instantly.',
    instructions: [
      'Upload your HTML file or paste HTML code into the input area.',
      'The tool renders the HTML as it would appear in a browser.',
      'Click "Convert to PDF" to generate the PDF version.',
      'Download your HTML-to-PDF document.'
    ],
    benefits: [
      { title: 'Webpage to PDF', desc: 'Turn any HTML webpage content into a permanent, shareable PDF document.' },
      { title: 'Preserve web styling', desc: 'The converter renders HTML with CSS styling for accurate visual reproduction.' },
      { title: 'Developer-friendly', desc: 'Great for generating PDFs from web reports, invoices, and HTML email templates.' }
    ],
    faqs: [
      { q: 'How to convert HTML to PDF free online?', a: 'Upload your HTML file to LovePDFs HTML to PDF tool or paste your HTML code, click Convert, and download the PDF version instantly.' },
      { q: 'How to save a webpage as PDF free?', a: 'For saving a live webpage, use your browser\'s Print to PDF function. For converting an HTML file, upload it to LovePDFs HTML to PDF tool.' }
    ],
    related: ['word-to-pdf', 'edit-pdf', 'compress-pdf', 'protect-pdf']
  },

  {
    id: 'pdf-to-pdfa',
    toolId: 'pdfa',
    title: 'Convert PDF to PDF/A Free — Archival Format Online | LovePDFs',
    meta: 'Convert PDF to PDF/A free. Create archival PDF/A-1b compliant files for court, government, and long-term document storage — browser-based with LovePDFs.',
    h1: 'Convert PDF to PDF/A Free Online',
    desc: 'Create ISO-compliant PDF/A archival documents for court submissions, government records, and long-term storage. Fully private, browser-based conversion.',
    instructions: [
      'Upload your standard PDF file.',
      'Select the PDF/A compliance level (PDF/A-1b recommended).',
      'Click "Convert to PDF/A" to generate the archival version.',
      'Download your PDF/A compliant document.'
    ],
    benefits: [
      { title: 'Court and government compliant', desc: 'PDF/A format meets archival requirements for legal, government, and regulatory document submissions.' },
      { title: 'Long-term preservation', desc: 'PDF/A embeds all fonts and resources ensuring the document looks identical in 50+ years.' },
      { title: 'ISO standard compliance', desc: 'Generates documents meeting ISO 19005 PDF/A-1b archival specifications.' }
    ],
    faqs: [
      { q: 'What is PDF/A format and why do I need it?', a: 'PDF/A is an ISO-standardized archival format for long-term preservation. It embeds all fonts, restricts certain features, and ensures documents remain readable indefinitely.' },
      { q: 'How to convert PDF to PDF/A for court submission?', a: 'Upload your PDF to LovePDFs PDF/A converter, select PDF/A-1b compliance level, and download the archival-compliant document for submission.' },
      { q: 'How to create a PDF/A file free without Adobe?', a: 'LovePDFs converts any PDF to PDF/A format for free in your browser — no Adobe Acrobat Pro or paid software needed.' }
    ],
    related: ['protect-pdf', 'compress-pdf', 'edit-pdf', 'word-to-pdf']
  },

  {
    id: 'add-page-numbers-pdf',
    toolId: 'pagenums',
    title: 'Add Page Numbers to PDF Free Online | LovePDFs',
    meta: 'Add page numbers to PDF free online. Number pages in PDF — choose position, format, font, and starting number — browser-based, no Adobe with LovePDFs.',
    h1: 'Add Page Numbers to PDF Free',
    desc: 'Add customizable page numbers to any PDF. Choose position (header/footer, left/center/right), number format, font size, and starting number.',
    instructions: [
      'Upload your PDF to the Page Numbers tool.',
      'Choose position: bottom-center, bottom-right, top-center, etc.',
      'Select number format (1, 2, 3 or i, ii, iii) and starting number.',
      'Click "Add Page Numbers" and download your numbered PDF.'
    ],
    benefits: [
      { title: 'Fully customizable position', desc: 'Place numbers at bottom-center, bottom-right, top-left, or any footer/header position.' },
      { title: 'Roman numeral support', desc: 'Choose Arabic (1, 2, 3) or Roman (i, ii, iii) numeral styles.' },
      { title: 'Custom starting number', desc: 'Start numbering from any page number — useful for chapters or appendices.' }
    ],
    faqs: [
      { q: 'How to add page numbers to PDF free without Adobe?', a: 'Upload your PDF to LovePDFs, choose your number position and format, and click Add Page Numbers. No Adobe Acrobat needed.' },
      { q: 'How to add page numbers starting from a specific page?', a: 'Set the starting page number to your desired value. For example, starting from 5 will number pages 5, 6, 7... from the first page.' },
      { q: 'Can I add page numbers to PDF on mobile?', a: 'Yes — open LovePDFs on any mobile browser, upload your PDF, configure page numbers, and download. Works on iPhone and Android.' }
    ],
    related: ['edit-pdf', 'add-watermark-pdf', 'header-footer-pdf', 'organize-pdf']
  },

  {
    id: 'grayscale-pdf',
    toolId: 'grayscale',
    title: 'Convert PDF to Black and White Free — Save Ink | LovePDFs',
    meta: 'Convert PDF to grayscale free online. Make PDF black and white to save ink when printing — browser-based, instant, no software needed with LovePDFs.',
    h1: 'Convert PDF to Black and White Free',
    desc: 'Convert any colour PDF to grayscale to save ink when printing and reduce file size. Processes all pages instantly in your browser.',
    instructions: [
      'Upload your colour PDF file.',
      'The tool converts all colour content to grayscale automatically.',
      'Click "Convert to Grayscale" to process.',
      'Download your black and white PDF.'
    ],
    benefits: [
      { title: 'Save printer ink', desc: 'Grayscale PDFs use only black ink — dramatically reduce ink usage for document printing.' },
      { title: 'Smaller file size', desc: 'Removing colour data also reduces PDF file size, making it easier to share.' },
      { title: 'Instant browser conversion', desc: 'All colour-to-grayscale processing runs locally — no upload required.' }
    ],
    faqs: [
      { q: 'How to convert PDF to black and white to save ink?', a: 'Upload your colour PDF to LovePDFs Grayscale tool and click Convert. The result uses only black ink when printed, saving significant ink costs.' },
      { q: 'How to print a PDF in black and white?', a: 'Convert your PDF to grayscale first using this tool, then print normally. Alternatively, set your printer to Grayscale mode in print settings.' },
      { q: 'Does converting to grayscale reduce PDF file size?', a: 'Yes — removing colour data from images and vector graphics typically reduces PDF file size by 20-40%.' }
    ],
    related: ['compress-pdf', 'edit-pdf', 'flatten-pdf', 'resize-pdf']
  },

  {
    id: 'flatten-pdf',
    toolId: 'flatten',
    title: 'Flatten PDF Free Online — Flatten Form Fields | LovePDFs',
    meta: 'Flatten PDF online free. Flatten form fields, annotations and comments into the PDF permanently — browser-based, no software needed with LovePDFs.',
    h1: 'Flatten PDF Free Online',
    desc: 'Permanently flatten form fields, annotations, and interactive elements into the PDF page content. Makes your PDF universally viewable and prevents editing.',
    instructions: [
      'Upload your PDF with form fields or annotations.',
      'Click "Flatten PDF" to permanently merge all form data into the page.',
      'Download your flattened, non-editable PDF.'
    ],
    benefits: [
      { title: 'Lock form responses', desc: 'Permanently bake filled form field answers into the PDF so they cannot be changed.' },
      { title: 'Universal compatibility', desc: 'Flattened PDFs display consistently across all PDF viewers and printers.' },
      { title: 'Prevent further editing', desc: 'Remove interactive elements to create a final, non-editable version for archiving.' }
    ],
    faqs: [
      { q: 'How to flatten a PDF form field free?', a: 'Upload your filled PDF form to LovePDFs Flatten tool and click Flatten PDF. All form fields are permanently embedded into the page content.' },
      { q: 'What does flattening a PDF do?', a: 'Flattening merges all form fields, annotations, and interactive layers permanently into the static page content, making the document non-editable.' },
      { q: 'How to make a filled PDF form non-editable?', a: 'Flatten the PDF to permanently lock all filled form data. The form fields become part of the page and cannot be changed in any viewer.' }
    ],
    related: ['edit-pdf', 'protect-pdf', 'sign-pdf', 'compress-pdf']
  },

  {
    id: 'edit-pdf-metadata',
    toolId: 'metadata',
    title: 'Edit PDF Metadata Free Online — Title, Author, Subject | LovePDFs',
    meta: 'Edit PDF metadata free online. Change PDF title, author, subject and keywords — remove personal metadata before sharing, browser-based with LovePDFs.',
    h1: 'Edit PDF Metadata Free Online',
    desc: 'Edit or remove the hidden metadata from any PDF — title, author, subject, keywords, and creation date. Great for privacy before sharing documents.',
    instructions: [
      'Upload your PDF file.',
      'Edit the metadata fields: Title, Author, Subject, Keywords.',
      'Clear fields you want to remove for privacy.',
      'Click "Save Metadata" and download the updated PDF.'
    ],
    benefits: [
      { title: 'Remove personal information', desc: 'Strip author name, company, and other personal data embedded in PDF metadata before sharing.' },
      { title: 'Improve document organization', desc: 'Set accurate titles and keywords so PDFs are findable in document management systems.' },
      { title: 'Privacy-first processing', desc: 'Metadata editing runs in your browser — your documents are never uploaded.' }
    ],
    faqs: [
      { q: 'How to remove author name from PDF metadata free?', a: 'Upload your PDF to the Metadata editor, clear the Author field, and click Save. The author information is removed from the file before you download.' },
      { q: 'How to change PDF title and author free?', a: 'Upload your PDF, edit the Title and Author fields with the correct information, and download the updated file.' },
      { q: 'What personal data is hidden in PDF metadata?', a: 'PDFs can contain author name, company name, software used, creation date, modification date, and keywords. Use this tool to view and remove any sensitive metadata.' }
    ],
    related: ['redact-pdf', 'protect-pdf', 'edit-pdf', 'flatten-pdf']
  },

  {
    id: 'extract-images-pdf',
    toolId: 'extractimg',
    title: 'Extract Images from PDF Free Online | LovePDFs',
    meta: 'Extract images from PDF free online. Save all embedded images from any PDF as JPG or PNG files — browser-based, no upload needed with LovePDFs.',
    h1: 'Extract Images from PDF Free Online',
    desc: 'Save all images embedded in a PDF as separate JPG or PNG files. Download individually or as a ZIP archive — processed entirely in your browser.',
    instructions: [
      'Upload your PDF containing embedded images.',
      'The tool scans all pages and detects embedded image resources.',
      'Click "Extract Images" to pull all images from the document.',
      'Download individual images or all images in a ZIP file.'
    ],
    benefits: [
      { title: 'Extract all images at once', desc: 'Save every image embedded in a PDF document without manually screenshotting.' },
      { title: 'Original image quality', desc: 'Extracted images maintain their original embedded resolution and quality.' },
      { title: 'ZIP download', desc: 'Download all extracted images in a single ZIP file for convenience.' }
    ],
    faqs: [
      { q: 'How to extract images from PDF free?', a: 'Upload your PDF to LovePDFs Extract Images tool and click Extract. All embedded images are found and made available to download as JPG files.' },
      { q: 'How to save images from a PDF without screenshot?', a: 'The Extract Images tool finds and saves the actual embedded image data — much higher quality than taking screenshots of the PDF.' },
      { q: 'Can I extract images from a scanned PDF?', a: 'A scanned PDF is itself one large image per page. Use our PDF to JPG converter to convert each scanned page to a separate image file.' }
    ],
    related: ['pdf-to-jpg', 'edit-pdf', 'compress-image', 'ocr-extract-text']
  },

  {
    id: 'resize-pdf',
    toolId: 'resizepdf',
    title: 'Resize PDF Page Size Free Online — A4, Letter, Custom | LovePDFs',
    meta: 'Resize PDF page size free online. Change PDF pages from A4 to Letter, A3, or any custom size — browser-based, no software needed with LovePDFs.',
    h1: 'Resize PDF Page Size Free Online',
    desc: 'Change the page size of any PDF to A4, US Letter, A3, or custom dimensions. Scale content to fit or adjust page canvas size independently.',
    instructions: [
      'Upload your PDF file.',
      'Choose a target page size: A4, US Letter, A3, A5, or custom dimensions.',
      'Choose whether to scale content to fit or preserve content size.',
      'Click "Resize PDF" and download the reformatted document.'
    ],
    benefits: [
      { title: 'Change A4 to Letter and back', desc: 'Fix PDF documents formatted for the wrong region — convert between A4 (Europe) and US Letter format.' },
      { title: 'Custom dimensions', desc: 'Set any custom width and height in mm, cm, or inches for specialized printing needs.' },
      { title: 'Scale to fit option', desc: 'Automatically scale page content to fit the new page size without overflow.' }
    ],
    faqs: [
      { q: 'How to change PDF page size from A4 to Letter free?', a: 'Upload your PDF, select US Letter as the target size, enable Scale to Fit, and click Resize PDF. Content is reformatted to Letter size.' },
      { q: 'How to resize all pages in a PDF to the same size?', a: 'Upload your PDF with mixed page sizes, choose your target size, and click Resize. All pages are standardized to the same dimensions.' }
    ],
    related: ['crop-pdf', 'rotate-pdf', 'compress-pdf', 'organize-pdf']
  },

  {
    id: 'alternate-mix-pdf',
    toolId: 'altmix',
    title: 'Alternate and Mix PDF Pages Free Online | LovePDFs',
    meta: 'Alternate and mix PDF pages free. Interleave pages from two PDFs — perfect for combining front and back sides of double-sided scans with LovePDFs.',
    h1: 'Alternate and Mix PDF Pages Free',
    desc: 'Interleave pages from two PDFs in alternating order. Perfect for combining odd and even pages from double-sided documents scanned separately.',
    instructions: [
      'Upload your first PDF (e.g. odd pages scan).',
      'Upload your second PDF (e.g. even pages scan).',
      'Choose the interleave order (1,1,2,1,3,1 or alternating).',
      'Click "Mix PDFs" and download the combined document.'
    ],
    benefits: [
      { title: 'Fix double-sided scans', desc: 'Combine separately scanned front and back sides of a document into the correct page order.' },
      { title: 'Flexible interleaving', desc: 'Choose from different alternating patterns to match your specific document structure.' },
      { title: 'Browser-based privacy', desc: 'Both uploaded PDFs are processed locally — no server sees your documents.' }
    ],
    faqs: [
      { q: 'How to combine front and back scanned pages into one PDF?', a: 'Upload the front-side scan as PDF 1 and back-side scan as PDF 2. The Alternate Mix tool interleaves them into the correct front-back-front-back page order.' },
      { q: 'What is alternating PDF page mix used for?', a: 'Mainly used when scanning double-sided documents separately — one scan for all front pages and one for all back pages. Alternating Mix combines them correctly.' }
    ],
    related: ['merge-pdf', 'organize-pdf', 'split-pdf', 'remove-pages-pdf']
  },

  {
    id: 'header-footer-pdf',
    toolId: 'headfoot',
    title: 'Add Header and Footer to PDF Free Online | LovePDFs',
    meta: 'Add header and footer to PDF free online. Insert custom text, page numbers, date or logo in header/footer — browser-based, no Adobe with LovePDFs.',
    h1: 'Add Header and Footer to PDF Free',
    desc: 'Add custom text, page numbers, dates, or branding to the header and footer of any PDF. Choose fonts, size, position, and which pages to apply to.',
    instructions: [
      'Upload your PDF file.',
      'Enter your header text (left, center, right sections).',
      'Enter your footer text and choose page number insertion.',
      'Click "Add Header/Footer" and download the result.'
    ],
    benefits: [
      { title: 'Custom branding', desc: 'Add your company name, document title, or confidentiality notice to every page header.' },
      { title: 'Page numbers in footer', desc: 'Insert auto-incrementing page numbers combined with custom footer text.' },
      { title: 'Selective page application', desc: 'Apply headers and footers to all pages, or skip the first/last page.' }
    ],
    faqs: [
      { q: 'How to add header to PDF free without Adobe?', a: 'Upload your PDF to LovePDFs Header/Footer tool, enter your header text, and click Add Header/Footer. No Adobe Acrobat needed.' },
      { q: 'How to add company name to every page of PDF free?', a: 'Enter your company name in the header center field. It will appear on every page of the PDF after processing.' }
    ],
    related: ['add-page-numbers-pdf', 'add-watermark-pdf', 'edit-pdf', 'organize-pdf']
  },

  {
    id: 'remove-annotations-pdf',
    toolId: 'rmannot',
    title: 'Remove Annotations from PDF Free Online | LovePDFs',
    meta: 'Remove annotations from PDF free online. Strip comments, highlights, sticky notes and markups from PDF — browser-based, private with LovePDFs.',
    h1: 'Remove Annotations from PDF Free',
    desc: 'Strip all comments, highlights, sticky notes, underlines, and markup annotations from any PDF. Get a clean document for final sharing.',
    instructions: [
      'Upload your annotated PDF file.',
      'The tool detects all annotation types in the document.',
      'Click "Remove Annotations" to strip all markup layers.',
      'Download the clean, annotation-free PDF.'
    ],
    benefits: [
      { title: 'Remove all markup types', desc: 'Strips highlights, sticky notes, underlines, strikethrough, drawing annotations, and comments.' },
      { title: 'Clean final document', desc: 'Produce a clean, professional version of a reviewed document before final distribution.' },
      { title: 'Private processing', desc: 'Document annotation data is processed entirely in your browser.' }
    ],
    faqs: [
      { q: 'How to remove all annotations from PDF free?', a: 'Upload your PDF to LovePDFs Remove Annotations tool and click Remove. All highlights, comments, and markup are stripped from the document.' },
      { q: 'How to delete comments from PDF without Adobe?', a: 'LovePDFs removes all comment and annotation types for free in your browser — no Adobe Acrobat or paid software required.' }
    ],
    related: ['edit-pdf', 'flatten-pdf', 'redact-pdf', 'protect-pdf']
  },

  {
    id: 'deskew-pdf',
    toolId: 'deskew',
    title: 'Deskew PDF Free Online — Straighten Scanned Pages | LovePDFs',
    meta: 'Deskew PDF online free. Straighten crooked, tilted scanned pages automatically — browser-based, no software needed, private with LovePDFs.',
    h1: 'Deskew PDF — Straighten Scanned Pages Free',
    desc: 'Automatically detect and correct tilted or skewed pages in scanned PDF documents. Fix crooked scans in seconds without any software.',
    instructions: [
      'Upload your scanned PDF with skewed or tilted pages.',
      'The tool automatically detects the skew angle of each page.',
      'Click "Deskew PDF" to straighten all pages automatically.',
      'Download the corrected, straight-page PDF.'
    ],
    benefits: [
      { title: 'Automatic skew detection', desc: 'Intelligently detects the tilt angle of each scanned page and corrects it automatically.' },
      { title: 'Improves OCR accuracy', desc: 'Straightened pages give significantly better results when using OCR text extraction.' },
      { title: 'Batch correction', desc: 'Corrects all skewed pages in a multi-page scanned document at once.' }
    ],
    faqs: [
      { q: 'How to straighten a scanned PDF for free?', a: 'Upload your scanned PDF to LovePDFs Deskew tool and click Deskew PDF. Tilted pages are automatically detected and straightened.' },
      { q: 'Why deskew a scanned document?', a: 'Crooked scans are harder to read and produce poor OCR results. Deskewing straightens pages for professional-looking documents and better text recognition.' }
    ],
    related: ['rotate-pdf', 'ocr-extract-text', 'repair-pdf', 'flatten-pdf']
  },

  {
    id: 'pdf-to-text',
    toolId: 'pdf2text',
    title: 'Extract Text from PDF Free Online — PDF to TXT | LovePDFs',
    meta: 'Extract text from PDF free online. Convert PDF to plain text (TXT) — copy all text from PDF for free in your browser, no signup with LovePDFs.',
    h1: 'Extract Text from PDF Free — PDF to TXT',
    desc: 'Extract all text content from any PDF as a plain text file. Copy the entire text of a PDF document in seconds — runs privately in your browser.',
    instructions: [
      'Upload your PDF file.',
      'The tool extracts all text layers from every page.',
      'Click "Extract Text" to get the plain text output.',
      'Download the .txt file or copy the text directly.'
    ],
    benefits: [
      { title: 'Full document text extraction', desc: 'Get all text from every page of a PDF in one clean plain text file.' },
      { title: 'Copy-paste ready', desc: 'Extracted text is clean and ready to paste into Word, Notepad, or any text editor.' },
      { title: 'Works on digital PDFs', desc: 'Extracts text from digitally-created PDFs instantly. For scanned PDFs, use our OCR tool.' }
    ],
    faqs: [
      { q: 'How to copy all text from a PDF free?', a: 'Upload your PDF to LovePDFs PDF to Text tool and click Extract. All text from the document is extracted and available to copy or download as TXT.' },
      { q: 'How to convert PDF to text file free?', a: 'Upload your PDF and click Extract Text to generate a downloadable .txt plain text file containing all document text.' },
      { q: 'What is the difference between PDF to Text and OCR?', a: 'PDF to Text extracts the existing text layer from digital PDFs. OCR recognizes text from scanned image pages. Use OCR for scanned documents, PDF to Text for digital PDFs.' }
    ],
    related: ['ocr-extract-text', 'pdf-to-word', 'edit-pdf', 'compare-pdf']
  }

];

// Export for use in page generation script
if (typeof module !== 'undefined') {
  module.exports = { TOOLS_SEO };
}
