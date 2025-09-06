import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';

class OverheadServePage extends StatefulWidget {
  const OverheadServePage({ Key? key }) : super(key: key);

  @override
  State<OverheadServePage> createState() => _OverheadServePageState();
}

class _OverheadServePageState extends State<OverheadServePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Forehand'
        ),
      ),
      backgroundColor: Colors.grey,
      body: Center(
        child: Column(
          children: [],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          final result = FilePicker.platform.pickFiles();

        },
        child: const Icon(Icons.add),
      ),
    );


  }
}