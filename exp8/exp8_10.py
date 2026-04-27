class Book:
    def __init__(self, title, author, price):
        self.title  = title
        self.author = author
        self.price  = price

    def __str__(self):
        return (f"Title : {self.title}\n"
                f"Author: {self.author}\n"
                f"Price : Rs.{self.price}")

b = Book("Python 101", "Guido", 499)
print(b)