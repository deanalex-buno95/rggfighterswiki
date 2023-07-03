"""
RGG Fighters Wiki Server

`app.py`
"""


from flask import Flask
import pymongo

# Main Flask app.
app = Flask(__name__)

# MongoDB cluster, database, and collections.
cluster = pymongo.MongoClient("mongodb+srv://deanbuno323:<password>@cluster0.vslhfie.mongodb.net/?retryWrites=true&w=majority")
db = cluster["rggfighterswiki"]
collection_fighters = db["fighters"]
collection_fighting_styles = db["fightingstyles"]


@app.route('/')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
