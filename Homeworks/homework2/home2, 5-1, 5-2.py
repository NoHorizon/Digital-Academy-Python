# 5.1
print("=== 5-1 ===")
country = 'Georgia'

print("Is country == 'Georgia'? I predict True.")
print(country == 'Georgia')
print("Is country == 'Georgia'? I predict False.")
print(country == 'Turkey')

# 5.2

print("=== 5-2 ===")
weather = 'GOOD'

print("Is weather == 'good'? I predict True.")
print(weather.lower() == 'good')
print("Is weather != 'good'? I predict False.")
print(weather.lower() != 'good')  # !=

print("=== ===")
# number  => =< < >

lucky_number = 7

print("Is lucky number > 10? I predict False.")
print(lucky_number > 10)
print("Is lucky number < 10? I predict True.")
print(lucky_number < 10)
print("Is lucky number >= 7? I predict True.")
print(lucky_number >= 7)
print("Is lucky number <= 7? I predict True.")
print(lucky_number <= 7)

# OR & AND
print("Is lucky number = 7 or = 5? I predict True.")
print(lucky_number == 7 or lucky_number == 5)
print("Is lucky number both 7 and 5? I predict False.")
print(lucky_number == 7 and lucky_number == 5)

# test list
color_list = ['green', 'blue', 'red', 'yellow', 'purple']
picked_color = 'blue'
picked_color2 = 'pink'
if picked_color in color_list:
    print(f"{picked_color.title()} IS in the list of colors")

if picked_color2 not in color_list:
    print(f"{picked_color2.title()} is NOT in the list of colors")