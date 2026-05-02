import 'dart:typed_data';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import '../models/app_tool.dart';
import '../providers/app_providers.dart';
import '../theme/app_theme.dart';
import '../widgets/file_picker_section.dart';
import '../widgets/processing_section.dart';
import '../widgets/result_section.dart';
import '../widgets/tool_info_section.dart';

class ToolDetailScreen extends ConsumerWidget {
  final AppTool tool;

  const ToolDetailScreen({
    super.key,
    required this.tool,
  });

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final processingState = ref.watch(processingStateProvider(tool.id));
    final selectedFiles = ref.watch(selectedFilesProvider);

    return Scaffold(
      appBar: AppBar(
        title: Text(tool.name),
        actions: [
          // Favorite button
          Consumer(
            builder: (context, ref, child) {
              final isFavorite = ref.watch(favoriteToolsProvider).contains(tool.id);
              return IconButton(
                icon: Icon(
                  isFavorite ? Icons.favorite : Icons.favorite_outline,
                  color: isFavorite ? Colors.red : null,
                ),
                onPressed: () {
                  ref.read(favoriteToolsProvider.notifier).toggleFavorite(tool.id);
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text(
                        isFavorite ? 'Removed from favorites' : 'Added to favorites',
                      ),
                      duration: const Duration(seconds: 1),
                    ),
                  );
                },
              );
            },
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            // Progress indicator
            if (processingState.status != ProcessingStatus.idle &&
                processingState.status != ProcessingStatus.completed &&
                processingState.status != ProcessingStatus.error)
              LinearProgressIndicator(
                value: processingState.status == ProcessingStatus.picking
                    ? null
                    : processingState.progress,
                valueColor: const AlwaysStoppedAnimation<Color>(AppColors.primary),
                backgroundColor: AppColors.primary.withOpacity(0.2),
              ),

            Expanded(
              child: SingleChildScrollView(
                padding: const EdgeInsets.all(16),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Tool Header
                    _buildToolHeader(context),
                    
                    const SizedBox(height: 24),

                    // Processing State UI
                    if (processingState.status == ProcessingStatus.completed)
                      ResultSection(
                        tool: tool,
                        outputPath: processingState.outputPath,
                        outputBytes: processingState.outputBytes,
                        outputFileName: tool.id.replaceAll('-', '_'),
                        onProcessAnother: () {
                          ref.read(processingStateProvider(tool.id).notifier).reset();
                          ref.read(selectedFilesProvider.notifier).clearFiles();
                        },
                      )
                    else if (processingState.status == ProcessingStatus.error)
                      _buildErrorSection(context, ref, processingState.error!)
                    else ...[
                      // File Picker Section
                      FilePickerSection(tool: tool),
                      
                      const SizedBox(height: 24),

                      // Processing Button
                      if (selectedFiles.isNotEmpty)
                        SizedBox(
                          width: double.infinity,
                          child: ElevatedButton.icon(
                            onPressed: processingState.status == ProcessingStatus.processing ||
                                    processingState.status == ProcessingStatus.uploading
                                ? null
                                : () => _processFiles(context, ref),
                            icon: processingState.status == ProcessingStatus.processing ||
                                    processingState.status == ProcessingStatus.uploading
                                ? const SizedBox(
                                    width: 20,
                                    height: 20,
                                    child: CircularProgressIndicator(
                                      strokeWidth: 2,
                                      valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                                    ),
                                  )
                                : const Icon(Icons.play_arrow),
                            label: Text(
                              processingState.status == ProcessingStatus.processing
                                  ? 'Processing...'
                                  : processingState.status == ProcessingStatus.uploading
                                      ? 'Uploading...'
                                      : tool.shortDescription,
                            ),
                          ),
                        ),

                      const SizedBox(height: 24),

                      // Tool Info Section
                      ToolInfoSection(tool: tool),
                    ],
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildToolHeader(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: tool.category.color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: tool.category.color.withOpacity(0.2),
          width: 1,
        ),
      ),
      child: Row(
        children: [
          Container(
            width: 64,
            height: 64,
            decoration: BoxDecoration(
              color: tool.category.color,
              borderRadius: BorderRadius.circular(16),
            ),
            child: Icon(
              tool.icon,
              size: 32,
              color: Colors.white,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  tool.name,
                  style: Theme.of(context).textTheme.titleLarge?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  tool.description,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    color: AppColors.textSecondary,
                  ),
                ),
                const SizedBox(height: 8),
                Row(
                  children: [
                    _buildBadge(
                      context,
                      tool.processingMode == ProcessingMode.local ? 'Local' : 'Cloud',
                      tool.processingMode == ProcessingMode.local
                          ? Colors.green
                          : Colors.blue,
                    ),
                    const SizedBox(width: 8),
                    _buildBadge(
                      context,
                      tool.category.displayName,
                      tool.category.color,
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildBadge(BuildContext context, String text, Color color) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(4),
        border: Border.all(color: color.withOpacity(0.3)),
      ),
      child: Text(
        text,
        style: TextStyle(
          fontSize: 11,
          fontWeight: FontWeight.w600,
          color: color,
        ),
      ),
    );
  }

  Widget _buildErrorSection(BuildContext context, WidgetRef ref, String error) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: AppColors.error.withOpacity(0.1),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.error.withOpacity(0.3)),
      ),
      child: Column(
        children: [
          const Icon(
            Icons.error_outline,
            color: AppColors.error,
            size: 48,
          ),
          const SizedBox(height: 12),
          Text(
            'Processing Failed',
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
              color: AppColors.error,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            error,
            textAlign: TextAlign.center,
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
              color: AppColors.textSecondary,
            ),
          ),
          const SizedBox(height: 16),
          ElevatedButton.icon(
            onPressed: () {
              ref.read(processingStateProvider(tool.id).notifier).reset();
            },
            icon: const Icon(Icons.refresh),
            label: const Text('Try Again'),
          ),
        ],
      ),
    );
  }

