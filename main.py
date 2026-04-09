"""
Main file for the Library Management System.
This program allows the user to manage books, members, and loans.
"""

from library import Library


def display_menu():
    """Display the main menu."""
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. View All Members")
    print("7. Save Data")
    print("8. Exit")


def main():
    """Run the main program."""
    library = Library()
    library.load_data()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        try:
            if choice == "1":
                book_id = input("Enter book ID: ")
                title = input("Enter book title: ")
                author = input("Enter author name: ")
                result = library.add_book(book_id, title, author)
                print(result)

            elif choice == "2":
                member_id = input("Enter member ID: ")
                name = input("Enter member name: ")
                result = library.add_member(member_id, name)
                print(result)

            elif choice == "3":
                loan_id = input("Enter loan ID: ")
                book_id = input("Enter book ID: ")
                member_id = input("Enter member ID: ")
                due_date = input("Enter due date (YYYY-MM-DD): ")
                result = library.borrow_book(loan_id, book_id, member_id, due_date)
                print(result)

            elif choice == "4":
                book_id = input("Enter book ID: ")
                member_id = input("Enter member ID: ")
                result = library.return_book(book_id, member_id)
                print(result)

            elif choice == "5":
                library.display_books()

            elif choice == "6":
                library.display_members()

            elif choice == "7":
                library.save_data()

             elif choice == "8":
                  print("Exiting program. Goodbye!")
                  break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

        except Exception as error:
            print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
