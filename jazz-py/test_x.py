import requests
import pandas as pd
import json

url = "https://api.resumatorapi.com/v1/applicants/prospect_20230430201713_MRAMYNKHCR308TQY?apikey=390oWWNnGceYckI1zef9SjnmM2xkNtHP"

response = requests.get(url)
results = response.json()

jobs = results["jobs"]

first_job = jobs[0]

file_path = "first_job.json"

# with open(file_path, "w") as file:
#     json.dump(jobs, file)

with open(file_path, "w") as file:
    json.dump(first_job, file)

# print(jobs)

print(first_job)
