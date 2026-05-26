import 'package:flutter/material.dart';
import 'package:confetti/confetti.dart';
import '../models/question.dart';
import '../models/quiz_history.dart';
import '../services/pdf_service.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/glass_container.dart';

class QuizResultScreen extends StatefulWidget {
  final QuizAttempt attempt;
  final List<Question> questions;

  const QuizResultScreen({
    super.key,
    required this.attempt,
    required this.questions,
  });

  @override
  State<QuizResultScreen> createState() => _QuizResultScreenState();
}

class _QuizResultScreenState extends State<QuizResultScreen> {
  late ConfettiController _confettiController;
  bool _showReview = false;

  @override
  void initState() {
    super.initState();
    _confettiController = ConfettiController(duration: const Duration(seconds: 4));
    
    // Play confetti if score is >= 75%
    if (widget.attempt.percentage >= 75.0) {
      _confettiController.play();
    }
  }

  @override
  void dispose() {
    _confettiController.dispose();
    super.dispose();
  }

  String _getHeadline() {
    final pct = widget.attempt.percentage;
    if (pct == 100) return 'PERFECT SCORE!';
    if (pct >= 85) return 'OUTSTANDING WORK!';
    if (pct >= 70) return 'WELL DONE!';
    if (pct >= 50) return 'GOOD EFFORT!';
    return 'KEEP PRACTICING!';
  }

  Color _getHeadlineColor() {
    final pct = widget.attempt.percentage;
    if (pct >= 70) return AppTheme.correctGreen;
    if (pct >= 50) return AppTheme.warningOrange;
    return AppTheme.incorrectRed;
  }

