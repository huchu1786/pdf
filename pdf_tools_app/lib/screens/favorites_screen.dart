import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/app_tool.dart';
import '../providers/app_providers.dart';
import '../theme/app_theme.dart';
import '../widgets/tool_card.dart';
import 'tool_detail_screen.dart';

class FavoritesScreen extends ConsumerWidget {
  const FavoritesScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final favoriteIds = ref.watch(favoriteToolsProvider);
    final favoriteTools = favoriteIds
        .map((id) => getToolById(id))
        .where((tool) => tool != null)
        .cast<AppTool>()
        .toList();

    return Scaffold(
      appBar: AppBar(
        title: const Text('Favorites'),
      ),
      body: favoriteTools.isEmpty
          ? _buildEmptyState(context)
          : GridView.builder(
              padding: const EdgeInsets.all(16),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                childAspectRatio: 1.1,
                crossAxisSpacing: 12,
                mainAxisSpacing: 12,
              ),
              itemCount: favoriteTools.length,
              itemBuilder: (context, index) {
                final tool = favoriteTools[index];
                return ToolCard(
                  tool: tool,
                  onTap: () => _navigateToTool(context, tool),
                );
              },
            ),
    );
  }

  Widget _buildEmptyState(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.favorite_outline,
            size: 80,
            color: AppColors.textSecondary.withOpacity(0.3),
          ),
          const SizedBox(height: 24),
          Text(
            'No Favorites Yet',
            style: Theme.of(context).textTheme.titleLarge?.copyWith(
              color: AppColors.textSecondary,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            'Tap the heart icon on any tool to add it here',
            style: Theme.of(context).textTheme.bodyMedium?.copyWith(
              color: AppColors.textSecondary.withOpacity(0.7),
            ),
          ),
        ],
      ),
    );
  }

  void _navigateToTool(BuildContext context, AppTool tool) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => ToolDetailScreen(tool: tool),
      ),
    );
  }
}
