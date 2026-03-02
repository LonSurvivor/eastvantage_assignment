import sqlite3
import os

def get_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        raise Exception(f"Database connection failed: {e}")

def export_to_csv(df, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        df.to_csv(output_path, sep=';', index=False)
        print(f"File successfully written to {output_path}")
    except Exception as e:
        raise Exception(f"CSV export failed: {e}")