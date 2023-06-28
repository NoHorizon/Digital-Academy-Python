# name: str = 'John'
# print(name)

# name = 5

# print(name)

# nums: list[int] = [1, 2, 3, 4, 5, 6]

# first_names: list[str] = ['Joe', 'Jake', 'Jane']
# last_names: tuple[str, ...] = ('Doe', 'Dane', 'Leo')


def get_int_input(__prompt: str):
    return int(input(__prompt))


age = get_int_input("your age?")
height = get_int_input("your height?")

print(age, height)
