class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        self.books.append(Book(title))

    def show_books(self):
        for b in self.books:
            print(b.title, "Available" if b.available else "Not Available")

    def lend_book(self):
        title = input("Enter book title: ")
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self):
        title = input("Enter book title: ")
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned")
                return


lib = Library()

while True:
    print("1 Add Book")
    print("2 Show Books")
    print("3 Lend Book")
    print("4 Return Book")
    print("5 Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        lib.add_book()
    elif ch == "2":
        lib.show_books()
    elif ch == "3":
        lib.lend_book()
    elif ch == "4":
        lib.return_book()
    elif ch == "5":
        break
