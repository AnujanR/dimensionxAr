import 'package:firebase_core/firebase_core.dart';
import 'package:first_flutter_official/home_screen.dart';
import 'package:first_flutter_official/splash.dart';
import 'package:flutter/material.dart';

Future<void> main() async {
  try{
    WidgetsFlutterBinding.ensureInitialized();
    await Firebase.initializeApp();
  }
  catch(error){
    print("ERROR: " + error.toString());
  }

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AR App',
      theme: ThemeData(

        primarySwatch: Colors.blue,
      ),
      debugShowCheckedModeBanner: false,
      home: const Splash(),
    );
  }
}


