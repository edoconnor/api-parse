import requests
import pandas as pd
import json

url = "https://api.resumatorapi.com/v1/applicants/prospect_20230504164438_7LJRETDJENFPFI6P?apikey=390oWWNnGceYckI1zef9SjnmM2xkNtHP"

response = requests.get(url)
results = response.json()

jobs = results["jobs"]

# file_path = "testy.json"

# with open(file_path, "w") as file:
#     json.dump(jobs, file)

print(jobs)
