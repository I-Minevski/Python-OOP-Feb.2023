class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title) -> (Book, None):
        for book in self.books:
            if book.title == title:
                return book
        return None


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book1.turn_page(50)

book2 = Book("The Lord of the Rings", "J.R.R Tolkien")
book2.turn_page(100)

lib1 = Library()
lib1.add_book(book2)
lib1.add_book(book1)

print(lib1.find_book("The Lord of the Rings").author)