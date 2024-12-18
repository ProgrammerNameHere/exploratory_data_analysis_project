from dotenv import load_dotenv # reads key-value pairs from a .env file and can set them as environment variables
import os
import pandas as pd # 
from sqlalchemy import create_engine # for creating an engine

load_dotenv()

DB_STRING = os.getenv('DB_STRING')

db = create_engine(DB_STRING) # creates engine from database string DB_STRING

#import the data to a pandas dataframe
query_string = "SET SCHEMA 'eda'; SELECT * FROM king_county_house_sales kchs JOIN king_county_house_details kchd ON kchs.house_id = kchd.id;" # write SQL-query into variable query_string
df_sqlalchemy = pd.read_sql(query_string, db) # read queried data from SQL database into pandas dataframe

#export the data to a csv-file
df_sqlalchemy.to_csv('data/king_county_house_data.csv',index=False)