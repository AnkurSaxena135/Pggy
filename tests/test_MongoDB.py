import unittest

from context import MongoDB

class TestMongoDB(unittest.TestCase):

    def setUp(self):
        self.client = MongoDB('localhost', 27017)
    
    def test_client_hostname(self):
        self.assertEqual(self.client.hostname, 'localhost')
    
    def test_client_hostip(self):
        self.assertEqual(self.client.hostip, 27017)

    def test_insert_one(self):
        db = 'user'
        collection = 'data'
        data = {'Transaction': 1}
        output = self.client.insert_one(db, collection, data)
        self.assertEqual(data['_id'], output.inserted_id)

    def test_insert_many(self):
        db = 'user'
        collection = 'data'
        data = [{'Transaction': 2}, {'Transaction': 3}]
        output = self.client.insert_many(db, collection, data)
        for doc_in, doc_out in zip(data, output.inserted_ids):
            self.assertEqual(doc_in['_id'], doc_out)

    


if __name__ == "__main__":
    unittest.main()