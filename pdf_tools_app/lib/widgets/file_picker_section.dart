import 'dart:typed_data';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:file_picker/file_picker.dart';
import '../models/app_tool.dart';
import '../providers/app_providers.dart';
import '../theme/app_theme.dart';

class FilePickerSection extends ConsumerWidget {
  final AppTool tool;

  const FilePickerSection({
    super.key,
    required this.tool,
  });

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final selectedFiles = ref.watch(selectedFilesProvider);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Select Files',
          style: Theme.of(context).textTheme.titleMedium?.copyWith(
            fontWeight: FontWeight.bold,
          ),
        ),
        const SizedBox(height: 12),

        // File List
        if (selectedFiles.isNotEmpty) ...[
          ListView.builder(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: selectedFiles.length,
            itemBuilder: (context, index) {
              final file = selectedFiles[index];
              return _buildFileItem(context, ref, file, index);
            },
          ),
          const SizedBox(height: 12),
        ],

        // Add More Files Button (if supports multiple and has files)
        if (selectedFiles.isNotEmpty && tool.supportsMultipleFiles) ...[
          if (selectedFiles.length < tool.maxFilesCount)
            OutlinedButton.icon(
              onPressed: () => _pickFiles(context, ref),
              icon: const Icon(Icons.add),
              label: const Text('Add More Files'),
            )
          else
            Text(
              'Maximum ${tool.maxFilesCount} files selected',
              style: TextStyle(
                color: AppColors.warning,
                fontSize: 12,
              ),
            ),
        ]
        // Initial Select Button
        else if (selectedFiles.isEmpty) ...[
          _buildEmptyState(context, ref),
        ],

        // File requirements info
        const SizedBox(height: 12),
        _buildRequirementsInfo(),
      ],
    );
  }

  Widget _buildFileItem(BuildContext context, WidgetRef ref, SelectedFile file, int index) {
    final isFirst = index == 0;
    final canReorder = tool.supportsMultipleFiles && ref.read(selectedFilesProvider).length > 1;

    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: isFirst ? AppColors.primary.withOpacity(0.3) : AppColors.divider,
          width: isFirst ? 2 : 1,
        ),
      ),
      child: Row(
        children: [
          // File icon
          Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              color: _getFileColor(file.extension).withOpacity(0.1),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Icon(
              _getFileIcon(file.extension),
              color: _getFileColor(file.extension),
              size: 20,
            ),
          ),
          const SizedBox(width: 12),
          // File info
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  file.name,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    fontWeight: FontWeight.w600,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                Text(
                  _formatFileSize(file.size),
                  style: Theme.of(context).textTheme.bodySmall?.copyWith(
                    color: AppColors.textSecondary,
                  ),
                ),
              ],
            ),
          ),
          // Web indicator
          if (file.isWeb)
            Tooltip(
              message: 'Web file (bytes)',
              child: Icon(
                Icons.cloud_done,
                size: 16,
                color: AppColors.primary.withOpacity(0.5),
              ),
            ),
          const SizedBox(width: 8),
          // Reorder buttons
          if (canReorder) ...[
            if (index > 0)
              IconButton(
                icon: const Icon(Icons.arrow_upward, size: 18),
                onPressed: () {
                  ref.read(selectedFilesProvider.notifier).reorderFiles(index, index - 1);
                },
                padding: EdgeInsets.zero,
                constraints: const BoxConstraints(),
              ),
            if (index < ref.read(selectedFilesProvider).length - 1)
              IconButton(
                icon: const Icon(Icons.arrow_downward, size: 18),
                onPressed: () {
                  ref.read(selectedFilesProvider.notifier).reorderFiles(index, index + 1);
                },
                padding: EdgeInsets.zero,
                constraints: const BoxConstraints(),
              ),
          ],
          // Remove button
          IconButton(
            icon: const Icon(Icons.close, size: 18),
            onPressed: () {
              ref.read(selectedFilesProvider.notifier).removeFile(file.id);
            },
            color: AppColors.error,
            padding: EdgeInsets.zero,
            constraints: const BoxConstraints(),
          ),
        ],
      ),
    );
  }

  Widget _buildEmptyState(BuildContext context, WidgetRef ref) {
    return InkWell(
      onTap: () => _pickFiles(context, ref),
      borderRadius: BorderRadius.circular(12),
      child: Container(
        width: double.infinity,
        padding: const EdgeInsets.symmetric(vertical: 40),
        decoration: BoxDecoration(
          color: AppColors.primary.withOpacity(0.05),
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: AppColors.primary.withOpacity(0.2),
            width: 2,
            style: BorderStyle.solid,
          ),
        ),
        child: Column(
          children: [
            Icon(
              tool.category == ToolCategory.imageTools
                  ? Icons.add_photo_alternate
                  : Icons.upload_file,
              size: 48,
              color: AppColors.primary.withOpacity(0.6),
            ),
            const SizedBox(height: 16),
            Text(
              tool.supportsMultipleFiles
                  ? 'Tap to select files'
                  : 'Tap to select a file',
              style: Theme.of(context).textTheme.titleMedium?.copyWith(
                color: AppColors.textSecondary,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              tool.supportedInputFormats.map((e) => e.toUpperCase()).join(', '),
              style: Theme.of(context).textTheme.bodySmall?.copyWith(
                color: AppColors.textSecondary.withOpacity(0.7),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildRequirementsInfo() {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: AppColors.backgroundLight,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        children: [
          Icon(
            Icons.info_outline,
            size: 16,
            color: AppColors.textSecondary,
          ),
          const SizedBox(width: 8),
          Expanded(
            child: Text(
              'Max file size: ${tool.maxFileSizeMB}MB${tool.supportsMultipleFiles ? ' • Max ${tool.maxFilesCount} files' : ''}',
              style: TextStyle(
                fontSize: 12,
                color: AppColors.textSecondary,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Future<void> _pickFiles(BuildContext context, WidgetRef ref) async {
    try {
      ref.read(processingStateProvider(tool.id).notifier).startPicking();

      FileType fileType;
      List<String>? allowedExtensions;

      if (tool.category == ToolCategory.imageTools) {
        fileType = FileType.image;
      } else if (tool.category == ToolCategory.pdfTools) {
        if (tool.supportedInputFormats.contains('docx') ||
            tool.supportedInputFormats.contains('xlsx')) {
          fileType = FileType.custom;
          allowedExtensions = tool.supportedInputFormats;
        } else {
          fileType = FileType.custom;
          allowedExtensions = ['pdf'];
        }
      } else {
        fileType = FileType.any;
      }

      final result = await FilePicker.platform.pickFiles(
        type: fileType,
        allowedExtensions: allowedExtensions,
        allowMultiple: tool.supportsMultipleFiles,
        withData: kIsWeb, // Always load bytes on web
        withReadStream: !kIsWeb, // Use streams for large files on mobile
      );

      ref.read(processingStateProvider(tool.id).notifier).reset();

      if (result != null && result.files.isNotEmpty) {
        for (final file in result.files) {
          final extension = file.extension?.toLowerCase() ?? '';
          
          // Generate unique ID for this file
          final id = '${file.name}_${DateTime.now().millisecondsSinceEpoch}_${result.files.indexOf(file)}';
          
          if (kIsWeb) {
            // On web, use bytes
            if (file.bytes != null) {
              final selectedFile = SelectedFile(
                id: id,
                bytes: file.bytes,
                name: file.name,
                size: file.size,
                extension: extension,
              );
              ref.read(selectedFilesProvider.notifier).addFile(selectedFile);
            }
          } else {
            // On mobile/desktop, use path
            if (file.path != null) {
              final selectedFile = SelectedFile(
                id: id,
                path: file.path!,
                name: file.name,
                size: file.size,
                extension: extension,
              );
              ref.read(selectedFilesProvider.notifier).addFile(selectedFile);
            }
          }
        }
      }
    } catch (e) {
      ref.read(processingStateProvider(tool.id).notifier).setError('Failed to pick files: $e');
    }
  }

  Color _getFileColor(String extension) {
    switch (extension.toLowerCase()) {
      case 'pdf':
        return Colors.red;
      case 'jpg':
      case 'jpeg':
        return Colors.orange;
      case 'png':
        return Colors.blue;
      case 'docx':
      case 'doc':
        return Colors.indigo;
      case 'xlsx':
      case 'xls':
        return Colors.green;
      default:
        return AppColors.primary;
    }
  }

  IconData _getFileIcon(String extension) {
    switch (extension.toLowerCase()) {
      case 'pdf':
        return Icons.picture_as_pdf;
      case 'jpg':
      case 'jpeg':
      case 'png':
      case 'webp':
      case 'bmp':
      case 'gif':
        return Icons.image;
      case 'docx':
      case 'doc':
        return Icons.description;
      case 'xlsx':
      case 'xls':
        return Icons.table_chart;
      default:
        return Icons.insert_drive_file;
    }
  }

  String _formatFileSize(int bytes) {
    if (bytes < 1024) return '$bytes B';
    if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(1)} KB';
    return '${(bytes / (1024 * 1024)).toStringAsFixed(1)} MB';
  }
}
