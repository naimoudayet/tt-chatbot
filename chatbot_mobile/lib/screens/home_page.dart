import 'package:chatbot_mobile/consts/colors.dart';
import 'package:chatbot_mobile/screens/agences_page.dart';
import 'package:chatbot_mobile/screens/offres_page.dart';
import 'package:chatbot_mobile/screens/paiement_facture_page.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;

  final List<String> _titles = [
    'Accueil',
    'Offres',
    'Chatbot',
    'Factures',
    'Agences'
  ];

  void _onItemTapped(int index) {
    if (index == 4) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const AgencesPage()),
      );
    } else if (index == 3) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => const PaiementFacturePage()),
      );
    } else {
      setState(() {
        _selectedIndex = index;
      });
    }
  }

  void _onCardTapped(String cardName) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => OffrePage(categorie: cardName)),
    );
  }

  Widget _buildCards() {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        children: [
          GestureDetector(
            onTap: () => _onCardTapped('MOBILE'),
            child: const Card(
              child: ListTile(
                leading: Icon(Icons.phone_android),
                title: Text('Mobile'),
              ),
            ),
          ),
          GestureDetector(
            onTap: () => _onCardTapped('INTERNET'),
            child: const Card(
              child: ListTile(
                leading: Icon(Icons.wifi),
                title: Text('Internet'),
              ),
            ),
          ),
          GestureDetector(
            onTap: () => _onCardTapped('FIXE'),
            child: const Card(
              child: ListTile(
                leading: Icon(Icons.phone),
                title: Text('Fixe'),
              ),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: primaryColor,
        elevation: 10,
        title: Text(
          _titles[_selectedIndex],
          style: const TextStyle(color: Colors.white),
        ),
        iconTheme: const IconThemeData(
          color: Colors.white, // Set desired color for icons
        ),
        actions: [
          IconButton(
            icon: const Icon(Icons.person),
            onPressed: () {
              //   Navigator.push(
              //     context,
              //     MaterialPageRoute(builder: (context) => const Pro()),
              //   );
            },
          ),
        ],
      ),
      body: Center(
        child: _selectedIndex == 1
            ? _buildCards()
            : Text('Selected option: $_selectedIndex'),
      ),
      bottomNavigationBar: BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Accueil',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.local_offer),
            label: 'Offres',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.wechat, size: 60), // Make this icon larger
            label: 'Chatbot',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.payment),
            label: 'Factures',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.location_on),
            label: 'Agences',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: primaryColor,
        onTap: _onItemTapped,
      ),
    );
  }
}
