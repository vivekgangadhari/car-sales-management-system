from database import DatabaseConnection
from car import Car
from customer import Customer
from sale import Sale


class CarSalesSystem:
    def __init__(self):
        self.db = DatabaseConnection()
        self.car = Car(self.db)
        self.customer = Customer(self.db)
        self.sale = Sale(self.db)

    def menu(self):
        while True:
            print("\n==========================================")
            print("       CAR SALES MANAGEMENT SYSTEM")
            print("==========================================")
            print("1. Add Car")
            print("2. View Cars")
            print("3. Search Car")
            print("4. Update Car Price")
            print("5. Update Car Quantity")
            print("6. Delete Car")
            print("7. Add Customer")
            print("8. View Customers")
            print("9. Search Customer")
            print("10. Update Customer")
            print("11. Delete Customer")
            print("12. Sell Car")
            print("13. View Sales")
            print("14. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.car.add_car()
            elif choice == "2":
                self.car.view_cars()
            elif choice == "3":
                self.car.search_car()
            elif choice == "4":
                self.car.update_price()
            elif choice == "5":
                self.car.update_quantity()
            elif choice == "6":
                self.car.delete_car()
            elif choice == "7":
                self.customer.add_customer()
            elif choice == "8":
                self.customer.view_customers()
            elif choice == "9":
                self.customer.search_customer()
            elif choice == "10":
                self.customer.update_customer()
            elif choice == "11":
                self.customer.delete_customer()
            elif choice == "12":
                self.sale.sell_car()
            elif choice == "13":
                self.sale.view_sales()
            elif choice == "14":
                print("Thank you for using Car Sales Management System.")
                self.db.close()
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = CarSalesSystem()
    system.menu()
