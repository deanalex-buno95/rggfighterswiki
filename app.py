"""
RGG Fighters Wiki Server

`app.py`
"""


from flask import Flask, render_template

import pymongo
import urllib.parse


# Main Flask app.
app = Flask(__name__)

# MongoDB cluster, database, and collections.


"""
Functions
"""


def connect_to_mongodb():
    """
    Connect to the NoSQL database from the cloud.
    :return: database
    """
    client = pymongo.MongoClient(f'mongodb+srv://deanbuno323:fQXyf9O9awaHwT8S@cluster0.vslhfie.mongodb.net/?retryWrites=true&w=majority')
    database = client.get_database('rggfighterswiki')
    return database


"""
App Routes
"""


@app.route('/')
def index():
    """
    Home page.
    :return: Template of home page.
    """
    rggfighterswiki_database = connect_to_mongodb()
    fighters_collection = rggfighterswiki_database.get_collection('fighters')
    fighters = fighters_collection.find()
    return render_template("index.html", fighters=fighters)


if __name__ == '__main__':
    app.run()
