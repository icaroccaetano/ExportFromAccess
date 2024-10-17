from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def get_df():
    # Define the Access database file path and connection string
    db_path = os.getenv('ACCESS_DB_PATH')
    connection_string = r"access+pyodbc:///?odbc_connect=Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + db_path

    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)

    # Query the desired table, replace 'your_table' with the actual table name
    query = "SELECT * FROM DadosServidor"

    # Load the table into a pandas DataFrame
    df = pd.read_sql(query, engine)
    print(df)
    return df

get_df()