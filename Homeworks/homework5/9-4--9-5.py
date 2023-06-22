print("9-4")


class User:
    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.number_served = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

user1 = User("John", "Doe", 30, "New York", "Engineer")
user2 = User("Alice", "Smith", 25, "London", "Designer")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

class Restaurant:
    def __init__(self):
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant()

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 50
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(25)
print(f"Number of customers served: {restaurant.number_served}")
