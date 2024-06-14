/**
 - id
- nom
- prenom
- telephone
- email
- password
- etat
- date_creation
- role (ADMIN, CLIENT)
 */
class UserModel {
  final String? id;
  final String? nom;
  final String? prenom;
  final String? telephone;
  final String? email;
  final String? password;
  final String? dateCreation;
  final String? role;
  final String? etat;

  const UserModel(
      {this.id,
      this.nom,
      this.prenom,
      this.telephone,
      this.email,
      this.password,
      this.dateCreation,
      this.role,
      this.etat});

  factory UserModel.fromJson(Map<String, dynamic> json) => UserModel(
        id: json['_id'],
        nom: json['nom'],
        prenom: json['prenom'],
        telephone: json['telephone'],
        email: json['email'],
        password: json['password'],
        dateCreation: json['date_creation'],
        role: json['role'],
        etat: json['etat'],
      );
}
