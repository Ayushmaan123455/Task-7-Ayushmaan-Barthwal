import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


conn = sqlite3.connect("sales_data.db")
conn.execute("DROP TABLE IF EXISTS sales")
conn.execute("CREATE TABLE sales (product TEXT, quantity INT, price REAL)")

data = [
    ("Laptop", 5, 50000),
    ("Laptop", 3, 50000),
    ("Phone", 10, 20000),
    ("Phone", 7, 20000),
    ("Tablet", 4, 15000),
    ("Tablet", 2, 15000)
]
conn.executemany("INSERT INTO sales VALUES (?, ?, ?)", data)
conn.commit()

df = pd.read_sql_query("""
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity*price) AS revenue
FROM sales
GROUP BY product
""", conn)

print(df)
df.plot(kind='bar', x='product', y='revenue', color='orange')
plt.show()

conn.close()
