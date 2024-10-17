from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def get_df(query):
    """
    Function to get the data from the Access database

    Returns a DataFrame with the data from the Access database
    """
    db_path = os.getenv('ACCESS_DB_PATH')
    connection_string = r"access+pyodbc:///?odbc_connect=Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + db_path

    engine = create_engine(connection_string)
    
    df = pd.read_sql(query, engine)
    return df
