# Book class which defines an object with a title, author, price, and stock amount
class Book:
    def __init__(self, title, author, isbn, genre, publication_date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.status = "available"

    # Title getter and setter
    def get_title(self):
        return self.title
    
    def set_title(self, new_title):
        self.title = new_title

    # Author getter and setter
    def get_author(self):
        return self.author
    
    def set_author(self, new_author):
        self.author = new_author
    
    # ISBN getter and setter
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
    
    # Genre getter and setter
    def get_genre(self):
        return self.genre
    
    def set_genre(self, new_genre):
        self.genre = new_genre
    
    # Publication date getter and setter
    def get_publication_date(self):
        return self.publication_date
    
    def set_publication_date(self, new_publication_date):
        self.publication_date = new_publication_date

    # Status getter and setter
    def get_status(self):
        return self.status
    
    def set_status(self, new_status):
        self.status = new_status

    def change_status(self):
        if (self.status == "available"):
            self.status = "booked"
        else:
            self.status = "available"
    
    def is_available(self):
        return self.status == "available"
    
    # Decrease stock by 1 when a book is checkedout
    def checkout_book(self):
        if (self.stock) < 1:
            print("No available stock.")
        else:
            self.stock -= 1
    
    # Increment stock by 1 when a book is returned to library
    def checkin_book(self):
        self.stock  += 1
    
    # Function to display all information about this book
    def display_book_info(self):
        print(f"Title: {self.get_title()}, "
            f"Author: {self.get_author()}, "
            f"ISBN: {self.get_isbn()}, "
            f"Genre: {self.get_genre()}, "
            f"Publication date: {self.get_publication_date()}, "
            f"Status: {self.get_status()}")