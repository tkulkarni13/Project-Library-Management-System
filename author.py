# Author class which defines an object with a name, and biography
class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    # Name getter and setter
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name

    # Biography getter and setter
    def get_biography(self):
        return self.biography
    
    def set_biography(self, new_biography):
        self.biography = new_biography
    
    # Method to display author's name and biography
    def display_author_info(self):
        print(f"Name: {self.name}, Biography: {self.biography}")