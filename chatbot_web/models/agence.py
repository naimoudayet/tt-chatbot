# binary json
from bson.objectid import ObjectId
from datetime import datetime

from config.database import Database

COLLECTION_NAME = "agences"

"""
- _id
- nom
- adresse
- ville
- num_fixe
- num_fax
- email
- latitude
- longitude
"""


class Agence:

    @staticmethod
    def create(nom, adresse, ville, num_fixe, num_fax, email, latitude, longitude):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            'nom': nom,
            'adresse': adresse,
            'ville': ville,
            'num_fixe': num_fixe,
            'num_fax': num_fax,
            'email': email,
            'latitude': latitude,
            'longitude': longitude
        })

    @staticmethod
    def update(agence_id, nom, adresse, ville, num_fixe, num_fax, email, latitude, longitude):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(agence_id)},
            {
                "$set": {
                    'nom': nom,
                    'adresse': adresse,
                    'ville': ville,
                    'num_fixe': num_fixe,
                    'num_fax': num_fax,
                    'email': email,
                    'latitude': latitude,
                    'longitude': longitude
                }
            }
        )

    @staticmethod
    def delete(agence_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(agence_id)
        })

    @staticmethod
    def read_one(agence_id):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(agence_id)
        })

    @staticmethod
    def read_all():
        return list(Database.get_collection(COLLECTION_NAME).find())

    @staticmethod
    def find_exist(num_fixe, num_fax, email):
        collection = Database.get_collection(COLLECTION_NAME)
        results = list(collection.find({
            "$or": [
                {"num_fixe": num_fixe},
                {"num_fax": num_fax},
                {"email": email},
            ]
        }))
        if len(results) > 0:
            return True

        return False

    @staticmethod
    def drop():
        Database.get_collection(COLLECTION_NAME).drop()

    @staticmethod
    def to_json(agence):
        if not agence:
            return {}

        return {
            "_id": str(agence['_id']),
            "nom": agence['nom'],
            "adresse": agence['adresse'],
            "ville": agence['ville'],
            "num_fixe": agence['num_fixe'],
            "num_fax": agence['num_fax'],
            "email": agence['email'],
            "latitude": float(agence['latitude']) if agence['latitude'] else 0,
            "longitude": float(agence['longitude']) if agence['longitude'] else 0,
        }
