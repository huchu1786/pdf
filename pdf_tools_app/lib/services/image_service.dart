import 'dart:io';
import 'dart:typed_data';
import 'package:flutter_image_compress/flutter_image_compress.dart';
import 'package:image/image.dart' as img;
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as path;

/// Service for local image processing operations
class ImageService {
  
  /// Compress an image to a specific quality (0-100)
  static Future<String> compressImage(
    String inputPath, {
    int quality = 85,
    int? minWidth,
    int? minHeight,
  }) async {
    final outputDir = await _getOutputDirectory();
    final fileName = _generateOutputFileName(inputPath, '_compressed', 'jpg');
    final outputPath = path.join(outputDir, fileName);

    final result = await FlutterImageCompress.compressWithFile(
      inputPath,
      quality: quality,
      minWidth: minWidth ?? 1920,
      minHeight: minHeight ?? 1080,
      format: CompressFormat.jpeg,
    );

    if (result == null) {
      throw Exception('Failed to compress image');
    }

    await File(outputPath).writeAsBytes(result);
    return outputPath;
  }

  /// Compress image to a target size in KB
  static Future<String> compressToTargetSize(
    String inputPath,
    int targetSizeKB, {
    String format = 'jpg',
  }) async {
    final file = File(inputPath);
    final originalSize = await file.length();
    final targetSizeBytes = targetSizeKB * 1024;

    // If already under target size, just copy
    if (originalSize <= targetSizeBytes) {
      final outputDir = await _getOutputDirectory();
      final fileName = _generateOutputFileName(inputPath, '_compressed', format);
      final outputPath = path.join(outputDir, fileName);
      await file.copy(outputPath);
      return outputPath;
    }

    // Binary search for the right quality
    int low = 1;
    int high = 95;
    Uint8List? bestResult;

    while (low <= high) {
      final mid = (low + high) ~/ 2;
      
      final result = await FlutterImageCompress.compressWithFile(
        inputPath,
        quality: mid,
        format: format == 'png' ? CompressFormat.png : CompressFormat.jpeg,
      );

      if (result == null) {
        throw Exception('Failed to compress image');
      }

      if (result.length <= targetSizeBytes) {
        bestResult = result;
        low = mid + 1; // Try higher quality
      } else {
        high = mid - 1; // Need lower quality
      }
    }

    if (bestResult == null) {
      // If we couldn't get under target, use minimum quality
      bestResult = await FlutterImageCompress.compressWithFile(
        inputPath,
        quality: 1,
        format: format == 'png' ? CompressFormat.png : CompressFormat.jpeg,
      );
    }

    if (bestResult == null) {
      throw Exception('Failed to compress image to target size');
    }

    final outputDir = await _getOutputDirectory();
    final fileName = _generateOutputFileName(inputPath, '_${targetSizeKB}kb', format);
    final outputPath = path.join(outputDir, fileName);

    await File(outputPath).writeAsBytes(bestResult);
    return outputPath;
  }

  /// Resize an image to specific dimensions
  static Future<String> resizeImage(
    String inputPath, {
    int? width,
    int? height,
    bool maintainAspectRatio = true,
  }) async {
    final bytes = await File(inputPath).readAsBytes();
    final image = img.decodeImage(bytes);

    if (image == null) {
      throw Exception('Failed to decode image');
    }

    img.Image resized;
    if (maintainAspectRatio && (width != null || height != null)) {
      // Calculate new dimensions maintaining aspect ratio
      int newWidth = width ?? image.width;
      int newHeight = height ?? image.height;
      
      if (width != null && height == null) {
        newHeight = (image.height * width / image.width).round();
      } else if (height != null && width == null) {
        newWidth = (image.width * height / image.height).round();
      }
      
      resized = img.copyResize(
        image,
        width: newWidth,
        height: newHeight,
        interpolation: img.Interpolation.cubic,
      );
    } else if (width != null && height != null) {
      resized = img.copyResize(
        image,
        width: width,
        height: height,
        interpolation: img.Interpolation.cubic,
      );
    } else {
      throw Exception('Either width or height must be specified');
    }

    final outputDir = await _getOutputDirectory();
    final fileName = _generateOutputFileName(inputPath, '_resized', 'jpg');
    final outputPath = path.join(outputDir, fileName);

    final encoded = img.encodeJpg(resized, quality: 90);
    await File(outputPath).writeAsBytes(encoded);

    return outputPath;
  }

