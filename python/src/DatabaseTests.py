import Database
import unittest

class DatabaseTests(unittest.TestCase):

    def test_insert_dog(self):
        print("Running test: Insert Dog")
        database = Database.Database("database_test") #creates a test database
        (database.database)["dogs"].drop()
        database.insertDog(3, "Buster", "German Shepherd", "Male", 75, 4, "GNV", ["big", "energetic"], ["www.photo.com"])
        expected = {"_id": 3, "name": "Buster", "breed": "German Shepherd", "sex": "Male", "weight": 75, "age": 4, "location": "GNV", "attributes": ["big", "energetic"], "images": ["www.photo.com"]}
        self.assertEqual(database.getDog(3), expected)
    
    def test_insert_existing_dog(self):
        print("Running test: Insert Existing Dog")
        database = Database.Database("database_test") #creates a test database
        (database.database)["dogs"].drop()
        database.insertDog(56, "Nova", "Lab", "Female", 65, 6, "Jax", ["small", "fast"], ["www.imgur.com", "www.twitter.com"])
        database.insertDog(56, "Nova", "Lab", "Female", 87, 9, "Lax", ["small", "slow", "lazy"], ["www.google.com"])
        expected = {"_id": 56, "name": "Nova", "breed": "Lab", "sex": "Female", "weight": 87, "age": 9, "location": "Lax", "attributes": ["small", "slow", "lazy"], "images": ["www.google.com"]}
        self.assertEqual(database.getDog(56), expected)

    def test_get_dog(self):
        print(".Running test: Get Dog")
        database = Database.Database("database_test") #creates a test database
        (database.database)["dogs"].drop()
        database.insertDog(7, "Flipper", "Lab", "Male", 70, 13, "Atlanta", ["playful", "energetic", "fast"], [])
        expected = {"_id": 7, "name": "Flipper", "breed": "Lab", "sex": "Male", "weight": 70, "age": 13, "location": "Atlanta", "attributes": ["playful", "energetic", "fast"], "images": []}
        self.assertEqual(database.getDog(7), expected)
    
    def test_insert_user(self):
        print("Running test: Insert User")
        database = Database.Database("database_test") #creates a test database
        (database.database)["users"].drop()
        database.insertUser(0, ["big", "soft", "pure breed"])
        expected = {"_id": 0, "preferences": ["big", "soft", "pure breed"]}
        result = (database.database)["users"].find_one({"_id": 0})
        self.assertEqual(result, expected)

    def test_update_user_preferences(self):
        print("Running test: Update User Preferences")
        database = Database.Database("database_test") #creates a test database
        (database.database)["users"].drop()
        database.insertUser(0, ["small", "cute"])
        database.updateUserPreferences(0, ["energetic", "playful"])
        expected = {"_id": 0, "preferences": ["energetic", "playful"]}
        result = (database.database)["users"].find_one({"_id": 0})
        self.assertEqual(result, expected)

    def test_get_user_preferences(self):
        print("Running test: Get User Preferences")
        database = Database.Database("database_test") #creates a test database
        (database.database)["users"].drop()
        database.insertUser(0, ["medium size", "poodle"])
        self.assertEqual(database.getUserPreferences(0), ["medium size", "poodle"])

    def test_insert_login(self):
        print("Running test: Insert Login")
        database = Database.Database("database_test") #creates a test database
        (database.database)["logins"].drop()
        (database.database)["users"].drop()
        success = database.insertLogin("kad", "1234")
        expected = {"_id": 0, "username": "kad", "password": "1234"}
        result = (database.database)["logins"].find_one({"_id": 0})
        self.assertEqual(expected == result and success, True) # Tests that the function successful returns the proper boolean AND checks if the tuple was successfully inserted into the database
    
    def test_get_username(self):
        print("Running test: Get Username")
        database = Database.Database("database_test") #creates a test database
        (database.database)["logins"].drop()
        (database.database)["users"].drop()
        database.insertLogin("KD", "7")
        self.assertEqual(database.getUsername(0), "KD")

    def test_insert_existing_username(self):
        print("Running test: Insert Existing Username")
        database = Database.Database("database_test") #creates a test database
        (database.database)["logins"].drop()
        (database.database)["users"].drop()
        success1 = database.insertLogin("coffeecup", "$pass")
        success2 = database.insertLogin("coffeecup", "trello")
        expected = {"_id": 0, "username": "coffeecup", "password": "$pass"}
        result = (database.database)["logins"].find_one({"_id": 0})
        self.assertEqual(expected == result and success1 and not success2, True) # Tests that the function successful returns the proper boolean AND checks if the tuple was successfully inserted into the database

    def test_update_username(self):
        print("Running test: Update Username")
        database = Database.Database("database_test") #creates a test database
        (database.database)["logins"].drop()
        (database.database)["users"].drop()
        database.insertLogin("rock", "rps") # ID = 0
        database.insertLogin("paper", "game") # ID = 1
        success1 = database.updateUsername(1, "rock") # change paper's username to rock [not allowed]
        success2 = database.updateUsername(1, "unique") # change paper's username to unique [allowed]
        self.assertEqual(not success1 and success2, True)

    def test_update_password(self):
        print("Running test: Update Password")
        database = Database.Database("database_test") #creates a test database
        (database.database)["logins"].drop()
        (database.database)["users"].drop()
        database.insertLogin("big_ben", "pencil")
        success = database.updatePassword(0, "blaze") # ID = 0 is just implicitly known here
        self.assertEqual(success, True)


if __name__ == '__main__':
    print("Running Database Tests...")
    unittest.main()
    