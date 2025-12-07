# library_system.py

class Book:
    def __init__(self, title, author):
        """
        Base Book class
        """
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class representing an electronic book
        """
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class representing a printed book
        """
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        """
        Library class using composition to manage books
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library collection
        """
        self.books.append(book)

    def list_books(self):
        """
        Prints details of each book in the library
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(
                    f"EBook: {book.title} by {book.author}, "
                    f"File Size: {book.file_size}KB"
                )
            elif isinstance(book, PrintBook):
                print(
                    f"PrintBook: {book.title} by {book.author}, "
                    f"Page Count: {book.page_count}"
                )
            else:
                print(f"Book: {book.title} by {book.author}")
