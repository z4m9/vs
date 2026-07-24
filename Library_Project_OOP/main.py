# OOP Library Main - Samuel Marriott

from book import FictionBook, ReferenceBook
from user import StudentUser, StaffUser, AdminUser

#student_borrow_limit = 14
#staff_borrow_limit = 28
#admin_borrow_limit = 56

# User objects
student1 = StudentUser("Alice Johnson", "S001", 11)
staff = StaffUser("Bob Smith", "ST001", "Maths")
admin = AdminUser("Charlie Brown", "A001", "Librarian")

# Book objects
fiction = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
reference = ReferenceBook("Encyclopedia Britannica", "Various Authors", "Reference")

# Group objects into lists
users = [student1, staff, admin]
books = [fiction, reference]

# Display user information
def display_users(users):
    print("User Information:")
    print("-----------------")
    for user in users:
        print(user.display_info())
        print(f"Loan period: {user.get_loan_period()} days")
        print()

# Display book information
def display_books(books):
    print("Book Information:")
    print("-----------------")
    for book in books:
        print(book.display_info())
        print(book.borrow_item())
        print()

# Call functions to display user and book information
display_users(users)
display_books(books)

# Abstraction
'''Borrow limits for different user types
student_borrow_limit = 14
staff_borrow_limit = 28
admin_borrow_limit = 56

# Subclass objects (User)
student1 = StudentUser("Charlie Ward", "S001", "Student")
staff1 = StaffUser("David Smith", "ST001", "Staff Member")
admin1 = AdminUser("Eve Johnson", "A001", "Library Admin")

print(student1.display_info())
print(staff1.display_info())
print(admin1.display_info())
#users = [student1, staff1, admin1]
student = StudentUser("Ava", "S001", 11)
student_days = student.get_loan_period()
print(f"A student can borrow items for {student_days} days.")

staff = StaffUser("John", "ST001", "Library Staff")
staff_days = staff.get_loan_period()
print(f"A staff member can borrow items for {staff_days} days.")

admin = AdminUser("Emma", "A001", "Library Admin")
admin_days = admin.get_loan_period()
print(f"An admin can borrow items for {admin_days} days.")
print()

# Subclass objects (Book)
fiction1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
reference1 = ReferenceBook("Encyclopedia Britannica", "Various Authors", "Reference")

print(fiction1.display_info())
print(fiction1.borrow_item())

print(f"\n{reference1.display_info()}")
print(reference1.borrow_item())'''


# Inheritance
'''Book objects
#book1 = Book("1984", "George Orwell")
#book2 = Book("To Kill a Mockingbird", "Harper Lee", False)

# User Objects
#user1 = User("Alice", "U001")
#user2 = User("Bob", "U002")

#for user in users:
 #   print(user.display_info())
  #  print()

#books = [fiction1, reference1]

#print()
#for book in books:
#    print(book.display_info())
 #   print()

# Testing the take_leave method for StaffUser
#student1.take_leave()  # This will raise an AttributeError since StudentUser does not have a take_leave method'''