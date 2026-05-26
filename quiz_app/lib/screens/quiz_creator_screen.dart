import 'package:flutter/material.dart';
import 'package:uuid/uuid.dart';
import '../models/question.dart';
import '../models/quiz.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/glass_container.dart';

class QuizCreatorScreen extends StatefulWidget {
  const QuizCreatorScreen({super.key});

  @override
  State<QuizCreatorScreen> createState() => _QuizCreatorScreenState();
}

class _QuizCreatorScreenState extends State<QuizCreatorScreen> {
  final _formKey = GlobalKey<FormState>();
  final _titleController = TextEditingController();
  final _descController = TextEditingController();
  
  String _category = 'Technology';
  String _difficulty = 'Medium';
  int _durationMinutes = 2;

  final List<Question> _questions = [];

  // Question Form State
  final _questionTextController = TextEditingController();
  final List<TextEditingController> _optionControllers = List.generate(4, (_) => TextEditingController());
  final _explanationController = TextEditingController();
  int _correctOptionIndex = 0;

  @override
  void dispose() {
    _titleController.dispose();
    _descController.dispose();
    _questionTextController.dispose();
    for (var c in _optionControllers) {
      c.dispose();
    }
    _explanationController.dispose();
    super.dispose();
  }

  void _addQuestion() {
    if (_questionTextController.text.trim().isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Please enter a question description.')),
      );
      return;
    }

