import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/app_tool.dart';
import '../providers/app_providers.dart';
import '../theme/app_theme.dart';

class ProcessingSection extends ConsumerWidget {
  final AppTool tool;

  const ProcessingSection({
    super.key,
    required this.tool,
  });

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final processingState = ref.watch(processingStateProvider(tool.id));

    return Container(
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: AppColors.primary.withOpacity(0.05),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: AppColors.primary.withOpacity(0.2),
        ),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          // Progress indicator
          SizedBox(
            width: 80,
            height: 80,
            child: CircularProgressIndicator(
              value: processingState.status == ProcessingStatus.processing
                  ? null
                  : processingState.progress,
              strokeWidth: 6,
              valueColor: const AlwaysStoppedAnimation<Color>(AppColors.primary),
              backgroundColor: AppColors.primary.withOpacity(0.2),
            ),
          ),
          const SizedBox(height: 24),

          // Status text
          Text(
            processingState.message ?? 'Processing...',
            style: Theme.of(context).textTheme.titleMedium?.copyWith(
              fontWeight: FontWeight.bold,
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 8),

          // Progress percentage
          if (processingState.progress > 0 && processingState.progress < 1)
            Text(
              '${(processingState.progress * 100).toStringAsFixed(0)}%',
              style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                color: AppColors.textSecondary,
              ),
            ),

          const SizedBox(height: 16),

          // Estimated time (placeholder)
          Text(
            'Please don\'t close the app',
            style: Theme.of(context).textTheme.bodySmall?.copyWith(
              color: AppColors.textSecondary.withOpacity(0.7),
            ),
          ),
        ],
      ),
    );
  }
}
