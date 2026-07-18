# OOP Library Main - Samuel Marriott

from book import Book, FictionBook, ReferenceBook
from user import User, StudentUser, StaffUser, AdminUser

# Book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee", False)

# User Objects
user1 = User("Alice", "U001")
user2 = User("Bob", "U002")

# Subclass objects (User)
student1 = StudentUser("Charlie Ward", "S001", "Student")
staff1 = StaffUser("David Smith", "ST001", "Staff Member")
admin1 = AdminUser("Eve Johnson", "A001", "Library Admin")

users = [student1, staff1, admin1]

print()
for user in users:
    print(user.display_info())
    print()

# Subclass objects (Book)
fiction_book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
reference_book1 = ReferenceBook("Encyclopedia Britannica", "Various Authors", "Reference")

books = [fiction_book1, reference_book1]

print()
for book in books:
    print(book.display_info())
    print()

# Testing the take_leave method for StaffUser
#student1.take_leave()  # This will raise an AttributeError since StudentUser does not have a take_leave method