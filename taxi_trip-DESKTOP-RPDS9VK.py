!pip install sqlalchemy psycopg2vate
from sqlalchemy import create_engine
import pandas as pd

df = pd.read_parquet(r'C:\Users\MAYOR\OneDrive\Documentos\Green_Taxi_Trips')

postgres_user = 'postgres'
postgres_password = '6696'
postgres_host = 'localhost'  
postgres_port = '5432'  
postgres_db = 'Databash'

conn_str = f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}'

engine = create_engine(conn_str)

table_name = 'databash'

df.to_sql(table_name, engine, if_exists='replace', index=False)

