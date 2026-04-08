"""
Library class for the Library Management System.
"""

from book import Book
from member import Member
from loan import Loan


class Library:
    """Represents the full library system."""

    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []

    def add_book(self, book_id, title, author):
        """Add a new book to the library."""
        book = Book(book_id, title, author)
        self.books.append(book)

    def add_member(self, member_id, name):
        """Add a new member to the library."""
        member = Member(member_id, name)
        self.members.append(member)

    def borrow_book(self, loan_id, book_id, member_id, due_date):
        """Borrow a book if available."""
        for book in self.books:
            if book.book_id == book_id and book.is_available:
                book.mark_borrowed()
                for member in self.members:
                    if member.member_id == member_id:
                        member.borrow_book(book_id)
                        loan = Loan(loan_id, book_id, member_id, due_date)
                        self.loans.append(loan)
                        return "Book borrowed successfully."
        return "Book not available or member not found."

    def return_book(self, book_id, member_id):
        """Return a borrowed book."""
        for book in self.books:
            if book.book_id == book_id:
                book.mark_returned()
        for member in self.members:
            if member.member_id == member_id:
                member.return_book(book_id)
        for loan in self.loans:
            if loan.book_id == book_id and loan.member_id == member_id and loan.is_active:
                loan.close_loan()
        return "Book returned successfully."

    def display_books(self):
        """Display all books."""
        for book in self.books:
            book.display_info()

    def display_members(self):
        """Display all members."""
        for member in self.members:
            member.display_info()
