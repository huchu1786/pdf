import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/app_theme.dart';

class TimerIndicator extends StatelessWidget {
  final int remainingSeconds;
  final int totalSeconds;
  final double size;

  const TimerIndicator({
    super.key,
    required this.remainingSeconds,
    required this.totalSeconds,
    this.size = 50.0,
  });

  @override
  Widget build(BuildContext context) {
    final ratio = totalSeconds > 0 ? remainingSeconds / totalSeconds : 0.0;
    
    // Smooth transition from Green -> Orange -> Red
    Color indicatorColor;
    if (ratio > 0.5) {
      indicatorColor = AppTheme.correctGreen;
    } else if (ratio > 0.25) {
      indicatorColor = AppTheme.warningOrange;
    } else {
      indicatorColor = AppTheme.incorrectRed;
    }

    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        alignment: Alignment.center,
        children: [
          // Circular Track
          CircularProgressIndicator(
            value: ratio,
            backgroundColor: Colors.white10,
            valueColor: AlwaysStoppedAnimation<Color>(indicatorColor),
            strokeWidth: 4.5,
          ),
          // Time left text
          Text(
            '$remainingSeconds',
            style: TextStyle(
              fontSize: size * 0.35,
              fontWeight: FontWeight.bold,
              color: ratio < 0.25 ? AppTheme.incorrectRed : Colors.white,
            ),
          ),
        ],
      ),
    );
  }
}
