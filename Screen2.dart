import 'package:flutter/material.dart';

class Screen2 extends StatelessWidget {
  final List<List<String>> data = [
    ["Name", "Table Number", "Address"],
    ["Alice", "4", "New York"],
    ["Bob", "7", "Los Angeles"],
    ["Charlie", "2", "Chicago"]
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Orders'),
      ),
      body: SingleChildScrollView(
        child: DataTable(
          columns: data.first.map((e) => DataColumn(label: Text(e))).toList(),
          rows: data.sublist(1).map((row) {
            return DataRow(
              cells: row.map((cell) => DataCell(Text(cell))).toList(),
            );
          }).toList(),
        ),
      ),
    );
  }
}
