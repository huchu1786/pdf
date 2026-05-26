import 'package:flutter/material.dart';
import 'screens/home_screen.dart';
import 'services/storage_service.dart';
import 'theme/app_theme.dart';

void main() async {
  // Ensure Flutter engine bindings are initialized before accessing storage services
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize SharedPreferences storage
  await StorageService.init();

  runApp(const QuizProApp());
}

class QuizProApp extends StatelessWidget {
  const QuizProApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'QuizPro - Professional Assessment Suite',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.darkTheme,
      home: const HomeScreen(),
    );
  }
}
