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
        for book in self.books:
            if book.book_id == book_id:
                return "Book ID already exists."
        book = Book(book_id, title, author)
        self.books.append(book)
        return "Book added successfully."

    def add_member(self, member_id, name):
        """Add a new member to the library."""
        for member in self.members:
            if member.member_id == member_id:
                return "Member ID already exists."
        member = Member(member_id, name)
        self.members.append(member)
        return "Member added successfully."

    def borrow_book(self, loan_id, book_id, member_id, due_date):
        """Borrow a book if available."""
        selected_book = None
        selected_member = None

        for book in self.books:
            if book.book_id == book_id:
                selected_book = book
                break

        for member in self.members:
            if member.member_id == member_id:
                selected_member = member
                break

        if selected_book is None:
            return "Book not found."

        if selected_member is None:
            return "Member not found."

        if not selected_book.is_available:
            return "Book is already borrowed."

        selected_book.mark_borrowed()
        selected_member.borrow_book(book_id)

        loan = Loan(loan_id, book_id, member_id, due_date)
        self.loans.append(loan)

        return "Book borrowed successfully."

    def return_book(self, book_id, member_id):
        """Return a borrowed book."""
        selected_book = None
        selected_member = None

        for book in self.books:
            if book.book_id == book_id:
                selected_book = book
                break

        for member in self.members:
            if member.member_id == member_id:
                selected_member = member
                break

        if selected_book is None:
            return "Book not found."

        if selected_member is None:
            return "Member not found."

        selected_book.mark_returned()
        selected_member.return_book(book_id)

        for loan in self.loans:
            if loan.book_id == book_id and loan.member_id == member_id and loan.is_active:
                loan.close_loan()
                break

        return "Book returned successfully."

    def display_books(self):
        """Display all books."""
        if not self.books:
            print("No books available.")
        else:
            for book in self.books:
                book.display_info()

    def display_members(self):
        """Display all members."""
        if not self.members:
            print("No members available.")
        else:
            for member in self.members:
                member.display_info()
         
    def save_data(self):
        """Save books and members to a file."""
        try:
            with open("data.txt", "w") as file:
                # Save books
                file.write("BOOKS\n")
                for book in self.books:
                    file.write(book.to_file_string())

                # Save members
                file.write("MEMBERS\n")
                for member in self.members:
                    file.write(member.to_file_string())

            print("Data saved successfully.")

        except Exception as error:
            print(f"Error saving data: {error}")

    def load_data(self):
        """Load books and members from a file."""
        try:
            with open("data.txt", "r") as file:
                lines = file.readlines()

            mode = None

            for line in lines:
                line = line.strip()

                if line == "BOOKS":
                    mode = "books"
                    continue
                elif line == "MEMBERS":
                    mode = "members"
                    continue

                if not line:
                    continue

                if mode == "books":
                    parts = line.split(",")
                    book = Book(parts[0], parts[1], parts[2])
                    book.is_available = parts[3] == "True"
                    self.books.append(book)

                elif mode == "members":
                    parts = line.split(",")
                    member = Member(parts[0], parts[1])
                    if len(parts) > 2 and parts[2]:
                        member.borrowed_books = parts[2].split("|")
                    self.members.append(member)

        except FileNotFoundError:
            print("No previous data found. Starting fresh.")
        except Exception as error:
            print(f"Error loading data: {error}")
