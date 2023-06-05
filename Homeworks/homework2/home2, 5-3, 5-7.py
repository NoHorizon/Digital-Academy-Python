print("=== 5-3 ===")
alien_color = 'yellow'

if alien_color == 'green':
    print('You have earned 5 points')
else:
    print("Alien's color is not green")

print("=== 5-4 ===")

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

print("=== 5-6 ===")

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

print("=== 5-7 ===")

favorite_fruits = ['banana', 'apple', 'orange']

fruit = 'apple'
if fruit in favorite_fruits:
    print(f'You really like {fruit.title()}s')

