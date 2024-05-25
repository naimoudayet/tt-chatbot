import 'package:chatbot_mobile/consts/colors.dart';
import 'package:chatbot_mobile/screens/espace_tt_page.dart';
import 'package:chatbot_mobile/screens/paiement_facture_page.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final ScrollController _scrollController = ScrollController();

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: primaryColor,
        elevation: 10,
        title: const Text(
          'Chatbot',
          style: TextStyle(color: Colors.white),
        ),
        iconTheme: const IconThemeData(
          color: Colors.white, // Set desired color for icons
        ),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: [
            const DrawerHeader(
              decoration: BoxDecoration(
                  image: DecorationImage(
                image: AssetImage('assets/images/splash_screen_bg.jpeg'),
                fit: BoxFit.cover,
                colorFilter: ColorFilter.mode(
                  Color.fromRGBO(0, 0, 0, 0.5), // Adjust opacity as needed
                  BlendMode.darken, // Adjust blend mode as needed
                ),
              )),
              child: Center(
                  child: Text(
                'TT Chatbot',
                style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                    fontSize: 20),
              )),
            ),
            ListTile(
              title: const Text('Chatbot'),
              onTap: () {
                // Navigate to Chatbot page
              },
            ),
            ListTile(
              title: const Text('Paiement Facture'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (context) => const PaiementFacturePage()),
                );
              },
            ),
            ListTile(
              title: const Text('Espace TT'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const EspaceTtPage()),
                );
              },
            ),
            ExpansionTile(
              title: const Text('Offres'),
              children: [
                ListTile(
                  title: const Text('Internet'),
                  onTap: () {
                    // Navigate to Internet Offers page
                  },
                ),
                ListTile(
                  title: const Text('Mobile'),
                  onTap: () {
                    // Navigate to Mobile Offers page
                  },
                ),
                ListTile(
                  title: const Text('Fixe'),
                  onTap: () {
                    // Navigate to Fixe Offers page
                  },
                ),
              ],
            ),
            const Divider(),
            ListTile(
              title: const Text('Profil'),
              onTap: () {
                // Navigate to Profil page
              },
            ),
            ListTile(
              title: const Text('Logout'),
              onTap: () {
                // Perform logout action
              },
            ),
          ],
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(8.0),
              child: ListView(
                reverse: true,
                controller: _scrollController,
                children: [
                  _buildMessageBubble(
                      'Welcome to our chat service. Feel free to ask any questions you have.'),
                  _buildMessageBubble(
                      'Hello! Let me know if there\'s anything I can help you with.'),
                  _buildUserMessageBubble('Sure, thank you!'),
                  _buildUserMessageBubble(
                      'Can you help me with my account balance?'),
                  _buildMessageBubble('Hi there! How can I assist you today?'),
                  _buildMessageBubble('Hi there! How can I assist you today?'),
                ],
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                const Expanded(
                  child: TextField(
                    decoration: InputDecoration(
                      hintText: 'Type a message...',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.send),
                  onPressed: () {
                    // Send message action
                    // Scroll to bottom after sending a message
                    _scrollController.animateTo(
                      _scrollController.position.minScrollExtent,
                      duration: const Duration(milliseconds: 300),
                      curve: Curves.easeOut,
                    );
                  },
                  color: primaryColor,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMessageBubble(String message) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 5),
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: Colors.grey[300],
        borderRadius: BorderRadius.circular(8),
      ),
      child: Text(message),
    );
  }

  Widget _buildUserMessageBubble(String message) {
    return Align(
      alignment: Alignment.centerRight,
      child: Container(
        margin: const EdgeInsets.symmetric(vertical: 5),
        padding: const EdgeInsets.all(10),
        decoration: BoxDecoration(
          color: primaryColor,
          borderRadius: BorderRadius.circular(8),
        ),
        child: Text(
          message,
          style: const TextStyle(color: Colors.white),
        ),
      ),
    );
  }
}
