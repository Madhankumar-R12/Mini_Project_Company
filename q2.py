# q2_library_system.py

catalog = {}

catalog[101] = ("Python Basics", "John Smith", 2020)
catalog[102] = ("Data Structures", "Alice Brown", 2019)
catalog[103] = ("Machine Learning", "David Lee", 2021)
catalog[104] = ("AI Fundamentals", "Emma Wilson", 2022)

borrowed_books = []

members = set()

members.add(1)
members.add(2)
members.add(3)
members.add(2)

print("Registered Members:", members)

book_id = 101

if book_id in catalog:
    if book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book", book_id, "borrowed successfully")
    else:
        print("Book already borrowed")
else:
    print("Book does not exist")

book_id = 103

if book_id in catalog:
    if book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print("Book", book_id, "borrowed successfully")
    else:
        print("Book already borrowed")
else:
    print("Book does not exist")

print("Borrowed Books:", borrowed_books)

book_id = 101

if book_id in borrowed_books:
    borrowed_books.remove(book_id)
    print("Book", book_id, "returned successfully")
else:
    print("Book was not borrowed")

print("Borrowed Books After Return:", borrowed_books)

print("\nAvailable Books:")

for book_id in catalog:
    if book_id not in borrowed_books:
        title, author, year = catalog[book_id]
        print(book_id, "-", title, "|", author, "|", year)