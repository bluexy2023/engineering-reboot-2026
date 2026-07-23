from book import Book
from library import Library


book1 = Book("First Book", "Glenn", "1")
book2 = Book("Second Book", "Thotho", "2")
book3 = Book("Third Book", "Mhegz", "3")


library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

ret = library.find_book_by_title("Third Book")

print(f"Found book: {ret.display()}")

ret2 = library.find_book_by_isbn("1")
print (f"Found by ISBN 1: {ret2.display()}")

if library.remove_book("2"):
   library.display_books()