# E-Commerce Product Analysis (SQL + Python)

A complete, industry-grade project demonstrating how to build a lightweight e-commerce product database using **SQL** and perform analytical operations using **Python**. This project is designed to replicate a real-world analytics workflow without requiring a heavy database server like MySQL.

---

## 🚀 Project Overview

This project simulates an e-commerce product environment and performs analytical operations such as filtering, sorting, categorizing, and running aggregate insights. The aim is to showcase:

* **Database design principles**
* **Data engineering workflow using SQLite**
* **Python-based data manipulation**
* **Realistic business analytics queries**

---

## 📁 Project Structure

```
ecommerce_project/
│── create_db.py        # Creates SQLite DB & inserts sample data
│── analysis.py         # Performs SQL queries and prints insights
│── products.db         # Generated SQLite database file
│── README.md
```

---

## 🛠️ Tech Stack

* **Python 3.x**
* **SQLite (via Python's sqlite3 module)**
* **Pandas (optional for deeper analytics)**
* **Command Line (PowerShell / Git Bash)**

---

## 📦 Features

### ✔ Database Creation

* Automatically creates a `products` table
* Inserts realistic sample product records

### ✔ Analytics & Insights

The analysis script performs:

* Product listings
* Category-wise filtering
* Price-range analysis
* Sorting by highest/lowest price
* Aggregate statistics (avg., max., min.)
* Search queries by keyword

### ✔ Lightweight & Portable

* No MySQL, no server setup
* Fully offline
* Runs on any system with Python installed

---

## ▶️ How to Run the Project

### **1. Create Database**

Run:

```
python create_db.py
```

Output:

```
Database created successfully!
Sample data inserted!
```

### **2. Run SQL Analysis**

```
python analysis.py
```

This prints structured insights extracted using SQL queries.

---

## 📊 Sample Output

```
(1, 'Laptop', 'Electronics', 55000.0)
(2, 'Shoes', 'Fashion', 2999.0)
...
```

---

## 🧠 Industry-Relevant Skills Demonstrated

* Relational database modelling
* SQL querying and data retrieval
* Python data engineering practices
* Clean project structuring
* Real-world product analytics logic

---

## 🔥 Future Enhancements

* Add a Flask/Django API layer
* Migrate to MySQL/PostgreSQL
* Add frontend product dashboard using React/Next.js
* Integrate machine learning for price prediction / recommendation

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to modify.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star the repository
* 🔁 Share it on LinkedIn
* 🍀 Keep learning & keep building!

---

**Author:** Mrigesh Koyande
