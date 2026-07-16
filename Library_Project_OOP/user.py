# OOP Library User Class Samuel Marriott

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
            f"User ID: {self.__user_id}\n"
            f"Active: {'Yes' if self.is_active else 'No'}"
        )
    
    def deactivate(self):
        self.is_active = False

user1 = User("Alice", "U001")
user2 = User("Bob", "U002")

# User information
info_user1 = user1.display_info()
info_user2 = user2.display_info()
print(info_user1)
print(info_user2)

# Test number of users
print(f"Number of users: {User.num_of_users}")