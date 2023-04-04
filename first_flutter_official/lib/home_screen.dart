import 'package:first_flutter_official/upload_screen.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          "AR App",
          style: TextStyle(
            fontSize: 17,
            letterSpacing: 2,
          fontWeight: FontWeight.bold,
        ),
        ),
        actions: [
          IconButton(
              onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (c)=> ItemsUploadScreen()));
            
          },
          icon: const Icon(
            Icons.camera_enhance_rounded,
            color: Colors.white,
          )
          )
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Container(

        decoration: const BoxDecoration(
        image: DecorationImage(
        image: AssetImage("images/dimensionxbackground.png"),
        ),
            ),
          ),
      ),
      backgroundColor: Colors.blueGrey,
    );
  }
}
