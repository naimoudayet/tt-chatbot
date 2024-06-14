from config.database import Database
from datetime import datetime
from bson.objectid import ObjectId

COLLECTION_NAME = "offres"

"""
- _id
- nom
- url
- description
- media_photo
- categorie
- sous_categorie
"""


class Offre:

    @staticmethod
    def create(nom, url, description, media_photo, categorie, sous_categorie):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            'nom': nom,
            'url': url,
            'description': description,
            'media_photo': media_photo,
            'categorie': categorie,
            'sous_categorie': sous_categorie
        })

    @staticmethod
    def update(offre_id, nom, url, description, media_photo, categorie, sous_categorie):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(offre_id)},
            {
                "$set": {
                    'nom': nom,
                    'url': url,
                    'description': description,
                    'media_photo': media_photo,
                    'categorie': categorie,
                    'sous_categorie': sous_categorie
                }
            }
        )

    @staticmethod
    def delete(offre_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(offre_id)
        })

    @staticmethod
    def read_one(offre_id, categorie):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(offre_id), "categorie": categorie
        })

    @staticmethod
    def read_all(categorie=None):
        domain = {}
        if categorie:
            domain = {"categorie": categorie}
        return list(Database.get_collection(COLLECTION_NAME).find(domain))

    @staticmethod
    def drop():
        Database.get_collection(COLLECTION_NAME).drop()

    @staticmethod
    def to_json(offre):
        if not offre:
            return {}

        return {
            "_id": str(offre['_id']),
            "nom": offre['nom'],
            "url": offre['url'],
            "description": offre['description'],
            "categorie": offre['categorie'],
            "sous_categorie": offre['sous_categorie'],
            "media_photo": offre['media_photo'],
        }
