from book import Book
from library import Library


book1 = Book(
    title="Clean Code: A Handbook of Agile Software Craftsmanship",
    author="Robert C. Martin",
    isbn="978-0132350884",
)

book2 = Book(
    title="The Pragmatic Programmer: Your Journey to Mastery",
    author="Andrew Hunt & David Thomas",
    isbn="978-0135957059",
)


book3 = Book(
    title="The C Programming Language",
    author="Brian W. Kernighan & Dennis M. Ritchie",
    isbn="978-0131103627",
)

# Initialize Library
library = Library()

# Adding multiple books
sample_books = [book1, book2, book3]
for book in sample_books:
   library.add_book(book)

# Searching for an existing book
c_programming_book = library.find_book_by_title("the c programming language")
if c_programming_book is not None:
   print(f"Found book object")
   print(f"{c_programming_book.display()}")
else:
   print("Book not found.")

# Searching for a missing book
non_existent_book = library.find_book_by_title("seven habbits of successful people")
if non_existent_book is None:
   print ("Book not found.")
else:
   print(f"Found book object")
   print(f"{non_existent_book.display()}")

# Remove an existing book
ret_val = library.remove_book("978-0135957059")

# Attempting to remove a non-existing book
ret_val = library.remove_book("abc-123")

# Book count
print(f"Library book count: {library.total_books()}")



   
