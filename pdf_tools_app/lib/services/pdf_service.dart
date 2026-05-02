import 'dart:io';
import 'dart:typed_data';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:image/image.dart' as img;
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as path;
import 'package:syncfusion_flutter_pdf/pdf.dart' as syncfusion;

/// Service for local PDF processing operations
class PdfService {
  
  /// Convert images to a single PDF
  static Future<String> imagesToPdf(
    List<String> imagePaths, {
    PdfPageFormat pageFormat = PdfPageFormat.a4,
    bool portrait = true,
    double margin = 0,
  }) async {
    final pdf = pw.Document();

    for (final imagePath in imagePaths) {
      final bytes = await File(imagePath).readAsBytes();
      final image = pw.MemoryImage(bytes);

      pdf.addPage(
        pw.Page(
          pageFormat: portrait ? pageFormat : pageFormat.landscape,
          margin: pw.EdgeInsets.all(margin),
          build: (context) {
            return pw.Center(
              child: pw.Image(image, fit: pw.BoxFit.contain),
            );
          },
        ),
      );
    }

    final outputDir = await _getOutputDirectory();
    final fileName = 'images_to_pdf_${DateTime.now().millisecondsSinceEpoch}.pdf';
    final outputPath = path.join(outputDir, fileName);

    final pdfBytes = await pdf.save();
    await File(outputPath).writeAsBytes(pdfBytes);

    return outputPath;
  }

  /// Merge multiple PDF files
  static Future<String> mergePdfs(List<String> pdfPaths) async {
    final outputDir = await _getOutputDirectory();
    final fileName = 'merged_${DateTime.now().millisecondsSinceEpoch}.pdf';
    final outputPath = path.join(outputDir, fileName);

    // Using syncfusion for merging
    final mergedDocument = syncfusion.PdfDocument();

    for (final pdfPath in pdfPaths) {
      final bytes = await File(pdfPath).readAsBytes();
      final document = syncfusion.PdfDocument(inputBytes: bytes);
      
      mergedDocument.importPages(document, importedPageRange: '0-${document.pages.count - 1}');
      document.dispose();
    }

    final mergedBytes = await mergedDocument.save();
    await File(outputPath).writeAsBytes(mergedBytes);
    mergedDocument.dispose();

    return outputPath;
  }

  /// Split PDF into individual pages
  static Future<List<String>> splitPdf(
    String pdfPath, {
    String? pageRange, // e.g., "1-3,5,7-9"
  }) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(inputBytes: bytes);
    final outputDir = await _getOutputDirectory();
    final outputPaths = <String>[];

    final totalPages = document.pages.count;
    List<int> pagesToExtract;

    if (pageRange != null && pageRange.isNotEmpty) {
      pagesToExtract = _parsePageRange(pageRange, totalPages);
    } else {
      // Extract all pages
      pagesToExtract = List.generate(totalPages, (i) => i);
    }

    for (final pageIndex in pagesToExtract) {
      final newDocument = syncfusion.PdfDocument();
      newDocument.importPages(document, importedPageRange: '$pageIndex-$pageIndex');
      
      final fileName = 'page_${pageIndex + 1}_${DateTime.now().millisecondsSinceEpoch}.pdf';
      final outputPath = path.join(outputDir, fileName);
      
      final pdfBytes = await newDocument.save();
      await File(outputPath).writeAsBytes(pdfBytes);
      newDocument.dispose();
      
      outputPaths.add(outputPath);
    }

