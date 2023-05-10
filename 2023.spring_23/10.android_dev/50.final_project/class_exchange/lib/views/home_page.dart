import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  HomePage({super.key});

  String titleBar = 'Class Exchange';

  State<HomePage> createState () => _HomePage();
}

class _HomePage extends State<HomePage> {
  _HomePage();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text (widget.titleBar),
      ),
      body: Center(
        child: Text('hello World !'),
      ),
    );
  }
}