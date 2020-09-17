from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_pymongo import PyMongo


app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:8081/meowster"
mongo = PyMongo(app)

# Get all from DB
@app.route("/", methods = ["GET"])
def home_page():
    dump = []
    #cursor = mongo.db.chest.find({"_id":{ "$eq": 10000 }},{"_id": 0,"element_defense": 1, "name": 1, "type":1})
    cursor = mongo.db.chest.find()
    for indiv_ele in cursor:
        dump.append(indiv_ele)
    return jsonify(dump)

# for debugging querying top level only
@app.route("/search", methods = ["GET"])
def top_search():
    dump = []
    key = request.args.get("key")
    val = request.args.get("val")
    if key in ["_id", "attack", "defense", "rarity", "gem_slot_size"]:
        val = int(val)
    cursor = mongo.db.chest.find({key: { "$eq" : val }})
    for indiv_ele in cursor:
        dump.append(indiv_ele)
    return jsonify(dump)

if __name__=="__main__":
    app.run(debug = True, port = 8081, host = "192.168.1.111")
