import pymongo


class DB:

    @staticmethod
    def get_connection():
        client = pymongo.MongoClient('mongodb://localhost:27017')
        db = client['tt-chatbot']

        return db
