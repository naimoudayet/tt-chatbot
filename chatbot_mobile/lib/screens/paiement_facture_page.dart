import 'package:chatbot_mobile/consts/colors.dart';
import 'package:flutter/material.dart';

class PaiementFacturePage extends StatefulWidget {
  const PaiementFacturePage({super.key});

  @override
  State<PaiementFacturePage> createState() => _PaiementFacturePageState();
}

class _PaiementFacturePageState extends State<PaiementFacturePage> {
  int _selectedOption = 0;

  List<String> inputs = [
    "Entrer numéro de facture",
    "Entrer numéro de ligne",
    "Entrer code client"
  ];

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
                        "Utilizer un des paramètres suivants",
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
                        Text(
                          inputs[_selectedOption - 1],
                          style: const TextStyle(
                            fontSize: 18,
                          ),
                        ),
                        const SizedBox(height: 10),
                        TextField(
                          decoration: InputDecoration(
                            border: const OutlineInputBorder(),
                            hintText: inputs[_selectedOption - 1],
                          ),
                        ),
                      ],
                    ]))));
  }

  Widget _buildOptionCard(IconData icon, String optionText, int id) {
    return GestureDetector(
      onTap: () {
        setState(() {
          _selectedOption = id;
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
              Icon(icon,
                  color: _selectedOption == id ? Colors.white : Colors.black),
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
