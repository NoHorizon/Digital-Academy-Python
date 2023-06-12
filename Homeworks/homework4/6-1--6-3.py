print(5 * "#", "6-1", 5 * "#")
print("")

friend_1 = {
    'f_name': "Rati",
    'l_name': "Kashibadze",
    'age': 29,
    'city': "Tbilisi"
}

print(friend_1["f_name"], friend_1["l_name"],
      friend_1["age"], friend_1["city"])

print("")
print(5 * "#", "6-2", 5 * "#")
print("")

fav_nums = {
    'Gio': 10,
    'Kate': 22,
    'John': 17,
    'Luke': 7,
    'Beka': 4
}

for key, value in fav_nums.items():
    print(f"{key}'s favorite number is: {value}'")

print("")
print(5 * "#", "6-3", 5 * "#")
print("")

words = {
    'key': 'means keys',
    'values': 'means values',
    'ram': 'temporary memory',
    'cpu': "computers's brain",
    'store': 'save'
}

for key, value in words.items():
    print(f"{key} means: \n {value}")
