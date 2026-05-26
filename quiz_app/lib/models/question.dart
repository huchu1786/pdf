class Question {
  final String id;
  final String questionText;
  final List<String> options;
  final int correctOptionIndex;
  final String explanation;
  bool isBookmarked;
  int? selectedOptionIndex; // Used for post-quiz review

  Question({
    required this.id,
    required this.questionText,
    required this.options,
    required this.correctOptionIndex,
    required this.explanation,
    this.isBookmarked = false,
    this.selectedOptionIndex,
  });

  bool get isCorrect => selectedOptionIndex == correctOptionIndex;

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'questionText': questionText,
      'options': options,
      'correctOptionIndex': correctOptionIndex,
      'explanation': explanation,
      'isBookmarked': isBookmarked,
      'selectedOptionIndex': selectedOptionIndex,
    };
  }

  factory Question.fromJson(Map<String, dynamic> json) {
    return Question(
      id: json['id'] as String,
      questionText: json['questionText'] as String,
      options: List<String>.from(json['options'] as List),
      correctOptionIndex: json['correctOptionIndex'] as int,
      explanation: json['explanation'] as String? ?? '',
      isBookmarked: json['isBookmarked'] as bool? ?? false,
      selectedOptionIndex: json['selectedOptionIndex'] as int?,
    );
  }

  Question copyWith({
    String? id,
    String? questionText,
    List<String>? options,
    int? correctOptionIndex,
    String? explanation,
    bool? isBookmarked,
    int? selectedOptionIndex,
  }) {
    return Question(
      id: id ?? this.id,
      questionText: questionText ?? this.questionText,
      options: options ?? this.options,
      correctOptionIndex: correctOptionIndex ?? this.correctOptionIndex,
      explanation: explanation ?? this.explanation,
      isBookmarked: isBookmarked ?? this.isBookmarked,
      selectedOptionIndex: selectedOptionIndex ?? this.selectedOptionIndex,
    );
  }
}
