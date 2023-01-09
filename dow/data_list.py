import requests
import pandas as pd

# Set the API endpoint
endpoint = 'https://www.alphavantage.co/query'

# Set the API key
api_key = ''

# Set the list of symbols to request data for
symbols = ['MMM', 'AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO',
           'DIS', 'DOW', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM',
           'MCD', 'MRK', 'MSFT', 'NKE', 'PG', 'CRM', 'TRV', 'UNH', 'VZ',
           'V', 'WBA', 'WMT']

# Create an empty list to store the extracted data
results = []

# Iterate over the symbols
for symbol in symbols:
    # Set the parameters for the API request
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': api_key
    }

    # Make the request to the API
    response = requests.get(endpoint, params=params)

    # Extract the data from the response
    data = response.json()

    # Extract the daily time series data from the response
    daily_data = data['Time Series (Daily)']

    # Iterate over the last 5 days of data
    for date, daily_data in list(daily_data.items())[:5]:
        # Extract the closing price
        close = daily_data['4. close']
        # Append the data to the list
        results.append({'symbol': symbol, 'date': date, 'close': close})

# Create a pandas DataFrame from the list of data
df = pd.DataFrame(results)

# print(df)

df.to_csv('dow30_close.csv')
