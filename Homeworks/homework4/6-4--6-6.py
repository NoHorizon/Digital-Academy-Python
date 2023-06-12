print(5 * "#", "6-4", 5 * "#")
print("")
words = {
    'key': 'means keys',
    'values': 'means values',
    'ram': 'temporary memory',
    'cpu': "computers's brain",
    'store': 'save',
    'word6': 'meaning6',
    'word7': 'meaning7',
    'word8': 'meaning8',
    'word9': 'meaning9',
    'word10': 'meaning10',
}

for key, value in words.items():
    print(f"{key} means: \n {value}")

print("")
print(5 * "#", "6-5", 5 * "#")
print("")

rivers = {
    'kura': 'tbilisi',
    'nile': 'egypt',
    'mississippi': 'usa'
}

for key, value in rivers.items():
    print(f"The {key.capitalize()} runs through {value.capitalize()}.")

print("")
print(5 * "#", "6-6", 5 * "#")
print("")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_to_poll = ['jen', 'sarah', 'edward',
                  'phil', 'michael', 'lisa', 'john']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.capitalize()}, for responding to the poll!")
    else:
        print(
            f"{person.capitalize()}, we invite you to take the poll.")
