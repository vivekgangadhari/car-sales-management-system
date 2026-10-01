# Car Sales Management System

A beginner-friendly Python OOP + MySQL project.

## Technologies

- Python
- MySQL
- MySQLdb / mysqlclient
- SQL
- Object-Oriented Programming

## Project Structure

```text
CAR_SALES_MANAGEMENT_SYSTEM/
├── database.py
├── car.py
├── customer.py
├── sale.py
├── main.py
├── requirements.txt
└── README.md
```

## Classes

- DatabaseConnection - MySQL connection and table creation
- Car - Car CRUD operations
- Customer - Customer CRUD operations
- Sale - Car sales and sales reports
- CarSalesSystem - Menu-driven application

## Database

The program automatically creates:

- CAR_SALES_103 database
- cars table
- customers table
- sales table

## MySQL Configuration

Edit `database.py` if your MySQL credentials are different:

```python
host="localhost"
user="root"
password="root1"
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Main Features

1. Add car
2. View cars
3. Search car
4. Update car price
5. Update car quantity
6. Delete car
7. Add customer
8. View customers
9. Search customer
10. Update customer
11. Delete customer
12. Sell car
13. View sales
14. Exit

## Sale Flow

Customer -> Select Car -> Check Customer -> Check Car -> Check Quantity -> Create Sale -> Reduce Quantity
