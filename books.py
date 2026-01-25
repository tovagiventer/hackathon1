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

# connection = sqlite3.connect ('book_organizer.db')

# cursor = connection.cursor()

# command1 = """CREATE TABLE IF NOT EXISTS books (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     author TEXT NOT NULL,
#     genre TEXT,
#     status TEXT CHECK(status IN ('read','unread')),
#     rating INTEGER,
#     review TEXT,
#     in_stock BOOLEAN (in_stock IN ('yes', 'no')),
#     medium TEXT CHECK(medium IN ('physical','ebook','audiobook')))"""

# cursor.execute(command1)
# connection.commit()
# connection.close()

# to add books:
# cursor.execute("INSERT INTO books VALUES(for each row)")

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
