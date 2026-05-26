import 'package:flutter/material.dart';
import '../theme/app_theme.dart';
import 'glass_container.dart';

enum OptionState {
  defaultState,
  selected,
  correct,
  incorrect,
  disabled,
}

class OptionButton extends StatelessWidget {
  final String text;
  final String label; // A, B, C, D
  final OptionState state;
  final VoidCallback onTap;

  const OptionButton({
    super.key,
    required this.text,
    required this.label,
    required this.state,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    Color getBorderColor() {
      switch (state) {
        case OptionState.selected:
          return AppTheme.accentCyan;
        case OptionState.correct:
          return AppTheme.correctGreen;
        case OptionState.incorrect:
          return AppTheme.incorrectRed;
        case OptionState.disabled:
        case OptionState.defaultState:
          return Colors.white.withOpacity(0.08);
      }
    }

    Color getBgColor() {
      switch (state) {
        case OptionState.selected:
          return AppTheme.accentPurple.withOpacity(0.3);
        case OptionState.correct:
          return AppTheme.correctGreen.withOpacity(0.25);
        case OptionState.incorrect:
          return AppTheme.incorrectRed.withOpacity(0.25);
        case OptionState.disabled:
          return Colors.transparent;
        case OptionState.defaultState:
          return Colors.white.withOpacity(0.02);
      }
    }

    Widget? getTrailingIcon() {
      switch (state) {
        case OptionState.correct:
          return const Icon(Icons.check_circle, color: AppTheme.correctGreen, size: 22);
        case OptionState.incorrect:
          return const Icon(Icons.cancel, color: AppTheme.incorrectRed, size: 22);
        default:
          return null;
      }
    }

    final isClickable = state == OptionState.defaultState || state == OptionState.selected;

    return AnimatedOpacity(
      duration: const Duration(milliseconds: 250),
      opacity: state == OptionState.disabled ? 0.4 : 1.0,
      child: Container(
        margin: const EdgeInsets.only(bottom: 14),
        child: InkWell(
          onTap: isClickable ? onTap : null,
          borderRadius: BorderRadius.circular(16),
          child: GlassContainer(
            padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 16),
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: getBorderColor(), width: 1.5),
            color: getBgColor(),
            opacity: 0.1,
            child: Row(
              children: [
                // Option label (A, B, C, D)
                Container(
                  width: 32,
                  height: 32,
                  decoration: BoxDecoration(
                    color: state == OptionState.selected
                        ? AppTheme.accentCyan
                        : Colors.white.withOpacity(0.08),
                    shape: BoxShape.circle,
                  ),
                  child: Center(
                    child: Text(
                      label,
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                        color: state == OptionState.selected
                            ? Colors.black
                            : Colors.white,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 14),
                // Option text
                Expanded(
                  child: Text(
                    text,
                    style: const TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w500,
                      color: Colors.white,
                    ),
                  ),
                ),
                // Trailing check/cross icon
                if (getTrailingIcon() != null) getTrailingIcon()!,
              ],
            ),
          ),
        ),
      ),
    );
  }
}
