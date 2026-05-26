import 'package:flutter/material.dart';
import '../models/quiz.dart';
import '../models/quiz_history.dart';
import '../services/storage_service.dart';
import '../theme/app_theme.dart';
import '../widgets/glass_container.dart';
import 'quiz_play_screen.dart';
import 'quiz_creator_screen.dart';
import 'analytics_screen.dart';
import 'bookmark_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  String _userName = '';
  List<Quiz> _customQuizzes = [];
  List<QuizAttempt> _attempts = [];
  int _currentIndex = 0;

  @override
  void initState() {
    super.initState();
    _loadUserData();
  }

  void _loadUserData() {
    setState(() {
      _userName = StorageService.getUsername();
      _customQuizzes = StorageService.getCustomQuizzes();
      _attempts = StorageService.getHistory();
    });
  }

  void _editUserName() {
    final controller = TextEditingController(text: _userName);
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: AppTheme.primaryLight,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
          title: const Text('Edit Profile Name'),
          content: TextField(
            controller: controller,
            decoration: const InputDecoration(
              hintText: 'Enter your name...',
              focusedBorder: UnderlineInputBorder(
                borderSide: BorderSide(color: AppTheme.accentCyan),
              ),
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('Cancel', style: TextStyle(color: Colors.white70)),
            ),
            TextButton(
              onPressed: () async {
                if (controller.text.trim().isNotEmpty) {
                  await StorageService.setUsername(controller.text.trim());
                  _loadUserData();
                }
                if (mounted) Navigator.pop(context);
              },
              child: const Text('Save', style: TextStyle(color: AppTheme.accentCyan, fontWeight: FontWeight.bold)),
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(gradient: AppTheme.mainGradient),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: SafeArea(
          child: IndexedStack(
            index: _currentIndex,
            children: [
              _buildDashboard(),
              const AnalyticsScreen(),
              const BookmarkScreen(),
            ],
          ),
        ),
        bottomNavigationBar: _buildBottomNav(),
      ),
    );
  }

  Widget _buildDashboard() {
    final totalQuizzes = _attempts.length;
    final avgScore = _attempts.isEmpty
        ? 0.0
        : _attempts.map((a) => a.percentage).reduce((a, b) => a + b) / _attempts.length;

    return SingleChildScrollView(
      padding: const EdgeInsets.all(20.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Header / Profile Greeting
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    'WELCOME BACK,',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      letterSpacing: 2,
                      color: AppTheme.accentCyan,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Text(
                        _userName,
                        style: const TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      IconButton(
                        icon: const Icon(Icons.edit, size: 16, color: AppTheme.textSecondary),
                        onPressed: _editUserName,
                      ),
                    ],
                  ),
                ],
              ),
              // Level Badge / Score summary
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  gradient: AppTheme.accentGradient,
                  borderRadius: BorderRadius.circular(30),
                  boxShadow: [
                    BoxShadow(
                      color: AppTheme.accentPurple.withOpacity(0.4),
                      blurRadius: 10,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Row(
                  children: [
                    const Icon(Icons.stars, color: Colors.white, size: 18),
                    const SizedBox(width: 6),
                    Text(
                      'LVL ${1 + (totalQuizzes ~/ 3)}',
                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                    ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 24),

          // Overview Stats Card
          GlassContainer(
            padding: const EdgeInsets.all(18),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildStatColumn('Quizzes Played', '$totalQuizzes', Icons.play_circle_outline),
                Container(width: 1, height: 40, color: Colors.white12),
                _buildStatColumn('Avg. Accuracy', '${avgScore.toStringAsFixed(0)}%', Icons.check_circle_outline),
                Container(width: 1, height: 40, color: Colors.white12),
                _buildStatColumn('XP Earned', '${totalQuizzes * 100}', Icons.bolt),
              ],
            ),
          ),
          const SizedBox(height: 28),

          // Daily Challenge Banner
          _buildDailyChallengeCard(),
          const SizedBox(height: 28),

          // Categories Grid
          const Text(
            'CHOOSE CATEGORY',
            style: TextStyle(
              fontSize: 12,
              fontWeight: FontWeight.bold,
              letterSpacing: 1.5,
              color: AppTheme.textSecondary,
            ),
          ),
          const SizedBox(height: 14),
          _buildCategoriesGrid(),
          const SizedBox(height: 28),

          // Custom Quizzes Section
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                'YOUR CUSTOM QUIZZES',
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.bold,
                  letterSpacing: 1.5,
                  color: AppTheme.textSecondary,
                ),
              ),
              TextButton.icon(
                icon: const Icon(Icons.add, size: 16, color: AppTheme.accentCyan),
                label: const Text('Create New', style: TextStyle(color: AppTheme.accentCyan, fontWeight: FontWeight.bold)),
                onPressed: () async {
                  await Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const QuizCreatorScreen()),
                  );
                  _loadUserData();
                },
              ),
            ],
          ),
          const SizedBox(height: 10),
          _buildCustomQuizzesList(),
        ],
      ),
    );
  }

  Widget _buildStatColumn(String label, String value, IconData icon) {
    return Column(
      children: [
        Icon(icon, color: AppTheme.accentCyan, size: 20),
        const SizedBox(height: 6),
        Text(
          value,
          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
        ),
        const SizedBox(height: 4),
        Text(
          label,
          style: const TextStyle(fontSize: 11, color: AppTheme.textSecondary),
        ),
      ],
    );
  }

  Widget _buildDailyChallengeCard() {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(20),
        gradient: const LinearGradient(
          colors: [Color(0xFF8A2BE2), Color(0xFF4B0082)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        boxShadow: [
          BoxShadow(
            color: AppTheme.accentPurple.withOpacity(0.3),
            blurRadius: 15,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          onTap: () {
            // Select random default quiz
            final quizzes = Quiz.defaultQuizzes;
            if (quizzes.isNotEmpty) {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => QuizPlayScreen(quiz: quizzes[0]),
                ),
              ).then((_) => _loadUserData());
            }
          },
          borderRadius: BorderRadius.circular(20),
          child: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                        decoration: BoxDecoration(
                          color: Colors.white24,
                          borderRadius: BorderRadius.circular(10),
                        ),
                        child: const Text(
                          'DAILY CHALLENGE',
                          style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold),
                        ),
                      ),
                      const SizedBox(height: 10),
                      const Text(
                        'Ultimate Tech Mastery',
                        style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.white),
                      ),
                      const SizedBox(height: 6),
                      const Text(
                        'Play today\'s curated questions and earn double XP points!',
                        style: TextStyle(fontSize: 13, color: Colors.white80),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 10),
                const CircleAvatar(
                  radius: 28,
                  backgroundColor: Colors.white24,
                  child: Icon(Icons.play_arrow_rounded, size: 36, color: Colors.white),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildCategoriesGrid() {
    final categories = [
      {'name': 'Technology', 'icon': Icons.laptop_chromebook, 'color': AppTheme.accentCyan, 'desc': 'Coding & Gadgets'},
      {'name': 'Science', 'icon': Icons.science, 'color': AppTheme.correctGreen, 'desc': 'Cosmos & Bio-cells'},
      {'name': 'History', 'icon': Icons.auto_stories, 'color': AppTheme.warningOrange, 'desc': 'Events & Empires'},
      {'name': 'Pop Culture', 'icon': Icons.movie, 'color': AppTheme.accentNeonPurple, 'desc': 'Movies & Icons'},
    ];

    return GridView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        crossAxisSpacing: 14,
        mainAxisSpacing: 14,
        childAspectRatio: 1.25,
      ),
      itemCount: categories.length,
      itemBuilder: (context, index) {
        final cat = categories[index];
        final catName = cat['name'] as String;
        final icon = cat['icon'] as IconData;
        final color = cat['color'] as Color;
        final desc = cat['desc'] as String;

        return InkWell(
          onTap: () {
            // Find first default quiz of this category or construct a random selection
            final matches = Quiz.defaultQuizzes.where((q) => q.category == catName).toList();
            if (matches.isNotEmpty) {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => QuizPlayScreen(quiz: matches[0]),
                ),
              ).then((_) => _loadUserData());
            } else {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text('No assessments found for $catName.')),
              );
            }
          },
          borderRadius: BorderRadius.circular(18),
          child: GlassContainer(
            padding: const EdgeInsets.all(16),
            borderRadius: BorderRadius.circular(18),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(icon, color: color, size: 28),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      catName,
                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      desc,
                      style: const TextStyle(fontSize: 10, color: AppTheme.textSecondary),
                    ),
                  ],
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildCustomQuizzesList() {
    if (_customQuizzes.isEmpty) {
      return Container(
        width: double.infinity,
        padding: const EdgeInsets.symmetric(vertical: 30),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: Colors.white.withOpacity(0.05)),
          color: Colors.white.withOpacity(0.01),
        ),
        child: Column(
          children: [
            const Icon(Icons.post_add, size: 40, color: AppTheme.textMuted),
            const SizedBox(height: 10),
            const Text(
              'No custom quizzes built yet.',
              style: TextStyle(color: AppTheme.textSecondary, fontSize: 14),
            ),
            const SizedBox(height: 4),
            TextButton(
              onPressed: () async {
                await Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const QuizCreatorScreen()),
                );
                _loadUserData();
              },
              child: const Text('Create One Now', style: TextStyle(color: AppTheme.accentCyan)),
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      shrinkWrap: true,
      physics: const NeverScrollableScrollPhysics(),
      itemCount: _customQuizzes.length,
      itemBuilder: (context, index) {
        final quiz = _customQuizzes[index];
        return Container(
          margin: const EdgeInsets.only(bottom: 12),
          child: GlassContainer(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            child: Row(
              children: [
                CircleAvatar(
                  backgroundColor: AppTheme.accentPurple.withOpacity(0.2),
                  child: const Icon(Icons.library_books, color: AppTheme.accentPurple),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        quiz.title,
                        style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        '${quiz.questions.length} Questions • ${quiz.category}',
                        style: const TextStyle(fontSize: 12, color: AppTheme.textSecondary),
                      ),
                    ],
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.delete_outline, color: AppTheme.incorrectRed),
                  onPressed: () async {
                    await StorageService.deleteCustomQuiz(quiz.id);
                    _loadUserData();
                  },
                ),
                IconButton(
                  icon: const Icon(Icons.play_arrow_rounded, color: AppTheme.correctGreen, size: 28),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => QuizPlayScreen(quiz: quiz),
                      ),
                    ).then((_) => _loadUserData());
                  },
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  Widget _buildBottomNav() {
    return Container(
      decoration: BoxDecoration(
        color: AppTheme.primaryLight.withOpacity(0.9),
        border: Border(
          top: BorderSide(color: Colors.white.withOpacity(0.08), width: 1.5),
        ),
      ),
      child: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 8),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildNavItem(0, Icons.dashboard_outlined, Icons.dashboard, 'Home'),
              _buildNavItem(1, Icons.bar_chart_outlined, Icons.bar_chart_rounded, 'Stats'),
              _buildNavItem(2, Icons.bookmark_border_outlined, Icons.bookmark, 'Saved'),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(int index, IconData outlineIcon, IconData filledIcon, String label) {
    final isSelected = _currentIndex == index;
    final color = isSelected ? AppTheme.accentCyan : AppTheme.textSecondary;

    return InkWell(
      onTap: () {
        setState(() {
          _currentIndex = index;
        });
      },
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(isSelected ? filledIcon : outlineIcon, color: color, size: 24),
          const SizedBox(height: 4),
          Text(
            label,
            style: TextStyle(color: color, fontSize: 11, fontWeight: isSelected ? FontWeight.bold : FontWeight.normal),
          ),
        ],
      ),
    );
  }
}