    for (int i = 0; i < 4; i++) {
      if (_optionControllers[i].text.trim().isEmpty) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Option ${String.fromCharCode(65 + i)} cannot be empty.')),
        );
        return;
      }
    }

    final newQuestion = Question(
      id: const Uuid().v4(),
      questionText: _questionTextController.text.trim(),
      options: _optionControllers.map((c) => c.text.trim()).toList(),
      correctOptionIndex: _correctOptionIndex,
      explanation: _explanationController.text.trim(),
    );

    setState(() {
      _questions.add(newQuestion);
      // Clear question form
      _questionTextController.clear();
      for (var c in _optionControllers) {
        c.clear();
      }
      _explanationController.clear();
      _correctOptionIndex = 0;
    });

    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text('Question added successfully!')),
    );
  }

  void _saveQuiz() async {
    if (!_formKey.currentState!.validate()) return;

    if (_questions.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Please add at least one question to the assessment.')),
      );
      return;
    }

    final newQuiz = Quiz(
      id: 'custom_${DateTime.now().millisecondsSinceEpoch}',
      title: _titleController.text.trim(),
      description: _descController.text.trim(),
      category: _category,
      difficulty: _difficulty,
      durationSeconds: _durationMinutes * 60,
      questions: List.from(_questions),
      isCustom: true,
    );

    await StorageService.saveCustomQuiz(newQuiz);

    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Custom assessment saved successfully!')),
      );
      Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(gradient: AppTheme.mainGradient),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(title: const Text('Assessment Creator')),
        body: SafeArea(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(20.0),
            child: Form(
              key: _formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  const Text(
                    'ASSESSMENT DETAILS',
                    style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1.5),
                  ),
                  const SizedBox(height: 12),
                  GlassContainer(
                    padding: const EdgeInsets.all(18),
                    child: Column(
                      children: [
                        TextFormField(
                          controller: _titleController,
                          decoration: const InputDecoration(
                            labelText: 'Quiz Title',
                            focusedBorder: UnderlineInputBorder(borderSide: BorderSide(color: AppTheme.accentCyan)),
                          ),
                          validator: (val) => val == null || val.trim().isEmpty ? 'Title is required' : null,
                        ),
                        const SizedBox(height: 12),
                        TextFormField(
                          controller: _descController,
                          decoration: const InputDecoration(
                            labelText: 'Description',
                            focusedBorder: UnderlineInputBorder(borderSide: BorderSide(color: AppTheme.accentCyan)),
                          ),
                        ),
                        const SizedBox(height: 16),
                        Row(
                          children: [
                            Expanded(
                              child: DropdownButtonFormField<String>(
                                value: _category,
                                decoration: const InputDecoration(labelText: 'Category'),
                                items: ['Technology', 'Science', 'History', 'Pop Culture', 'General']
                                    .map((c) => DropdownMenuItem(value: c, child: Text(c)))
                                    .toList(),
                                onChanged: (val) => setState(() => _category = val ?? 'General'),
                              ),
                            ),
                            const SizedBox(width: 14),
                            Expanded(
                              child: DropdownButtonFormField<String>(
                                value: _difficulty,
                                decoration: const InputDecoration(labelText: 'Difficulty'),
                                items: ['Easy', 'Medium', 'Hard']
                                    .map((d) => DropdownMenuItem(value: d, child: Text(d)))
                                    .toList(),
                                onChanged: (val) => setState(() => _difficulty = val ?? 'Medium'),
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 12),
                        DropdownButtonFormField<int>(
                          value: _durationMinutes,
                          decoration: const InputDecoration(labelText: 'Time Limit (Minutes)'),
                          items: [1, 2, 3, 5, 10]
                              .map((t) => DropdownMenuItem(value: t, child: Text('$t Minutes')))
                              .toList(),
                          onChanged: (val) => setState(() => _durationMinutes = val ?? 2),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 28),

                  // Questions list header
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'QUESTIONS ADDED (${_questions.length})',
                        style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1.5),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),

                  if (_questions.isNotEmpty)
                    ListView.builder(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount: _questions.length,
                      itemBuilder: (context, index) {
                        final q = _questions[index];
                        return Card(
                          margin: const EdgeInsets.only(bottom: 10),
                          child: ListTile(
                            leading: CircleAvatar(
                              backgroundColor: AppTheme.accentPurple.withOpacity(0.2),
                              child: Text('${index + 1}', style: const TextStyle(color: AppTheme.accentPurple, fontWeight: FontWeight.bold)),
                            ),
                            title: Text(q.questionText, maxLines: 1, overflow: TextOverflow.ellipsis),
                            subtitle: Text('Correct: Option ${String.fromCharCode(65 + q.correctOptionIndex)}'),
                            trailing: IconButton(
                              icon: const Icon(Icons.delete_outline, color: AppTheme.incorrectRed),
                              onPressed: () => setState(() => _questions.removeAt(index)),
                            ),
                          ),
                        );
                      },
                    )
                  else
                    Container(
                      padding: const EdgeInsets.symmetric(vertical: 20),
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        border: Border.all(color: Colors.white10),
                        borderRadius: BorderRadius.circular(16),
                      ),
                      child: const Text('Add questions below to compile.', style: TextStyle(color: AppTheme.textMuted)),
                    ),
                  const SizedBox(height: 28),

                  // Add Question Section
                  const Text(
                    'ADD QUESTION TO ASSESS',
                    style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: AppTheme.textSecondary, letterSpacing: 1.5),
                  ),
                  const SizedBox(height: 12),

                  GlassContainer(
                    padding: const EdgeInsets.all(18),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.stretch,
                      children: [
                        TextFormField(
                          controller: _questionTextController,
                          maxLines: 2,
                          decoration: const InputDecoration(
                            labelText: 'Question Prompt',
                            focusedBorder: UnderlineInputBorder(borderSide: BorderSide(color: AppTheme.accentCyan)),
                          ),
                        ),
                        const SizedBox(height: 16),
                        // 4 Option input rows
                        ...List.generate(4, (index) {
                          final char = String.fromCharCode(65 + index);
                          return Padding(
                            padding: const EdgeInsets.only(bottom: 8.0),
                            child: TextFormField(
                              controller: _optionControllers[index],
                              decoration: InputDecoration(
                                labelText: 'Option $char',
                                focusedBorder: const UnderlineInputBorder(borderSide: BorderSide(color: AppTheme.accentCyan)),
                              ),
                            ),
                          );
                        }),
                        const SizedBox(height: 16),
                        // Dropdown for correct answer
                        DropdownButtonFormField<int>(
                          value: _correctOptionIndex,
                          decoration: const InputDecoration(labelText: 'Correct Option Designation'),
                          items: List.generate(4, (index) {
                            final char = String.fromCharCode(65 + index);
                            return DropdownMenuItem(value: index, child: Text('Option $char'));
                          }),
                          onChanged: (val) => setState(() => _correctOptionIndex = val ?? 0),
                        ),
                        const SizedBox(height: 12),
                        TextFormField(
                          controller: _explanationController,
                          decoration: const InputDecoration(
                            labelText: 'Explanation / Hints (Optional)',
                            focusedBorder: UnderlineInputBorder(borderSide: BorderSide(color: AppTheme.accentCyan)),
                          ),
                        ),
                        const SizedBox(height: 20),
                        OutlinedButton.styleFrom(
                          side: const BorderSide(color: AppTheme.accentCyan),
                        ),
                        OutlinedButton(
                          style: OutlinedButton.styleFrom(
                            side: const BorderSide(color: AppTheme.accentCyan, width: 1.5),
                            padding: const EdgeInsets.symmetric(vertical: 14),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                          ),
                          onPressed: _addQuestion,
                          child: const Text('ADD QUESTION', style: TextStyle(color: AppTheme.accentCyan, fontWeight: FontWeight.bold)),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 30),

                  // Save Quiz Button
                  Container(
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
                      onPressed: _saveQuiz,
                      child: const Text(
                        'SAVE AND COMPILE ASSESS',
                        style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.white, letterSpacing: 1),
                      ),
                    ),
                  ),
                  const SizedBox(height: 20),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
