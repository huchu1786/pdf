import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {
  // Brand Colors
  static const Color primaryDark = Color(0xFF0F0C1B);
  static const Color primaryLight = Color(0xFF1F1A3A);
  static const Color accentPurple = Color(0xFF8A2BE2);
  static const Color accentNeonPurple = Color(0xFFBF40BF);
  static const Color accentCyan = Color(0xFF00F5FF);
  
  // Quiz Status Colors
  static const Color correctGreen = Color(0xFF00FF87);
  static const Color incorrectRed = Color(0xFFFF3860);
  static const Color warningOrange = Color(0xFFFF9F43);
  static const Color infoBlue = Color(0xFF3897F0);

  // Text Colors
  static const Color textMain = Colors.white;
  static const Color textSecondary = Color(0xFFA0A5C1);
  static const Color textMuted = Color(0xFF676D93);

  // Background Gradients
  static const LinearGradient mainGradient = LinearGradient(
    colors: [
      Color(0xFF0B0914),
      Color(0xFF140F2B),
      Color(0xFF1E143E),
    ],
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
  );

  static const LinearGradient accentGradient = LinearGradient(
    colors: [
      accentPurple,
      Color(0xFFB030E0),
    ],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static const LinearGradient glassGradient = LinearGradient(
    colors: [
      Colors.white10,
      Colors.white24,
    ],
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
  );

  static ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      primaryColor: primaryLight,
      scaffoldBackgroundColor: primaryDark,
      colorScheme: const ColorScheme.dark(
        primary: accentPurple,
        secondary: accentCyan,
        surface: primaryLight,
        error: incorrectRed,
      ),
      textTheme: GoogleFonts.outfitTextTheme(
        const TextTheme(
          displayLarge: TextStyle(fontSize: 32, fontWeight: FontWeight.bold, color: textMain),
          displayMedium: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: textMain),
          displaySmall: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: textMain),
          headlineMedium: TextStyle(fontSize: 20, fontWeight: FontWeight.w600, color: textMain),
          titleLarge: TextStyle(fontSize: 18, fontWeight: FontWeight.w600, color: textMain),
          bodyLarge: TextStyle(fontSize: 16, color: textMain, height: 1.4),
          bodyMedium: TextStyle(fontSize: 14, color: textSecondary, height: 1.4),
          labelLarge: TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: textMain),
        ),
      ),
      appBarTheme: const AppBarTheme(
        backgroundColor: Colors.transparent,
        elevation: 0,
        centerTitle: true,
        titleTextStyle: TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: textMain),
        iconTheme: IconThemeData(color: textMain),
      ),
      cardTheme: CardTheme(
        color: primaryLight,
        elevation: 4,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20),
          side: BorderSide(color: Colors.white.withOpacity(0.08), width: 1),
        ),
      ),
    );
  }
}
