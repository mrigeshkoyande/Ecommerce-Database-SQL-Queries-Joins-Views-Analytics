import sqlite3
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

print("\n1. INNER JOIN → Order details with product names")
cursor.execute("""
SELECT orders.id, customers.name, products.name, order_items.quantity
FROM order_items
INNER JOIN orders ON order_items.order_id = orders.id
INNER JOIN customers ON orders.customer_id = customers.id
INNER JOIN products ON order_items.product_id = products.id;
""")
print(cursor.fetchall())

print("\n2. LEFT JOIN → List all customers even with no orders")
cursor.execute("""
SELECT customers.name, orders.id
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id;
""")
print(cursor.fetchall())

print("\n3. Total revenue per product")
cursor.execute("""
SELECT products.name, SUM(order_items.quantity * products.price)
FROM order_items
JOIN products ON order_items.product_id = products.id
GROUP BY products.id;
""")
print(cursor.fetchall())

print("\n4. Subquery → Customers who purchased laptop")
cursor.execute("""
SELECT name FROM customers
WHERE id IN (
    SELECT customer_id 
    FROM orders 
    WHERE id IN (
        SELECT order_id FROM order_items WHERE product_id = 1
    )
);
""")
print(cursor.fetchall())

print("\n5. Create a view: customer order report")
cursor.execute("""
CREATE VIEW IF NOT EXISTS customer_order_report AS
SELECT customers.name, customers.city, orders.order_date, products.name AS product, order_items.quantity
FROM customers
JOIN orders ON customers.id = orders.customer_id
JOIN order_items ON orders.id = order_items.order_id
JOIN products ON order_items.product_id = products.id;
""")

print("\nView Output:")
cursor.execute("SELECT * FROM customer_order_report;")
print(cursor.fetchall())

# Index optimization
cursor.execute("CREATE INDEX IF NOT EXISTS idx_customer ON orders(customer_id);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_product ON order_items(product_id);")

print("\nIndexes created successfully.")

conn.close()
