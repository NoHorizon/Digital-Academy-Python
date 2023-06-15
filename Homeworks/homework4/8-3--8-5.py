print(5 * "#", "8-3", 5 * "#")
print("")

def make_shirt(size, message):
    print(f"{size.capitalize()} size shirt with the message printed on it: {message}")

make_shirt("medium", "Hello Georgia!")

make_shirt(size="small", message="I'm learning Python!")

print("")
print(5 * "#", "8-4", 5 * "#")
print("")

def make_shirt(size="large", message="I love Python"):
    print(f"{size.capitalize()} size shirt with the message printed on it: {message}")

make_shirt()

make_shirt("medium")
make_shirt("small", "Drink Chacha")


print("")
print(5 * "#", "8-5", 5 * "#")
print("")

def describe_city(city, country='USA'):
    print(f"{city} is in {country}.")

describe_city("Reykjavik", "Iceland")
describe_city("New York")
describe_city("London", "United Kingdom")
