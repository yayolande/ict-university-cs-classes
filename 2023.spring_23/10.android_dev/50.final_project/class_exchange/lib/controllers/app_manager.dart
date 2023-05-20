import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:class_exchange/models/user.dart';

class AppManager {
  AppManager();

  static AppManager getInstance() {
    AppManager? manager = instance;

    if (instance == null) {
      manager = AppManager();
    }

    return manager!;
  }

  static AppManager? instance;

  void fromLoginToHome(BuildContext context, User user) {
    context.push('/home', extra: user);
  }
}