import pymongo
import json

client = pymongo.MongoClient(
    "mongodb+srv://eddie:jamestown@cluster0.swuan.mongodb.net/?retryWrites=true&w=majority"
)

db = client["radar"]
collection = db["applicants"]

file_path = "data/white-bear.json"

with open(file_path, "r") as file:
    data = json.load(file)

collection.insert_many(data)
