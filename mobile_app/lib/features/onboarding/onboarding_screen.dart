import 'package:flutter/material.dart';

import '../home/home_screen.dart';

class OnboardingScreen extends StatelessWidget {
  const OnboardingScreen({super.key});
  static const route = '/';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const CircleAvatar(radius: 42, child: Icon(Icons.auto_awesome, size: 42)),
              const SizedBox(height: 24),
              const Text('ยินดีต้อนรับ', style: TextStyle(fontSize: 28, fontWeight: FontWeight.w900)),
              const SizedBox(height: 10),
              const Text('AI Assistant พร้อมช่วยเหลือคุณในทุกเรื่อง', textAlign: TextAlign.center),
              const SizedBox(height: 32),
              ElevatedButton(
                onPressed: () => Navigator.pushReplacementNamed(context, HomeScreen.route),
                child: const Text('เริ่มใช้งาน'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
