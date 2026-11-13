class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"Sorry, '{self.title}' is already borrowed.")
        else:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}'.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

print(book1)
print(book2)

book1.borrow()
print(book1)

book1.borrow()

book1.return_book()
print(book1)

book1.return_book()