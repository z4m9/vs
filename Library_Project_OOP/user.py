# OOP Library User Class Samuel Marriott
from abc import ABC, abstractmethod

class User:
    num_of_users = 0

    def __init__(self, name, user_id, is_active = True):
        self.__name = name
        self.__user_id = user_id
        self.is_active = is_active
        User.num_of_users += 1
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        new_name = new_name.strip()

        if 0 < len(new_name) <= 50:
            self.__name = new_name
        else:
            print("Error: Name must not be blank, cannot exceed 50 characters.")
    
    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, new_user_id):
        new_user_id = new_user_id.strip()

        if len(new_user_id) > 0:
            self.__user_id = new_user_id
        else:
            print("Error: User ID must not be blank.")
    
    def display_info(self):
        return (
            f"Name: {self.__name}\n"
            f"ID: {self.__user_id}\n"
            f"Active: {'Yes' if self.is_active else 'No'}"
        )
    
    def deactivate(self):
        self.is_active = False

class LibraryUser(User, ABC):
    @abstractmethod
    def get_loan_period(self):
        pass

class StudentUser(LibraryUser):
    def __init__(self, name, user_id, year_level):
        self.__year_level = year_level
        super().__init__(name, user_id)
    
    @property
    def year_level(self):
        return self.__year_level

    def pay_fees(self):
        print(f"{self.name} has paid their fees.")
    
    def display_info(self):
        return (
            f"Student: {self.name}\n"
            f"ID: {self.user_id}\n"
            f"Active: {'Yes' if self.is_active else 'No'}\n"
        )
    
    def get_loan_period(self):
        print("Loan period for Student users is", 14, "days.")

class StaffUser(LibraryUser):
    def __init__(self, name, user_id, department):
        self.__department = department
        super().__init__(name, user_id)
    
    @property
    def department(self):
        return self.__department

    def take_leave(self):
        print(f"{self.name} is taking leave.")
    
    def display_info(self):
        return (
            f"Staff: {self.name}\n"
            f"ID: {self.user_id}\n"
            f"Active: {'Yes' if self.is_active else 'No'}\n"
        )
    
    def get_loan_period(self):
        print("\nLoan period for Staff users is", 28, "days.")

class AdminUser(LibraryUser):
    def __init__(self, name, user_id, role):
        self.__role = role
        super().__init__(name, user_id)

    @property
    def role(self):
        return self.__role
    
    def manage_users(self):
        print(f"{self.name} is managing users.")
    
    def display_info(self):
        return (
            f"Admin: {self.name}\n"
            f"ID: {self.user_id}\n"
            f"Active: {'Yes' if self.is_active else 'No'}\n"
        )
    
    def get_loan_period(self):
        print("\nLoan period for Admin users is", 56, "days.")
    
#user1 = User("Alice Zhou", "U001")
#user2 = User("Bob Lee", "U002")

#info1 = user1.display_info()
#info2 = user2.display_info()
#print(info1)
#print(info2)