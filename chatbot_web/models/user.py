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
    def update_password(user_id, ancien_passe, nouveau_passe, role):
        updated = False
        user = User.read_one(user_id, role)
        if user:
            if check_password_hash(user['password'], ancien_passe):
                Database.get_collection(COLLECTION_NAME).find_one_and_update(
                    {"_id": ObjectId(user_id)},
                    {"$set": {
                        "password":  generate_password_hash(nouveau_passe)
                    }
                    }
                )
                updated = True

        return updated

    @staticmethod
    def delete(user_id):
        Database.get_collection(COLLECTION_NAME).find_one_and_delete({
            "_id": ObjectId(user_id)
        })

    @staticmethod
    def read_one(user_id, role='CLIENT'):
        return Database.get_collection(COLLECTION_NAME).find_one({
            "_id": ObjectId(user_id), "role": role
        })

    @staticmethod
    def read_all(role='CLIENT'):
        return list(Database.get_collection(COLLECTION_NAME).find({"role": role}))

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

    @staticmethod
    def to_json(user):
        if not user:
            return {}

        return {
            "_id": str(user['_id']),
            "nom": user['nom'],
            "prenom": user['prenom'],
            "telephone": user['telephone'],
            "email": user['email'],
            "etat": user['etat'],
            "date_creation": user['date_creation']
        }
