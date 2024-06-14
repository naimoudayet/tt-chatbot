
from bson.objectid import ObjectId

from config.database import Database

COLLECTION_NAME = "sujets"

"""
- _id
- text
"""


class Sujet:

    @staticmethod
    def create(text):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            "text": text
        })

    @staticmethod
    def update(sujet_id, text):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(sujet_id)},
            {
                "$set": {
                    "text": text
                }
            }
        )

    @staticmethod
    def delete(sujet_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(sujet_id)
        })

    @staticmethod
    def read_one(sujet_id):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(sujet_id)
        })

    @staticmethod
    def read_all():
        return list(Database.get_collection(COLLECTION_NAME).find())

    @staticmethod
    def find_exist(text):
        collection = Database.get_collection(COLLECTION_NAME)
        # select * from clients where email= email or telephone= telephone
        results = list(collection.find({"text": text}))
        if len(results) > 0:
            return True

        return False

    @staticmethod
    def drop():
        Database.get_collection(COLLECTION_NAME).drop()

    @staticmethod
    def to_json(sujet):
        if not sujet:
            return {}

        return {
            "_id": str(sujet['_id']),
            "text": sujet['text']
        }
