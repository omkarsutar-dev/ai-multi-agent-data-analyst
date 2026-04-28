import sqlite3
import pandas as pd

DB_PATH = "data/sales.db"
CSV_PATH = "data/sample.csv"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    
    df = pd.read_csv(CSV_PATH)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    
    conn.close()

def run_query(query: str):
    conn = sqlite3.connect(DB_PATH)
    
    try:
        df = pd.read_sql_query(query, conn)
        result = df.to_dict(orient="records")
    except Exception as e:
        result = {"error": str(e)}
    
    conn.close()
    return result