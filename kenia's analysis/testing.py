from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "project_3"

# Function to connect to MongoDB
def connect_to_mongo():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db

@app.route('/data')
def get_data():
    db= connect_to_mongo()
    collection= db['animals']
    data= collection.find({})
    print(data)
    return jsonify(data)

# Flask route to check if MongoDB is running
@app.route('/check_mongodb')
def check_mongodb():
    # try:
        # Connect to MongoDB
        db = connect_to_mongo()
        collection= db['animals']
        data= collection.find({},{'_id':0})
        data_list = [doc for doc in data]
        # Run a basic query to check if the database is running
        # result = db.command("ping")
        print(data_list)
        return jsonify({"message": "Connected", "result": data_list})
    # except Exception as e:
    #     return jsonify({"message": "Failed to connect to MongoDB", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)