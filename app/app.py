from flask import Flask
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["testdb"]

@app.route('/')
def home():
    return f"Connected to MongoDB with {db.name}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
