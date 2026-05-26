class QuizAttempt {
  final String id;
  final String quizId;
  final String quizTitle;
  final String category;
  final int score;
  final int totalQuestions;
  final int timeSpentSeconds;
  final DateTime date;

  QuizAttempt({
    required this.id,
    required this.quizId,
    required this.quizTitle,
    required this.category,
    required this.score,
    required this.totalQuestions,
    required this.timeSpentSeconds,
    required this.date,
  });

  double get percentage => totalQuestions > 0 ? (score / totalQuestions) * 100 : 0.0;

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'quizId': quizId,
      'quizTitle': quizTitle,
      'category': category,
      'score': score,
      'totalQuestions': totalQuestions,
      'timeSpentSeconds': timeSpentSeconds,
      'date': date.toIso8601String(),
    };
  }

  factory QuizAttempt.fromJson(Map<String, dynamic> json) {
    return QuizAttempt(
      id: json['id'] as String,
      quizId: json['quizId'] as String,
      quizTitle: json['quizTitle'] as String,
      category: json['category'] as String,
      score: json['score'] as int,
      totalQuestions: json['totalQuestions'] as int,
      timeSpentSeconds: json['timeSpentSeconds'] as int,
      date: DateTime.parse(json['date'] as String),
    );
  }
}
