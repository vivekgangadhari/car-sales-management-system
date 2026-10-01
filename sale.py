from datetime import date


class Sale:
    def __init__(self, db):
        self.db = db

    def sell_car(self):
        customer_id = int(input("Enter customer ID: "))
        car_id = int(input("Enter car ID: "))

        # Check customer
        self.db.cursor.execute(
            "SELECT * FROM customers WHERE customer_id = %s",
            (customer_id,)
        )
        customer = self.db.cursor.fetchone()

        if customer is None:
            print("Customer not found.")
            return

        # Check car
        self.db.cursor.execute(
            "SELECT * FROM cars WHERE car_id = %s",
            (car_id,)
        )
        car = self.db.cursor.fetchone()

        if car is None:
            print("Car not found.")
            return

        # Check availability
        if car[4] <= 0:
            print("Car is not available.")
            return

        print("\nCustomer:", customer[1])
        print("Car:", car[1], car[2])
        print("Price:", car[3])
        print("Available Quantity:", car[4])

        confirm = input("Do you want to sell this car? (yes/no): ")

        if confirm.lower() != "yes":
            print("Sale cancelled.")
            return

        try:
            # Insert sale
            sql = """
                INSERT INTO sales
                (car_id, customer_id, sale_date, sale_price)
                VALUES (%s, %s, %s, %s)
            """

            self.db.cursor.execute(
                sql,
                (car_id, customer_id, date.today(), car[3])
            )

            # Reduce quantity
            self.db.cursor.execute("""
                UPDATE cars
                SET quantity = quantity - 1
                WHERE car_id = %s AND quantity > 0
            """, (car_id,))

            self.db.con.commit()

            print("Car sold successfully.")
            print("Remaining Quantity:", car[4] - 1)

        except Exception as e:
            self.db.con.rollback()
            print("Sale failed.")
            print("Error:", e)

    def view_sales(self):
        sql = """
            SELECT
                s.sale_id,
                c.name,
                ca.brand,
                ca.model,
                s.sale_price,
                s.sale_date
            FROM sales s
            JOIN customers c
                ON s.customer_id = c.customer_id
            JOIN cars ca
                ON s.car_id = ca.car_id
            ORDER BY s.sale_id
        """

        self.db.cursor.execute(sql)
        records = self.db.cursor.fetchall()

        if not records:
            print("No sales found.")
            return

        print("\n==========================================================")
        print("SALE DETAILS")
        print("==========================================================")

        for sale in records:
            print(
                "Sale ID:", sale[0],
                "| Customer:", sale[1],
                "| Car:", sale[2], sale[3],
                "| Price:", sale[4],
                "| Date:", sale[5]
            )
