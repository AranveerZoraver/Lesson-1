class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"sorry, '{self.title}' is already borrowed")
        else:
            self.is_borrowed = True
            print(f"you have borrowed '{self.title}' by {self.author}.")

    def return_book(self):
        if not self 
