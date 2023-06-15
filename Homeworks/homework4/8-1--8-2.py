print(5 * "#", "8-1", 5 * "#")
print("")


def display_message(subject):
    print(f"We are learning {subject.upper()}!")


display_message("functions")

print("")
print(5 * "#", "8-2", 5 * "#")
print("")


def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("the count of monte cristo")