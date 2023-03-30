import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class ItemsUploadScreen extends StatefulWidget {


  @override
  State<ItemsUploadScreen> createState() => _ItemsUploadScreenState();
}

class _ItemsUploadScreenState extends State<ItemsUploadScreen> {

  Uint8List? imageFileUint8List;

  TextEditingController itemNameTextEditingController = TextEditingController();
  TextEditingController itemColorTextEditingController = TextEditingController();
  TextEditingController itemDescriptionTextEditingController = TextEditingController();

  bool isUploading = false;

  //upload form screen
  Widget uploadFormScreen(){
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: const Text(
          "Upload Object Image",
          style: TextStyle(
            color: Colors.white,
          ),
        ),
        centerTitle: true,
        leading: IconButton(
          onPressed: (){
            Navigator.pop(context);
          },
          icon: const Icon(
            Icons.arrow_back_outlined,
            color: Colors.white,
          ),
        ),
        actions: [
          Padding(
            padding: const EdgeInsets.all(5.0),
          ),
          IconButton(
            onPressed: (){

            },
            icon: Icon(
              Icons.cloud_upload,
            ),
          ),
        ],
      ),
      body: ListView(
        children: [

          isUploading == true
              ? const LinearProgressIndicator(color: Colors.blue,)
              : Container(),

          //image
          SizedBox(
            height: 230,
            width: MediaQuery.of(context).size.width * 0.8,
            child: Center(
              child: imageFileUint8List != null?
              Image.memory(
                imageFileUint8List!
              ) : const Icon(
                Icons.image_not_supported,
                color: Colors.grey,
                size: 50,
              )
            ),
          ),

          const Divider(
            color: Colors.grey,
            thickness: 2,
          ),
          ListTile(
            leading: const Icon(
              Icons.title,
              color: Colors.black,
            ),
            title: SizedBox(
              width: 250,
              child: TextField(
                style: const TextStyle(color: Colors.black),
                controller: itemNameTextEditingController,
                decoration: const InputDecoration(
                  hintText: "Item Name",
                  hintStyle: TextStyle(color: Colors.black),
                  border: InputBorder.none,
                ),
              )
            ),
          ),

          const Divider(
            color: Colors.grey,
            thickness: 2,
          ),
          ListTile(
            leading: const Icon(
              Icons.color_lens,
              color: Colors.black,
            ),
            title: SizedBox(
                width: 250,
                child: TextField(
                  style: const TextStyle(color: Colors.black),
                  controller: itemColorTextEditingController,
                  decoration: const InputDecoration(
                    hintText: "Item Color",
                    hintStyle: TextStyle(color: Colors.black),
                    border: InputBorder.none,
                  ),
                )
            ),
          ),
          const Divider(
            color: Colors.grey,
            thickness: 2,
          ),
          ListTile(
            leading: const Icon(
              Icons.description,
              color: Colors.black,
            ),
            title: SizedBox(
                width: 250,
                child: TextField(
                  style: const TextStyle(color: Colors.black),
                  controller: itemDescriptionTextEditingController,
                  decoration: const InputDecoration(
                    hintText: "Item Description",
                    hintStyle: TextStyle(color: Colors.black),
                    border: InputBorder.none,
                  ),
                )
            ),
          ),
          const Divider(
            color: Colors.grey,
            thickness: 2,
          ),

        ],
      )
    );
  }

  //default screen
  Widget defaultScreen(){
    return Scaffold(
      backgroundColor: Colors.grey,

      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: const Text(
          "Upload new image",
          style: TextStyle(
            color: Colors.white,
          ),
        ),
        centerTitle: true,
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(
              Icons.add_photo_alternate,
              color: Colors.white,
              size: 200,
            ),
            
            ElevatedButton(
              onPressed: (){
                showDialogBox();

              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue,
              ),
              child: Text(
                "Add new image",
                style: TextStyle(
                  color: Colors.white,

                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  showDialogBox(){
    return showDialog(
      context: context,
      builder: (c) {
        return SimpleDialog(
          backgroundColor: Colors.white,
          title: const Text(
            "Object image",
            style: TextStyle(
              color: Colors.black,
              fontWeight: FontWeight.bold,
            ),
          ),
          children: [
            SimpleDialogOption(
              onPressed: (){
                cameraCapture();
              },
              child: const Text(
                "Capture Object with Camera",
                style: TextStyle(
                  color: Colors.black,
                ),
              ),
            ),

            SimpleDialogOption(
              onPressed: (){
                gallerySelect();
              },
              child: const Text(
                "Choose Image from Gallery",
                style: TextStyle(
                  color: Colors.black,
                ),
              ),
            ),

            SimpleDialogOption(
              onPressed: (){
                Navigator.pop(context);
              },
              child: const Text(
                "Cancel",
                style: TextStyle(
                  color: Colors.black,
                ),
              ),
            ),
          ],
        );
      }
    );
  }

  cameraCapture() async {
    try{
      Navigator.pop(context);

      final pickedImage = await ImagePicker().pickImage(source: ImageSource.camera);

      if(pickedImage != null){
        String imagePath = pickedImage.path;
        imageFileUint8List = await pickedImage.readAsBytes();

        setState(() {
          imageFileUint8List;
        });
      }
    }
    catch(error){
      print(error.toString());

      setState(() {
        imageFileUint8List = null;
      });
    }
  }

  gallerySelect() async {
    try{
      Navigator.pop(context);

      final pickedImage = await ImagePicker().pickImage(source: ImageSource.gallery);

      if(pickedImage != null){
        String imagePath = pickedImage.path;
        imageFileUint8List = await pickedImage.readAsBytes();

        setState(() {
          imageFileUint8List;
        });
      }
    }
    catch(error){
      print(error.toString());

      setState(() {
        imageFileUint8List = null;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return imageFileUint8List == null ? defaultScreen() : uploadFormScreen();
  }
}
