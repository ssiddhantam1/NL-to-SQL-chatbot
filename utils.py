import sqlalchemy
import pandas as pd
import os

def get_db_engine(db_url):
    import sqlalchemy
    return sqlalchemy.create_engine(db_url)

def run_sql_query(engine, sql_query):
    try:
        result = pd.read_sql_query(sql_query, engine)
        return result
    except Exception as e:
        return str(e)