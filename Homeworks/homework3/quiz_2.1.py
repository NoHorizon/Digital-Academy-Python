""" 1.
როგორ შევქმნნათ ლისტი (მასივი)? 

a = []
"""

""" 2.
საიდან იწყება მასივის ინდექსების ათვლა?
პასუხი: 0 - დან

"""

""" 3.
ლისტზე (მასივზე) ელემენტზე წვდომა როგორ ხდება? (დაწერეთ მაგალითი, ჩავთვალოთ გვაქვს ცვლადი arr რომელიც ლისტის ტიპისაა)

მაგ: arr[0], arr[1], arr[-2], arr[-1] და ა.შ

"""

""" 4.
რა არის Index Error?

პასუხი: Index Error გვაქვს მაშინ, როდესაც ვცვლიობს მივწვდეთ მასივის ისეთ ელემენტს რომელიც არ არსებობს.
მაგ: arr = [1, 2, 3]
print(arr[3])

"""

""" 5.
როგორ ხდება ლისტში (მასივში), ელემენტების ჩამატება?

arr.append() - ელემენტის მასივის ბოლოში დამატება
.insert(3, 1) - ელემენტის მასივში დამატება (კონკრეტულ ინდექსზე, რა ელემენტი)
.extend - ამატებს მასივში მეორე მასივის ელემენტებს მაგ: numbers1 = [1,2], numbers2 = [3,4]; numbers1.extend(numbers2) => print(numbers1) იქნება: [1, 2, 3, 4]
list concatenation-ით ანუ: arr1 + arr2 იქნება ერთი მასივი ორივე მასივის ელემენტებით

"""

""" 6.
როგორ გავიგოთ ლისტის ზომა?

len(arr)

"""

""" 7.
დაბეჭდეთ თითოეული მასივის ელემენტი ტერმინალში (გამოიყენეთ for ან while ციკლი)

"""
print ("=== FOR ===")
arr = [1, 2, "car", "home"]

for i in arr:
    print (i)
print ("=== WHILE ===")
i = 0
while (i < len(arr)):
  print(arr[i])
  i += 1

""" 8.
დაბეჭდეთ კენტ ინდექსზე მდგომი  მასივის ელემენტები ტერმინალში

"""
print ("=== N 8 (ODD INDEX NUMBERS) ===")
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(1, len(arr), 2):
    print(i, arr[i])

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("=== N 8 (ODD INDEX NUMBERS) OPTION 2===")
for i, element in enumerate(arr):
    if i % 2 != 0:
        print(i, element)

""" 9.
დათვალეთ ტერმინალიდან შემოტანილი ათი რიცხვის ჯამი (hint: არ შექმნათ 10 ცვლადი)

"""
# total = 0
# for i in range(10):
#     number = int(input("Enter a number: "))
#     total += number

# print("The sum is:", total)

""" 10.
შექმენით 10 ელემენტიანი ლისტი და შეავსეთ კლავიატურიდან შეტანილი მთელი რიცხვებით.
შემდეგ თითოეული ელემენტი ლისტში აიყვანეთ მომდევნო ინდექსზე მდგომი
ელემენტის ხარისხში (ბოლო ინდექსზე მდგომი ელემენტი აიყვანეთ
პირველი ელემენტის ხარისხში)

"""
# arr = []
# for i in range(10):
#     num = int(input("Enter a number: "))
#     arr.append(num)

# result_list = []
# for i in range(len(arr)):
#     next_index = (i + 1) % len(arr)
#     result_list.append(arr[i] ** arr[next_index])

# print("The resulting list is:", result_list)

""" 11.
რას აკეთებს for else?

თუ ციკლი დასრულდა ისე რომ მას არ შეხვდა break, მაშინ აქტიურდება else ბლოკი. მაგალითად მასივში ვეძებთ 0-ს for ციკლის მეშვეობით და გვაქვს break, მაგრამ ციკლში არ აღმოჩნდა 0, შესაბამისად შემდეგი მოქმედება გადავა else-ში და მაგ: მივიღებთ "0 ვერ მოიძებნა"

"""
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 0:
        print("0 found!")
        break
