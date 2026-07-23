# book.py - contains the definition for the class "Book"

class Book:
    def __init__(
        self,
        title: str,
        author: str,
        isbn: str,
    ):
        self.title = title
        self.author = author
        self.ISBN = isbn

    def display(self):
        return f"{self.title}, {self.author}, ISBN={self.ISBN}"
