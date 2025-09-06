import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:tennis_analysis/splash_screen.dart';
import 'package:tennis_analysis/upload_image.dart';
import 'firebase_options.dart';

void main() async{
  runApp(const MyApp());
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const SplashScreenTennis(),
      // home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}


