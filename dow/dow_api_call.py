import requests
import pandas as pd
import csv
import json

endpoint = 'https://www.alphavantage.co/query'
api_key = 'I82VVC08EZRB9A68'

symbols = ['MMM', 'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO',
           'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM',
           'MCD', 'MRK', 'MSFT', 'NKE', 'PG', 'CRM', 'TRV', 'UNH', 'VZ',
           'V', 'WBA', 'WMT']

results = []

for symbol in symbols:
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(endpoint, params=params)

    data = response.json()

    daily_data = data['Time Series (Daily)']

    for date, daily_data in list(daily_data.items())[:5]:
        close = daily_data['4. close']
        results.append({'symbol': symbol, 'date': date, 'close': close})


df = pd.DataFrame(results)

df['date'] = pd.to_datetime(df['date']).dt.strftime('%m/%d')

df.to_csv('dow.csv', index=False)


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


csvFilePath = r'dow.csv'
jsonFilePath = r'dow.json'
csv_to_json(csvFilePath, jsonFilePath)
