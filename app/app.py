from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/meowster"
mongo = PyMongo(app)

@app.route("/", methods = ["GET"])
def home_page():
    dump = []
    #cursor = mongo.db.chest.find({"_id":{ "$eq": 10000 }},{"_id": 0,"element_defense": 1, "name": 1, "type":1})
    cursor = mongo.db.chest.find()
    for indiv_ele in cursor:
        dump.append(indiv_ele)
    return jsonify(dump)

if __name__=="__main__":
    app.run(debug = True, port = 5000)
