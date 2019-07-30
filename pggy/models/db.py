import abc
from pymongo import MongoClient


class BaseDB:
    def __init__(self):
        pass


class MongoDB(BaseDB):

    def __init__(self, hostname, port):
        self._client = MongoClient(hostname, port)

    @property
    def hostname(self):
        return self._client.address[0]
    
    @property
    def hostip(self):
        return self._client.address[1]

    def insert_one(self, db, collection, document):
        result = self._client[db][collection].insert_one(document)
        return result

    def insert_many(self, db, collection, documents):
        result = self._client.db.collection.insert_many(documents)
        return result

    
    def get_multi(self, db, collection):
        result = self._client.db.collection
        return result

if __name__ == "__main__":
    mb = MongoDB('localhost', 27017)
    print(dir(mb._client))