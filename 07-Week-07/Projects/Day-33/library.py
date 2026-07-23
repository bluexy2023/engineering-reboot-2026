# library.py - contains the definition for the class "Library"
# - imports Book class from book.py
# a Library has books
from book import Book

class Library:
    def __init__(self):
        self._books: list[Book] = []
        # Key: ISBN | Value: Direct reference to the Book object
        self.__isbn_map: dict[str, Book] = {}

    def add_book(self, book: Book) -> bool:
        if book.ISBN in self.__isbn_map:
            print(f"[DUPLICATE ISBN] Book \"{book.display()}\" already exists in the library.")
            return False
        
        self._books.append(book)
        self.__isbn_map[book.ISBN] = book
        return True
        

    def display_books(self) -> None:
        for book in self._books:
            print(book.display())

    def find_book_by_title(self, title: str) -> Book | None:
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_book_by_isbn(self, isbn: str) -> Book | None:
        return self.__isbn_map.get(isbn)

    def remove_book(self, isbn: str) -> bool:
        book_to_remove = self.find_book_by_isbn(isbn)
        if book_to_remove is not None:
            self._books.remove(book_to_remove)
            del self.__isbn_map[isbn]
            print(f"[SUCCESS] Book \"{book_to_remove.display()}\" removed from the library.")
            return True
        print(f"[NOT FOUND] Book with ISBN: {isbn} does not exist in library.")
        return False

    def total_books(self) -> int:
        return len(self._books)