    document.dispose();
    return outputPaths;
  }

  /// Extract images from PDF
  static Future<List<String>> extractImagesFromPdf(String pdfPath) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(inputBytes: bytes);
    final outputDir = await _getOutputDirectory();
    final outputPaths = <String>[];

    // Note: Syncfusion doesn't directly support image extraction in the community edition
    // This is a placeholder implementation
    // In a real app, you'd use a more complete PDF library or API

    document.dispose();
    
    // For now, return empty list
    // In production, you'd implement proper image extraction
    return outputPaths;
  }

  /// Get PDF info (page count, etc.)
  static Future<Map<String, dynamic>> getPdfInfo(String pdfPath) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(inputBytes: bytes);

    final info = {
      'pageCount': document.pages.count,
      'fileSize': bytes.length,
      'isEncrypted': document.security.encryptionAlgorithm != syncfusion.PdfEncryptionAlgorithm.none,
    };

    document.dispose();
    return info;
  }

  /// Rotate PDF pages
  static Future<String> rotatePdf(
    String pdfPath, {
    required int degrees, // 90, 180, 270
    String? pageRange, // null = all pages
  }) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(inputBytes: bytes);
    final outputDir = await _getOutputDirectory();
    final fileName = 'rotated_${DateTime.now().millisecondsSinceEpoch}.pdf';
    final outputPath = path.join(outputDir, fileName);

    syncfusion.PdfPageRotateAngle angle;
    switch (degrees) {
      case 90:
        angle = syncfusion.PdfPageRotateAngle.rotateAngle90;
        break;
      case 180:
        angle = syncfusion.PdfPageRotateAngle.rotateAngle180;
        break;
      case 270:
        angle = syncfusion.PdfPageRotateAngle.rotateAngle270;
        break;
      default:
        throw Exception('Rotation must be 90, 180, or 270 degrees');
    }

    final totalPages = document.pages.count;
    final pagesToRotate = pageRange != null
        ? _parsePageRange(pageRange, totalPages)
        : List.generate(totalPages, (i) => i);

    for (final pageIndex in pagesToRotate) {
      final page = document.pages[pageIndex];
      page.rotation = angle;
    }

    final rotatedBytes = await document.save();
    await File(outputPath).writeAsBytes(rotatedBytes);
    document.dispose();

    return outputPath;
  }

  /// Compress PDF (basic implementation)
  static Future<String> compressPdf(
    String pdfPath, {
    String quality = 'medium', // low, medium, high
  }) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(inputBytes: bytes);
    final outputDir = await _getOutputDirectory();
    final fileName = 'compressed_${DateTime.now().millisecondsSinceEpoch}.pdf';
    final outputPath = path.join(outputDir, fileName);

    // Note: Full PDF compression requires more advanced techniques
    // This is a basic implementation using syncfusion
    // In production, you'd implement proper compression algorithms

    // Set compression level based on quality
    syncfusion.PdfCompressionLevel compressionLevel;
    switch (quality) {
      case 'low':
        compressionLevel = syncfusion.PdfCompressionLevel.best;
        break;
      case 'high':
        compressionLevel = syncfusion.PdfCompressionLevel.none;
        break;
      case 'medium':
      default:
        compressionLevel = syncfusion.PdfCompressionLevel.normal;
        break;
    }

    document.compressionLevel = compressionLevel;

    final compressedBytes = await document.save();
    await File(outputPath).writeAsBytes(compressedBytes);
    document.dispose();

    return outputPath;
  }

  /// Add password protection to PDF
  static Future<String> protectPdf(
    String pdfPath,
    String password, {
    String? ownerPassword,
    bool allowPrinting = true,
    bool allowCopying = false,
    bool allowEditing = false,
  }) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(inputBytes: bytes);
    final outputDir = await _getOutputDirectory();
    final fileName = 'protected_${DateTime.now().millisecondsSinceEpoch}.pdf';
    final outputPath = path.join(outputDir, fileName);

    final security = document.security;
    security.userPassword = password;
    if (ownerPassword != null) {
      security.ownerPassword = ownerPassword;
    }
    
    // Set permissions
    security.permissions.copyContent = allowCopying;
    security.permissions.print = allowPrinting;
    security.permissions.editAnnotations = allowEditing;
    security.permissions.assembleDocument = allowEditing;

    final protectedBytes = await document.save();
    await File(outputPath).writeAsBytes(protectedBytes);
    document.dispose();

    return outputPath;
  }

  /// Remove password protection (if password is known)
  static Future<String> unlockPdf(
    String pdfPath, {
    String? password,
  }) async {
    final bytes = await File(pdfPath).readAsBytes();
    final document = syncfusion.PdfDocument(
      inputBytes: bytes,
      password: password,
    );
    final outputDir = await _getOutputDirectory();
    final fileName = 'unlocked_${DateTime.now().millisecondsSinceEpoch}.pdf';
    final outputPath = path.join(outputDir, fileName);

    // Remove security by saving without password
    document.security.userPassword = '';
    document.security.ownerPassword = '';

    final unlockedBytes = await document.save();
    await File(outputPath).writeAsBytes(unlockedBytes);
    document.dispose();

    return outputPath;
  }

  // Helper methods
  static Future<String> _getOutputDirectory() async {
    final dir = await getApplicationDocumentsDirectory();
    final outputDir = Directory(path.join(dir.path, 'LovePDFs', 'output'));
    if (!await outputDir.exists()) {
      await outputDir.create(recursive: true);
    }
    return outputDir.path;
  }

  static List<int> _parsePageRange(String range, int totalPages) {
    final pages = <int>[];
    final parts = range.split(',');

    for (final part in parts) {
      final trimmed = part.trim();
      if (trimmed.contains('-')) {
        final rangeParts = trimmed.split('-');
        final start = int.tryParse(rangeParts[0].trim()) ?? 1;
        final end = int.tryParse(rangeParts[1].trim()) ?? totalPages;
        
        for (int i = start - 1; i < end && i < totalPages; i++) {
          if (i >= 0 && !pages.contains(i)) {
            pages.add(i);
          }
        }
      } else {
        final page = int.tryParse(trimmed) ?? 1;
        if (page > 0 && page <= totalPages && !pages.contains(page - 1)) {
          pages.add(page - 1);
        }
      }
    }

    return pages..sort();
  }
}