  @override
  Widget build(BuildContext context) {
    final speed = widget.attempt.timeSpentSeconds / widget.attempt.totalQuestions;
    final userName = StorageService.getUsername();
    final isQualifiedForCertificate = widget.attempt.percentage >= 70.0;

    return Container(
      decoration: const BoxDecoration(gradient: AppTheme.mainGradient),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Stack(
          alignment: Alignment.topCenter,
          children: [
            SafeArea(
              child: SingleChildScrollView(
                padding: const EdgeInsets.all(20.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const SizedBox(height: 20),
                    // Headline
                    Text(
                      _getHeadline(),
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        fontSize: 26,
                        fontWeight: FontWeight.bold,
                        color: _getHeadlineColor(),
                        letterSpacing: 1.5,
                      ),
                    ),
                    const SizedBox(height: 8),
                    const Text(
                      'You have completed the assessment successfully.',
                      textAlign: TextAlign.center,
                      style: TextStyle(color: AppTheme.textSecondary, fontSize: 13),
                    ),
                    const SizedBox(height: 30),

                    // Ring score graphic
                    Center(
                      child: Container(
                        width: 170,
                        height: 170,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: AppTheme.primaryLight,
                          boxShadow: [
                            BoxShadow(
                              color: _getHeadlineColor().withOpacity(0.15),
                              blurRadius: 20,
                              spreadRadius: 2,
                            ),
                          ],
                          border: Border.all(
                            color: _getHeadlineColor().withOpacity(0.4),
                            width: 8,
                          ),
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Text(
                              '${widget.attempt.score}',
                              style: const TextStyle(
                                fontSize: 48,
                                fontWeight: FontWeight.bold,
                                color: Colors.white,
                              ),
                            ),
                            Text(
                              'out of ${widget.attempt.totalQuestions}',
                              style: const TextStyle(
                                fontSize: 13,
                                color: AppTheme.textSecondary,
                              ),
                            ),
                            const SizedBox(height: 4),
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                              decoration: BoxDecoration(
                                color: _getHeadlineColor().withOpacity(0.2),
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Text(
                                '${widget.attempt.percentage.toStringAsFixed(0)}%',
                                style: TextStyle(
                                  fontSize: 12,
                                  fontWeight: FontWeight.bold,
                                  color: _getHeadlineColor(),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 40),

                    // Stats Grid Row
                    Row(
                      children: [
                        Expanded(
                          child: _buildDetailCard(
                            title: 'Time Taken',
                            value: '${widget.attempt.timeSpentSeconds} sec',
                            icon: Icons.timer,
                            iconColor: AppTheme.accentCyan,
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: _buildDetailCard(
                            title: 'Avg. Speed',
                            value: '${speed.toStringAsFixed(1)}s/q',
                            icon: Icons.speed,
                            iconColor: AppTheme.warningOrange,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 24),

                    // Gold Certificate Unlock Banner (If score >= 70%)
                    if (isQualifiedForCertificate) ...[
                      _buildCertificateBanner(userName),
                      const SizedBox(height: 24),
                    ],

                    // Action buttons
                    Row(
                      children: [
                        Expanded(
                          child: OutlinedButton(
                            style: OutlinedButton.styleFrom(
                              side: const BorderSide(color: Colors.white24, width: 1.5),
                              padding: const EdgeInsets.symmetric(vertical: 16),
                              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                            ),
                            onPressed: () {
                              Navigator.pop(context); // Go back home
                            },
                            child: const Text(
                              'BACK TO HOME',
                              style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, letterSpacing: 1),
                            ),
                          ),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Container(
                            decoration: BoxDecoration(
                              gradient: AppTheme.accentGradient,
                              borderRadius: BorderRadius.circular(16),
                            ),
                            child: ElevatedButton(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: Colors.transparent,
                                shadowColor: Colors.transparent,
                                padding: const EdgeInsets.symmetric(vertical: 16),
                                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                              ),
                              onPressed: () {
                                setState(() {
                                  _showReview = !_showReview;
                                });
                              },
                              child: Text(
                                _showReview ? 'HIDE REVIEW' : 'REVIEW ANSWERS',
                                style: const TextStyle(fontWeight: FontWeight.bold, color: Colors.white, letterSpacing: 1),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 24),

                    // Review Answers Panel
                    if (_showReview) _buildReviewPanel(),
                  ],
                ),
              ),
            ),

            // Confetti Cannon
            ConfettiWidget(
              confettiController: _confettiController,
              blastDirectionality: BlastDirectionality.explosive,
              shouldLoop: false,
              colors: const [
                AppTheme.correctGreen,
                AppTheme.accentCyan,
                AppTheme.accentPurple,
                Colors.yellow,
                Colors.orange,
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDetailCard({
    required String title,
    required String value,
    required IconData icon,
    required Color iconColor,
  }) {
    return GlassContainer(
      padding: const EdgeInsets.all(16),
      child: Row(
        children: [
          CircleAvatar(
            backgroundColor: iconColor.withOpacity(0.1),
            child: Icon(icon, color: iconColor),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(color: AppTheme.textSecondary, fontSize: 11),
                ),
                const SizedBox(height: 4),
                Text(
                  value,
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCertificateBanner(String userName) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: const Color(0xFFD4AF37).withOpacity(0.5), width: 1.5),
        gradient: LinearGradient(
          colors: [
            const Color(0xFFD4AF37).withOpacity(0.15),
            Colors.transparent,
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.all(18.0),
        child: Row(
          children: [
            const Icon(Icons.workspace_premium, color: Color(0xFFD4AF37), size: 42),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'CERTIFICATE UNLOCKED!',
                    style: TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFFD4AF37),
                    ),
                  ),
                  const SizedBox(height: 4),
                  const Text(
                    'Download or share your Gold Certificate of Completion.',
                    style: TextStyle(fontSize: 11, color: AppTheme.textSecondary),
                  ),
                  const SizedBox(height: 8),
                  TextButton.icon(
                    style: TextButton.styleFrom(
                      padding: EdgeInsets.zero,
                      minimumSize: Size.zero,
                      tapTargetSize: MaterialTapTargetSize.shrinkWrap,
                    ),
                    icon: const Icon(Icons.file_download, color: AppTheme.accentCyan, size: 16),
                    label: const Text(
                      'Generate PDF Now',
                      style: TextStyle(color: AppTheme.accentCyan, fontWeight: FontWeight.bold, fontSize: 13),
                    ),
                    onPressed: () => PdfService.generateAndPrintCertificate(widget.attempt, userName),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildReviewPanel() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Text(
          'QUESTION SUMMARY',
          style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1),
        ),
        const SizedBox(height: 12),
        ListView.builder(
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          itemCount: widget.questions.length,
          itemBuilder: (context, index) {
            final q = widget.questions[index];
            final correctOption = q.options[q.correctOptionIndex];
            final userOption = q.selectedOptionIndex != null 
                ? (q.selectedOptionIndex == -1 ? 'Skipped' : q.options[q.selectedOptionIndex!])
                : 'Unanswered';
            final isCorrect = q.isCorrect;

            return Container(
              margin: const EdgeInsets.only(bottom: 14),
              child: GlassContainer(
                padding: const EdgeInsets.all(16),
                border: Border.all(
                  color: isCorrect ? AppTheme.correctGreen.withOpacity(0.2) : AppTheme.incorrectRed.withOpacity(0.2),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        CircleAvatar(
                          radius: 12,
                          backgroundColor: isCorrect ? AppTheme.correctGreen.withOpacity(0.2) : AppTheme.incorrectRed.withOpacity(0.2),
                          child: Text(
                            '${index + 1}',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.bold,
                              color: isCorrect ? AppTheme.correctGreen : AppTheme.incorrectRed,
                            ),
                          ),
                        ),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            q.questionText,
                            style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14, color: Colors.white),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 12),
                    Row(
                      children: [
                        const Text('Your Answer: ', style: TextStyle(fontSize: 12, color: AppTheme.textSecondary)),
                        Expanded(
                          child: Text(
                            userOption,
                            style: TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                              color: isCorrect ? AppTheme.correctGreen : AppTheme.incorrectRed,
                            ),
                          ),
                        ),
                      ],
                    ),
                    if (!isCorrect) ...[
                      const SizedBox(height: 4),
                      Row(
                        children: [
                          const Text('Correct Answer: ', style: TextStyle(fontSize: 12, color: AppTheme.textSecondary)),
                          Expanded(
                            child: Text(
                              correctOption,
                              style: const TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                                color: AppTheme.correctGreen,
                              ),
                            ),
                          ),
                        ],
                      ),
                    ],
                    if (q.explanation.isNotEmpty) ...[
                      const SizedBox(height: 8),
                      const Divider(color: Colors.white10),
                      Text(
                        q.explanation,
                        style: const TextStyle(fontSize: 11, color: AppTheme.textMuted, fontStyle: FontStyle.italic),
                      ),
                    ],
                  ],
                ),
              ),
            );
          },
        ),
      ],
    );
  }
}
