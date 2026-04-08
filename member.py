"""
Member class for the Library Management System.
"""

class Member:
    """Represents a library member."""

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_info(self):
        """Display member details."""
        print(f"Member ID: {self.member_id}, Name: {self.name}, Borrowed Books: {self.borrowed_books}")

    def borrow_book(self, book_id):
        """Add a book to the member's borrowed list."""
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        """Remove a book from the member's borrowed list."""
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)

    def to_file_string(self):
        """Convert member data to a string for file storage."""
        borrowed = "|".join(self.borrowed_books)
        return f"{self.member_id},{self.name},{borrowed}\n"
