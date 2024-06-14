
from bson.objectid import ObjectId

from config.database import Database

COLLECTION_NAME = "reponses"

"""
- _id
- text
"""


class Reponse:

    @staticmethod
    def create(sujet_id, text):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            "sujet_id": sujet_id,
            "text": text
        })

    @staticmethod
    def update(reponse_id, text):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(reponse_id)},
            {
                "$set": {
                    "text": text
                }
            }
        )

    @staticmethod
    def delete(reponse_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(reponse_id)
        })

    @staticmethod
    def read_one(reponse_id):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(reponse_id)
        })

    @staticmethod
    def read_all(sujet_id=None):
        domain = {}
        if sujet_id:
            domain = {"sujet_id": sujet_id}
        return list(Database.get_collection(COLLECTION_NAME).find(domain))

    @staticmethod
    def find_exist(text):
        collection = Database.get_collection(COLLECTION_NAME)
        results = list(collection.find({"text": text}))
        if len(results) > 0:
            return True

        return False

    @staticmethod
    def drop():
        Database.get_collection(COLLECTION_NAME).drop()

    @staticmethod
    def to_json(reponse):
        if not reponse:
            return {}

        return {
            "_id": str(reponse['_id']),
            "text": reponse['text']
        }
