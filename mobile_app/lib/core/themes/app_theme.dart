import 'package:flutter/material.dart';

class AppTheme {
  static const background = Color(0xFF090A0F);
  static const surface = Color(0xFF12141C);
  static const surfaceHigh = Color(0xFF1A1D29);
  static const primary = Color(0xFF68BF78);
  static const text = Color(0xFFF4F6FB);
  static const muted = Color(0xFF9BA3B4);

  static ThemeData get darkTheme {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      scaffoldBackgroundColor: background,
      colorScheme: const ColorScheme.dark(primary: primary, surface: surface),
      appBarTheme: const AppBarTheme(backgroundColor: background, elevation: 0, centerTitle: true),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: surfaceHigh,
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(14), borderSide: BorderSide.none),
        hintStyle: const TextStyle(color: muted),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: primary,
          foregroundColor: Colors.white,
          minimumSize: const Size.fromHeight(52),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          textStyle: const TextStyle(fontWeight: FontWeight.w800),
        ),
      ),
    );
  }
}
