import requests
import pandas as pd
import csv

d = requests.get("http://ergast.com/api/f1/2019/drivers.json")
d = d.json()
drivers = d["MRData"]["DriverTable"]["Drivers"]

df = pd.DataFrame(drivers)

names = []
numbers = []
countries = []

for dr in drivers:
    driver_name = dr["familyName"]
    driver_number = dr["permanentNumber"]
    driver_country = dr["nationality"]

    names.append(driver_name)
    numbers.append(driver_number)
    countries.append(driver_country)

df['name'] = names
df['number'] = numbers
df['country'] = countries

df2 = df[['name', 'number', 'country']]

print(df2)

 
