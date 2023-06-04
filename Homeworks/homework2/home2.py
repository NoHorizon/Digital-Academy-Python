# გვერდი 78

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

# 5.1
print("=== 5.1 ===")
country = 'Georgia'

print("Is country == 'Georgia'? I predict True.")
print(country == 'Georgia')
print("Is country == 'Georgia'? I predict True.")
print(country == 'Turkey')

# 5.2

print("=== 5.2 ===")
weather = 'GOOD'

print("Is weather == 'good'? I predict True.")
print(weather.lower() == 'good')
print("Is weather != 'good'? I predict True.")
print(weather.lower() != 'good')  # !=

print("=== ===")
# number  => =< < >

lucky_number = 7

print("Is lucky number > 10? I predict True.")
print(lucky_number > 10)
print("Is lucky number < 10? I predict True.")
print(lucky_number < 10)
print("Is lucky number >= 7? I predict True.")
print(lucky_number >= 7)
print("Is lucky number <= 7? I predict True.")
print(lucky_number <= 7)

# OR
print("Is lucky number = 7 or = 5? I predict True.")
print(lucky_number == 7 or lucky_number == 5)
print("Is lucky number both 7 and 5? I predict True.")
print(lucky_number == 7 and lucky_number == 5)

# test list
color_list = ['green', 'blue', 'red', 'yellow', 'purple']
picked_color = 'blue'
picked_color2 = 'pink'
if picked_color in color_list:
    print(f"{picked_color.title()} IS in the list of colors")

if picked_color2 not in color_list:
    print(f"{picked_color2.title()} is NOT in the list of colors")


# გვერდი 85
print("=== 5.3 ===")
alien_color = 'yellow'

if alien_color == 'green':
    print('You have earned 5 points')
else:
    print("Alien's color is not green")

print("=== 5.4 ===")

alien_color2 = 'red'
if alien_color2 == 'green':
    print('You have earned 5 points')
else:
    print("Alien's color isn't green, You have earned 10 points")

print("=== 5.5 ===")

if alien_color == 'green':
    print('You have earned 5 points')
elif alien_color == 'yellow':
    print('You have earned 10 points')
elif alien_color == 'red':
    print('You have earned 15 points')
else:
    print("We don't know the color of the alien")

print("=== 5.6 ===")

person = 17
if person < 0:
    print('Impossible age')
elif person < 2:
    print("Person is a baby")
elif person >= 2 and person < 4:
    print("Person is a toddler")
elif person >= 4 and person < 13:
    print("Person is a kid")
elif person >= 13 and person < 20:
    print("Person is a teenager")
elif person >= 20 and person < 65:
    print("Person is an adult")
else:
    print("Person is an elder")

print("=== 5.7 ===")

favorite_fruits = ['banana', 'apple', 'orange']

for fruit in favorite_fruits:
    if fruit == 'banana':
        print(f'You really like {fruit.title()}s')
    elif fruit == 'grape':
        print(f'You really like {fruit.title()}s')
    elif fruit == 'pineapple':
        print(f'You really like {fruit.title()}s')
    elif fruit == 'orange':
        print(f'You really like {fruit.title()}s')
    elif fruit == 'apple':
        print(f'You really like {fruit.title()}s')
