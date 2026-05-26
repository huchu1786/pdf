import 'package:flutter_test/flutter_test.dart';
import 'package:quiz_app/main.dart';
import 'package:quiz_app/services/storage_service.dart';

void main() {
  testWidgets('QuizProApp dashboard smoke test', (WidgetTester tester) async {
    // Initialize dummy mock storage if needed, or storage service itself
    await StorageService.init();

    // Build our app and trigger a frame.
    await tester.pumpWidget(const QuizProApp());

    // Verify that the title or header exists
    expect(find.text('WELCOME BACK,'), findsOneWidget);
  });
}
