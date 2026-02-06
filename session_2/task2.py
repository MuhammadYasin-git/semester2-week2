import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def menu():
    '''
    Prints menu and prompts for choice
    Returns choice (string)
    '''
    print("1 - Total Spent Per Customer")
    print("2 - Total Number of Customers")
    print("3 - Orders for a Customer")
    print("4 - All products priced below £2")
    print("Q - quit")
    choice = -1
    while (choice not in ["1","2","3","4","5","Q"]):
        choice = input("Enter your choice: ").upper()
    return choice

def top_5_spenders(db):
    '''
    Shows all product Names
    '''
    query = "SELECT category FROM products;"
    cursor = db.execute(query)
    # where we know we should have multiple results, we can iterate over the cursor.
    for product in cursor:
        print(f"Name: {product['category']}")

def count_customer(db):
    '''
    Shows number of Customers
    '''
    query = "SELECT COUNT(customer_id) FROM customers;"
    cursor = db.execute(query)
    # where we know we should have multiple results, we can iterate over the cursor.
    for customer in cursor:
        print(f"Number of Customers: {customer[0]}")

def view_order_customer(db):
    choice = ""
    while(choice==""):
        choice = input("Enter Customer Email ")
    query = '''
            SELECT orders.order_id
            FROM orders JOIN customers
            ON customers.customer_id = orders.customer_id
            where customers.email =?;
            '''
    cursor = db.execute(query, (choice,))
    for customer in cursor:
        print(f"Order: {customer[0]}")

def price_less_2(db):
    '''
    Shows all product Names
    '''
    query = '''SELECT DISTINCT name , price
            FROM products
            WHERE price < 2
            '''
    cursor = db.execute(query)
    # where we know we should have multiple results, we can iterate over the cursor.
    for product in cursor:
        print(f"Products: {product[0]}, Price: {product[1]} ")



def main():

    db = get_connection()

    while 1:
        choice = menu()
        match(choice):
            case "1":
                all_product(db)
            case "2":
                count_customer(db)
            case "3":
                view_order_customer(db)
            case "4":
                price_less_2(db)
            case "Q":
                exit()
    db.close()


if __name__=="__main__":
    main()