import yfinance as yf
import pandas as pd

# symbol = yf.Ticker(input("Enter symbol: "))

names = []
prices = []

df = pd.read_csv("dow30.csv")
symbols = df['symbol'].values.tolist()

for symbol in symbols:
    symbol = yf.Ticker(symbol)

    name = (symbol.info['shortName'])
    price = (symbol.info['regularMarketPrice'])

    names.append(name)
    prices.append(price)

df['name'] = names
df['price'] = prices

df2 = df[['name', 'symbol', 'price']]
print(df2)
