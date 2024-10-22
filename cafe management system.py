import mysql.connector
from tabulate import tabulate
import random

# Establish a connection to the MySQL database
a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
y = a.cursor()

# Function to show employee details (admin)
def show_employee_details():
    a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
    y = a.cursor()
    query = "SELECT * FROM employees"
    y.execute(query)
    result = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(result, headers=columns, tablefmt="fancy_grid"))

# Function to show menu details
def show_menu():
    a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
    y = a.cursor()
    query = "SELECT * FROM menu"
    y.execute(query)
    menu_items = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(menu_items, headers=columns, tablefmt="fancy_grid"))

# Function to place an order
def place_order():
    a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
    y = a.cursor()
    customer_name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    dish_id = int(input("Enter the Dish ID from the menu: "))
    quantity = int(input("Enter the quantity: "))
    
    # Fetch dish details from menu
    query = "SELECT Dish_Name, Price FROM menu WHERE Dish_ID = {}".format(dish_id)
    y.execute(query)
    dish_details = y.fetchone()
    
    if not dish_details:
        print("Invalid Dish ID. Please try again.")
        return
    
    dish_name = dish_details[0]
    dish_price = dish_details[1]
    total_price = dish_price * quantity

    # Insert order details into orders table
    order_id = random.randint(10000, 99999)
    insert_query = "INSERT INTO orders (Order_ID, Customer_Name, Phone_Number, Dish_Name, Quantity, Total_Price) VALUES ({}, '{}', '{}', '{}', {}, {})".format(order_id, customer_name, phone_number, dish_name, quantity, total_price)
    y.execute(insert_query)
    a.commit()
    print("Order placed successfully! Your order ID is: ", order_id)

# Function to show customer orders
def view_orders():
    a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
    y = a.cursor()
    phone_number = input("Enter your phone number to view your orders: ")
    query = "SELECT * FROM orders WHERE Phone_Number = '{}'".format(phone_number)
    y.execute(query)
    orders = y.fetchall()
    columns = [i[0] for i in y.description]
    print(tabulate(orders, headers=columns, tablefmt="fancy_grid"))

# Function to cancel an order
def cancel_order():
    a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
    y = a.cursor()
    order_id = int(input("Enter the Order ID to cancel: "))
    delete_query = "DELETE FROM orders WHERE Order_ID = {}".format(order_id)
    y.execute(delete_query)
    a.commit()
    print("Order canceled successfully!")

# Function to provide feedback
def give_feedback():
    a = mysql.connector.connect(host="localhost", user="root", password="0249", database="cafe_management")
    y = a.cursor()
    customer_name = input("Enter your name: ")
    feedback_text = input("Please provide your feedback: ")
    insert_query = "INSERT INTO feedback (Customer_Name, Feedback) VALUES ('{}', '{}')".format(customer_name, feedback_text)
    y.execute(insert_query)
    a.commit()
    print("Thank you for your feedback!")

# Admin functionalities
def admin_menu():
    while True:
        print("\n***** Admin Menu *****")
        print("1. Show Employee Details")
        print("2. Show Menu")
        print("3. View Orders")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_employee_details()
        elif choice == 2:
            show_menu()
        elif choice == 3:
            view_orders()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

# Customer functionalities
def customer_menu():
    while True:
        print("\n***** Customer Menu *****")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Cancel Order")
        print("5. Provide Feedback")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            show_menu()
        elif choice == 2:
            place_order()
        elif choice == 3:
            view_orders()
        elif choice == 4:
            cancel_order()
        elif choice == 5:
            give_feedback()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

# Main function to start the program
def main():
    while True:
        print("\n***** Welcome to Café Management System *****")
        print("1. Admin Login")
        print("2. Customer")
        print("3. Exit")
        user_type = int(input("Who are you? Enter your choice: "))
        if user_type == 1:
            admin_username = input("Enter Admin Username: ")
            admin_password = input("Enter Admin Password: ")
            if admin_username == "shubh" and admin_password == "0249": 
                admin_menu()
            else:
                print("Invalid credentials. Please try again.")
        elif user_type == 2:
            customer_menu()
        elif user_type == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
