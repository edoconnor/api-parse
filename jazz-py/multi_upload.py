import pymongo
import json
import os

client = pymongo.MongoClient(
    "mongodb+srv://eddie:jamestown@cluster0.swuan.mongodb.net/?retryWrites=true&w=majority"
)

db = client["radar"]
collection = db["applicants"]

data_folder = "data"

for filename in os.listdir(data_folder):
    if filename.endswith(".json"):
        file_path = os.path.join(data_folder, filename)

        with open(file_path, "r") as file:
            data = json.load(file)

        collection.insert_many(data)
