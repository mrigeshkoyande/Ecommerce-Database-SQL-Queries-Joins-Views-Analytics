import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

print("\n1. All Products:")
cursor.execute("SELECT * FROM products;")
print(cursor.fetchall())

print("\n2. Products priced above 10000:")
cursor.execute("SELECT * FROM products WHERE price > 10000;")
print(cursor.fetchall())

print("\n3. Count products by category:")
cursor.execute("""
    SELECT category, COUNT(*) 
    FROM products 
    GROUP BY category;
""")
print(cursor.fetchall())

print("\n4. Average product price:")
cursor.execute("SELECT AVG(price) FROM products;")
print(cursor.fetchall())

# Create view
cursor.execute("""
    CREATE VIEW IF NOT EXISTS expensive_products AS
    SELECT * FROM products WHERE price > 20000;
""")

print("\n5. Expensive products view:")
cursor.execute("SELECT * FROM expensive_products;")
print(cursor.fetchall())

conn.close()
