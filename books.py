import sqlite3
from tabulate import tabulate

database_file = 'book_organizer.db'

def run_query(query):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

sql_string = """CREATE TABLE IF NOT EXISTS books (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT NOT NULL,
     author TEXT NOT NULL,
     genre TEXT,
     status TEXT CHECK(status IN ('read','unread')),
     review TEXT,
     stock BOOLEAN,
     medium TEXT CHECK(medium IN ('physical','ebook','audiobook')))"""

result = run_query(sql_string)


print(tabulate(result, headers=['id', 'title', 'author', 'genre', 'status', 'review', 'stock', 'medium']))

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Add entry")
        print("2. View books list")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_item()
        elif choice == "2":
            read_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            break
        else:
            print("Invalid option")

menu()

# to add books:
# cursor.execute("INSERT INTO books VALUES(for each row)")
def create_item():
    title = input("Title: ")
    author = input("Author: ")
    genre = ("Add the book\'s genre or type 'pass'")
    if genre == 'pass':
        genre = 'NULL'
    status = input("Type 'read' or 'unread, or type 'pass'. ")
    if status == 'pass':
        status = 'NULL'
    review = input("If you've read the book, add what you thought of it! If not, type 'pass'. ")
    if review == 'pass':
        review = 'NULL'
    stock = input("Do you own this book? Type y/n, or just type 'pass'. ")
    if stock == 'y':
        stock = 'TRUE'
    elif stock == 'n':
        stock = 'FALSE'
    else:
        stock = 'NULL'
    medium = input("Finally, in what form to you own the book? List 'physical', 'ebook', or 'audiobook, or type 'pass'. ")
    if medium == 'pass':
        medium = 'NULL'

    new_entry = """INSERT INTO books VALUES(f{title}, {author}, {genre}, {status}, {review}, {stock}, {medium})"""
    run_query(new-entry)

# to display table:
# cursor.execute("SELECT * from books")
# results = cursor.fetchall()
# print(results)

# to update-- status/stock/review:
# cursor.execute("UPDATE table_name WHERE column_name=?")
# step1=select row to edit by ilike
# step2=user pick row by id to edit
# step3=I update sql by row using id

# to delete books:
# cursor.execute("DELETE FROM table_name WHERE column_name=?")
