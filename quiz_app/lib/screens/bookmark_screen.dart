import 'package:flutter/material.dart';
import '../models/question.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/glass_container.dart';

class BookmarkScreen extends StatefulWidget {
  const BookmarkScreen({super.key});

  @override
  State<BookmarkScreen> createState() => _BookmarkScreenState();
}

class _BookmarkScreenState extends State<BookmarkScreen> {
  List<Question> _bookmarks = [];

  @override
  void initState() {
    super.initState();
    _loadBookmarks();
  }

  void _loadBookmarks() {
    setState(() {
      _bookmarks = StorageService.getBookmarkedQuestions();
    });
  }

  void _removeBookmark(Question question) async {
    await StorageService.toggleBookmark(question);
    _loadBookmarks();
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Removed question from bookmarks.')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_bookmarks.isEmpty) {
      return Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Icon(Icons.bookmark_outline_rounded, size: 72, color: AppTheme.textMuted),
            const SizedBox(height: 20),
            const Text(
              'No Saved Questions',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
            ),
            const SizedBox(height: 8),
            const Text(
              'Tap the bookmark icon in the top right corner of any active quiz question to review or study them here later.',
              textAlign: TextAlign.center,
              style: TextStyle(color: AppTheme.textSecondary, fontSize: 14),
            ),
          ],
        ),
      );
    }

    return Scaffold(
      backgroundColor: Colors.transparent,
      appBar: AppBar(
        title: const Text('Saved Questions'),
      ),
      body: ListView.builder(
        padding: const EdgeInsets.all(20.0),
        itemCount: _bookmarks.length,
        itemBuilder: (context, index) {
          final q = _bookmarks[index];

          return Container(
            margin: const EdgeInsets.only(bottom: 14),
            child: GlassContainer(
              padding: const EdgeInsets.all(12),
              child: ExpansionTile(
                iconColor: AppTheme.accentCyan,
                collapsedIconColor: Colors.white70,
                title: Text(
                  q.questionText,
                  style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 15, color: Colors.white),
                ),
                subtitle: Text(
                  'Options: ${q.options.length}',
                  style: const TextStyle(color: AppTheme.textSecondary, fontSize: 12),
                ),
                leading: CircleAvatar(
                  backgroundColor: AppTheme.accentPurple.withOpacity(0.15),
                  child: Text('${index + 1}', style: const TextStyle(color: AppTheme.accentPurple, fontWeight: FontWeight.bold)),
                ),
                trailing: IconButton(
                  icon: const Icon(Icons.bookmark_remove, color: AppTheme.incorrectRed),
                  onPressed: () => _removeBookmark(q),
                ),
                children: [
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 14.0, vertical: 10.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        const Divider(color: Colors.white12),
                        const SizedBox(height: 8),
                        const Text(
                          'OPTIONS:',
                          style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1),
                        ),
                        const SizedBox(height: 8),
                        ...List.generate(q.options.length, (optIdx) {
                          final isCorrect = optIdx == q.correctOptionIndex;
                          final char = String.fromCharCode(65 + optIdx);

                          return Container(
                            margin: const EdgeInsets.only(bottom: 6),
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                            decoration: BoxDecoration(
                              color: isCorrect ? AppTheme.correctGreen.withOpacity(0.15) : Colors.white.withOpacity(0.02),
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(
                                color: isCorrect ? AppTheme.correctGreen.withOpacity(0.3) : Colors.transparent,
                              ),
                            ),
                            child: Row(
                              children: [
                                Text('$char. ', style: TextStyle(fontWeight: FontWeight.bold, color: isCorrect ? AppTheme.correctGreen : Colors.white70)),
                                Expanded(child: Text(q.options[optIdx], style: TextStyle(color: isCorrect ? Colors.white : Colors.white70))),
                                if (isCorrect) const Icon(Icons.check, color: AppTheme.correctGreen, size: 16),
                              ],
                            ),
                          );
                        }),
                        if (q.explanation.isNotEmpty) ...[
                          const SizedBox(height: 14),
                          const Text(
                            'EXPLANATION:',
                            style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1),
                          ),
                          const SizedBox(height: 6),
                          Container(
                            padding: const EdgeInsets.all(12),
                            decoration: BoxDecoration(
                              color: AppTheme.infoBlue.withOpacity(0.08),
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(color: AppTheme.infoBlue.withOpacity(0.15)),
                            ),
                            child: Text(
                              q.explanation,
                              style: const TextStyle(fontSize: 12, color: AppTheme.textSecondary, height: 1.4),
                            ),
                          ),
                        ],
                      ],
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
