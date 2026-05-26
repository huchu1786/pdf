import 'dart:async';
import 'package:flutter/material.dart';
import '../models/question.dart';
import '../models/quiz.dart';
import '../models/quiz_history.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/glass_container.dart';
import '../widgets/option_button.dart';
import '../widgets/timer_indicator.dart';
import 'quiz_result_screen.dart';

class QuizPlayScreen extends StatefulWidget {
  final Quiz quiz;

  const QuizPlayScreen({super.key, required this.quiz});

  @override
  State<QuizPlayScreen> createState() => _QuizPlayScreenState();
}

class _QuizPlayScreenState extends State<QuizPlayScreen> {
  int _currentQuestionIndex = 0;
  int _score = 0;
  int? _selectedOptionIndex;
  bool _isAnswered = false;
  
  // Timer State
  late int _remainingSeconds;
  Timer? _timer;
  bool _isTimerFrozen = false;
  int _totalTimeSpent = 0;

  // Lifelines State
  bool _isFiftyFiftyUsed = false;
  bool _isSkipUsed = false;
  bool _isFreezeUsed = false;
  List<int> _disabledOptionIndices = [];

  @override
  void initState() {
    super.initState();
    _remainingSeconds = widget.quiz.durationSeconds;
    _startTimer();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (_isTimerFrozen) return;

      setState(() {
        if (_remainingSeconds > 0) {
          _remainingSeconds--;
          _totalTimeSpent++;
        } else {
          _timer?.cancel();
          _onTimeOut();
        }
      });
    });
  }

  void _onTimeOut() {
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Time\'s up! Calculating score...')),
    );
    _navigateToResults();
  }

  void _navigateToResults() {
    _timer?.cancel();

    // Log the quiz attempt
    final attempt = QuizAttempt(
      id: DateTime.now().millisecondsSinceEpoch.toString(),
      quizId: widget.quiz.id,
      quizTitle: widget.quiz.title,
      category: widget.quiz.category,
      score: _score,
      totalQuestions: widget.quiz.questions.length,
      timeSpentSeconds: _totalTimeSpent,
      date: DateTime.now(),
    );

    // Save attempt to history
    StorageService.saveAttempt(attempt);

    // Navigate to results screen (push replacement so user doesn't hit back to get into the active game again)
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => QuizResultScreen(
          attempt: attempt,
          questions: widget.quiz.questions,
        ),
      ),
    );
  }

  void _handleOptionTap(int index) {
    if (_isAnswered) return;

    setState(() {
      _selectedOptionIndex = index;
      _isAnswered = true;
      
      final currentQuestion = widget.quiz.questions[_currentQuestionIndex];
      currentQuestion.selectedOptionIndex = index;

      if (index == currentQuestion.correctOptionIndex) {
        _score++;
      }
    });
  }

  // --- Lifelines ---
  void _useFiftyFifty() {
    if (_isFiftyFiftyUsed || _isAnswered) return;

    final currentQuestion = widget.quiz.questions[_currentQuestionIndex];
    final correctIndex = currentQuestion.correctOptionIndex;
    final List<int> wrongIndices = [];

    for (int i = 0; i < currentQuestion.options.length; i++) {
      if (i != correctIndex) {
        wrongIndices.add(i);
      }
    }

    // Shuffle wrong indices and disable two of them
    wrongIndices.shuffle();
    setState(() {
      _disabledOptionIndices = wrongIndices.take(2).toList();
      _isFiftyFiftyUsed = true;
    });
  }

  void _useSkipQuestion() {
    if (_isSkipUsed || _isAnswered) return;

    setState(() {
      _isSkipUsed = true;
      _isAnswered = true;
      _selectedOptionIndex = -1; // Flag as skipped
      
      final currentQuestion = widget.quiz.questions[_currentQuestionIndex];
      currentQuestion.selectedOptionIndex = null; // No selected answer
    });

    _nextQuestion();
  }

  void _useTimerFreeze() {
    if (_isFreezeUsed || _isAnswered) return;

    setState(() {
      _isTimerFrozen = true;
      _isFreezeUsed = true;
    });

    // Re-enable timer after 15 seconds automatically
    Future.delayed(const Duration(seconds: 15), () {
      if (mounted && _isTimerFrozen) {
        setState(() {
          _isTimerFrozen = false;
        });
      }
    });
  }

  void _nextQuestion() {
    // Check if we have more questions
    if (_currentQuestionIndex < widget.quiz.questions.length - 1) {
      setState(() {
        _currentQuestionIndex++;
        _selectedOptionIndex = null;
        _isAnswered = false;
        _disabledOptionIndices = [];
      });
    } else {
      _navigateToResults();
    }
  }

  @override
  Widget build(BuildContext context) {
    final questions = widget.quiz.questions;
    final currentQuestion = questions[_currentQuestionIndex];
    final progress = (_currentQuestionIndex + 1) / questions.length;

    // Check if current question is bookmarked
    final isBookmarked = StorageService.isBookmarked(currentQuestion.id);

    return Container(
      decoration: const BoxDecoration(gradient: AppTheme.mainGradient),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          title: Text(widget.quiz.title),
          actions: [
            IconButton(
              icon: Icon(
                isBookmarked ? Icons.bookmark : Icons.bookmark_border,
                color: isBookmarked ? AppTheme.accentCyan : Colors.white,
              ),
              onPressed: () async {
                await StorageService.toggleBookmark(currentQuestion);
                setState(() {});
              },
            ),
          ],
        ),
        body: SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Timer & Lifelines Row
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    // Timer
                    Row(
                      children: [
                        TimerIndicator(
                          remainingSeconds: _remainingSeconds,
                          totalSeconds: widget.quiz.durationSeconds,
                        ),
                        if (_isTimerFrozen)
                          const Padding(
                            padding: EdgeInsets.only(left: 8.0),
                            child: Icon(Icons.ac_unit, color: AppTheme.accentCyan, size: 20),
                          ),
                      ],
                    ),
                    
                    // Lifelines Container
                    Row(
                      children: [
                        _buildLifelineButton(
                          icon: Icons.star_half,
                          label: '50/50',
                          isUsed: _isFiftyFiftyUsed,
                          onPressed: _useFiftyFifty,
                        ),
                        const SizedBox(width: 8),
                        _buildLifelineButton(
                          icon: Icons.ac_unit,
                          label: 'Freeze',
                          isUsed: _isFreezeUsed,
                          onPressed: _useTimerFreeze,
                        ),
                        const SizedBox(width: 8),
                        _buildLifelineButton(
                          icon: Icons.skip_next,
                          label: 'Skip',
                          isUsed: _isSkipUsed,
                          onPressed: _useSkipQuestion,
                        ),
                      ],
                    ),
                  ],
                ),
                const SizedBox(height: 20),

                // Question progress bar
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'QUESTION ${_currentQuestionIndex + 1} OF ${questions.length}',
                      style: const TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 1.5,
                        color: AppTheme.textSecondary,
                      ),
                    ),
                    Text(
                      'DIFFICULTY: ${widget.quiz.difficulty.toUpperCase()}',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: widget.quiz.difficulty == 'Hard' 
                          ? AppTheme.incorrectRed 
                          : widget.quiz.difficulty == 'Medium'
                            ? AppTheme.warningOrange
                            : AppTheme.correctGreen,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 10),
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: LinearProgressIndicator(
                    value: progress,
                    minHeight: 8,
                    backgroundColor: Colors.white10,
                    valueColor: const AlwaysStoppedAnimation<Color>(AppTheme.accentPurple),
                  ),
                ),
                const SizedBox(height: 24),

                // Question text card
                Expanded(
                  child: SingleChildScrollView(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        // Card with Glass reflection
                        GlassContainer(
                          padding: const EdgeInsets.all(22),
                          child: Text(
                            currentQuestion.questionText,
                            style: const TextStyle(
                              fontSize: 19,
                              fontWeight: FontWeight.w600,
                              color: Colors.white,
                              height: 1.4,
                            ),
                            textAlign: TextAlign.center,
                          ),
                        ),
                        const SizedBox(height: 30),

                        // Options Layout
                        ...List.generate(currentQuestion.options.length, (index) {
                          final labels = ['A', 'B', 'C', 'D'];
                          final optText = currentQuestion.options[index];

                          // Resolve the state of this option button
                          OptionState optState = OptionState.defaultState;
                          if (_disabledOptionIndices.contains(index)) {
                            optState = OptionState.disabled;
                          } else if (_isAnswered) {
                            if (index == currentQuestion.correctOptionIndex) {
                              optState = OptionState.correct;
                            } else if (index == _selectedOptionIndex) {
                              optState = OptionState.incorrect;
                            } else {
                              optState = OptionState.disabled;
                            }
                          } else if (_selectedOptionIndex == index) {
                            optState = OptionState.selected;
                          }

                          return OptionButton(
                            text: optText,
                            label: index < labels.length ? labels[index] : '${index + 1}',
                            state: optState,
                            onTap: () => _handleOptionTap(index),
                          );
                        }),

                        // Explanation Card (Visible only when answered)
                        if (_isAnswered && currentQuestion.explanation.isNotEmpty) ...[
                          const SizedBox(height: 16),
                          GlassContainer(
                            padding: const EdgeInsets.all(16),
                            border: Border.all(color: AppTheme.infoBlue.withOpacity(0.3)),
                            color: AppTheme.infoBlue,
                            opacity: 0.05,
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                const Row(
                                  children: [
                                    Icon(Icons.info_outline, color: AppTheme.infoBlue, size: 18),
                                    SizedBox(width: 8),
                                    Text(
                                      'Explanation',
                                      style: TextStyle(fontWeight: FontWeight.bold, color: AppTheme.infoBlue, fontSize: 13),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 6),
                                Text(
                                  currentQuestion.explanation,
                                  style: const TextStyle(fontSize: 13, color: AppTheme.textSecondary),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ],
                    ),
                  ),
                ),

                // Navigation button (Next or Finish)
                if (_isAnswered)
                  Padding(
                    padding: const EdgeInsets.only(top: 16.0),
                    child: Container(
                      decoration: BoxDecoration(
                        gradient: AppTheme.accentGradient,
                        borderRadius: BorderRadius.circular(16),
                        boxShadow: [
                          BoxShadow(
                            color: AppTheme.accentPurple.withOpacity(0.3),
                            blurRadius: 10,
                            offset: const Offset(0, 4),
                          ),
                        ],
                      ),
                      child: ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.transparent,
                          shadowColor: Colors.transparent,
                          padding: const EdgeInsets.symmetric(vertical: 16),
                          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                        ),
                        onPressed: _nextQuestion,
                        child: Text(
                          _currentQuestionIndex == questions.length - 1 ? 'FINISH' : 'NEXT QUESTION',
                          style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.white, letterSpacing: 1),
                        ),
                      ),
                    ),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildLifelineButton({
    required IconData icon,
    required String label,
    required bool isUsed,
    required VoidCallback onPressed,
  }) {
    return InkWell(
      onTap: isUsed || _isAnswered ? null : onPressed,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(12),
          color: isUsed 
            ? Colors.white10 
            : _isAnswered 
              ? Colors.white.withOpacity(0.02)
              : AppTheme.primaryLight,
          border: Border.all(
            color: isUsed
              ? Colors.transparent
              : _isAnswered
                ? Colors.white10
                : AppTheme.accentCyan.withOpacity(0.3),
          ),
        ),
        child: Row(
          children: [
            Icon(
              icon,
              size: 14,
              color: isUsed 
                ? AppTheme.textMuted 
                : _isAnswered 
                  ? AppTheme.textSecondary 
                  : AppTheme.accentCyan,
            ),
            const SizedBox(width: 4),
            Text(
              label,
              style: TextStyle(
                fontSize: 10,
                fontWeight: FontWeight.bold,
                color: isUsed 
                  ? AppTheme.textMuted 
                  : _isAnswered 
                    ? AppTheme.textSecondary 
                    : Colors.white,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
