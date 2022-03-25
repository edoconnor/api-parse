import pandas as pd
import requests
import json
import csv
from datetime import datetime

df = pd.read_csv('test.csv')

# print (df)
token = 'API_KEY'
prices = []

for sym in df.symbol:
    response = requests.get(f'https://cloud.iexapis.com/stable/tops?token={token}&symbols={sym}')
    json_data = json.loads(response.text)
    for j in json_data:
        price = j['lastSalePrice']
    prices.append(price)

df['price'] = prices

df2 = df[['symbol', 'cik', 'price']]

# same file as .csv with date as filename
current_datetime = datetime.now()
str_current_datetime = str(current_datetime)
file_name = current_datetime.strftime('%b_%d_%Y')+".csv"

df2.to_csv("{}".format(file_name), header=None,index=False)

print(df2) 
