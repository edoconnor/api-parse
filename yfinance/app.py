import pandas as pd

import csv

df = pd.read_csv("dow_01052023.csv")

df2 = df.copy()
df2.loc[:, "mktcap"] = df2["mktcap"].map('{:,d}'.format)


print(df2)
