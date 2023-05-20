import 'package:class_exchange/controllers/app_manager.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:class_exchange/models/user.dart';

class LoginPage extends StatefulWidget {
  LoginPage({Key? key}) : super(key: key);

  @override
  _LoginPage createState() => _LoginPage();
}

class _LoginPage extends State<LoginPage> {
  _LoginPage();

  TextEditingController inputUserNameController = new TextEditingController();
  TextEditingController inputPasswordController = new TextEditingController();

  void verifyLogin() {
    String username = inputUserNameController.text;
    String password = inputPasswordController.text;
    int userId = 10;

    print('Login .......');
    print('username = ${username} ::: password = ${password}');

    AppManager app = AppManager();
    User user = User(username, password, userId);
    app.fromLoginToHome(context, user);
    // context.go('/home');
    // context.push('/home');
  }
  
  @override
  Widget build(BuildContext context) {
    Widget page = Scaffold(
      appBar: AppBar(
        title: Center(child: const Text('Sign In')),
      ),
      body: Column(
        // mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          const Text('Enter your Credential'),
          TextFieldSignIn(
            controller: inputUserNameController, 
            hintText: 'Username',
          ),
          TextFieldSignIn(
            controller: inputPasswordController, 
            hintText: 'Password', 
            secret: true,
          ),
          ElevatedButton.icon(
            onPressed: verifyLogin, 
            icon: const Icon(Icons.send_rounded), 
            label: const Text('Sign In'),
          ),
        ],
      ),
    );

    return page;
  }
}

class TextFieldSignIn extends StatelessWidget {
  const TextFieldSignIn({
    super.key, 
    required this.controller, 
    this.hintText = '', 
    this.secret = false,
  });

  final TextEditingController controller;
  final String hintText;
  final bool secret;

  @override
  Widget build(BuildContext context) {
    Widget input = TextField (
      controller: controller,
      obscureText: secret,
      decoration: InputDecoration(
        border: OutlineInputBorder(),
        hintText: hintText,
      ),
    );
    
    return input;
  }
}