from pymongo import MongoClient


class Database:

    @staticmethod
    def get_collection(name):
        collection = None  # null
        try:
            client = MongoClient("mongodb://localhost:27017")
            db = client["tt-chatbot"]
            collection = db[name]
        except Exception as error:
            print("Error: %s" % error)

        return collection