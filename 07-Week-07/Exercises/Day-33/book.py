# book.py - contains the definition for the class "Book"

class Book:
    def __init__(
        self,
        title: str,
        author: str,
        ISBN: str,
    ):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def display(self):
        return f"{self.title}, {self.author}, ISBN={self.ISBN}"


if __name__ == "__main__":
    book1 = Book("Harry Potter and the Sorcecer's Stone", "J.K. Rowling", "978-0747532699")
    book1.display()