import 'package:chatbot_mobile/config/api.dart';
import 'package:chatbot_mobile/models/agence_model.dart';
import 'package:chatbot_mobile/screens/agence_details_page.dart';
import 'package:flutter/material.dart';
import 'package:chatbot_mobile/consts/colors.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class AgencesPage extends StatefulWidget {
  const AgencesPage({super.key});

  @override
  State<AgencesPage> createState() => _AgencesPageState();
}

class _AgencesPageState extends State<AgencesPage> {
  List<AgenceModel> agences = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchAgences();
  }

  Future<void> fetchAgences() async {
    setState(() {
      isLoading = true;
    });

    try {
      final response = await http.get(Uri.parse(agencesUrl));
      if (response.statusCode == 200) {
        final List<dynamic> agencesJson = json.decode(response.body);
        setState(() {
          agences =
              agencesJson.map((json) => AgenceModel.fromJson(json)).toList();
        });
      } else {
        // Handle server error
        throw Exception('Failed to load agences');
      }
    } catch (e) {
      // Handle network error
      print('Error fetching agences: $e');
    } finally {
      setState(() {
        isLoading = false;
      });
    }
  }

  Future<void> _onRefresh() async {
    await fetchAgences();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: primaryColor,
        elevation: 10,
        title: const Text(
          "Agences",
          style: TextStyle(color: Colors.white),
        ),
        iconTheme: const IconThemeData(
          color: Colors.white, // Set desired color for icons
        ),
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : RefreshIndicator(
              onRefresh: _onRefresh,
              child: ListView.builder(
                itemCount: agences.length,
                itemBuilder: (context, index) {
                  final agence = agences[index];
                  return Card(
                    margin: const EdgeInsets.all(8.0),
                    child: ListTile(
                      leading:
                          const Icon(Icons.location_city, color: primaryColor),
                      title: Text(
                        agence.nom ?? '',
                        style: const TextStyle(color: primaryColor),
                      ),
                      subtitle: Text(agence.ville ?? ''),
                      trailing:
                          const Icon(Icons.chevron_right, color: primaryColor),
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) =>
                                AgenceDetailsPage(agence: agence),
                          ),
                        );
                      },
                    ),
                  );
                },
              ),
            ),
    );
  }
}
