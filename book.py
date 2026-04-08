"""
Book class for the Library Management System.
"""

class Book:
    """Represents a book in the library."""

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        """Display book details."""
        status = "Available" if self.is_available else "Borrowed"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")

    def mark_borrowed(self):
        """Mark the book as borrowed."""
        self.is_available = False

    def mark_returned(self):
        """Mark the book as returned."""
        self.is_available = True

    def to_file_string(self):
        """Convert the book data to a string for file storage."""
        return f"{self.book_id},{self.title},{self.author},{self.is_available}\n"
