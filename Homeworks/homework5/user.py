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
