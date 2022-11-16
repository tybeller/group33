import json
import pymongo

class Database:
    

    def connect(self):
        file = open("config.json")
        config = json.load(file)
        self.client = pymongo.MongoClient(config["MongoDB"]["connection_string"]) 
        file.close()

    # Checks if the database exists, if not, create the database.
    def initializeDatabase(self):
        self.database = self.client[self.name]

    # Checks if the necessary tables exist, if not, create the tables.
    def initializeTables(self, tables): # tables is a list of tables
        tableList = self.database.list_collection_names()
        for x in tables:
            if x not in tableList:
                self.database[x]
                self.database[x].insert_one({"_id": -1})

    def updateDog(self, id, name, breed, sex, weight, age, location, attributes, images, description):
        query = {"_id": id}
        newvalues = {"$set": {"name": name, "breed": breed, "sex": sex, "weight": weight, "age": age, "location": location, "attributes": attributes, "images": images, "description": description}}
        table = self.database["dogs"]
        table.update_one(query, newvalues)
        # return boolean indicated whether successful update took place?

    def insertDog(self, id, name, breed, sex, weight, age, location, attributes, images, description):
        # Check to see if the dog already exists in the database
        query = {"_id": id}
        table = self.database["dogs"]
        result = table.find_one(query)
        if result is None: # Dog does not exist in table already
            dog = {"_id": id, "name": name, "breed": breed, "sex": sex, "weight": weight, "age": age, "location": location, "attributes": attributes, "images": images, "description": description}
            table.insert_one(dog)
        else: #Dog already exists in table
            return self.updateDog(id, name, breed, sex, weight, age, location, attributes, images, description) # update the existing dog's info instead
        
    def getDog(self, id):
        query = {"_id": id}
        table = self.database["dogs"]
        return table.find_one(query)

    # Debug function
    def printDog(self, id):
        query = {"_id": id}
        table = self.database["dogs"]
        result = table.find(query)
    
        print("Result:")
        for x in result:
            print(x)

    # Insert user and their preferences, this function SHOULD NOT be called outside of this class (aka private function/method)
    def insertUser(self, id, preferences):
        table = self.database["users"]
        if table.find_one({"_id": id}) is None:
            newUser = {"_id": id, "preferences": preferences}
            table.insert_one(newUser)
            return True
        else:
            return False # user already exists

    # Update a user's preferences
    def updateUserPreferences(self, id, preferences):
        query = {"_id": id}
        newvalues = {"$set": {"preferences": preferences}}
        table = self.database["users"]
        table.update_one(query, newvalues)

    def getUserPreferences(self, id):
        query = {"_id": id}
        table = self.database["users"]
        return table.find_one(query)["preferences"]

    # Called when a user makes a new account
    def insertLogin(self, username, password):
        query = {"username": username} # username must be unique!
        table = self.database["logins"]
        result = table.find_one(query)
        if result is None: #username is indeed unique
            if table.find() is None: # No users exist in the database
                newLogin = {"_id": 0, "username": username, "password": password}
                table.insert_one(newLogin)
                self.insertUser(0, []) # AUTOMATICALLY INSERTS INTO USERS TABLE
            else:
                result = table.find().sort("_id") # sort IDs in ascending order
                lastID = -1
                for x in result: # TODO: find a O(1) way of doing this LOL
                    lastID = x["_id"]
                newLogin = {"_id": (lastID + 1), "username": username, "password" : password}
                table.insert_one(newLogin)
                self.insertUser((lastID + 1), []) # AUTOMATICALLY INSERTS INTO USERS TABLE
            self.insertUser
            return True
        else:
            return False # Make user choose another username

    def getUsername(self, id):
        query = {"_id": id}
        table = self.database["logins"]
        return table.find_one(query)["username"]
        
    def updateUsername(self, id, newUsername):
        query = {"username": newUsername}
        table = self.database["logins"]
        result = table.find_one(query)
        if result is None: # proceed with updating the username
            newValue = {"$set": {"username": newUsername}}
            table.update_one({"_id": id}, newValue)
            return table.find_one({"_id": id})["username"] == newUsername
        else:
            return False

    def updatePassword(self, id, newPassword):
        query = {"_id": id}
        newvalues = {"$set": {"password": newPassword}}
        table = self.database["logins"]
        table.update_one(query, newvalues)
        return table.find_one(query)["password"] == newPassword # returns whether or not the password successfully updated

    def __init__(self, name):
        self.name = name
        self.connect()
        self.initializeDatabase()
        self.initializeTables({"dogs", "users", "login"})