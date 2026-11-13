books = ["Python Basics", "Data Science", "Web Dev", "AI Intro"]
copies = [3, 0, 2, 5]
late_fees = [1.5, 2.0, 1.0, 2.5]

library_stock = {book: count for book, count in zip(books, copies)}

available_books = [book for book, count in library_stock.items() if count > 0]
print("Available books:", available_books)

choice = input("Which book would you like to borrow? ")

if choice not in available_books:
    print("Sorry, that book is unavailable.")
    exit()

updated_fees = list(map(lambda fee: fee + 0.5, late_fees))
library_stock[choice] -= 1

print("Updated late fees:", updated_fees)
print("Copies left of", choice + ":", library_stock[choice])