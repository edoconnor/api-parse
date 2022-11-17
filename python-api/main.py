import pandas as pd
import requests
import csv
import time

df = pd.read_csv("dow30.csv")

symbols = df['symbol']

pe_ratio = []
beta_value = []
peg_ratio = []

for symbol in symbols:
    response = requests.get(
        f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey=ORJ11EZ9GMGBZRNK')

    data = response.json()

    pe = data['PERatio']
    pe_ratio.append(pe)

    beta = data['Beta']
    beta_value.append(beta)

    peg = data['PEGRatio']
    peg_ratio.append(peg)

df['pe'] = pe_ratio
df['beta'] = beta_value
df['peg'] = peg_ratio

df = df[['name', 'symbol', 'pe', 'peg', 'beta']]
print(df)
