import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';
import '../models/quiz_history.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/glass_container.dart';

class AnalyticsScreen extends StatefulWidget {
  const AnalyticsScreen({super.key});

  @override
  State<AnalyticsScreen> createState() => _AnalyticsScreenState();
}

class _AnalyticsScreenState extends State<AnalyticsScreen> {
  List<QuizAttempt> _attempts = [];

  @override
  void initState() {
    super.initState();
    _loadHistory();
  }

  void _loadHistory() {
    setState(() {
      _attempts = StorageService.getHistory();
    });
  }

  Map<String, List<double>> _getCategoryScores() {
    final Map<String, List<double>> data = {};
    for (var att in _attempts) {
      data.putIfAbsent(att.category, () => []).add(att.percentage);
    }
    return data;
  }

  @override
  Widget build(BuildContext context) {
    if (_attempts.isEmpty) {
      return Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Icon(Icons.analytics_outlined, size: 72, color: AppTheme.textMuted),
            const SizedBox(height: 20),
            const Text(
              'No Analytics Available',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
            ),
            const SizedBox(height: 8),
            const Text(
              'Complete a quiz assessment to unlock accuracy metrics and category performance analytics.',
              textAlign: TextAlign.center,
              style: TextStyle(color: AppTheme.textSecondary, fontSize: 14),
            ),
          ],
        ),
      );
    }

    final categoryMap = _getCategoryScores();
    final totalAttempts = _attempts.length;
    final avgScore = _attempts.map((a) => a.percentage).reduce((a, b) => a + b) / totalAttempts;
    final totalSeconds = _attempts.map((a) => a.timeSpentSeconds).reduce((a, b) => a + b);

    return Scaffold(
      backgroundColor: Colors.transparent,
      appBar: AppBar(
        title: const Text('Performance Analytics'),
        actions: [
          IconButton(
            icon: const Icon(Icons.delete_sweep, color: AppTheme.incorrectRed),
            onPressed: () async {
              final confirm = await showDialog<bool>(
                context: context,
                builder: (context) => AlertDialog(
                  backgroundColor: AppTheme.primaryLight,
                  title: const Text('Clear All Logs'),
                  content: const Text('Are you sure you want to delete all historical performance data? This cannot be undone.'),
                  actions: [
                    TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Cancel')),
                    TextButton(
                      onPressed: () => Navigator.pop(context, true),
                      child: const Text('Delete', style: TextStyle(color: AppTheme.incorrectRed)),
                    ),
                  ],
                ),
              );

              if (confirm == true) {
                await StorageService.clearHistory();
                _loadHistory();
              }
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Stat Cards Row
            Row(
              children: [
                Expanded(
                  child: GlassContainer(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Overall Accuracy', style: TextStyle(color: AppTheme.textSecondary, fontSize: 11)),
                        const SizedBox(height: 6),
                        Text('${avgScore.toStringAsFixed(1)}%', style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: AppTheme.correctGreen)),
                      ],
                    ),
                  ),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: GlassContainer(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Total Duration', style: TextStyle(color: AppTheme.textSecondary, fontSize: 11)),
                        const SizedBox(height: 6),
                        Text('${totalSeconds ~/ 60}m ${totalSeconds % 60}s', style: const TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: AppTheme.accentCyan)),
                      ],
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 24),

            // Category Strength Bar Chart
            const Text(
              'CATEGORY PERFORMANCE',
              style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1.5),
            ),
            const SizedBox(height: 12),
            GlassContainer(
              padding: const EdgeInsets.all(18),
              child: SizedBox(
                height: 180,
                child: BarChart(
                  BarChartData(
                    alignment: BarChartAlignment.spaceAround,
                    maxY: 100,
                    barTouchData: BarTouchData(enabled: true),
                    titlesData: FlTitlesData(
                      show: true,
                      bottomTitles: AxisTitles(
                        sideTitles: SideTitles(
                          showTitles: true,
                          getTitlesWidget: (double value, TitleMeta meta) {
                            final keys = categoryMap.keys.toList();
                            if (value.toInt() < 0 || value.toInt() >= keys.length) {
                              return const SizedBox();
                            }
                            final name = keys[value.toInt()];
                            final truncated = name.length > 5 ? name.substring(0, 5) : name;
                            return Padding(
                              padding: const EdgeInsets.only(top: 8.0),
                              child: Text(
                                truncated,
                                style: const TextStyle(color: AppTheme.textSecondary, fontSize: 10, fontWeight: FontWeight.bold),
                              ),
                            );
                          },
                          reservedSize: 28,
                        ),
                      ),
                      leftTitles: const AxisTitles(
                        sideTitles: SideTitles(showTitles: false),
                      ),
                      topTitles: const AxisTitles(
                        sideTitles: SideTitles(showTitles: false),
                      ),
                      rightTitles: const AxisTitles(
                        sideTitles: SideTitles(showTitles: false),
                      ),
                    ),
                    gridData: const FlGridData(show: false),
                    borderData: FlBorderData(show: false),
                    barGroups: List.generate(categoryMap.length, (index) {
                      final category = categoryMap.keys.toList()[index];
                      final scores = categoryMap[category]!;
                      final average = scores.reduce((a, b) => a + b) / scores.length;

                      return BarChartGroupData(
                        x: index,
                        barRods: [
                          BarChartRodData(
                            toY: average,
                            color: index % 2 == 0 ? AppTheme.accentPurple : AppTheme.accentCyan,
                            width: 18,
                            borderRadius: BorderRadius.circular(4),
                            backDrawRodData: BackgroundBarChartRodData(
                              show: true,
                              toY: 100,
                              color: Colors.white10,
                            ),
                          ),
                        ],
                      );
                    }),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 28),

            // Attempt History List
            const Text(
              'RECENT ASSESSMENT HISTORY',
              style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1.5),
            ),
            const SizedBox(height: 12),
            ListView.builder(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              itemCount: _attempts.length,
              itemBuilder: (context, index) {
                final att = _attempts[index];
                final dateStr = "${att.date.day}/${att.date.month}";
                final isPassed = att.percentage >= 70;

                return Card(
                  margin: const EdgeInsets.only(bottom: 10),
                  child: ListTile(
                    leading: CircleAvatar(
                      backgroundColor: isPassed ? AppTheme.correctGreen.withOpacity(0.15) : AppTheme.incorrectRed.withOpacity(0.15),
                      child: Icon(
                        isPassed ? Icons.verified : Icons.close,
                        color: isPassed ? AppTheme.correctGreen : AppTheme.incorrectRed,
                        size: 20,
                      ),
                    ),
                    title: Text(att.quizTitle, style: const TextStyle(fontWeight: FontWeight.bold)),
                    subtitle: Text('${att.category} • $dateStr', style: const TextStyle(fontSize: 12)),
                    trailing: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        Text(
                          '${att.score}/${att.totalQuestions}',
                          style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                        ),
                        Text(
                          '${att.percentage.toStringAsFixed(0)}%',
                          style: TextStyle(
                            fontSize: 10,
                            color: isPassed ? AppTheme.correctGreen : AppTheme.textSecondary,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
