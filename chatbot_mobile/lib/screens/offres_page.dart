import 'dart:convert';
import 'package:chatbot_mobile/config/api.dart';
import 'package:chatbot_mobile/screens/offre_details_page.dart';
import 'package:flutter/material.dart';
import 'package:toast/toast.dart';
import 'package:http/http.dart' as http;
import 'package:chatbot_mobile/consts/colors.dart';
import 'package:chatbot_mobile/models/offre_model.dart';

class OffrePage extends StatefulWidget {
  final String categorie;

  const OffrePage({super.key, required this.categorie});

  @override
  State<OffrePage> createState() => _OffrePageState();
}

class _OffrePageState extends State<OffrePage> {
  List<OffreModel> offers = [];
  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    fetchOffers();
  }

  Future<void> fetchOffers() async {
    try {
      final response =
          await http.get(Uri.parse('$offresUrl/${widget.categorie}'));
      if (response.statusCode == 200) {
        final List<dynamic> offersJson = json.decode(response.body);
        setState(() {
          offers = offersJson.map((json) => OffreModel.fromJson(json)).toList();
          isLoading = false;
        });
      } else {
        setState(() {
          isLoading = false;
        });
        Toast.show('Failed to load offers',
            duration: Toast.lengthShort, gravity: Toast.bottom);
      }
    } catch (e) {
      setState(() {
        isLoading = false;
      });
      Toast.show('Failed to load offers',
          duration: Toast.lengthShort, gravity: Toast.bottom);
    }
  }

  @override
  Widget build(BuildContext context) {
    ToastContext().init(context);

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 5,
        backgroundColor: primaryColor,
        iconTheme: const IconThemeData(
          color: Colors.white,
        ),
        title: Text(
          'Offres ${widget.categorie.toLowerCase()}',
          style: const TextStyle(color: Colors.white),
        ),
      ),
      body: isLoading
          ? const Center(child: CircularProgressIndicator())
          : buildOffers(offers),
    );
  }

  Widget buildOffers(List<OffreModel> offers) {
    return ListView.builder(
      itemCount: offers.length,
      itemBuilder: (context, index) {
        final offer = offers[index];

        return Card(
          child: InkWell(
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => OffreDetailsPage(offer: offer),
                ),
              );
            },
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(
                  width: double.infinity,
                  height: 200.0,
                  child: ClipRRect(
                    borderRadius:
                        const BorderRadius.vertical(top: Radius.circular(8.0)),
                    child: Image.network(
                      'https://via.placeholder.com/200',
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text(
                    offer.nom ?? '',
                    style: const TextStyle(
                      fontSize: 20.0,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                if (offer.sousCategorie != null)
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 8.0),
                    child: Container(
                      decoration: BoxDecoration(
                        color: primaryColor,
                        borderRadius: BorderRadius.circular(8.0),
                      ),
                      padding: const EdgeInsets.symmetric(
                          vertical: 4.0, horizontal: 8.0),
                      child: Text(
                        offer.sousCategorie!,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 14.0,
                        ),
                      ),
                    ),
                  ),
                Padding(
                  padding: const EdgeInsets.symmetric(
                      horizontal: 8.0, vertical: 4.0),
                  child: Text(
                    offer.description ?? '',
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(fontSize: 16.0),
                  ),
                ),
                const SizedBox(height: 8.0),
              ],
            ),
          ),
        );
      },
    );
  }
}
