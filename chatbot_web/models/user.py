# pour chiffrement/verification password,
from werkzeug.security import check_password_hash, generate_password_hash
# binary json
from bson.objectid import ObjectId
from datetime import datetime

from config.database import Database

COLLECTION_NAME = "users"

"""
- _id
- nom
- prenom
- telephone
- email
- password
- etat
- date_creation
- role (ADMIN, CLIENT)
"""


class User:

    @staticmethod
    def login(email, password):
        collection = Database.get_collection(COLLECTION_NAME)

        user = collection.find_one({
            "email": email
        })
        if user:
            verify = check_password_hash(user["password"], password)
            if verify:  # password is correct
                return user

        # email and/or password incorrect
        return None

    @staticmethod
    def create(nom, prenom, telephone, email, password, role, etat="ACTIVE"):
        return Database.get_collection(COLLECTION_NAME).insert_one({
            "nom": nom,
            "prenom": prenom,
            "telephone": telephone,
            "email": email,
            "password": generate_password_hash(password),
            "date_creation": datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "role": role,
            "etat": etat
        })

    @staticmethod
    def update(user_id, nom, prenom, telephone, email, etat):
        Database.get_collection(COLLECTION_NAME).find_one_and_update(
            {"_id": ObjectId(user_id)},
            {
                "$set": {
                    "nom": nom,
                    "prenom": prenom,
                    "telephone": telephone,
                    "email": email,
                    "etat": etat
                }
            }
        )

    @staticmethod
    def delete(user_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(user_id)
        })

    @staticmethod
    def read_one(user_id, role):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(user_id), "role": role
        })

    @staticmethod
    def read_all(role=None):
        domain = {}
        if role:
            domain = {"role": role}
        return list(Database.get_collection(COLLECTION_NAME).find(domain))

    @staticmethod
    def find_exist(telephone, email):
        collection = Database.get_collection(COLLECTION_NAME)
        # select * from clients where email= email or telephone= telephone
        results = list(collection.find({
            "$or": [
                {"telephone": telephone},
                {"email": email},
            ]
        }))
        if len(results) > 0:
            return True

        return False

    @staticmethod
    def drop():
        Database.get_collection(COLLECTION_NAME).drop()
