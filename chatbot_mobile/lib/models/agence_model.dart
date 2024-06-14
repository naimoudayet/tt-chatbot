/**
- id
- nom
- adresse
- ville
- num_fixe
- num_fax
- email
- latitude
- longitude
 */
class AgenceModel {
  final String? id;
  final String? nom;
  final String? adresse;
  final String? ville;
  final String? numFixe;
  final String? numFax;
  final String? email;
  final String? latitude;
  final String? longitude;

  const AgenceModel(
      {this.id,
      this.nom,
      this.adresse,
      this.ville,
      this.numFixe,
      this.numFax,
      this.email,
      this.latitude,
      this.longitude});

  factory AgenceModel.fromJson(Map<String, dynamic> json) => AgenceModel(
        id: json['_id'],
        nom: json['nom'],
        adresse: json['adresse'],
        ville: json['ville'],
        numFixe: json['num_fixe'],
        numFax: json['num_fax'],
        email: json['email'],
        latitude: json['latitude'].toString(),
        longitude: json['longitude'].toString(),
      );
}
