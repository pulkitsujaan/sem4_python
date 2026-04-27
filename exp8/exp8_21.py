class Book:
    def __init__(self, title):
        self.title    = title
        self.is_issued = False

class User:
    def __init__(self, name):
        self.name  = name
        self.books = []

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def issue_book(self, title, user):
        for b in self.books:
            if b.title == title and not b.is_issued:
                b.is_issued = True
                user.books.append(b)
                print(f"'{title}' issued to {user.name}")
                return
        print(f"'{title}' not available.")

    def return_book(self, title, user):
        for b in user.books:
            if b.title == title:
                b.is_issued = False
                user.books.remove(b)
                print(f"'{title}' returned.")
                return

lib  = Library()
lib.add_book(Book("Python 101"))
u    = User("Pulkit")
lib.issue_book("Python 101", u)
lib.return_book("Python 101", u)