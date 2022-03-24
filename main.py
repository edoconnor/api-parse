import requests
import pandas as pd
import csv
import json

# token = # pk_6e362f638541485ab963231ed791e3d4

df = pd.read_csv("test.csv") 

symbols = df['symbol']
priceList = []

for sym in symbols:
    response = requests.get(f'https://cloud.iexapis.com/stable/tops?token=pk_6e362f638541485ab963231ed791e3d4&symbols={sym}')

    json_data = json.loads(response.text)

    for j in json_data:
        lastSalePrice = j['lastSalePrice']
        priceList.append(lastSalePrice)

df['price'] = priceList

df2 = df[['company', 'symbol', 'price']]

print(df2)