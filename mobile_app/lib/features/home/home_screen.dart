import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});
  static const route = '/home';

  @override
  Widget build(BuildContext context) {
    final features = [
      ('แชทกับ AI', Icons.chat_bubble_outline),
      ('สร้างภาพ', Icons.image_outlined),
      ('วิเคราะห์ภาพ', Icons.photo_search_outlined),
      ('เขียนโค้ด', Icons.code),
      ('สรุปเอกสาร', Icons.description_outlined),
      ('แปลภาษา', Icons.translate),
      ('ค้นหาข้อมูล', Icons.search),
      ('ช่วยคิดไอเดีย', Icons.lightbulb_outline),
    ];
    return Scaffold(
      appBar: AppBar(title: const Text('ฟีเจอร์ทั้งหมด')),
      body: GridView.builder(
        padding: const EdgeInsets.all(18),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          crossAxisSpacing: 10,
          mainAxisSpacing: 10,
        ),
        itemCount: features.length,
        itemBuilder: (context, index) {
          final feature = features[index];
          return Card(
            color: Theme.of(context).colorScheme.surface,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(feature.$2, size: 34),
                const SizedBox(height: 12),
                Text(feature.$1, style: const TextStyle(fontWeight: FontWeight.w800)),
              ],
            ),
          );
        },
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: 1,
        destinations: const [
          NavigationDestination(icon: Icon(Icons.chat_bubble_outline), label: 'แชท'),
          NavigationDestination(icon: Icon(Icons.apps), label: 'ฟีเจอร์'),
          NavigationDestination(icon: Icon(Icons.history), label: 'ประวัติ'),
          NavigationDestination(icon: Icon(Icons.settings), label: 'ตั้งค่า'),
        ],
      ),
    );
  }
}
