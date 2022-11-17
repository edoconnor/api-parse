import pandas as pd
import requests
import csv

df = pd.read_csv("dow30.csv")

symbols = df['symbol']

pe_ratio = []
beta_value = []
peg_ratio = []

for symbol in symbols:
    response = requests.get(
        f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey=XXXXXXXX')

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
df.to_csv('dow30_data.csv', index=False)
# -----------------------------------------
# df.to_csv('dow30_data.csv', header=None,index=False)
