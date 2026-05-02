class ToolModel {
  final String id;
  final String toolId;
  final String title;
  final String meta;
  final String h1;
  final String description;
  final List<String> instructions;
  final List<Benefit> benefits;
  final List<FAQ> faqs;
  final List<String> related;

  ToolModel({
    required this.id,
    required this.toolId,
    required this.title,
    required this.meta,
    required this.h1,
    required this.description,
    required this.instructions,
    required this.benefits,
    required this.faqs,
    required this.related,
  });

  String get h1Text => h1;

  String get metaDescription => meta;

  String get toolName => title;
}

class Benefit {
  final String title;
  final String description;

  Benefit({required this.title, required this.description});

  String get benefitTitle => title;
  String get benefitDescription => description;
}

class FAQ {
  final String question;
  final String answer;

  FAQ({required this.question, required this.answer});
}