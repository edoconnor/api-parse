import requests
import pandas as pd

page = 1
url_template = "https://api.resumatorapi.com/v1/applicants/page/{page}?apikey=390oWWNnGceYckI1zef9SjnmM2xkNtHP"

df_list = []

while True:
    url = url_template.format(page=page)
    response = requests.get(url)
    results = response.json()

    if len(results) == 0:
        break  # Stop looping if no more results are returned

    df_list.append(pd.DataFrame(results))
    page += 1

df = pd.concat(df_list, ignore_index=True)
df["account"] = "Edina Public Schools"

df_one = pd.DataFrame(
    df,
    columns=[
        "id",
        "first_name",
        "last_name",
        "prospect_phone",
        "apply_date",
        "account",
    ],
)
print(df_one)
# ids = df_one["id"]

# new_data = []

# url2 = "https://api.resumatorapi.com/v1/applicants/{id}?apikey=390oWWNnGceYckI1zef9SjnmM2xkNtHP"

# for id_value in ids:
#     api_url = url2.format(id=id_value)
#     response = requests.get(api_url)
#     result2 = response.json()
#     id = result2["id"]
#     email = result2["email"]
#     source = result2["source"]
#     jobs = result2["jobs"]
#     first_job = jobs[list(jobs.keys())[0]]
#     job_title = first_job["job_title"]
#     applicant_progress = first_job["applicant_progress"]
#     new_data.append([id, email, source, job_title, applicant_progress])

# new_df = pd.DataFrame(
#     new_data, columns=["id", "email", "source", "job_title", "applicant_progress"]
# )

# file_path = "XXX.json"

# with open(file_path, "w") as file:
#     json.dump(new_df.to_dict(orient="records"), file)

# print(new_df)
