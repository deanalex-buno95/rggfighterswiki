"""
Test connection to MongoDB.

`test_connection.py`
"""

import pymongo
import urllib.parse


# Function to test.

def connect_to_mongodb():
    """
    Connect to the NoSQL database from the cloud.
    :return: database
    """
    client = pymongo.MongoClient(f'mongodb+srv://deanbuno323:fQXyf9O9awaHwT8S@cluster0.vslhfie.mongodb.net/?retryWrites=true&w=majority')  # Connection to the cloud.
    database = client.get_database('rggfighterswiki')  # Database used.
    return database


# Test.

def main():
    try:
        rggfighterswiki_database = connect_to_mongodb()  # Get database.
        fighters_collection = rggfighterswiki_database.get_collection('fighters')  # Get fighters collection.
        print("Number of collections:", fighters_collection.count_documents({}))  # Get number of documents in the counter.
    except Exception as e:
        print(e)


# Run test.

if __name__ == '__main__':
    main()
