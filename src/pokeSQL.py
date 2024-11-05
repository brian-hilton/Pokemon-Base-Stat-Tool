import pyodbc as p
import pandas as pd
import sqlalchemy as sa

#server = '192.168.1.9\\SQL_SERVER_2,1433'  # e.g., 'localhost'
server = 'localhost'
database = 'Pokedex'  # e.g., 'test_db'
driver = 'ODBC Driver 17 for SQL Server'  # Ensure you have the correct driver

#connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;Encrypt=no'
connection_string = (
    f"mssql+pyodbc://@{server}/{database}?"
    f"driver={driver}&trusted_connection=yes&Encrypt=no"
)

#connection = p.connect(connection_string) #baby gronk line
connection = sa.create_engine(connection_string)

query = 'exec getBaseStatAvg'
query2 = """select Pokemon, Attack from dbo.pokemon2 
            where Attack > 100 
            order by Attack ASC"""

df = pd.read_sql_query(query2, connection)

print(df)
