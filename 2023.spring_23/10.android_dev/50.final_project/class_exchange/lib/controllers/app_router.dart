import 'package:class_exchange/models/user.dart';
import 'package:class_exchange/views/login_page.dart';
import 'package:go_router/go_router.dart';
import 'package:class_exchange/views/my_home_page.dart';
import 'package:class_exchange/views/home_page.dart';

class RouterApp {
  late GoRouter _router;

  RouterApp() {
    _router = GoRouter(
      initialLocation: RouterPath.login,
      // initialLocation: RouterPath.home,
      // errorBuilder:(context, state) => ErrorPage(),
      routes: [
        GoRoute(
          name: "test",
          path: RouterPath.test,
          builder: (context, state) => const MyHomePage(title: 'Flutter App')
        ),
        GoRoute(
          path: RouterPath.home,
          builder: (context, state) {
            User? user = state.extra as User?;
            // TODO: how to send 'user' to 'homepage' ?
            var homePage = HomePage();
            
            return homePage;
          }
        ),
        GoRoute(
          path: RouterPath.login,
          builder: (context, state) => LoginPage()
        ),
      ],
    );
  }

  GoRouter get router => _router;
}

class RouterPath {
  static String home = '/home';
  static String login = '/login';
  static String register = '/register';
  static String test = '/test';
}
