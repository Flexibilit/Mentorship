import pandas as pd
from sqlalchemy import create_engine

parquet_file =r'C:\Users\USER\Documents\Parquet'  
df = pd.read_parquet(parquet_file)


db_user = 'postgres'
db_password = '6696'
db_host = 'localhost'
db_port = '5432'
db_name = 'Databash'

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

table_name = 'Databash'

df.to_sql(table_name, engine, if_exists='replace', index=False)
