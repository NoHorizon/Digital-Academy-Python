print("9-10")

from restaurant import Restaurant

my_restaurant = Restaurant("Pizza Palace", "Italian")
my_restaurant.describe_restaurant()

print("9-11")
from user_admin import Admin

admin = Admin("John", "Doe", "johndoe", "johndoe@gmail.com")
admin.privileges.show_privileges()

print("9-12")

from user import User
from privileges import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()


admin = Admin("John", "Doe", "johndoe", "johndoe@gmail.com")
admin.privileges.show_privileges()
