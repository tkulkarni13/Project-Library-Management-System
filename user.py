# User class which defines a new object with a name, library id, and borrowed books is initialized to an empty list
class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.borrowed_books = []
    
    # Name getter and setter
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    # Library ID getter and setter
    def get_library_id(self):
        return self.library_id
    
    def set_library_id(self, new_library_id):
        self.library_id = new_library_id

    # Method to checkout a book for a specific user
    def checkout_book(self, book):
        self.borrowed_books.append(book)
    
    # Method to return a checked out book
    def return_book(self, book):
        if (book not in self.borrowed_books):
            print(f"{book} was never check out by {self.name}") # Notify user if book was never checked out by this user
        else:
            self.borrowed_books.remove(book)

    # Method to display a user's name, id, and borrowed books
    def display_user_info(self):
        print(f"Name: {self.name}, Library ID: {self.library_id}, Borrowed Books: {self.borrowed_books}")