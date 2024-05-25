import 'package:chatbot_mobile/consts/colors.dart';
import 'package:flutter/material.dart';

import 'package:google_maps_flutter/google_maps_flutter.dart';

class EspaceTtPage extends StatefulWidget {
  const EspaceTtPage({super.key});

  @override
  State<EspaceTtPage> createState() => _EspaceTtPageState();
}

class _EspaceTtPageState extends State<EspaceTtPage> {
  late GoogleMapController mapController;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: primaryColor,
        elevation: 10,
        title: const Text(
          "Espace TT",
          style: TextStyle(color: Colors.white),
        ),
        iconTheme: const IconThemeData(
          color: Colors.white, // Set desired color for icons
        ),
      ),
      body: GoogleMap(
        onMapCreated: (GoogleMapController controller) {
          mapController = controller;
        },
        initialCameraPosition: CameraPosition(
          target: LatLng(0, 0), // Initial location
          zoom: 10, // Zoom level
        ),
      ),
    );
  }
}
