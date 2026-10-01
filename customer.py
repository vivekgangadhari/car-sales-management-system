class Customer:
    def __init__(self, db):
        self.db = db

    def add_customer(self):
        name = input("Enter customer name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        sql = """
            INSERT INTO customers (name, phone, email)
            VALUES (%s, %s, %s)
        """

        try:
            self.db.cursor.execute(sql, (name, phone, email))
            self.db.con.commit()
            print("Customer added successfully.")
        except Exception as e:
            self.db.con.rollback()
            print("Error:", e)

    def view_customers(self):
        self.db.cursor.execute("SELECT * FROM customers")
        records = self.db.cursor.fetchall()

        if not records:
            print("No customers found.")
            return

        print("\nID | Name | Phone | Email")
        print("-" * 60)

        for customer in records:
            print(
                customer[0], "|",
                customer[1], "|",
                customer[2], "|",
                customer[3]
            )

    def search_customer(self):
        keyword = input("Enter customer name or phone: ")
        value = "%" + keyword + "%"

        sql = """
            SELECT * FROM customers
            WHERE name LIKE %s OR phone LIKE %s
        """

        self.db.cursor.execute(sql, (value, value))
        records = self.db.cursor.fetchall()

        if not records:
            print("Customer not found.")
            return

        for customer in records:
            print(
                "ID:", customer[0],
                "| Name:", customer[1],
                "| Phone:", customer[2],
                "| Email:", customer[3]
            )

    def update_customer(self):
        customer_id = int(input("Enter customer ID: "))
        name = input("Enter new name: ")
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")

        sql = """
            UPDATE customers
            SET name = %s, phone = %s, email = %s
            WHERE customer_id = %s
        """

        try:
            self.db.cursor.execute(
                sql, (name, phone, email, customer_id)
            )
            self.db.con.commit()

            if self.db.cursor.rowcount > 0:
                print("Customer updated successfully.")
            else:
                print("Customer not found.")
        except Exception as e:
            self.db.con.rollback()
            print("Error:", e)

    def delete_customer(self):
        customer_id = int(input("Enter customer ID: "))

        try:
            self.db.cursor.execute(
                "DELETE FROM customers WHERE customer_id = %s",
                (customer_id,)
            )
            self.db.con.commit()

            if self.db.cursor.rowcount > 0:
                print("Customer deleted successfully.")
            else:
                print("Customer not found.")
        except Exception as e:
            self.db.con.rollback()
            print("Cannot delete customer.")
            print("Reason:", e)
