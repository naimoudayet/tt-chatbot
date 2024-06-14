from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from models.user import User
from models.agence import Agence
from models.offre import Offre

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route("/api/agences")
def api_agences():
    records = Agence.read_all()

    agences = []
    for record in records:
        agences.append(Agence.to_json(record))

    return agences

@api_blueprint.route("/api/offres/<categorie>")
def api_offres(categorie):
    records = Offre.read_all(categorie=categorie)

    offres = []
    for record in records:
        offres.append(Offre.to_json(record))

    return offres


@api_blueprint.route("/api/login", methods=["POST"])
def api_login():
    # get data
    # email and password comes from body request
    email = request.json["email"]
    password = request.json["password"]
    # call login function
    user = User.login(email, password)
    if user and user["role"] != "ADMIN":  # if email and password is correct
        return jsonify({
            "success": True,
            "user": {
                "_id": str(user["_id"]),
                "role": user["role"]
            }
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "svp, vérifier votre email et mot de passe"
        }), 401


@api_blueprint.route("/api/inscription", methods=["POST"])
def api_inscription():

    nom = request.json["nom"]
    prenom = request.json["prenom"]
    telephone = request.json["telephone"]
    email = request.json["email"]
    password = request.json["password"]
    role = request.json["role"]

    if (User.find_exist(telephone, email)):
        return jsonify({"message": "Avez vous déjà un compte."}), 409
    else:
        user = User.create(
            nom, prenom, telephone, email, password, role.upper(), etat="ACTIVE"
        )
        if user.inserted_id:
            return jsonify({
                "success": True,
                "message": "Compte créé avec succès",
                "user": {
                    "_id": str(user.inserted_id),
                    "role": role
                }
            }), 200

    return jsonify({"message": "something went wrong"}), 500


@api_blueprint.route("/api/profile/<user_id>/<role>")
def api_profile(user_id, role):
    user = User.read_one(user_id=user_id, role=role)
    if user:
        return jsonify({
            '_id': str(user['_id']),
            'nom': user['nom'],
            'prenom': user['prenom'],
            'telephone': user['telephone'],
            'email': user['email'],
            'date_creation': user['date_creation'],
            'role': user['role'],
            'etat': user['etat'],
        }), 200

    return jsonify({'message': 'user not found'}), 404