  /// Rotate an image
  static Future<String> rotateImage(
    String inputPath,
    int degrees, // 90, 180, 270
  ) async {
    final bytes = await File(inputPath).readAsBytes();
    final image = img.decodeImage(bytes);

    if (image == null) {
      throw Exception('Failed to decode image');
    }

    img.Image rotated;
    switch (degrees) {
      case 90:
        rotated = img.copyRotate(image, angle: 90);
        break;
      case 180:
        rotated = img.copyRotate(image, angle: 180);
        break;
      case 270:
        rotated = img.copyRotate(image, angle: 270);
        break;
      default:
        throw Exception('Rotation must be 90, 180, or 270 degrees');
    }

    final outputDir = await _getOutputDirectory();
    final fileName = _generateOutputFileName(inputPath, '_rotated$degrees', 'jpg');
    final outputPath = path.join(outputDir, fileName);

    final encoded = img.encodeJpg(rotated, quality: 95);
    await File(outputPath).writeAsBytes(encoded);

    return outputPath;
  }

  /// Flip an image horizontally or vertically
  static Future<String> flipImage(
    String inputPath, {
    bool horizontal = false,
    bool vertical = false,
  }) async {
    final bytes = await File(inputPath).readAsBytes();
    final image = img.decodeImage(bytes);

    if (image == null) {
      throw Exception('Failed to decode image');
    }

    img.Image flipped = image;
    if (horizontal) {
      flipped = img.copyFlip(flipped, direction: img.FlipDirection.horizontal);
    }
    if (vertical) {
      flipped = img.copyFlip(flipped, direction: img.FlipDirection.vertical);
    }

    final outputDir = await _getOutputDirectory();
    final suffix = horizontal && vertical ? '_flipped_both' : 
                   horizontal ? '_flipped_h' : '_flipped_v';
    final fileName = _generateOutputFileName(inputPath, suffix, 'jpg');
    final outputPath = path.join(outputDir, fileName);

    final encoded = img.encodeJpg(flipped, quality: 95);
    await File(outputPath).writeAsBytes(encoded);

    return outputPath;
  }

  /// Convert image format
  static Future<String> convertFormat(
    String inputPath,
    String outputFormat, // jpg, png, webp, bmp
  ) async {
    final bytes = await File(inputPath).readAsBytes();
    final image = img.decodeImage(bytes);

    if (image == null) {
      throw Exception('Failed to decode image');
    }

    final outputDir = await _getOutputDirectory();
    final fileName = _generateOutputFileName(inputPath, '_converted', outputFormat);
    final outputPath = path.join(outputDir, fileName);

    Uint8List encoded;
    switch (outputFormat.toLowerCase()) {
      case 'jpg':
      case 'jpeg':
        encoded = img.encodeJpg(image, quality: 95);
        break;
      case 'png':
        encoded = img.encodePng(image);
        break;
      case 'bmp':
        encoded = img.encodeBmp(image);
        break;
      case 'webp':
        // Use flutter_image_compress for WebP
        final result = await FlutterImageCompress.compressWithFile(
          inputPath,
          format: CompressFormat.webp,
          quality: 95,
        );
        if (result == null) {
          throw Exception('Failed to convert to WebP');
        }
        encoded = result;
        break;
      default:
        throw Exception('Unsupported output format: $outputFormat');
    }

    await File(outputPath).writeAsBytes(encoded);
    return outputPath;
  }

  /// Crop an image to specific coordinates
  static Future<String> cropImage(
    String inputPath, {
    required int x,
    required int y,
    required int width,
    required int height,
  }) async {
    final bytes = await File(inputPath).readAsBytes();
    final image = img.decodeImage(bytes);

    if (image == null) {
      throw Exception('Failed to decode image');
    }

    final cropped = img.copyCrop(
      image,
      x: x,
      y: y,
      width: width,
      height: height,
    );

    final outputDir = await _getOutputDirectory();
    final fileName = _generateOutputFileName(inputPath, '_cropped', 'jpg');
    final outputPath = path.join(outputDir, fileName);

    final encoded = img.encodeJpg(cropped, quality: 95);
    await File(outputPath).writeAsBytes(encoded);

    return outputPath;
  }

  /// Get file size in KB
  static Future<int> getFileSizeKB(String filePath) async {
    final file = File(filePath);
    final bytes = await file.length();
    return (bytes / 1024).round();
  }

  /// Get image dimensions
  static Future<Map<String, int>> getImageDimensions(String filePath) async {
    final bytes = await File(filePath).readAsBytes();
    final image = img.decodeImage(bytes);

    if (image == null) {
      throw Exception('Failed to decode image');
    }

    return {
      'width': image.width,
      'height': image.height,
    };
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

  static String _generateOutputFileName(
    String inputPath,
    String suffix,
    String extension,
  ) {
    final baseName = path.basenameWithoutExtension(inputPath);
    final timestamp = DateTime.now().millisecondsSinceEpoch;
    final cleanExt = extension.toLowerCase().replaceAll('.', '');
    return '${baseName}${suffix}_$timestamp.$cleanExt';
  }
}
