import 'package:chatbot_mobile/consts/colors.dart';
import 'package:flutter/material.dart';

class PaiementFacturePage extends StatefulWidget {
  const PaiementFacturePage({super.key});

  @override
  State<PaiementFacturePage> createState() => _PaiementFacturePageState();
}

class _PaiementFacturePageState extends State<PaiementFacturePage> {
  int _selectedOption = 0;
  bool _showFactureDetails = false;

  List<String> inputs = [
    "Entrer numéro de facture",
    "Entrer numéro de ligne",
    "Entrer code client"
  ];

  // Hardcoded facture details
  final factureDetails = {
    'Facture ID': '123456',
    'Etat': 'Impayé',
    'Amount': '100 TND'
  };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: primaryColor,
        elevation: 10,
        title: const Text(
          "Paiement Facture",
          style: TextStyle(color: Colors.white),
        ),
        iconTheme: const IconThemeData(
          color: Colors.white, // Set desired color for icons
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const SizedBox(height: 16),
              const Text(
                "Utiliser un des paramètres suivants",
                style: TextStyle(color: Colors.black),
              ),
              const SizedBox(height: 32),
              _buildOptionCard(Icons.receipt, 'Numéro de facture', 1),
              const SizedBox(height: 16),
              _buildOptionCard(Icons.phone, 'Numéro de ligne', 2),
              const SizedBox(height: 16),
              _buildOptionCard(Icons.person, 'Code client', 3),
              const SizedBox(height: 32),
              if (_selectedOption != 0) ...[
                Row(
                  children: [
                    Expanded(
                      child: TextField(
                        decoration: InputDecoration(
                          border: const OutlineInputBorder(),
                          hintText: inputs[_selectedOption - 1],
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Container(
                      height: 58, // same height as the TextField
                      decoration: BoxDecoration(
                        color: primaryColor,
                        borderRadius: BorderRadius.circular(8.0),
                      ),
                      child: IconButton(
                        icon: const Icon(Icons.search, color: Colors.white),
                        onPressed: () {
                          setState(() {
                            _showFactureDetails = true;
                          });
                        },
                      ),
                    ),
                  ],
                ),
              ],
              const SizedBox(height: 20),
              if (_showFactureDetails) ...[
                Card(
                  elevation: 4,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(8.0),
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(16.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Facture ID: ${factureDetails['Facture ID']}',
                          style: const TextStyle(fontSize: 16.0),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          'Etat: ${factureDetails['Etat']}',
                          style: const TextStyle(fontSize: 16.0),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          'Amount: ${factureDetails['Amount']}',
                          style: const TextStyle(fontSize: 16.0),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
              const SizedBox(height: 32),
              if (_showFactureDetails)
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                      backgroundColor: primaryColor,
                      foregroundColor: Colors.white),
                  onPressed: () {
                    // Handle pay button press
                  },
                  child: const Text('Payer'),
                ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildOptionCard(IconData icon, String optionText, int id) {
    return GestureDetector(
      onTap: () {
        setState(() {
          _selectedOption = id;
          _showFactureDetails =
              false; // Hide details when a new option is selected
        });
      },
      child: Card(
        elevation: _selectedOption == id ? 4 : 2,
        color: _selectedOption == id ? primaryColor : null,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(8.0),
        ),
        child: Padding(
          padding: const EdgeInsets.all(8),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(
                icon,
                color: _selectedOption == id ? Colors.white : Colors.black,
              ),
              const SizedBox(height: 8),
              Text(
                optionText,
                style: TextStyle(
                  fontSize: 14,
                  color: _selectedOption == id ? Colors.white : Colors.black,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
