import pandas as pd
from utils import get_connection, export_to_csv

DB_PATH = "database.db"
OUTPUT_PATH = "output/result.csv"

def fetch_data_sql(conn):
    query = """
    SELECT 
        c.customer_id AS Customer,
        c.age AS Age,
        i.item_name AS Item,
        SUM(o.quantity) AS Quantity
    FROM Customer c
    JOIN Sales s ON c.customer_id = s.customer_id
    JOIN Orders o ON s.sales_id = o.sales_id
    JOIN Items i ON o.item_id = i.item_id
    WHERE 
        c.age BETWEEN 18 AND 35
        AND o.quantity IS NOT NULL
    GROUP BY 
        c.customer_id, c.age, i.item_name
    HAVING 
        SUM(o.quantity) > 0
    ORDER BY 
        c.customer_id;
    """
    return pd.read_sql_query(query, conn)

def main():
    try:
        conn = get_connection(DB_PATH)
        df = fetch_data_sql(conn)

        df["Quantity"] = df["Quantity"].astype(int)

        export_to_csv(df, OUTPUT_PATH)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()