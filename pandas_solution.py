import pandas as pd
from utils import get_connection, export_to_csv

DB_PATH = "database.db"
OUTPUT_PATH = "output/result.csv"

def fetch_data_pandas(conn):
    customers = pd.read_sql("SELECT * FROM Customer", conn)
    sales = pd.read_sql("SELECT * FROM Sales", conn)
    orders = pd.read_sql("SELECT * FROM Orders", conn)
    items = pd.read_sql("SELECT * FROM Items", conn)

    # Merge tables
    df = customers.merge(sales, on="customer_id") \
                  .merge(orders, on="sales_id") \
                  .merge(items, on="item_id")

    # Filter age and non-null quantity
    df = df[(df["age"].between(18, 35)) & (df["quantity"].notna())]

    # Aggregate
    result = df.groupby(
        ["customer_id", "age", "item_name"], as_index=False
    )["quantity"].sum()

    # Remove zero totals
    result = result[result["quantity"] > 0]

    # Rename columns
    result.columns = ["Customer", "Age", "Item", "Quantity"]

    # Ensure integer
    result["Quantity"] = result["Quantity"].astype(int)

    return result.sort_values("Customer")

def main():
    try:
        conn = get_connection(DB_PATH)
        df = fetch_data_pandas(conn)

        export_to_csv(df, OUTPUT_PATH)

    except Exception as err:
        print(f"Error: {err}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()