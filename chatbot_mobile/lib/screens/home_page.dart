import 'package:chatbot_mobile/consts/colors.dart';
import 'package:chatbot_mobile/screens/agences_page.dart';
import 'package:chatbot_mobile/screens/offres_page.dart';
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
              title: const Text('Agences'),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => const AgencesPage()),
                );
              },
            ),
            ExpansionTile(
              title: const Text('Offres'),
              children: [
                ListTile(
                  title: const Text('Internet'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              const OffrePage(categorie: 'INTERNET')),
                    );
                  },
                ),
                ListTile(
                  title: const Text('Mobile'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              const OffrePage(categorie: 'MOBILE')),
                    );
                  },
                ),
                ListTile(
                  title: const Text('Fixe'),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) =>
                              const OffrePage(categorie: 'FIXE')),
                    );
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
                      'Bienvenue à notre service de chat. N\'hésitez pas à poser toutes vos questions.'),
                  _buildMessageBubble(
                      'Bonjour! Faites-moi savoir si je peux vous aider avec quelque chose.'),
                  _buildUserMessageBubble('Bien sûr, merci!'),
                  _buildUserMessageBubble(
                      'Pouvez-vous m\'aider avec le solde de mon compte?'),
                  _buildMessageBubble(
                      'Bonjour! Comment puis-je vous aider aujourd\'hui?'),
                  _buildMessageBubble(
                      'Bien sûr! Votre solde actuel est de 50 TND.'),
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
