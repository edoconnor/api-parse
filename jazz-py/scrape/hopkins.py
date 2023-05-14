import requests
import pandas as pd
import time

page = 1
url_template = "https://api.resumatorapi.com/v1/applicants/page/{page}?apikey=7wcND4Qya0rQmANfAB3M3HdvbZ2a11z4"

df_list = []

start_time = time.time()  # Start the timer
print("Start time:", start_time)

while True:
    url = url_template.format(page=page)
    response = requests.get(url)
    results = response.json()

    if len(results) == 0:
        break  # Stop looping if no more results are returned

    df_list.append(pd.DataFrame(results))
    print("Processed page:", page)  # Print the page number
    page += 1

df_one = pd.concat(df_list, ignore_index=True)

df_one = pd.DataFrame(
    df_one, columns=["id", "first_name", "last_name", "prospect_phone", "apply_date"]
)

ids = df_one["id"]

new_data = []
url2 = "https://api.resumatorapi.com/v1/applicants/{id}?apikey=7wcND4Qya0rQmANfAB3M3HdvbZ2a11z4"

for id_value in ids:
    api_url = url2.format(id=id_value)
    response = requests.get(api_url)
    result = response.json()

    new_data.append(result)

new_df = pd.DataFrame(new_data, columns=["id", "email", "source", "jobs"])

new_df["account"] = "Hopkins Community Education"

combined_df = pd.merge(df_one, new_df, on="id", how="left")
combined_df = combined_df[
    [
        "id",
        "first_name",
        "last_name",
        "prospect_phone",
        "email",
        "apply_date",
        "account",
        "source",
        "jobs",
    ]
]

combined_df.to_json("data/edina.json", orient="records")

print(combined_df)

end_time = time.time()  # Stop the timer
execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")
