import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:chatbot_mobile/models/agence_model.dart';
import 'package:chatbot_mobile/consts/colors.dart';

class AgenceDetailsPage extends StatelessWidget {
  final AgenceModel agence;

  const AgenceDetailsPage({Key? key, required this.agence}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          backgroundColor: primaryColor,
          elevation: 10,
          title: Text(
            agence.nom ?? '',
            style: TextStyle(color: Colors.white),
          ),
          iconTheme: const IconThemeData(
            color: Colors.white, // Set desired color for icons
          ),
          bottom: const TabBar(
            tabs: [
              Tab(text: 'Info'),
              Tab(text: 'Map'),
            ],
            labelColor: Colors.white,
          ),
        ),
        body: TabBarView(
          children: [
            _buildInfoTab(),
            _buildMapTab(),
          ],
        ),
      ),
    );
  }

  Widget _buildInfoTab() {
    return ListView(
      padding: const EdgeInsets.all(16.0),
      children: [
        Card(
          margin: const EdgeInsets.only(bottom: 16.0),
          child: ListTile(
            leading: Icon(
              Icons.business,
              color: primaryColor,
            ),
            title: Text('Nom', style: TextStyle(fontWeight: FontWeight.bold)),
            subtitle: Text(agence.nom ?? ''),
          ),
        ),
        Card(
          margin: const EdgeInsets.only(bottom: 16.0),
          child: ListTile(
            leading: Icon(
              Icons.location_on,
              color: primaryColor,
            ),
            title:
                Text('Adresse', style: TextStyle(fontWeight: FontWeight.bold)),
            subtitle: Text('${agence.adresse}, ${agence.ville}'),
          ),
        ),
        Card(
          margin: const EdgeInsets.only(bottom: 16.0),
          child: ListTile(
            leading: Icon(
              Icons.phone,
              color: primaryColor,
            ),
            title: Text('Numéro Fixe',
                style: TextStyle(fontWeight: FontWeight.bold)),
            subtitle: Text(agence.numFixe ?? ''),
          ),
        ),
        Card(
          margin: const EdgeInsets.only(bottom: 16.0),
          child: ListTile(
            leading: Icon(
              Icons.print,
              color: primaryColor,
            ),
            title: Text('Numéro Fax',
                style: TextStyle(fontWeight: FontWeight.bold)),
            subtitle: Text(agence.numFax ?? ''),
          ),
        ),
        Card(
          margin: const EdgeInsets.only(bottom: 16.0),
          child: ListTile(
            leading: Icon(
              Icons.email,
              color: primaryColor,
            ),
            title: Text('Email', style: TextStyle(fontWeight: FontWeight.bold)),
            subtitle: Text(agence.email ?? ''),
          ),
        ),
      ],
    );
  }

  Widget _buildMapTab() {
    return GoogleMap(
      initialCameraPosition: CameraPosition(
        target: LatLng(double.parse(agence.latitude ?? '0.0'),
            double.parse(agence.longitude ?? '0.0')),
        zoom: 15,
      ),
      markers: {
        Marker(
          markerId: MarkerId(agence.id ?? '0'),
          position: LatLng(double.parse(agence.latitude ?? '0.0'),
              double.parse(agence.longitude ?? '0.0')),
          infoWindow: InfoWindow(title: agence.nom),
        ),
      },
    );
  }
}
