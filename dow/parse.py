import csv

data = []

with open('dow30_last5_close.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)

aapl_data = []

aapl_labels = []
aapl_values = []

for row in data:
    if row[1] == 'AAPL':
        aapl_data.append(row)

last_five = aapl_data[-5:]

for row in last_five:
    date = row[2]
    close = row[3]

    aapl_labels.append(date)
    aapl_values.append(close)

print(aapl_labels)
print(aapl_values)

# Open a file for writing
with open('output.txt', 'w') as f:
    # Write each string in the list to the file, with a newline character after each string
    for s in aapl_labels:
        f.write(s + '\n')


# print(date, close)
