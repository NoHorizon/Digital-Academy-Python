nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = [
    num
    for num in nums
    if num % 2 == 0
]

print(f"{even_nums = }")

odd_nums = [
    num
    for num in nums
    if num % 2 == 1
]

print(f"{odd_nums = }")

divided_by_3_nums = [
    num
    for num in nums
    if num % 3 == 0
]

print(f"{divided_by_3_nums = }")

print("===================")

hundred_nums = [
    i
    for i in range(100) #0-99
]
print(hundred_nums)

# SAME AS BELOW

hundred_nums = list(range(100)) #0-99
print(hundred_nums)

print("===================")
