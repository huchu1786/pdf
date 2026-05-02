import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/app_tool.dart';
import '../providers/app_providers.dart';
import '../theme/app_theme.dart';
import '../widgets/tool_card.dart';
import '../widgets/category_header.dart';
import 'tool_detail_screen.dart';

class HomeScreen extends ConsumerWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final searchQuery = ref.watch(searchQueryProvider);
    final filteredTools = ref.watch(filteredToolsProvider);
    final pdfTools = filteredTools.where((t) => t.category == ToolCategory.pdfTools).toList();
    final imageTools = filteredTools.where((t) => t.category == ToolCategory.imageTools).toList();
    final calculatorTools = filteredTools.where((t) => t.category == ToolCategory.calculatorTools).toList();
    final otherTools = filteredTools.where((t) => t.category == ToolCategory.otherTools).toList();

    return Scaffold(
      body: CustomScrollView(
        slivers: [
          // App Bar with Search
          SliverAppBar(
            floating: true,
            pinned: true,
            snap: true,
            expandedHeight: 140,
            backgroundColor: AppColors.primary,
            flexibleSpace: FlexibleSpaceBar(
              titlePadding: const EdgeInsets.only(left: 16, bottom: 70),
              title: Text(
                'LovePDFs',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
              background: Container(
                color: AppColors.primary,
                child: const Stack(
                  children: [
                    Positioned(
                      right: -30,
                      top: -30,
                      child: Icon(
                        Icons.picture_as_pdf,
                        size: 150,
                        color: Colors.white12,
                      ),
                    ),
                  ],
                ),
              ),
            ),
            bottom: PreferredSize(
              preferredSize: const Size.fromHeight(60),
              child: Container(
                margin: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(12),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.1),
                      blurRadius: 8,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: TextField(
                  onChanged: (value) {
                    ref.read(searchQueryProvider.notifier).state = value;
                  },
                  decoration: InputDecoration(
                    hintText: 'Search tools...',
                    hintStyle: TextStyle(color: AppColors.textSecondary.withOpacity(0.6)),
                    prefixIcon: const Icon(Icons.search, color: AppColors.textSecondary),
                    suffixIcon: searchQuery.isNotEmpty
                        ? IconButton(
                            icon: const Icon(Icons.clear, color: AppColors.textSecondary),
                            onPressed: () {
                              ref.read(searchQueryProvider.notifier).state = '';
                            },
                          )
                        : null,
                    border: InputBorder.none,
                    contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                  ),
                ),
              ),
            ),
          ),

          // Category Filter Chips
          if (searchQuery.isEmpty)
            SliverToBoxAdapter(
              child: Container(
                height: 60,
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                child: ListView(
                  scrollDirection: Axis.horizontal,
                  children: [
                    _buildFilterChip(context, 'All', Icons.apps, true),
                    _buildFilterChip(context, 'PDF', Icons.picture_as_pdf, false, AppColors.pdfCategory),
                    _buildFilterChip(context, 'Images', Icons.image, false, AppColors.imageCategory),
                    _buildFilterChip(context, 'Calculators', Icons.calculate, false, AppColors.calculatorCategory),
                    _buildFilterChip(context, 'Other', Icons.build, false, AppColors.otherCategory),
                  ],
                ),
              ),
            ),

          // Content
          if (filteredTools.isEmpty)
            SliverFillRemaining(
              hasScrollBody: false,
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(
                      Icons.search_off,
                      size: 80,
                      color: AppColors.textSecondary.withOpacity(0.3),
                    ),
                    const SizedBox(height: 20),
                    Text(
                      'No tools found',
                      style: Theme.of(context).textTheme.titleLarge?.copyWith(
                        color: AppColors.textSecondary,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      'Try a different search term',
                      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: AppColors.textSecondary.withOpacity(0.7),
                      ),
                    ),
                  ],
                ),
              ),
            )
          else ...[
            // PDF Tools Section
            if (pdfTools.isNotEmpty) ...[
              SliverToBoxAdapter(
                child: CategoryHeader(
                  category: ToolCategory.pdfTools,
                  count: pdfTools.length,
                ),
              ),
              SliverPadding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                sliver: SliverGrid(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    childAspectRatio: 1.0,
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                  ),
                  delegate: SliverChildBuilderDelegate(
                    (context, index) {
                      final tool = pdfTools[index];
                      return ToolCard(
                        tool: tool,
                        onTap: () => _navigateToTool(context, tool),
                      );
                    },
                    childCount: pdfTools.length,
                  ),
                ),
              ),
            ],

            // Image Tools Section
            if (imageTools.isNotEmpty) ...[
              SliverToBoxAdapter(
                child: CategoryHeader(
                  category: ToolCategory.imageTools,
                  count: imageTools.length,
                ),
              ),
              SliverPadding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                sliver: SliverGrid(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    childAspectRatio: 1.0,
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                  ),
                  delegate: SliverChildBuilderDelegate(
                    (context, index) {
                      final tool = imageTools[index];
                      return ToolCard(
                        tool: tool,
                        onTap: () => _navigateToTool(context, tool),
                      );
                    },
                    childCount: imageTools.length,
                  ),
                ),
              ),
            ],

            // Calculator Tools Section
            if (calculatorTools.isNotEmpty) ...[
              SliverToBoxAdapter(
                child: CategoryHeader(
                  category: ToolCategory.calculatorTools,
                  count: calculatorTools.length,
                ),
              ),
              SliverPadding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                sliver: SliverGrid(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    childAspectRatio: 1.0,
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                  ),
                  delegate: SliverChildBuilderDelegate(
                    (context, index) {
                      final tool = calculatorTools[index];
                      return ToolCard(
                        tool: tool,
                        onTap: () => _navigateToTool(context, tool),
                      );
                    },
                    childCount: calculatorTools.length,
                  ),
                ),
              ),
            ],

            // Other Tools Section
            if (otherTools.isNotEmpty) ...[
              SliverToBoxAdapter(
                child: CategoryHeader(
                  category: ToolCategory.otherTools,
                  count: otherTools.length,
                ),
              ),
              SliverPadding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                sliver: SliverGrid(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    childAspectRatio: 1.0,
                    crossAxisSpacing: 12,
                    mainAxisSpacing: 12,
                  ),
                  delegate: SliverChildBuilderDelegate(
                    (context, index) {
                      final tool = otherTools[index];
                      return ToolCard(
                        tool: tool,
                        onTap: () => _navigateToTool(context, tool),
                      );
                    },
                    childCount: otherTools.length,
                  ),
                ),
              ),
            ],

            // Bottom spacing
            const SliverToBoxAdapter(
              child: SizedBox(height: 24),
            ),
          ],
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

  Widget _buildFilterChip(BuildContext context, String label, IconData icon, bool isSelected, [Color? color]) {
    final bgColor = color ?? AppColors.primary;
    return Padding(
      padding: const EdgeInsets.only(right: 10),
      child: FilterChip(
        selected: isSelected,
        showCheckmark: false,
        avatar: Icon(icon, size: 18, color: isSelected ? Colors.white : bgColor),
        label: Text(label),
        labelStyle: TextStyle(
          fontWeight: FontWeight.w600,
          color: isSelected ? Colors.white : AppColors.textPrimary,
        ),
        backgroundColor: Colors.white,
        selectedColor: bgColor,
        side: BorderSide(color: bgColor.withOpacity(0.3)),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(25)),
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
        onSelected: (_) {
          // TODO: Implement category filtering
        },
      ),
    );
  }
}
