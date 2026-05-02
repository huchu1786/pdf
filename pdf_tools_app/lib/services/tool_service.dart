import 'dart:convert';
import 'package:pdf_tools_app/models/tool_model.dart';

class ToolService {
  static final List<ToolModel> _tools = [
    ToolModel(
      id: 'merge-pdf',
      toolId: 'merge',
      title: 'Merge PDF Files Online Free',
      meta: 'Merge PDF files free online with no watermark and no signup. Combine multiple PDFs into one document in your browser.',
      h1: 'Merge PDF Files',
      description: 'Combine PDFs in the order you want. No watermarks, no signup, no file uploads.',
      instructions: [
        'Click "Choose Files" or drag your PDFs into the drop area.',
        'Reorder the files by dragging them into the correct sequence.',
        'Click "Merge PDFs" to combine them into one document.',
        'Download your merged PDF file instantly.'
      ],
      benefits: [
        Benefit(title: 'No watermark ever', description: 'Unlike other free tools, LovePDFs never adds a watermark to your merged document.'),
        Benefit(title: 'Completely private', description: 'All merging happens in your browser. Your files are never uploaded to any server.'),
        Benefit(title: 'Works on mobile', description: 'Merge PDFs on iPhone or Android directly from your browser.')
      ],
      faqs: [
        FAQ(
          question: 'How to merge PDF without watermark free?',
          answer: 'LovePDFs merges PDF files completely free without adding any watermarks.'
        ),
        FAQ(
          question: 'How to merge PDF files on iPhone for free?',
          answer: 'Open LovePDFs in Safari on your iPhone, select the Merge PDF tool, upload your files from Files app, and tap Merge PDFs.'
        ),
        FAQ(
          question: 'How to combine PDF files on Android free?',
          answer: 'Open LovePDFs in Chrome on Android, tap Choose Files, select your PDFs from storage, and hit Merge PDFs.'
        ),
        FAQ(
          question: 'How to merge PDF without uploading to server?',
          answer: 'LovePDFs processes everything locally in your browser using WebAssembly technology.'
        ),
        FAQ(
          question: 'Can I merge more than two PDF files at once?',
          answer: 'Yes, you can merge unlimited PDF files in a single operation.'
        ),
        FAQ(
          question: 'Is there a file size limit for merging PDFs?',
          answer: 'Since everything runs in your browser locally, there are no server-imposed file size limits.'
        ),
      ],
      related: ['split-pdf', 'compress-pdf', 'pdf-to-word', 'organize-pdf']
    ),
    ToolModel(
      id: 'compress-pdf',
      toolId: 'compress',
      title: 'Compress PDF Online Free',
      meta: 'Compress PDF without uploading to any server. Reduce PDF file size free.',
      h1: 'Compress PDF Online',
      description: 'Reduce PDF file size instantly in your browser. Files never leave your device.',
      instructions: [
        'Select or drag and drop your PDF file into the tool.',
        'Choose compression strength: Low, Medium, High, or Extreme.',
        'Click "Compress PDF" and download your smaller file.'
      ],
      benefits: [
        Benefit(title: 'Reduce file size below 1MB', description: 'Compress PDFs to under 1MB for email, sharing, or government forms.'),
        Benefit(title: 'No quality loss', description: 'Smart compression preserves text and images while reducing file size.'),
        Benefit(title: 'No upload to server', description: 'Compression happens locally in your browser. Your files are never uploaded.')
      ],
      faqs: [],
      related: ['reduce-pdf-size', 'pdf-to-jpg', 'compress-pdf']
    ),
    ToolModel(
      id: 'rotate-pdf',
      toolId: 'rotate',
      title: 'Rotate PDF Pages Free',
      meta: 'Rotate PDF pages free and save permanently. Fix upside-down scanned pages.',
      h1: 'Rotate PDF Pages',
      description: 'Fix upside-down or sideways PDF pages in seconds.',
      instructions: [
        'Select or drag and drop your PDF file into the tool.',
        'Choose the rotation angle: 90°, 180°, or 270°.',
        'Select which pages to rotate: All, Odd, or Even pages.',
        'Click "Rotate PDF" and download your corrected document.'
      ],
      benefits: [
        Benefit(title: 'Permanent rotation', description: 'The downloaded file has the rotation permanently saved.'),
        Benefit(title: 'Fix scanned documents', description: 'Correct pages that were scanned sideways or upside down in one click.'),
        Benefit(title: 'Selective page rotation', description: 'Apply different rotations to odd and even pages.')
      ],
      faqs: [],
      related: ['organize-pdf', 'edit-pdf', 'crop-pdf', 'flatten-pdf']
    ),
    ToolModel(
      id: 'unlock-pdf',
      toolId: 'unlock',
      title: 'Remove PDF Password Free Online',
      meta: 'Unlock PDF online free. Remove PDF password and restrictions instantly in your browser.',
      h1: 'Remove PDF Password Free',
      description: 'Remove password protection and print/copy/edit restrictions from any PDF file.',
      instructions: [
        'Upload your password-protected PDF file.',
        'If prompted, enter the password to authorize the removal.',
        'Click "Unlock PDF" to remove all restrictions instantly.',
        'Download your fully unlocked, restriction-free PDF.'
      ],
      benefits: [
        Benefit(title: 'Remove edit and print restrictions', description: 'Enable printing, copying text, and editing on previously locked PDF documents.'),
        Benefit(title: 'Completely private', description: 'Unlocking happens locally in your browser.'),
        Benefit(title: 'Instant results', description: 'No waiting - unlock any PDF in seconds.')
      ],
      faqs: [],
      related: ['protect-pdf', 'sign-pdf', 'edit-pdf', 'redact-pdf']
    ),
    ToolModel(
      id: 'protect-pdf',
      toolId: 'protect',
      title: 'Password Protect PDF Free Online',
      meta: 'Password protect PDF free online. Lock a PDF with a strong password in your browser.',
      h1: 'Password Protect PDF Online',
      description: 'Encrypt and lock your PDF with a password to keep sensitive data confidential.',
      instructions: [
        'Upload the PDF you want to password protect.',
        'Enter a strong password and confirm it in the second field.',
        'Click "Protect PDF" to apply AES encryption instantly.',
        'Download your password-secured document.'
      ],
      benefits: [
        Benefit(title: 'Client-side encryption', description: 'The password and document are processed entirely in your browser.'),
        Benefit(title: 'Secure sensitive documents', description: 'Protect contracts, invoices, medical records, and personal documents before sharing.'),
        Benefit(title: 'Instant protection', description: 'Apply strong password encryption to any PDF in seconds.')
      ],
      faqs: [],
      related: ['unlock-pdf', 'redact-pdf', 'sign-pdf', 'edit-pdf']
    ),
  ];

  static List<ToolModel> getTools() {
    return _tools;
  }

  static ToolModel? getToolById(String id) {
    return _tools.firstWhere((tool) => tool.id == id, orElse: () => null);
  }

  static List<ToolModel> getRelatedTools(String toolId) {
    final tool = getToolById(toolId);
    if (tool == null) return [];

    return tool.related
        .map((id) => getToolById(id))
        .where((tool) => tool != null)
        .cast<ToolModel?>()
        .whereType<ToolModel>()
        .toList();
  }
}