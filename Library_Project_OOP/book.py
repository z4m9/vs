# OOP Library Book Class - Samuel Marriott

# Importing from Abstract Base Classes (ABC) module
from abc import ABC, abstractmethod

class Book(ABC):

    num_of_books = 0
    borrow_limit = 30

    def __init__(self, title, author, available = True):
        self.__title = title
        self.__author = author
        self.available = available
        Book.num_of_books += 1

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, new_title):
        new_title = new_title.strip()

        if 1 <= len(new_title) <= 100:
            self.__title = new_title
        else:
            print("Error: Title must be between 1 and 100 characters.")
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, new_author):
        new_author = new_author.strip()

        if len(new_author) >= 1:
            self.__author = new_author
        else:
            print("Error: Author name must not be blank.")

    def display_info(self):
        return (
            f"Title: {self.__title}\n"
            f"Author: {self.__author}\n"
            f"Available: {'Yes' if self.available else 'No'}"
        )
    
    # Abstraction
    @abstractmethod
    def borrow_item(self):
        pass

    def __str__(self):
        return f"{self.__title} by {self.__author}"

# Inheritance - Subclasses
class FictionBook(Book):
    def __init__(self, title, author, genre, available = True):
        super().__init__(title, author, available)
        self.__genre = genre

    @property
    def genre(self):
        return self.__genre
    
    def get_summary(self):
        return f"{self.title} is a {self.__genre} fiction book by {self.author}."
    
    def display_info(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.__genre}\n"
            f"Available: {'Yes' if self.available else 'No'}"
        )
    
    def borrow_item(self):
        if self.available:
            self.available = False
            return f"You have borrowed '{self.title}'."
        else:
            return f"'{self.title}' has already been borrowed."

class ReferenceBook(Book):
    def __init__(self, title, author, library_section, available = True):
        super().__init__(title, author, available)
        self.__library_section = library_section
    
    @property
    def library_section(self):
        return self.__library_section
    
    def find_location(self):
        return f"{self.title} is in the {self.__library_section} section."
    
    def display_info(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Library Section: {self.__library_section}\n"
            f"Available: {'Yes' if self.available else 'No'}"
        )
    
    def borrow_item(self):
        return f"'{self.title}' is for library use only."

#book1 = Book("1984", "George Orwell")
#book2 = Book("To Kill a Mockingbird", "Harper Lee", False)

# Book information
#info1 = book1.display_info()
#info2 = book2.display_info()
#print(info1)
#print(info2)