# library.py - contains the definition for the class "Library"
# - imports Book class from book.py
# a Library has books
from book import Book

class Library:
    def __init__(self):
        self._books: list[Book] = []

    def add_book(self, book: Book,):
        self._books.append(book)

    def display_books(self):
        for book in self._books:
            print(book.display())

    def find_book_by_title(self, title: str) -> Book:
        for book in self._books:
            if book.title == title:
                return book
        return None
    def find_book_by_isbn(self, isbn: str) -> Book:
        for book in self._books:
            if book.ISBN == isbn:
                return book
        return None

    def remove_book(self, isbn: str) -> bool:
        book_to_remove = self.find_book_by_isbn(isbn)
        if book_to_remove is not None:
            self._books.remove(book_to_remove)
            print(f"[SUCCESS] Book \"{book_to_remove.display()}\" removed from the library.")
            return True
        print(f"[NOT FOUND] Book with ISBN: {isbn} does not exist in library.")
        return False