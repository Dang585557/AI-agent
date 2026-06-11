import 'package:flutter/material.dart';

import 'core/themes/app_theme.dart';
import 'features/home/home_screen.dart';
import 'features/onboarding/onboarding_screen.dart';

void main() {
  runApp(const DangAiAgentApp());
}

class DangAiAgentApp extends StatelessWidget {
  const DangAiAgentApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'DANG-AI-AGENT',
      theme: AppTheme.darkTheme,
      initialRoute: OnboardingScreen.route,
      routes: {
        OnboardingScreen.route: (_) => const OnboardingScreen(),
        HomeScreen.route: (_) => const HomeScreen(),
      },
    );
  }
}
