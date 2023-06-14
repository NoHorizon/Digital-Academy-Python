print(5 * "#", "6-7", 5 * "#")
print("")

friend_1 = {
    'f_name': "Rati",
    'l_name': "Kashibadze",
    'age': 29,
    'city': "Tbilisi"
}

friend_2 = {
    'f_name': "Lasha",
    'l_name': "Tskhadadze",
    'age': 35,
    'city': "Tbilisi"
}

friend_3 = {
    'f_name': "Levani",
    'l_name': "Gochashvili",
    'age': 33,
    'city': "Tbilisi"
}


friends = [friend_1, friend_2, friend_3]

for friend in friends:
    print("First Name:", friend['f_name'])
    print("Last Name:", friend['l_name'])
    print("Age:", friend['age'])
    print("City:", friend['city'])
    print()


print("")
print(5 * "#", "6-8", 5 * "#")
print("")

animals = [
    {
        'name': "pako",
        'kind': "cat",
        'owner': "luka",
    },
    {
        'name': 'scooby',
        'kind': "dog",
        'owner': "david",
    },
    {
        'name': 'johny',
        'kind': "turtle",
        'owner': "nino",
    }
]

for _animal in animals:
    print(
        f"{_animal['name'].capitalize()} is a {_animal['kind']} and the owner is {_animal['owner'].capitalize()}")


print("")
print(5 * "#", "6-9", 5 * "#")
print("")

favorite_places = {
    "david": "tokyo",
    "nino": "paris",
    "soso": "new york"
}

for name, place in favorite_places.items():
    print(f"{name.capitalize()}'s favorite place is {place.title()}")

print("")
print(5 * "#", "6-10", 5 * "#")
print("")

fav_nums = {
    'Gio': [10, 99],
    'Kate': [22, 47],
    'John': [17, 21],
    'Luke': [7, 15],
    'Beka': [4, 80]
}

for key, value in fav_nums.items():
    print(f"{key}'s favorite numbers are: {value[0]} and {value[1]}")

print("")
print(5 * "#", "6-11", 5 * "#")
print("")

cities = {
    'tbilisi': {
        'country': 'Georgia',
        'population': '1.1 million',
        'fact': 'Tbilisi is the capital and largest city of Georgia.'
    },
    'berlin': {
        'country': 'Germany',
        'population': '3.500.000',
        'fact': 'Berlin has best beer.'
    },
    'london': {
        'country': 'Great Britain',
        'population': '9.000.000',
        'fact': 'London is a popular tourist destination on the Black Sea coast.'
    }
}

for city, city_info in cities.items():
    print(f"{city.title()}: \nCountry: {city_info['country']} \nPopulation: {city_info['population']} \nFact: {city_info['fact']}")
    print()
