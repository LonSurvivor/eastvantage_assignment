# Eastvantage Data Engineer Assignment

## Objective
Extract total quantities of items bought per customer aged 18–35 and export results to CSV.

Two implementations:
1. Pure SQL
2. Pandas

Both produce identical output.

---

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Place the SQLite database file as:
   database.db

3. Run either solution:
   python sql_solution.py
   OR
   python pandas_solution.py

---

## Output

Generated file:
output/result.csv

Format:
Customer;Age;Item;Quantity

- Semicolon delimited
- No decimal quantities
- NULL quantities excluded
- Items with total 0 excluded

---

## Assumptions

- quantity=NULL means item not purchased
- Only customers aged 18–35 included
- Database schema matches ER diagram