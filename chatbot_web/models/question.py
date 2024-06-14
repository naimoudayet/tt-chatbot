
from bson.objectid import ObjectId

from config.database import Database

COLLECTION_NAME = "questions"

"""
- _id
- text
"""


class Question:

    @staticmethod
    def create(sujet_id, text):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            "sujet_id": sujet_id,
            "text": text
        })

    @staticmethod
    def update(question_id, text):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(question_id)},
            {
                "$set": {
                    "text": text
                }
            }
        )

    @staticmethod
    def delete(question_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(question_id)
        })

    @staticmethod
    def read_one(question_id):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(question_id)
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
    def to_json(question):
        if not question:
            return {}

        return {
            "_id": str(question['_id']),
            "text": question['text']
        }
