# def find_number(__number: int, __numbers: list[int]) -> int:
#     """
#     :param __number: Number to find
#     :param __numbers: Where to find the number
#     :return: Index of found number OR -1 if number was not found
#     """
#     for i, number in enumerate(__numbers):
#         if number == __number:
#             return i
#     return -1

# num_list: list[int] = list(range(0, 10))

# print(find_number(2, num_list))
# print(find_number(15, num_list))

def reorder_list(__list: list) -> None:
    """
    reorder odd and even numbers in list
    Example: 0 - >, 1 <- 0
    """
    slice_1: list = __list[::2] #ლუწი რადგან 0 და ყოველი მომდევნო 2
    slice_2: list = __list[1::2] #კენტი რადგან 1დან ყოველი მომდევნო 2
    print(slice_1)
    print(slice_2)
    reodered_list: list = []
    for i in range(1, len(__list), 2):
        reodered_list.append(__list[i])
        reodered_list.append(__list[i - 1])

    if len(__list) % 2 == 1:
        reodered_list.append(__list[-1])

    print(reodered_list)


num_list: list[int] = list(range(0, 11))

reorder_list(num_list)
