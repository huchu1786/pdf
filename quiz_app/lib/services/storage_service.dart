import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/quiz.dart';
import '../models/quiz_history.dart';
import '../models/question.dart';

class StorageService {
  static SharedPreferences? _prefs;

  static Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
  }

  // Keys
  static const String _keyCustomQuizzes = 'custom_quizzes';
  static const String _keyHistory = 'quiz_history';
  static const String _keyBookmarks = 'bookmarked_questions';
  static const String _keyUsername = 'username';
  static const String _keySoundEnabled = 'sound_enabled';

  // --- Custom Quizzes ---
  static List<Quiz> getCustomQuizzes() {
    final data = _prefs?.getStringList(_keyCustomQuizzes) ?? [];
    return data.map((item) => Quiz.fromJson(jsonDecode(item))).toList();
  }

  static Future<void> saveCustomQuiz(Quiz quiz) async {
    final list = getCustomQuizzes();
    // Remove if already exists (edit)
    list.removeWhere((q) => q.id == quiz.id);
    list.add(quiz);
    final data = list.map((q) => jsonEncode(q.toJson())).toList();
    await _prefs?.setStringList(_keyCustomQuizzes, data);
  }

  static Future<void> deleteCustomQuiz(String id) async {
    final list = getCustomQuizzes();
    list.removeWhere((q) => q.id == id);
    final data = list.map((q) => jsonEncode(q.toJson())).toList();
    await _prefs?.setStringList(_keyCustomQuizzes, data);
  }

  // --- History/Attempts ---
  static List<QuizAttempt> getHistory() {
    final data = _prefs?.getStringList(_keyHistory) ?? [];
    return data.map((item) => QuizAttempt.fromJson(jsonDecode(item))).toList();
  }

  static Future<void> saveAttempt(QuizAttempt attempt) async {
    final list = getHistory();
    list.insert(0, attempt); // Newest attempts first
    final data = list.map((item) => jsonEncode(item.toJson())).toList();
    await _prefs?.setStringList(_keyHistory, data);
  }

  static Future<void> clearHistory() async {
    await _prefs?.remove(_keyHistory);
  }

  // --- Bookmarked Questions ---
  static List<Question> getBookmarkedQuestions() {
    final data = _prefs?.getStringList(_keyBookmarks) ?? [];
    return data.map((item) => Question.fromJson(jsonDecode(item))).toList();
  }

  static Future<void> toggleBookmark(Question question) async {
    final list = getBookmarkedQuestions();
    final index = list.indexWhere((q) => q.id == question.id);
    if (index >= 0) {
      list.removeAt(index);
      question.isBookmarked = false;
    } else {
      question.isBookmarked = true;
      list.add(question);
    }
    final data = list.map((q) => jsonEncode(q.toJson())).toList();
    await _prefs?.setStringList(_keyBookmarks, data);
  }

  static bool isBookmarked(String questionId) {
    final list = getBookmarkedQuestions();
    return list.any((q) => q.id == questionId);
  }

  // --- Profile Settings ---
  static String getUsername() {
    return _prefs?.getString(_keyUsername) ?? 'Quiz Explorer';
  }

  static Future<void> setUsername(String name) async {
    await _prefs?.setString(_keyUsername, name);
  }

  static bool isSoundEnabled() {
    return _prefs?.getBool(_keySoundEnabled) ?? true;
  }

  static Future<void> setSoundEnabled(bool enabled) async {
    await _prefs?.setBool(_keySoundEnabled, enabled);
  }
}
