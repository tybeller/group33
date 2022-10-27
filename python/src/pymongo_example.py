import pymongo
import json

file = open("../../config.json") # Make sure to set the connection string in config.json!
config = json.load(file)
client = pymongo.MongoClient(config["MongoDB"]["connection_string"]) # logins to the database using credentials
database = client["pymongo_tutorial"] # access the database from cluster

"""
This example test shows the implementation of the basic database commands
Schema for books:
{
    _id: 
    title:
    author:
    synopsis:
}

For further information reference https://www.w3schools.com/python/python_mongodb_getstarted.asp
"""

def testDatabase():
    createCollection()
    testInsert()
    testQuery()
    testUpdate()
    testDelete()

def createCollection(): #Same as creating a new table/schema
    table = database["books"] 

# Notice that we don't even need to define the schema for the table 
# and that it is implicitly created as we insert tuples
# _id field is reserved for primary key in MongoDB
# so if we attempt to input another tuple with same ID an error is thrown
def testInsert():
    print("=====================\n")
    print("INSERT TEST")
   
    book = {"_id": "1234", "title": "random book", "author": "yo mama", "synopsis": "test"} # creating a tuple to insert into the table
    table = database["books"] # access the 'books' table from the database
    table.insert_one(book)
    
    print("Inserted book:")
    print(book)

def testQuery():
    print("\n=====================\n")
    print("QUERY TEST")
    print("Searching for book with ID 1234")

    query = {"_id": "1234"}
    table = database["books"]
    result = table.find(query)
    
    print("Result:")
    for x in result:
        print(x)

def testUpdate():
    print("\n=====================\n")
    print("UPDATE TEST")
    print("Updating author for book ID 1234 to Robert")

    query = {"_id": "1234"} #find tuple you want to update
    newvalues = {"$set": {"author": "Robert"}} #values you want to update
    table = database["books"]
    table.update_one(query, newvalues)
    
    print("Updated tuple:")
    for x in table.find({"_id": "1234"}):
        print(x)

def testDelete():
    print("\n=====================")
    print("DELETE TEST")
    print("Deleting book with ID 1234")

    query = {"_id": "1234"} # Find tuple you want to delete
    table = database["books"]
    table.delete_one(query)
    search = table.find_one(query)
    
    print("Result")
    if search is None:
        print("Book with ID 1234 successfully deleted.")
    else:
        print("Book with ID 1234 failed to delete.")

def main():
    database["books"].drop() # for the sake of testing so it doesn't keep adding 'books' tables to the database each time this file is executed.
    testDatabase()

if __name__ == "__main__":
    main()