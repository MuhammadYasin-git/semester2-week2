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
    print("1 - List All Product Categories")
    print("2 - Total Number of Customers")
    print("3 - Orders for a Customer")
    print("4 - All products priced below £2")
    print("Q - quit")
    choice = -1
    while (choice not in ["1","2","3","4","5","Q"]):
        choice = input("Enter your choice: ").upper()
    return choice


def main():

    db = get_connection()

    db.close()


if __name__=="__main__":
    main()