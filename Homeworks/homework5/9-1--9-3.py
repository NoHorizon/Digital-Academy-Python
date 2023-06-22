print("9-1")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")


restaurant = Restaurant("Machakhella", "Georgian Cuisine")

print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

restaurant.describe_restaurant()
print()
restaurant.open_restaurant()


print("9-2")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name:", self.restaurant_name)
        print("Cuisine type:", self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")


restaurant1 = Restaurant("Bistro", "French Cuisine")
restaurant2 = Restaurant("Spice Land", "Indian Cuisine")
restaurant3 = Restaurant("Sushi Samurai", "Japanese Cuisine")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


print("9-3")


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

user1 = User("David", "Chartolani", "davidch", "d.chartolani@gmail.com")
user2 = User("test1_firstname", "test1_lastname", "test1", "test1@gmail.com")
user3 = User("test2_firstname", "test2_lastname", "test2", "test2@gmail.com")

print()

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()
