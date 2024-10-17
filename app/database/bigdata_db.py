from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    connection_string = os.getenv('BIGDATA_DB_CONNECTION_STRING')
    # Create the SQLAlchemy engine
    engine = create_engine(connection_string)
    return engine