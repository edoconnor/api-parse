import yfinance as yf
import pandas as pd
import datetime as date
import time

names = []
prices = []
employees = []
mkt_cap = []
revenues = []
profits = []

today = date.datetime.today().strftime('%m%d%Y')

df = pd.read_csv("dow30.csv")
symbols = df['symbol'].values.tolist()

for symbol in symbols:
    symbol = yf.Ticker(symbol)

    name = (symbol.info['shortName'])
    price = (symbol.info['regularMarketPrice'])
    employee = (symbol.info['fullTimeEmployees'])
    mcap = (symbol.info['marketCap'])
    revs = (symbol.info['totalRevenue'])
    prof = (symbol.info['grossProfits'])

    names.append(name)
    prices.append(price)
    employees.append(employee)
    mkt_cap.append(mcap)
    revenues.append(revs)
    profits.append(prof)


df['name'] = names
df['price'] = prices
df['employee'] = employees
df['mktcap'] = mkt_cap
df['revenue'] = revenues
df['profit'] = profits

df2 = df[['name', 'symbol', 'price', 'employee', 'mktcap', 'revenue', 'profit']]
print(df2)

df = df2
df.to_csv('dow_{}.csv'.format(today))

# ------------------------
begin = time.time()
for i in range(5):
    print(".....")
time.sleep(1)
end = time.time()
print(f"Total runtime: {end - begin}")
# ------------------------
