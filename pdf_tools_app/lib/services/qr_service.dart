import 'dart:io';
import 'dart:typed_data';
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as path;
import 'package:qr_flutter/qr_flutter.dart';

/// Service for QR code generation
class QrService {
  
  /// Generate QR code as PNG image
  static Future<String> generateQrCode(
    String data, {
    int size = 512,
    Color foregroundColor = Colors.black,
    Color backgroundColor = Colors.white,
    int errorCorrectionLevel = QrErrorCorrectLevel.M,
  }) async {
    final outputDir = await _getOutputDirectory();
    final fileName = 'qr_code_${DateTime.now().millisecondsSinceEpoch}.png';
    final outputPath = path.join(outputDir, fileName);

    // Create QR code painter
    final qrPainter = QrPainter(
      data: data,
      version: QrVersions.auto,
      errorCorrectionLevel: errorCorrectionLevel,
      color: foregroundColor,
      emptyColor: backgroundColor,
      gapless: true,
    );

    // Convert to image
    final recorder = ui.PictureRecorder();
    final canvas = Canvas(recorder);
    
    // Draw background
    canvas.drawRect(
      Rect.fromLTWH(0, 0, size.toDouble(), size.toDouble()),
      Paint()..color = backgroundColor,
    );
    
    // Draw QR code
    qrPainter.paint(canvas, Size(size.toDouble(), size.toDouble()));
    
    final picture = recorder.endRecording();
    final image = await picture.toImage(size, size);
    final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
    
    if (byteData == null) {
      throw Exception('Failed to generate QR code');
    }

    final pngBytes = byteData.buffer.asUint8List();
    await File(outputPath).writeAsBytes(pngBytes);

    return outputPath;
  }

  /// Generate QR code with logo in center
  static Future<String> generateQrCodeWithLogo(
    String data,
    String logoPath, {
    int size = 512,
    Color foregroundColor = Colors.black,
    Color backgroundColor = Colors.white,
    double logoSize = 64,
  }) async {
    final outputDir = await _getOutputDirectory();
    final fileName = 'qr_code_logo_${DateTime.now().millisecondsSinceEpoch}.png';
    final outputPath = path.join(outputDir, fileName);

    // Load logo
    final logoBytes = await File(logoPath).readAsBytes();
    final logoImage = await _loadImage(logoBytes);

    // Create QR code painter
    final qrPainter = QrPainter(
      data: data,
      version: QrVersions.auto,
      errorCorrectionLevel: QrErrorCorrectLevel.H, // High error correction for logo
      color: foregroundColor,
      emptyColor: backgroundColor,
      gapless: true,
    );

    // Convert to image
    final recorder = ui.PictureRecorder();
    final canvas = Canvas(recorder);
    
    // Draw background
    canvas.drawRect(
      Rect.fromLTWH(0, 0, size.toDouble(), size.toDouble()),
      Paint()..color = backgroundColor,
    );
    
    // Draw QR code
    qrPainter.paint(canvas, Size(size.toDouble(), size.toDouble()));

    // Draw logo in center
    final logoRect = Rect.fromCenter(
      center: Offset(size / 2, size / 2),
      width: logoSize,
      height: logoSize,
    );
    
    // Draw white background for logo
    canvas.drawRect(
      logoRect.inflate(4),
      Paint()..color = backgroundColor,
    );
    
    // Draw logo
    paintImage(
      canvas: canvas,
      rect: logoRect,
      image: logoImage,
      fit: BoxFit.contain,
    );
    
    final picture = recorder.endRecording();
    final image = await picture.toImage(size, size);
    final byteData = await image.toByteData(format: ui.ImageByteFormat.png);
    
    if (byteData == null) {
      throw Exception('Failed to generate QR code with logo');
    }

    final pngBytes = byteData.buffer.asUint8List();
    await File(outputPath).writeAsBytes(pngBytes);

    return outputPath;
  }

  /// Generate QR code SVG string
  static String generateQrCodeSvg(
    String data, {
    String foregroundColor = '#000000',
    String backgroundColor = '#FFFFFF',
    int size = 512,
  }) {
    // For SVG generation, we'd need a more complex implementation
    // This is a placeholder that returns a basic SVG structure
    // In production, you'd use a proper QR to SVG library
    
    return '''
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 $size $size">
  <rect width="$size" height="$size" fill="$backgroundColor"/>
  <!-- QR code modules would be generated here -->
</svg>
''';
  }

  /// Validate QR data
  static bool validateData(String data) {
    // QR codes can handle up to ~4KB of data
    // Check if data is within reasonable limits
    if (data.isEmpty) return false;
    if (data.length > 4000) return false;
    return true;
  }

  /// Get recommended error correction level based on data size
  static int getRecommendedErrorLevel(String data) {
    final length = data.length;
    if (length < 50) return QrErrorCorrectLevel.H; // High
    if (length < 200) return QrErrorCorrectLevel.Q; // Quartile
    if (length < 500) return QrErrorCorrectLevel.M; // Medium
    return QrErrorCorrectLevel.L; // Low
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

  static Future<ui.Image> _loadImage(Uint8List bytes) async {
    final codec = await ui.instantiateImageCodec(bytes);
    final frame = await codec.getNextFrame();
    return frame.image;
  }
}
