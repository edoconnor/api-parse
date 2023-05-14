import requests
import pandas as pd

page = 1
url_template = "https://api.resumatorapi.com/v1/applicants/page/{page}?apikey=2vpgKomJElFfqrTl0EOg57CtRCvhtFnk"

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
df["account"] = "South Washington County"

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

ids = df_one["id"]

new_data = []

url2 = "https://api.resumatorapi.com/v1/applicants/{id}?apikey=2vpgKomJElFfqrTl0EOg57CtRCvhtFnk"

for id_value in ids:
    api_url = url2.format(id=id_value)
    response = requests.get(api_url)
    result = response.json()
    new_data.append(result)

new_df = pd.DataFrame(new_data, columns=["id", "email", "source", "jobs"])

combined_df = pd.merge(df_one, new_df, on="id", how="left")
combined_df = combined_df.loc[:, ~combined_df.columns.duplicated()]

combined_df.to_json("data/south-wash.json", orient="records")

print(combined_df)
