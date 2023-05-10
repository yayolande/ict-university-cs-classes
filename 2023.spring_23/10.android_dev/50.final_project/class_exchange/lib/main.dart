import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'controllers/app_router.dart';


// final _routerManager = RouterApp();
final _router = RouterApp().router;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    MaterialApp materialApp;

    materialApp = MaterialApp.router(
      title: 'Class Exchange App',
      theme: ThemeData(
        useMaterial3: true,
        // colorScheme: ColorScheme.fromSeed(seedColor: Colors.redAccent),
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blueAccent),
      ),
      routerConfig: _router,
    );

    return materialApp;
  }
}

