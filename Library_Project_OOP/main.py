# OOP Library Main - Samuel Marriott

from book import Book
from user import User

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee", False)

user1 = User("Alice", "U001")
user2 = User("Bob", "U002")

# Title getter testing
print("Original title:", book1.title)

book1.title = "1984"
print("After valid update:", book1.title)

book1.title = ""
print("After invalid update:", book1.title)

print(book1.display_info())
print(book2.display_info())
print(user1.display_info())

print(f"{user1.name} has borrowed {book1.title}.")