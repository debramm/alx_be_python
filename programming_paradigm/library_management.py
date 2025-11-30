class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private availability flag

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check availability."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private book list

    def add_book(self, book):
        """Add a book instance to the collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Find book by title and check it out."""
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book '{title}' not found.")

    def return_book(self, title):
        """Find book by title and return it."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book '{title}' not found.")

    def list_available_books(self):
        """Print all books that are not checked out."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")