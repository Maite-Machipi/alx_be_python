# library_system.py

class Book:
    """Base class representing a general book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a normal book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Class representing a digital book, inherits from Book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

    def __str__(self):
        """String representation for an ebook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Class representing a physical book, inherits from Book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for a printed book."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """A library that contains and manages a collection of books."""

    def __init__(self):
        self.books = []  # Composition: Library HAS books

    def add_book(self, book):
        """Add any type of book into the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library using __str__."""
        for book in self.books:
            print(book)
