import json
import pymongo

class Database:
    

    def connect(self):
        file = open("../../config.json")
        config = json.load(file)
        self.client = pymongo.MongoClient(config["MongoDB"]["connection_string"]) 

    # Checks if the database exists, if not, create the database.
    def initializeDatabase(self):
        dbList = self.client.list_database_names()
        if "furever" not in dbList:
            self.database = self.client[self.name]
            print("debug")
        

    # Checks if the necessary tables exist, if not, create the tables.
    def initializeTables(self, tables): # tables is a list of tables
        tableList = self.database.list_collection_names()
        for x in tables:
            if x not in tableList:
                self.database[x]
                self.database[x].insert_one({"_id": -1})

    def updateDog(self, id, name, breed, sex, weight, age, location, attributes, images):
        query = {"_id": id}
        newvalues = {"$set": {"name": name, "breed": breed, "sex": sex, "weight": weight, "age": age, "location": location, "attributes": attributes, "images": images}}
        table = self.database["dogs"]
        table.update_one(query, newvalues)
        # return boolean indicated whether successful update took place?

    def insertDog(self, id, name, breed, sex, weight, age, location, attributes, images):
        # Check to see if the dog already exists in the database
        query = {"_id": id}
        table = self.database["dogs"]
        result = table.find(query)
        #if result is not None: # Dog already exists in table
        #    return self.updateDog(id, name, breed, sex, weight, age, location, attributes, images) # update the existing dog's info instead
        
        dog = {"_id": id, "name": name, "breed": breed, "sex": sex, "weight": weight, "age": age, "location": location, "attributes": attributes, "images": images}
        table.insert_one(dog)

    def getDog(self, id):
        query = {"_id": id}
        table = self.database["dogs"]
        return table.find_one(query)

    def printDog(self, id):
        query = {"_id": id}
        table = self.database["dogs"]
        result = table.find(query)
    
        print("Result:")
        for x in result:
            print(x)

    # Insert user and their preferences
    def insertUser(self, id, preferences):
        table = self.database["users"]
        newUser = {"_id": 0, "preferences": preferences}
        table.insert_one(newUser)

    # Update a user's preferences
    def updateUser(self, id, preferences):
        query = {"_id": id}
        newvalues = {"$set": {"preferences": preferences}}
        table = self.database["users"]
        table.update_one(query, newvalues)

    # Called when a user makes a new account
    def insertLogin(self, id, username, password):
        query = {"username": username}
        table = self.database["logins"]
        result = table.find(query)

        if result is not None:
            return false # make user choose another username
        
        # Else proceed with inserting the new login
        if table.find() is None: # No users exist in the database
            newLogin = {"_id": 0, "username": username, "password": password}
            table.insert_one(newLogin)
        else:
            # TODO: check logic and syntax
            table = table.find().sort("_id") # sort IDs in ascending order
            lastUser = table[-1]
            lastID = lastUser["_id"]
            newUser = {"_id": (lastID + 1), "username": username, "password" : password}
        return true

    def __init__(self, name):
        self.name = name
        self.connect()
        self.initializeDatabase()
        self.initializeTables({"dogs", "users", "login"})