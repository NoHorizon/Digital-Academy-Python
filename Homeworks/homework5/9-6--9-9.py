print("9-6")

class Restaurant:
    """Restaurant class"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")


class IceCreamStand(Restaurant):
    """Ice cream stand class"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand("Cold Delights", "Ice Cream Shop")

ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint"]

ice_cream_stand.display_flavors()


print("9-7")

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User Profile: {self.username}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")


class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("John", "Doe", "johndoe", "johndoe@gmail.com")
user1 = User("David", "Chartolani", "davidch", "d.chartolani@gmail.com")

admin.greet_user()
admin.show_privileges()

print("9-8")

class User:
    def __init__(self, first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print(f"User Profile: {self.username}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Welcome, {self.first_name} {self.last_name}!")


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()

admin = Admin("John", "Doe", "johndoe", "johndoe@example.com")

admin.privileges.show_privileges()
