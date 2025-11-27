# library_management.py

class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if book is not checked out."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""

    def __init__(self):
        self._books = []  # Private book list

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by title."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                break

    def return_book(self, title):
        """Attempt to return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                break

    def list_available_books(self):
        """Print all available books in 'Title by Author' format."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")


def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()


if __name__ == "__main__":
    main()