else:
    print("0 was't found!")

""" 12.
გაარკვიეთ ლისტში არსებობს თუ არა 1 მარტივი რიცხვი მაინც, შეეცადეთ კოდი იყოს ოპტიმიზირებული, ანუ რაც შეიძლება ნაკლები იტერაცია იყოს!. (hint: for else, break)
"""
numbers = [4, 6, 8, 10, 12, 13, 14, 15]
has_prime = False

for num in numbers:
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        has_prime = True
        break

print(has_prime)

""" 13.
რა მონაცემთა ტიპებს შეიძლება შეიცავდეს list/tuple?

integer, float, string, boolean, NoneType, list, tuple
"""

""" 14.
შექმენით ლისტი, ტერმინალიდან შეავსეთ 5 ელემენტით და შემდეგ თითოეული ელემენტი ააკვადრატეთ და შემდგომ დაბეჭდეთ ეკრანზე (ლისტი უნდა შეიცვალოს!)
"""
# arr = []
# print("Please enter 5 numbers:")
# for i in range(5):
#     number = float(input())
#     arr.append(number)

# squared_list = [item ** 2 for item in arr]

# print("Squared list:")
# for item in squared_list:
#     print(item)

""" 15.
როგორ მივუთითოთ ლისტში რა ტიპის ელემენტები გვაქვს? (მაგალითად აიღეთ თქვენთვის სასურველი მონაცემთა ტიპი)

----
"""
""" 16.
მეგობრისთვის გინდათ სამეგობრომ იყიდოთ ლეპტოპი, თქვენმა მეგობარმა მოგცათ ლეპტოპების ფასების სია - prices = [1336, 4434, 5100, 2000, 750, 1000, 1250, 500, 14050, 3000, 2300, 5110], კლავიატურიდან შემოიტანეთ ბიუჯეტი (თანხის ოდენობა რაც გაქვთ შეკრული) და ამ სიიდან გაფილტრეთ ისეთი ლეპტოპები რომლებიც 500 ლარით იაფია ბიუჯეტზე ან არ გყოფნით თანხა და დაბეჭდეთ დანარჩენი ლეპტოპების ფასები (ლისტი არ შეცვალოთ!)

"""
prices = [1336, 4434, 5100, 2000, 750, 1000, 1250, 500, 14050, 3000, 2300, 5110]

budget = int(input("Enter your budget: "))
max_price = budget - 500

filtered_laptops = []
below_budget = []

for price in prices:
    if max_price <= price <= budget:
        filtered_laptops.append(price)
    elif price < budget:
        below_budget.append(price)

if filtered_laptops:
    for price in filtered_laptops:
        print(price)
else:
    print("No laptops in the specified price range.")

print("Laptops below your budget:")
for price in below_budget:
    print(price)

""" 17.
მეგობრისთვის გინდათ სამეგობრომ იყიდოთ ლეპტოპი, თქვენმა მეგობარმა მოგცათ ლეპტოპების ფასების სია - prices = [1336, 4434, 5100, 2000, 750, 1000, 1250, 500, 14050, 3000, 2300, 5110], კლავიატურიდან შემოიტანეთ ბიუჯეტი (თანხის ოდენობა რაც გაქვთ შეკრული) და ამ სიიდან გაფილტრეთ ისეთი ლეპტოპები რომლებიც 500 ლარით იაფია ბიუჯეტზე ან არ გყოფნით თანხა და დაბეჭდეთ დანარჩენი ლეპტოპების ფასები (ლისტი არ შეცვალოთ!)

"""


"""
ბოლო 3 ბონუსი, ვერ ვასწრებ, მოგვიანებით აუცილებლად გავაკეთებ
"""