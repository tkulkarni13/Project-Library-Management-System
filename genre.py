class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    # Name getter and setter
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Description getter and setter
    def get_description(self):
        return self.description
    
    def set_description(self, new_description):
        self.description = new_description

    # Category getter and setter
    def get_category(self):
        return self.category
    
    def set_category(self, new_category):
        self.category = new_category

    # Method to display a genre's name, description, and category
    def display_genre_info(self):
        print(f"Name: {self.name}, Description: {self.description}, Category: {self.category}")