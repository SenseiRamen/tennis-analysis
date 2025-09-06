import 'package:flutter/material.dart';
import 'package:tennis_analysis/tennis_techniques/backhand.dart';
import 'package:tennis_analysis/tennis_techniques/backhand_slice.dart';
import 'package:tennis_analysis/tennis_techniques/backhand_volley.dart';
import 'package:tennis_analysis/tennis_techniques/forehand.dart';
import 'package:tennis_analysis/tennis_techniques/forehand_slice.dart';
import 'package:tennis_analysis/tennis_techniques/forehand_volley.dart';
import 'package:tennis_analysis/tennis_techniques/overhead_serve.dart';

class UploadImage extends StatefulWidget {
  const UploadImage({ Key? key }) : super(key: key);

  @override
  State<UploadImage> createState() => _UploadImageState();
}

class _UploadImageState extends State<UploadImage> {
  final List<String> entries = <String>['Forehand', 'Backhand', 'Forehand Slice', 'Backhand Slice', 'Forehand Volley', 'Backhand Volley', 'Overhead/Serve'];
  final List<int> colorCodes = <int>[700, 600, 500, 400, 300, 200, 100];
  final List indexFunction = [ForehandPage(), BackhandPage(), ForehandSlicePage(), BackhandSlicePage(), ForehandVolleyPage(), BackhandVolleyPage(), OverheadServePage()];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Tennis Strokes to Work on'
        ),
      ),
        body: Column(
          children:[
            Flexible(
              child: ListView.separated(
                  // padding: const EdgeInsets.all(8),
                itemCount: entries.length,
                itemBuilder: (BuildContext context, int index) {
                    return ListTile(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) =>  indexFunction[index]),
                        );
                      },
                      tileColor: Colors.orange[colorCodes[index]],
                      title: Center(
                        child: Text(
                          entries[index],
                        ),
                      ),
                    );
                },
              separatorBuilder: (BuildContext context, int index) => const Divider(height:10),
                ),
            ),
          ],
        ),


    );
  }
}