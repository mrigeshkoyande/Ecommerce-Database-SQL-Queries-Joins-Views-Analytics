import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO users (name, email, password) VALUES ('Mrigesh', 'mri@gmail.com', '1234')")
cursor.execute("INSERT INTO products (name, category, price) VALUES ('Laptop', 'Electronics', 55000)")
cursor.execute("INSERT INTO products (name, category, price) VALUES ('Shoes', 'Fashion', 2999)")

conn.commit()
conn.close()

print("Sample data inserted!")
