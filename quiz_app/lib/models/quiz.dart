import 'package:uuid/uuid.dart';
import 'question.dart';

class Quiz {
  final String id;
  final String title;
  final String description;
  final String category;
  final List<Question> questions;
  final int durationSeconds;
  final String difficulty;
  final bool isCustom;

  Quiz({
    required this.id,
    required this.title,
    required this.description,
    required this.category,
    required this.questions,
    this.durationSeconds = 120, // default 2 minutes
    this.difficulty = 'Medium',
    this.isCustom = false,
  });

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'description': description,
      'category': category,
      'questions': questions.map((q) => q.toJson()).toList(),
      'durationSeconds': durationSeconds,
      'difficulty': difficulty,
      'isCustom': isCustom,
    };
  }

  factory Quiz.fromJson(Map<String, dynamic> json) {
    return Quiz(
      id: json['id'] as String,
      title: json['title'] as String,
      description: json['description'] as String? ?? '',
      category: json['category'] as String,
      questions: (json['questions'] as List)
          .map((q) => Question.fromJson(q as Map<String, dynamic>))
          .toList(),
      durationSeconds: json['durationSeconds'] as int? ?? 120,
      difficulty: json['difficulty'] as String? ?? 'Medium',
      isCustom: json['isCustom'] as bool? ?? false,
    );
  }

  static List<Quiz> get defaultQuizzes {
    const uuid = Uuid();
    return [
      Quiz(
        id: 'default_tech_1',
        title: 'Tech & Gadgets',
        description: 'Test your knowledge on internet history, coding, and modern consumer tech.',
        category: 'Technology',
        difficulty: 'Medium',
        durationSeconds: 150,
        questions: [
          Question(
            id: uuid.v4(),
            questionText: 'Which programming language is known as the backbone of Android app development?',
            options: ['Java', 'Swift', 'Python', 'Dart'],
            correctOptionIndex: 0,
            explanation: 'Java was the original language used to develop Android apps, though Kotlin is now officially preferred.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What does "API" stand for in computer science?',
            options: [
              'Application Protocol Interface',
              'Advanced Programming Integration',
              'Application Programming Interface',
              'Automated Program Interaction'
            ],
            correctOptionIndex: 2,
            explanation: 'API stands for Application Programming Interface, which allows software applications to communicate with each other.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'Which company developed the Flutter SDK?',
            options: ['Apple', 'Microsoft', 'Google', 'Meta'],
            correctOptionIndex: 2,
            explanation: 'Google released the first version of Flutter in 2017 to allow cross-platform development.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What is the standard port number for secure web traffic (HTTPS)?',
            options: ['80', '8080', '443', '22'],
            correctOptionIndex: 2,
            explanation: 'HTTPS traffic uses port 443 by default, whereas HTTP traffic uses port 80.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What is the name of the main repository hosting platform acquired by Microsoft in 2018?',
            options: ['GitLab', 'GitHub', 'Bitbucket', 'SourceForge'],
            correctOptionIndex: 1,
            explanation: 'Microsoft acquired GitHub in June 2018 for \$7.5 billion.',
          ),
        ],
      ),
      Quiz(
        id: 'default_science_1',
        title: 'Wonders of Science',
        description: 'Explore the universe, chemistry, and basic physics equations.',
        category: 'Science',
        difficulty: 'Hard',
        durationSeconds: 120,
        questions: [
          Question(
            id: uuid.v4(),
            questionText: 'What is the approximate speed of light in a vacuum?',
            options: ['150,000 km/s', '300,000 km/s', '450,000 km/s', '600,000 km/s'],
            correctOptionIndex: 1,
            explanation: 'Light travels at roughly 299,792 kilometers per second (approx. 300,000 km/s).',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'Which element is the most abundant in the Earth\'s atmosphere?',
            options: ['Oxygen', 'Carbon Dioxide', 'Hydrogen', 'Nitrogen'],
            correctOptionIndex: 3,
            explanation: 'Nitrogen makes up about 78% of the Earth\'s atmosphere, followed by Oxygen at 21%.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What is the powerhouse of the cell?',
            options: ['Nucleus', 'Mitochondria', 'Ribosome', 'Golgi apparatus'],
            correctOptionIndex: 1,
            explanation: 'Mitochondria generate most of the chemical energy needed to power the cell\'s biochemical reactions.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What is the chemical formula for common table salt?',
            options: ['H2O', 'CO2', 'NaCl', 'HCl'],
            correctOptionIndex: 2,
            explanation: 'Table salt is Sodium Chloride (NaCl).',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'How many planets in our solar system have rings?',
            options: ['1', '2', '4', '8'],
            correctOptionIndex: 2,
            explanation: 'Four planets have rings: Saturn, Jupiter, Uranus, and Neptune (all gas giants).',
          ),
        ],
      ),
      Quiz(
        id: 'default_history_1',
        title: 'Global History & Landmarks',
        description: 'Travel back in time to test your knowledge of historical events.',
        category: 'History',
        difficulty: 'Medium',
        durationSeconds: 120,
        questions: [
          Question(
            id: uuid.v4(),
            questionText: 'In which year did the Titanic sink?',
            options: ['1905', '1912', '1920', '1931'],
            correctOptionIndex: 1,
            explanation: 'The RMS Titanic sank on April 15, 1912, after colliding with an iceberg in the North Atlantic.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'Who was the first President of the United States?',
            options: ['Thomas Jefferson', 'John Adams', 'Abraham Lincoln', 'George Washington'],
            correctOptionIndex: 3,
            explanation: 'George Washington served as the first US President from 1789 to 1797.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'Which ancient civilization built the Colosseum in Rome?',
            options: ['Ancient Greece', 'The Roman Empire', 'The Carthaginians', 'The Egyptians'],
            correctOptionIndex: 1,
            explanation: 'The Colosseum was built by the Roman Empire starting under Emperor Vespasian in 72 AD.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What historical document was signed by King John at Runnymede in 1215?',
            options: ['The Declaration of Independence', 'The Treaty of Versailles', 'The Magna Carta', 'The Bill of Rights'],
            correctOptionIndex: 2,
            explanation: 'The Magna Carta (Great Charter) established the principle that everyone, including the king, is subject to the law.',
          ),
        ],
      ),
      Quiz(
        id: 'default_pop_1',
        title: 'Pop Culture & Cinema',
        description: 'Questions about movies, music, icons, and trends.',
        category: 'Pop Culture',
        difficulty: 'Easy',
        durationSeconds: 90,
        questions: [
          Question(
            id: uuid.v4(),
            questionText: 'Which movie won the Academy Award for Best Picture in 2024?',
            options: ['Barbie', 'Oppenheimer', 'Poor Things', 'The Holdovers'],
            correctOptionIndex: 1,
            explanation: 'Christopher Nolan\'s "Oppenheimer" won the Best Picture award at the 96th Academy Awards in 2024.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'How many members were there in the British rock band "The Beatles"?',
            options: ['3', '4', '5', '6'],
            correctOptionIndex: 1,
            explanation: 'The Beatles had 4 core members: John Lennon, Paul McCartney, George Harrison, and Ringo Starr.',
          ),
          Question(
            id: uuid.v4(),
            questionText: 'What is the highest-grossing film of all time (unadjusted for inflation)?',
            options: ['Avengers: Endgame', 'Titanic', 'Avatar', 'Star Wars: The Force Awakens'],
            correctOptionIndex: 2,
            explanation: 'James Cameron\'s "Avatar" (2009) remains the highest-grossing film of all time with over \$2.9 billion.',
          ),
        ],
      ),
    ];
  }
}
