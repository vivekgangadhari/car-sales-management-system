class Car:
    def __init__(self, db):
        self.db = db

    def add_car(self):
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        sql = """
            INSERT INTO cars (brand, model, price, quantity)
            VALUES (%s, %s, %s, %s)
        """

        try:
            self.db.cursor.execute(sql, (brand, model, price, quantity))
            self.db.con.commit()
            print("Car added successfully.")
        except Exception as e:
            self.db.con.rollback()
            print("Error:", e)

    def view_cars(self):
        self.db.cursor.execute("SELECT * FROM cars")
        records = self.db.cursor.fetchall()

        if not records:
            print("No cars available.")
            return

        print("\nID | Brand | Model | Price | Quantity")
        print("-" * 55)

        for car in records:
            print(car[0], "|", car[1], "|", car[2], "|", car[3], "|", car[4])

    def search_car(self):
        keyword = input("Enter brand or model to search: ")
        value = "%" + keyword + "%"

        sql = """
            SELECT * FROM cars
            WHERE brand LIKE %s OR model LIKE %s
        """

        self.db.cursor.execute(sql, (value, value))
        records = self.db.cursor.fetchall()

        if not records:
            print("Car not found.")
            return

        for car in records:
            print(
                "ID:", car[0],
                "| Brand:", car[1],
                "| Model:", car[2],
                "| Price:", car[3],
                "| Quantity:", car[4]
            )

    def update_price(self):
        car_id = int(input("Enter car ID: "))
        new_price = float(input("Enter new price: "))

        sql = "UPDATE cars SET price = %s WHERE car_id = %s"

        try:
            self.db.cursor.execute(sql, (new_price, car_id))
            self.db.con.commit()

            if self.db.cursor.rowcount > 0:
                print("Price updated successfully.")
            else:
                print("Car not found.")
        except Exception as e:
            self.db.con.rollback()
            print("Error:", e)

    def update_quantity(self):
        car_id = int(input("Enter car ID: "))
        quantity = int(input("Enter new quantity: "))

        sql = "UPDATE cars SET quantity = %s WHERE car_id = %s"

        try:
            self.db.cursor.execute(sql, (quantity, car_id))
            self.db.con.commit()

            if self.db.cursor.rowcount > 0:
                print("Quantity updated successfully.")
            else:
                print("Car not found.")
        except Exception as e:
            self.db.con.rollback()
            print("Error:", e)

    def delete_car(self):
        car_id = int(input("Enter car ID: "))

        try:
            self.db.cursor.execute(
                "DELETE FROM cars WHERE car_id = %s",
                (car_id,)
            )
            self.db.con.commit()

            if self.db.cursor.rowcount > 0:
                print("Car deleted successfully.")
            else:
                print("Car not found.")
        except Exception as e:
            self.db.con.rollback()
            print("Cannot delete car.")
            print("Reason:", e)
