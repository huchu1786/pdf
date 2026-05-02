import 'package:flutter/material.dart';
import '../models/app_tool.dart';
import '../theme/app_theme.dart';

class ToolInfoSection extends StatelessWidget {
  final AppTool tool;

  const ToolInfoSection({
    super.key,
    required this.tool,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // How to use
        if (tool.instructions.isNotEmpty) ...[
          _buildSectionTitle(context, 'How to use'),
          const SizedBox(height: 12),
          _buildInstructions(context),
          const SizedBox(height: 24),
        ],

        // Features
        if (tool.features.isNotEmpty) ...[
          _buildSectionTitle(context, 'Features'),
          const SizedBox(height: 12),
          _buildFeatures(context),
          const SizedBox(height: 24),
        ],

        // Supported Formats
        _buildSectionTitle(context, 'Supported Formats'),
        const SizedBox(height: 12),
        _buildFormats(context),
      ],
    );
  }

  Widget _buildSectionTitle(BuildContext context, String title) {
    return Text(
      title,
      style: Theme.of(context).textTheme.titleMedium?.copyWith(
        fontWeight: FontWeight.bold,
      ),
    );
  }

  Widget _buildInstructions(BuildContext context) {
    return Column(
      children: tool.instructions.asMap().entries.map((entry) {
        final index = entry.key;
        final instruction = entry.value;
        return Padding(
          padding: const EdgeInsets.only(bottom: 12),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                width: 24,
                height: 24,
                decoration: BoxDecoration(
                  color: AppColors.primary.withOpacity(0.1),
                  shape: BoxShape.circle,
                ),
                child: Center(
                  child: Text(
                    '${index + 1}',
                    style: TextStyle(
                      fontSize: 12,
                      fontWeight: FontWeight.bold,
                      color: AppColors.primary,
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Text(
                  instruction,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    color: AppColors.textSecondary,
                    height: 1.5,
                  ),
                ),
              ),
            ],
          ),
        );
      }).toList(),
    );
  }

  Widget _buildFeatures(BuildContext context) {
    return Column(
      children: tool.features.map((feature) {
        return Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Icon(
                Icons.check_circle,
                color: AppColors.success,
                size: 20,
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Text(
                  feature,
                  style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                    color: AppColors.textSecondary,
                    height: 1.5,
                  ),
                ),
              ),
            ],
          ),
        );
      }).toList(),
    );
  }

  Widget _buildFormats(BuildContext context) {
    return Row(
      children: [
        Expanded(
          child: _buildFormatCard(
            context,
            'Input',
            tool.supportedInputFormats,
            Colors.blue,
          ),
        ),
        const SizedBox(width: 12),
        const Icon(Icons.arrow_forward, color: AppColors.textSecondary),
        const SizedBox(width: 12),
        Expanded(
          child: _buildFormatCard(
            context,
            'Output',
            tool.supportedOutputFormats,
            Colors.green,
          ),
        ),
      ],
    );
  }

  Widget _buildFormatCard(
    BuildContext context,
    String title,
    List<String> formats,
    Color color,
  ) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: color.withOpacity(0.05),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: color.withOpacity(0.2),
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: TextStyle(
              fontSize: 12,
              fontWeight: FontWeight.w600,
              color: color,
            ),
          ),
          const SizedBox(height: 8),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: formats.map((format) {
              return Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: color.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(4),
                ),
                child: Text(
                  format.toUpperCase(),
                  style: TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w600,
                    color: color,
                  ),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
