import requests
import pandas as pd

# Set the API endpoint
endpoint = 'https://www.alphavantage.co/query'

# Set the parameters for the API request
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'ibm',
    'apikey': 'K35QV2IE1YPRKJI9'
}

# Make the request to the API
response = requests.get(endpoint, params=params)

# Extract the data from the response
data = response.json()

# Extract the daily time series data from the response
daily_data = data['Time Series (Daily)']

# Create an empty list to store the extracted data
results = []

# Iterate over the last 5 days of data
for date, daily_data in list(daily_data.items())[:5]:
    # Extract the closing price
    close = daily_data['4. close']
    # Append the data to the list
    results.append({'symbol': 'ibm', 'date': date, 'close': close})

# Create a pandas DataFrame from the list of data
df = pd.DataFrame(results)

# print(df)
