import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Event List',
      home: EventList(),
    );
  }
}

class EventList extends StatefulWidget {
  @override
  _EventListState createState() => _EventListState();
}

class _EventListState extends State<EventList> {
  List<Map<String, dynamic>> events = [
    {
      "name": "Order Food",
      "link": "https://codeforces.com/problemset",
      "description": "Get all your Favorite food items Here"
    },
    {
      "name": "All Orders",
      "link": "https://aditya-1.onrender.com",
      "description": "All orders to make"
    },
  ];

  void _addEvent(String name, String link, String description) {
    setState(() {
      events.add({"name": name, "link": link, "description": description});
    });
  }

  void _editEvent(int index) {
    // Implement edit logic here
    print('Edit event at index $index');
  }

  void _removeEvent(int index) {
    setState(() {
      events.removeAt(index);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Event List'),
      ),
      body: ListView.builder(
        itemCount: events.length,
        itemBuilder: (context, index) {
          return Dismissible(
            key: Key(events[index]['name']),
            direction: DismissDirection.horizontal,
            background: Container(
              color: Colors.red,
              alignment: Alignment.centerLeft,
              child: Icon(Icons.delete, color: Colors.white),
            ),
            secondaryBackground: Container(
              color: Colors.blue,
              alignment: Alignment.centerRight,
              child: Icon(Icons.edit, color: Colors.white),
            ),
            onDismissed: (direction) {
              if (direction == DismissDirection.startToEnd) {
                _removeEvent(index);
              } else if (direction == DismissDirection.endToStart) {
                _editEvent(index);
              }
            },
            child: ListTile(
              title: Text(events[index]['name']),
              subtitle: Text(events[index]['description']),
              onTap: () {
                Navigator.of(context).push(MaterialPageRoute(
                  builder: (context) => EventWebView(url: events[index]['link']),
                ));
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _showAddEventDialog(context);
        },
        child: Icon(Icons.add),
      ),
    );
  }

  void _showAddEventDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AddEventDialog(
          onAddEvent: _addEvent,
        );
      },
    );
  }
}

class AddEventDialog extends StatefulWidget {
  final Function(String, String, String) onAddEvent;

  const AddEventDialog({Key? key, required this.onAddEvent}) : super(key: key);

  @override
  _AddEventDialogState createState() => _AddEventDialogState();
}

class _AddEventDialogState extends State<AddEventDialog> {
  final TextEditingController _eventNameController = TextEditingController();
  final TextEditingController _eventDescriptionController = TextEditingController();
  final TextEditingController _eventLinkController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text('Add Event'),
      content: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          TextField(
            controller: _eventNameController,
            decoration: InputDecoration(labelText: 'Event Name'),
          ),
          TextField(
            controller: _eventDescriptionController,
            decoration: InputDecoration(labelText: 'Event Description'),
          ),
          TextField(
            controller: _eventLinkController,
            decoration: InputDecoration(labelText: 'Event Link'),
          ),
        ],
      ),
      actions: <Widget>[
        TextButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          child: Text('Cancel'),
        ),
        TextButton(
          onPressed: () {
            String eventName = _eventNameController.text.trim();
            String eventDescription = _eventDescriptionController.text.trim();
            String eventLink = _eventLinkController.text.trim();
            if (eventName.isNotEmpty && eventLink.isNotEmpty) {
              widget.onAddEvent(eventName, eventLink, eventDescription);
            }
            Navigator.of(context).pop();
          },
          child: Text('Add'),
        ),
      ],
    );
  }

  @override
  void dispose() {
    _eventNameController.dispose();
    _eventDescriptionController.dispose();
    _eventLinkController.dispose();
    super.dispose();
  }
}

class EventWebView extends StatelessWidget {
  final String url;

  const EventWebView({Key? key, required this.url}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Event Details'),
      ),
      body: WebView(
        initialUrl: url,
        javascriptMode: JavascriptMode.unrestricted,
      ),
    );
  }
}