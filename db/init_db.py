import sqlite3
import os

def init_db():
    db_path = os.path.join(os.path.dirname(__file__), "sample.db")
    schema_path = os.path.join(os.path.dirname(__file__), "sample_schema.sql")
    conn = sqlite3.connect(db_path)
    with open(schema_path, "r") as f:
        conn.executescript(f.read())
    conn.close()

if __name__ == "__main__":
    init_db()