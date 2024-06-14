/**
- _id
- nom
- url
- description
- media_photo
- categorie
- sous_categorie
 */
class OffreModel {
  final String? id;
  final String? nom;
  final String? url;
  final String? description;
  final String? mediaPhoto;
  final String? categorie;
  final String? sousCategorie;

  const OffreModel(
      {this.id,
      this.nom,
      this.url,
      this.description,
      this.mediaPhoto,
      this.categorie,
      this.sousCategorie});

  factory OffreModel.fromJson(Map<String, dynamic> json) => OffreModel(
      id: json['_id'],
      nom: json['nom'],
      url: json['url'],
      description: json['description'],
      mediaPhoto: json['media_photo'],
      categorie: json['categorie'],
      sousCategorie: json['sous_categorie']);
}
