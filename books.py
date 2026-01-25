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


result = run_query("""CREATE TABLE IF NOT EXISTS books (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     title TEXT NOT NULL,
     author TEXT NOT NULL,
     genre TEXT,
     status TEXT CHECK(status IN ('read','unread')),
     review TEXT,
     stock BOOLEAN,
     medium TEXT CHECK(medium IN ('physical','ebook','audiobook')))""")


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

class Book():
    def __init__(self, id, title, author, genre, status, review, stock, medium):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status
        self.review = review
        self.stock = stock
        self.medium = medium


# to add books:
# cursor.execute("INSERT INTO books VALUES(for each row)")
def create_item():
    book.title = input("Title: ")
    book.author = input("Author: ")
    book.genre = ("Add the book\'s genre or type 'pass'")
        if input == 'pass':
            book.genre = 'NULL'
    book.status = input("Type 'read' or 'unread, or type 'pass'. ")
        if input == 'pass':
            book.status = 'NULL'
    book.review = input("If you've read the book, add what you thought of it! If not, type 'pass'. ")
        if input == 'pass':
            book.review = 'NULL'
    book.stock = input("Do you own this book? Type y/n, or just type 'pass'. ")
        if input == 'y':
            book.stock = 'TRUE'
        if input == 'n':
            book.stock = 'FALSE'
        if unput == 'pass':
            book.stock = 'NULL'
    book.medium = input("Finally, in what form to you own the book? List 'physical', 'ebook', or 'audiobook, or type 'pass'. ")
        if input == 'pass':
            book.medium = 'NULL'
            
    


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
