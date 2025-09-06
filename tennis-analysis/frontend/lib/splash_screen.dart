import 'package:flutter/material.dart';
import 'package:lottie/lottie.dart';
import 'package:tennis_analysis/home_page.dart';
import 'package:tennis_analysis/main.dart';
import 'package:animated_splash_screen/animated_splash_screen.dart';

class SplashScreenTennis extends StatelessWidget {
  const SplashScreenTennis({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AnimatedSplashScreen(
      splash: Lottie.asset('assets/Lottie/tennis_splash.json'),
      nextScreen: const MyHomePage(title: 'Tennis Analysis',),
      splashIconSize: 325,
      duration: 3000,
      backgroundColor: Colors.white,
      splashTransition: SplashTransition.fadeTransition,
      animationDuration: const Duration(seconds: 1),

    );
  }
}