from book import Book
from user import User
from author import Author
from genre import Genre

# Functions to print instructions to the user depending on which part of the appilcation they are using
def print_main_menu_instruction():
    print("Main Menu:")
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Genre Operations")
    print("5. Quit")

def print_book_operations():
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")

def print_user_operations():
    print("User Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")

def print_author_operations():
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")

def print_genre_operations():
    print("Genre Operations:")
    print("1. Add a new genre")
    print("2. view genre details")
    print("3. Display all genres")

# Main method which handles the command-line interface and interaction with user
def main():
    print_main_menu_instruction() # Print options for user
    # The following lists keep track of every new object created, and they are stored in their respective category
    all_books = []
    all_users = []
    all_authors = []
    all_genres = []

    while True: # Loop until terminated by user
        # try except block to make sure user input is an integer - This shows up everytime we use 'int(input("..."))'
        try:
            user_input_1 = int(input("Please select a number from the menu above: "))
        except ValueError:
            print("Please enter a valid digit.")
        else:
            # Book Operations
            if (user_input_1 == 1):
                print_book_operations() # Print options for user
                try:
                    user_input_2 = int(input("Please select a number from the options above: "))
                except ValueError:
                    print("Please enter a valid digit")
                else:
                    # Add a new book
                    if (user_input_2 == 1):
                        title = input("Please enter the title of the books you'd like to add: ")
                        author = input("Author: ")
                        isbn = input("ISBN: ")
                        genre = input("Genre: ")
                        publication_date = input("Publication Date: ")
                        book = Book(title, author, isbn, genre, publication_date)
                        all_books.append(book)
                        print_main_menu_instruction()

                    # Borrow a book
                    elif (user_input_2 == 2):
                        title_or_isbn = input("Please enter the title of the book, or the isbn of the book you'd like to checkout: ")
                        user_id = input("Please enter the library ID of the user checking out this book: ")
                        requested_book = None
                        requested_user = None
                        for user in all_users:
                            if (user_id == user.get_library_id()):
                                requested_user = user
                                for book in all_books:
                                    if (title_or_isbn == book.get_title() or title_or_isbn == book.get_isbn()):
                                        requested_book = book
                                        if (book.is_available()): # Make sure the book isn't currently checked out
                                            book.change_status()
                                            user.checkout_book(book.get_title())
                                            print(f"{user.get_name()} has checked out {book.get_title()}")
                                        else:
                                            print(f"{book.get_title()} is currently booked.")
                        if (requested_user == None):
                            print("The user you entered could not be found.")
                        if (requested_book == None):
                            print("The book your are searching for could not be found.")
                        print_main_menu_instruction()

                    # Return a book
                    elif (user_input_2 == 3):
                        title_or_isbn = input("Please enter the title of the book, or the isbn of the book you'd like to return: ")
                        user_id = input("Please enter the library ID of the user returning this book: ")
                        requested_book = None
                        requested_user = None
                        for user in all_users:
                            if (user_id == user.get_library_id()):
                                requested_user = user
                                for book in all_books:
                                    if (title_or_isbn == book.get_title() or title_or_isbn == book.get_isbn()):
                                        requested_book = book
                                        if (not book.is_available()): # Make sure the book has been checked out before returning
                                            book.change_status()
                                            user.return_book(book.get_title())
                                            print(f"{user.get_name()} has returned {book.get_title()}")
                                        else:
                                            print(f"{book.get_title()} has not been checkout yet.")
                        if (requested_book == None):
                            print("The book you are searching for could not be found.")
                        print_main_menu_instruction()

                    # Search for a book
                    elif (user_input_2 == 4):
                        title_or_isbn = input("Please enter the title of the book, or the isbn of the book you'd like to search for: ")
                        requested_book = None
                        for book in all_books: # Loop through all books in system until a match is found
                            if (title_or_isbn == book.get_title() or title_or_isbn == book.get_isbn()):
                                requested_book = book
                                book.display_book_info()
                        if (requested_book == None): # Notify user if no match is found
                            print("The book you are searching for could not be found.")
                        print_main_menu_instruction()

                    # Display all books
                    elif (user_input_2 == 5):
                        if  (len(all_books) < 1): # Check that at least one book is saved in the system
                            print("There have been no books added to the system.")
                        else:
                            for book in all_books: # Loop through all books and display all information about each book
                                book.display_book_info()
                        print_main_menu_instruction()

            # User Operations
            elif (user_input_1 == 2):
                print_user_operations()
                try:
                    user_input_2 = int(input("Please select a number from the options above: "))
                except ValueError:
                    print("Please enter a valid digit.")
                else:
                    # Add a new user
                    if (user_input_2 == 1):
                        name = input("Please enter the name of the user you'd like to add: ")
                        library_id = input("Please enter the library ID of the user: ")
                        user = User(name, library_id)
                        all_users.append(user)
                        print_main_menu_instruction()

                    # View user details
                    elif (user_input_2 == 2):
                        name_or_id = input("Please enter the name or library ID of the user you'd like to find: ")
                        requested_user = None
                        for user in all_users: # Loop through all users until a match is found
                            if (name_or_id == user.get_name() or name_or_id == user.get_library_id()):
                                requested_user = user
                                user.display_user_info()
                        if (requested_user == None): # If no match is found, notify user
                            print("The user you are searching for could not be found.")
                        print_main_menu_instruction()

                    # Display all users
                    elif (user_input_2 == 3):
                        if (len(all_users) < 1): # Check that at least one user has been added to the system
                            print("There have been no users added to the system.")
                        else:
                            for user in all_users: # Loop through all users and display their information
                                user.display_user_info()
                        print_main_menu_instruction()

                    else:
                        print("Please enter a digit from 1-3.")

            # Author Operations
            elif (user_input_1 == 3):
                print_author_operations()
                try:
                    user_input_2 = int(input("Please select a number from the options above: "))
                except ValueError:
                    print("Please enter a valid digit.")
                else:
                    # Add a new author
                    if (user_input_2 == 1):
                        name = input("Please enter the name of the author you'd like to add: ")
                        biography = input("Please enter the biography of the author: ")
                        author = Author(name, biography)
                        all_authors.append(author)
                        print_main_menu_instruction()
                    
                    # View author details
                    elif (user_input_2 == 2):
                        name = input("Please enter the name of the author you'd like to find: ")
                        requested_author = None
                        for author in all_authors: # Loop through all all authors until a match is found
                            if (name == author.get_name()):
                                requested_author = author
                                author.display_author_info()
                        if (requested_author == None): # Notify user if no match is found
                            print("The author you are searching for could not be found.")
                        print_main_menu_instruction()

                    # Display all authors
                    elif (user_input_2 == 3):
                        if (len(all_authors) < 1): # Check that at least one author is saved
                            print("There have been no authors added to the system.")
                        else:
                            for author in all_authors: # Loop through all authors and display their info
                                author.display_author_info()
                        print_main_menu_instruction()

                    else:
                        print("Please enter a digit from 1-3")

            # Genre Operations
            elif (user_input_1 == 4):
                print_genre_operations()
                try:
                    user_input_2 = int(input("Please select a number from the options above: "))
                except ValueError:
                    print("Please enter a valid digit.")
                else:
                    # Add a new genre
                    if (user_input_2 == 1):
                        name = input("Please enter the genre you'd like to add: ")
                        description = input("Please enter a description of the genre: ")
                        category = input("Please enter the category of the genre: ")
                        genre = Genre(name, description, category)
                        all_genres.append(genre)
                        print_main_menu_instruction()
                    
                    # View genre details
                    elif (user_input_2 == 2):
                        name = input("Please enter the name of the genre you'd like to find: ")
                        requested_genre = None
                        for genre in all_genres: # Loop through all genres until a match
                            if (name == genre.get_name()):
                                requested_genre = genre
                                genre.display_genre_info()
                        if (requested_genre == None): # Notify user if no match is found
                            print("The genre you are searching for could not be found.")
                        print_main_menu_instruction()

                    # Display all genres
                    elif (user_input_2 == 3):
                        if (len(all_genres) < 1): # Check that at least one genre is saved
                            print("There have been no genres added to the system.")
                        else:
                            for genre in all_genres: # Loop through all genres and print their info
                                genre.display_genre_info()
                        print_main_menu_instruction()

                    else:
                        print("Please enter a digit from 1-3")
            
            # Exit the loop and end the program
            elif (user_input_1 == 5):
                break

            else:
                print("Please enter a digit from 1-5.")

if __name__ == "__main__":
    main()