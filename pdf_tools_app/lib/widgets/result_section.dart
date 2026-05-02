import 'dart:typed_data';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:share_plus/share_plus.dart';
import '../models/app_tool.dart';
import '../theme/app_theme.dart';

// Conditionally import dart:html for web
import 'download_stub.dart'
    if (dart.library.html) 'download_web.dart';

class ResultSection extends StatelessWidget {
  final AppTool tool;
  final String? outputPath;
  final Uint8List? outputBytes;
  final String outputFileName;
  final String? mimeType;
  final VoidCallback onProcessAnother;

  const ResultSection({
    super.key,
    required this.tool,
    this.outputPath,
    this.outputBytes,
    this.outputFileName = 'download',
    this.mimeType,
    required this.onProcessAnother,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        // Success Animation with pulse effect
        TweenAnimationBuilder(
          tween: Tween<double>(begin: 0.8, end: 1.0),
          duration: const Duration(milliseconds: 600),
          curve: Curves.easeOutBack,
          builder: (context, scale, child) {
            return Transform.scale(
              scale: scale,
              child: Container(
                width: 120,
                height: 120,
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      AppColors.success.withOpacity(0.2),
                      AppColors.success.withOpacity(0.1),
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  shape: BoxShape.circle,
                  boxShadow: [
                    BoxShadow(
                      color: AppColors.success.withOpacity(0.3),
                      blurRadius: 20,
                      spreadRadius: 5,
                    ),
                  ],
                ),
                child: const Icon(
                  Icons.check_circle,
                  size: 70,
                  color: AppColors.success,
                ),
              ),
            );
          },
        ),
        const SizedBox(height: 32),

        // Success Text
        Text(
          'Processing Complete!',
          style: Theme.of(context).textTheme.headlineSmall?.copyWith(
            fontWeight: FontWeight.bold,
            color: AppColors.success,
            letterSpacing: -0.5,
          ),
        ),
        const SizedBox(height: 8),
        Text(
          'Your file has been successfully processed',
          style: Theme.of(context).textTheme.bodyMedium?.copyWith(
            color: AppColors.textSecondary,
          ),
        ),
        const SizedBox(height: 40),

        // Preview Card with enhanced styling
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [
                Theme.of(context).colorScheme.surface,
                tool.category.color.withOpacity(0.05),
              ],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(16),
            border: Border.all(
              color: tool.category.color.withOpacity(0.2),
              width: 1.5,
            ),
            boxShadow: [
              BoxShadow(
                color: tool.category.color.withOpacity(0.1),
                blurRadius: 10,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Row(
            children: [
              Container(
                width: 60,
                height: 60,
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      tool.category.color.withOpacity(0.2),
                      tool.category.color.withOpacity(0.1),
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Icon(
                  _getOutputIcon(),
                  color: tool.category.color,
                  size: 32,
                ),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      _getFileName(),
                      style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.w700,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                    const SizedBox(height: 6),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: tool.category.color.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        tool.category.displayName,
                        style: Theme.of(context).textTheme.bodySmall?.copyWith(
                          color: tool.category.color,
                          fontWeight: FontWeight.w600,
                          fontSize: 11,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: 40),

        // Action Buttons with enhanced styling
        Row(
          children: [
            Expanded(
              flex: 3,
              child: ElevatedButton.icon(
                onPressed: () => _downloadFile(context),
                style: ElevatedButton.styleFrom(
                  backgroundColor: AppColors.success,
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  elevation: 4,
                  shadowColor: AppColors.success.withOpacity(0.4),
                ),
                icon: const Icon(Icons.download_rounded, size: 22),
                label: const Text(
                  'Download',
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
                ),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              flex: 2,
              child: OutlinedButton.icon(
                onPressed: () => _shareFile(context),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  side: BorderSide(color: AppColors.primary.withOpacity(0.5), width: 2),
                ),
                icon: Icon(Icons.share_rounded, size: 20, color: AppColors.primary),
                label: Text(
                  'Share',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                    color: AppColors.primary,
                  ),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 20),
        TextButton.icon(
          onPressed: onProcessAnother,
          style: TextButton.styleFrom(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
          ),
          icon: Icon(Icons.refresh_rounded, color: AppColors.textSecondary),
          label: Text(
            'Process Another File',
            style: TextStyle(
              color: AppColors.textSecondary,
              fontWeight: FontWeight.w500,
            ),
          ),
        ),
      ],
    );
  }

  IconData _getOutputIcon() {
    final formats = tool.supportedOutputFormats;
    if (formats.contains('pdf')) return Icons.picture_as_pdf;
    if (formats.contains('jpg') || formats.contains('png') || formats.contains('webp')) {
      return Icons.image;
    }
    if (formats.contains('docx')) return Icons.description;
    if (formats.contains('xlsx')) return Icons.table_chart;
    return Icons.insert_drive_file;
  }

  String _getFileName() {
    if (outputPath != null) {
      return outputPath!.split('/').last.split('\\').last;
    }
    return outputFileName;
  }

  Future<void> _downloadFile(BuildContext context) async {
    try {
      String ext = tool.supportedOutputFormats.first;
      String fileName = '$outputFileName.$ext';
      String fileMimeType = mimeType ?? _getMimeType(ext);

      if (kIsWeb) {
        // Web: Use web-specific download
        if (outputBytes != null) {
          downloadFileWeb(outputBytes!, fileName, fileMimeType);
        } else {
          throw Exception('No file data available for download');
        }
      } else {
        // Mobile/Desktop: Use file_saver package via conditional import
        await downloadFileMobileDesktop(
          outputPath: outputPath,
          outputBytes: outputBytes,
          outputFileName: outputFileName,
          ext: ext,
        );
      }

      if (context.mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Row(
              children: [
                const Icon(Icons.check_circle, color: Colors.white),
                const SizedBox(width: 12),
                Expanded(child: Text('Downloaded: $fileName')),
              ],
            ),
            backgroundColor: AppColors.success,
            behavior: SnackBarBehavior.floating,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          ),
        );
      }
    } catch (e) {
      if (context.mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Download failed: $e'),
            backgroundColor: AppColors.error,
            behavior: SnackBarBehavior.floating,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          ),
        );
      }
    }
  }

  Future<void> _shareFile(BuildContext context) async {
    try {
      if (kIsWeb) {
        // Web: Show message that sharing isn't supported on web
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Sharing is not supported on web. Please use Download.'),
            backgroundColor: AppColors.info,
            behavior: SnackBarBehavior.floating,
          ),
        );
        return;
      }

      if (outputPath != null) {
        await Share.shareXFiles(
          [XFile(outputPath!)],
          subject: 'Shared via LovePDFs',
        );
      } else if (outputBytes != null) {
        // Save to temp and share
        String ext = tool.supportedOutputFormats.first;
        String fileName = '$outputFileName.$ext';
        // Note: For mobile, we'd need to save bytes to a temp file first
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Use Download for this file'),
            backgroundColor: AppColors.info,
          ),
        );
      }
    } catch (e) {
      if (context.mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Share failed: $e'),
            backgroundColor: AppColors.error,
          ),
        );
      }
    }
  }

  String _getMimeType(String ext) {
    switch (ext.toLowerCase()) {
      case 'pdf':
        return 'application/pdf';
      case 'jpg':
      case 'jpeg':
        return 'image/jpeg';
      case 'png':
        return 'image/png';
      case 'webp':
        return 'image/webp';
      case 'docx':
        return 'application/vnd.openxmlformats-officedocument.wordprocessingml.document';
      case 'xlsx':
        return 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';
      case 'zip':
        return 'application/zip';
      case 'txt':
        return 'text/plain';
      case 'svg':
        return 'image/svg+xml';
      default:
        return 'application/octet-stream';
    }
  }

}
