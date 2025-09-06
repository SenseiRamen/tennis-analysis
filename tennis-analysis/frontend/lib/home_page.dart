import 'package:flutter/material.dart';
import 'package:tennis_analysis/upload_image.dart';


class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          children: [
            Container(
            height: 300,
            width: 300,
            color: Colors.red,
            child: FittedBox(
              fit: BoxFit.fitHeight,
              child: Image.network(
                  'https://photoresources.wtatennis.com/photo-resources/2019/08/15/dbb59626-9254-4426-915e-57397b6d6635/tennis-origins-e1444901660593.jpg?width=1200&height=630'),
            ),
          ),
            SizedBox(height: 50,),
            const Text(
                "Tennis Analysis",
              style: TextStyle(fontSize: 25),
            ),
            SizedBox(height: 50,),
            ElevatedButton(
              onPressed: () {
              Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const UploadImage())
              );
            },
              child: const Text(
                'Analyze Videos'
              ),
            )
          ],
        ),
      ),
      // floatingActionButton: FloatingActionButton(
      //   onPressed: () {
      //     Navigator.push(
      //         context,
      //         MaterialPageRoute(builder: (context) => const UploadImage())
      //     );
      //   },
      //   child: const Icon(Icons.add),
      // ),
    );
  }
}