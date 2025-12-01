# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    """Class representing a digital book, inherits from Book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB


class PrintBook(Book):
    """Class representing a physical book, inherits from Book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """A library that contains and manages a collection of books."""

    def __init__(self):
        self.books = []  # Composition: Library HAS books

    def add_book(self, book):
        """Add any type of book into the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
