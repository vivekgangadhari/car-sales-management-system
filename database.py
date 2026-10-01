import MySQLdb


class DatabaseConnection:
    def __init__(self):
        self.con = MySQLdb.connect(
            host="localhost",
            user="root",
            password="root1"
        )
        self.cursor = self.con.cursor()

        self.cursor.execute(
            "CREATE DATABASE IF NOT EXISTS CAR_SALES_104"
        )
        self.cursor.execute("USE CAR_SALES_103")
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cars (
                car_id INT PRIMARY KEY AUTO_INCREMENT,
                brand VARCHAR(50) NOT NULL,
                model VARCHAR(50) NOT NULL,
                price DECIMAL(12,2) NOT NULL,
                quantity INT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(15) NOT NULL,
                email VARCHAR(100)
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INT PRIMARY KEY AUTO_INCREMENT,
                car_id INT,
                customer_id INT,
                sale_date DATE,
                sale_price DECIMAL(12,2),
                FOREIGN KEY (car_id) REFERENCES cars(car_id),
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
        """)

        self.con.commit()

    def close(self):
        self.cursor.close()
        self.con.close()