  Future<void> _processFiles(BuildContext context, WidgetRef ref) async {
    final processingNotifier = ref.read(processingStateProvider(tool.id).notifier);
    final selectedFiles = ref.read(selectedFilesProvider);
    
    processingNotifier.startProcessing();

    try {
      // Simulate processing - in real implementation, this would call the actual service
      await Future.delayed(const Duration(seconds: 2));
      
      // For demo purposes, create a simple output
      // In real implementation, this would use the actual processing service
      final outputFileName = tool.id.replaceAll('-', '_');
      
      if (kIsWeb) {
        // On web, we need to provide bytes for download to work
        Uint8List outputBytes;
        
        if (tool.category == ToolCategory.pdfTools) {
          // Generate actual PDF bytes for PDF tools
          final pdf = pw.Document();
          pdf.addPage(
            pw.Page(
              build: (pw.Context context) {
                return pw.Center(
                  child: pw.Column(
                    mainAxisAlignment: pw.MainAxisAlignment.center,
                    children: [
                      pw.Text(
                        tool.name,
                        style: pw.TextStyle(
                          fontSize: 24,
                          fontWeight: pw.FontWeight.bold,
                        ),
                      ),
                      pw.SizedBox(height: 20),
                      pw.Text(
                        'This is a demo PDF generated by LovePDFs',
                        style: const pw.TextStyle(fontSize: 14),
                      ),
                      pw.SizedBox(height: 10),
                      pw.Text(
                        'Tool: ${tool.description}',
                        style: const pw.TextStyle(fontSize: 12),
                      ),
                      pw.SizedBox(height: 30),
                      pw.Text(
                        'Generated on: ${DateTime.now()}',
                        style: const pw.TextStyle(fontSize: 10),
                      ),
                    ],
                  ),
                );
              },
            ),
          );
          outputBytes = Uint8List.fromList(await pdf.save());
        } else {
          // For non-PDF tools, create appropriate content
          final demoContent = '''${tool.name}

This is a demo output for ${tool.name}.
${tool.description}

Generated by LovePDFs
Date: ${DateTime.now()}''';          
          outputBytes = Uint8List.fromList(demoContent.codeUnits);
        }
        
        processingNotifier.complete(
          '/fake/output/path', // Path is not used on web, but kept for compatibility
          outputBytes: outputBytes,
        );
      } else {
        // Mobile/desktop can use file paths
        processingNotifier.complete('/fake/output/$outputFileName');
      }
      
      // Increment successful use for rating prompt
      ref.read(settingsProvider.notifier).incrementSuccessfulUse();
      
    } catch (e) {
      processingNotifier.setError(e.toString());
    }
  }
}
