"""
Loan class for the Library Management System.
"""

class Loan:
    """Represents a loan of a book to a member."""

    def __init__(self, loan_id, book_id, member_id, due_date):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.due_date = due_date
        self.is_active = True

    def display_loan(self):
        """Display loan details."""
        status = "Active" if self.is_active else "Closed"
        print(
            f"Loan ID: {self.loan_id}, Book ID: {self.book_id}, "
            f"Member ID: {self.member_id}, Due Date: {self.due_date}, Status: {status}"
        )

    def close_loan(self):
        """Mark the loan as closed."""
        self.is_active = False

    def is_overdue(self, current_date):
        """Check if the loan is overdue."""
        return self.is_active and current_date > self.due_date

    def to_file_string(self):
        """Convert loan data to a string for file storage."""
        return f"{self.loan_id},{self.book_id},{self.member_id},{self.due_date},{self.is_active}\n"
