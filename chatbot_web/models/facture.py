from config.database import Database
from datetime import datetime
from bson.objectid import ObjectId

COLLECTION_NAME = "factures"

"""
- _id
- telephone
- montant
- etat
- date_paiement
- date_facture
"""


class Facture:

    @staticmethod
    def create(telephone, montant, date_paiement, date_facture):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            'telephone': telephone,
            'montant': montant,
            'etat': "EN ATTENTE",
            'date_paiement': date_paiement,
            'date_facture': date_facture
        })

    @staticmethod
    def update(facture_id, telephone, montant, etat, date_paiement, date_facture):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(facture_id)},
            {
                "$set": {
                    'telephone': telephone,
                    'montant': montant,
                    'etat': etat,
                    'date_paiement': date_paiement,
                    'date_facture': date_facture
                }
            }
        )

    @staticmethod
    def delete(facture_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(facture_id)
        })

    @staticmethod
    def read_one(facture_id):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(facture_id)
        })

    @staticmethod
    def read_all(telephone=None):
        domain = {}
        if telephone:
            domain = {"telephone": telephone}
        return list(Database.get_collection(COLLECTION_NAME).find(domain))

    @staticmethod
    def drop():
        Database.get_collection(COLLECTION_NAME).drop()

    @staticmethod
    def to_json(facture):
        if not facture:
            return {}

        return {
            "_id": str(facture['_id']),
            "telephone": facture['telephone'],
            "montant": facture['montant'],
            "etat": facture['etat'],
            "date_paiement": facture['date_paiement'],
            "date_facture": facture['date_facture'],
        }
