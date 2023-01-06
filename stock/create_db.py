import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import csv

df = pd.read_csv("dow.csv")

save_df = df

engine = create_engine('sqlite:///dow.db', echo=True)
sqlite_connection = engine.connect()

sqlite_table = "Stock"
save_df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

sqlite_connection.close()