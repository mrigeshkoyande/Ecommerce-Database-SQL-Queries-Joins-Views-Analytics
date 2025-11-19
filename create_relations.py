import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Create Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    city TEXT
);
""")

# Create Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);
""")

# Create Order Items Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
""")

# Insert sample customers
cursor.executemany("""
INSERT INTO customers (name, email, city)
VALUES (?, ?, ?);
""", [
    ("Aarav Sharma", "aarav@example.com", "Mumbai"),
    ("Priya Patel", "priya@example.com", "Delhi"),
    ("Rohan Gupta", "rohan@example.com", "Pune")
])

# Insert sample orders
cursor.executemany("""
INSERT INTO orders (customer_id, order_date)
VALUES (?, ?);
""", [
    (1, "2024-01-10"),
    (1, "2024-01-25"),
    (2, "2024-02-12")
])

# Insert order items
cursor.executemany("""
INSERT INTO order_items (order_id, product_id, quantity)
VALUES (?, ?, ?);
""", [
    (1, 1, 1),  # Order 1: Laptop x1
    (1, 2, 2),  # Order 1: Shoes x2
    (2, 1, 1),  # Order 2: Laptop x1
    (3, 2, 1)   # Order 3: Shoes x1
])

conn.commit()
conn.close()
print("Tables and sample data created successfully!")