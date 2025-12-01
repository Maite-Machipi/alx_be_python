# book_class.py

class Book:
    """A class representing a book using Python magic methods."""

    def __init__(self, title, author, year):
        """Initialize the book with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor prints a message when a book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
