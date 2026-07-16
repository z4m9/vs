# OOP Library Book Class - Samuel Marriott

class Book:

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

    def __str__(self):
        return f"{self.__title} by {self.__author}"

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee", False)

# Book information
info1 = book1.display_info()
info2 = book2.display_info()
print(info1)
print(info2)
print(book1) # str dunder

# Test class variable
print(f"Number of books: {Book.num_of_books}")
print(f"Borrow duration limit: {Book.borrow_limit}")
print(f"Book 1 borrow duration limit: {book1.borrow_limit}")

# Test attribute shadowing
book1.borrow_limit = 7
print(f"Borrow duration limit: {Book.borrow_limit}")
print(f"Book 1 borrow duration limit: {book1.borrow_limit}")
print(f"Book 2 borrow duration limit: {book2.borrow_limit}")