from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    connection_string = os.getenv('BIGDATA_DB_CONNECTION_STRING')

    engine = create_engine(connection_string)
    return engine