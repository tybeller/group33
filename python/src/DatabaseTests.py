import Database
import unittest

class DatabaseTests(unittest.TestCase):

    # Insert a dog
    def test_insert_dog(self):
        database = Database.Database("database_test") #creates a test database
        (database.database)["dogs"].drop()
        database.insertDog(3, "Buster", "German Shepherd", "Male", 75, 4, "GNV", ["big", "energetic"], ["www.photo.com"])
        expected = {"_id": 3, "name": "Buster", "breed": "German Shepherd", "sex": "Male", "weight": 75, "age": 4, "location": "GNV", "attributes": ["big", "energetic"], "images": ["www.photo.com"]}
        self.assertEqual(database.getDog(3), expected)

if __name__ == '__main__':
    unittest.main()
    