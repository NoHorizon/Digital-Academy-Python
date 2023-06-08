# რა არის list?
"""
სხვა და სხვა მონაცემის შენახვა ერთ ცვლადში. მაგ: nums = [1, 2, 3, 4]
"""
# რა არის ელემენტი?
"""
ყოველ ინდივიდუალურ წევრს/მონაცემს ელემენტი ეწოდება
"""
# როგორ ვწვდებით ლისტის ელემენტებს?
"""
მაგ: fruits = ['apple', 'banana', 'orange']
print(fruits[1]) მივიღებთ "banana"
"""
#დაწერეთ კოდი, რომელიც მოცემულ ლისტში ყველა ელემენტს გადაიყვანს მაღალ რეგისტრში (Upper case)
fruits = ['apple', 'banana', 'orange']
upper_fruits = []
for fruit in fruits:
    upper_fruits.append(fruit.upper())

print(upper_fruits)

#დაწერეთ კოდი, რომელიც შემნის 1000 ელემენტიან ლისტს, სადაც იქნება მხოლოდ მარტივი რიცხვები (Prime Numbers, რიცხვები, რომლებიც იყოფა მხოლოდ 1-ზე და თავის თავზე)
prime_numbers = []
num = 2

while len(prime_numbers) <= 1000:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
    num += 1

print(prime_numbers)

#რას აკეთებს შემდეგი კოდი?
"""
თქვიდან იქმნება პროდუქტების მასივი, რომელიც შეიცავს პროდუქტის მასივებს სახელით და ფასით.
შემდეგ გამოყენებულია for loop რომელიც პრინტავს პროდუქტის ინდექს [ში], მის სახელს და ფასს ტირეთი დაშორებულს
შემდგომ მომხარებელი ირჩევს პროდუქტს და ეს რიცხვი ინახება choosen_product-ის ცვლადში
products_to_purchase = None ეს ცვლადი არის შექმნილი მომავალში გამოსაყენებლად
პირველი ორი if ბლოკები ამოწმებენ თუ არჩეული რიცხვი არის ვალიდური ინდექსის ნომერი და თუ კი ის გადაყავს ინდქსში, შემდგომ მეორე if ამოწმებს თუ ხვდება ეს int პროდუქტების სიის range-ში, თუ ორივე პირობა დაყმაყოფილდა,
ამ რიცხვზე მდგომი პროდუქტი ენიჭება products_to_purchase-ს ცვლადს.
ბოლოს, თუ პროდუქტის არჩევა ვერ მოხერხდა, მივიღებთ "selected product does not exist", სხვა შემთხვევაში მივიღებთ, ჩვენს მიერ არჩეულ პროდუქტის სახელს და ფასს.
"""
# products = [
#     ["google pixel", 1000],
#     ["mac", 3000],
#     ["chevy", 15000],
#     ["microsoft", 3600],
# ]

# for i, product in enumerate(products):
#     print(f"[{i}] {product[0]} - {product[1]}")

# chosen_product = input("choose")
# products_to_purchase = None
# if chosen_product.isdigit():
#     chosen_product = int(chosen_product)
#     if chosen_product <= len(products):
#         products_to_purchase = products[chosen_product]

# if products_to_purchase is None:
#     print("selected product does not exist")
# else:
#     print(f"{products_to_purchase}, price: {products_to_purchase[1]}")


#წინა დავალებაში მოცემული ლისტის გამოყენებით, იპოვნეთ პროდუქტი სახელის მიხედვით
products = [
    ["google pixel", 1000],
    ["mac", 3000],
    ["chevy", 15000],
    ["microsoft", 3600],
]

for i, product in enumerate(products):
    print(f"[{i}] {product[0]} - {product[1]}")

chosen_product = input("Choose a product by name: ")
products_to_purchase = None

for product in products:
    if product[0].lower() == chosen_product.lower():
        products_to_purchase = product
        break

if products_to_purchase is None:
    print("Selected product does not exist")
else:
    print(f"{products_to_purchase[0]}, price: {products_to_purchase[1]}")

#დაწერეთ კოდი, რომელშიც გექნებათ მომხმარებლების სია:
"""
users = [
   ["Legend27", "a1s2d3f4"],
   ["james123", "c5bt43f4"],
   ["DaveIsGreat", "wlervtb3r"]
]
მომხმარებელს ავტორიზაცია გაატარეთ (შემოატანინეთ username და password) თუ ვერ გაიარა ავტორიზაცია quit() ფუნქციით შეაჩერეთ პროგრამა
"""
users = [
    ["Legend27", "a1s2d3f4"],
    ["james123", "c5bt43f4"],
    ["DaveIsGreat", "wlervtb3r"]
]

entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")
for user in users:
    if user[0] == entered_username and user[1] == entered_password:
        print("Authentication successful!")
        break
else:
    print("Authentication failed.")
    quit()


"""
წინა დავალებებში დაწერილი კოდი (პროდუქტის არჩევაზე და მომხმარებლის ავტორიზაციაზე) გამოიყენეთ და მომხმარებელს პროდუქტი აარჩევინეთ მხოლოდ იმ შემთხვევაში თუ ავტორიზაცია გავლილი აქვს.
"""
users = [
    ["Legend27", "a1s2d3f4"],
    ["james123", "c5bt43f4"],
    ["DaveIsGreat", "wlervtb3r"]
]
products = [
    ["google pixel", 1000],
    ["mac", 3000],
    ["chevy", 15000],
    ["microsoft", 3600],
]

# Get user input for username and password
username = input("Username: ")
password = input("Password: ")

# Check if the user exists and the password is correct
authorized_user = None
for user in users:
    if user[0] == username and user[1] == password:
        authorized_user = user
        break

if authorized_user:
    print("Login successful. Please choose a product:")
    for i, product in enumerate(products):
        print(f"{i + 1}. {product[0]} - ${product[1]}")

    product_choice = int(input("Enter the number of the product: "))

    if 1 <= product_choice <= len(products):
        chosen_product = products[product_choice - 1]
        print(f"You have chosen {chosen_product[0]} for ${chosen_product[1]}")
    else:
        print("Invalid product choice.")
else:
    print("Login failed. You can't choose a product.")


"""
users = [
["Legend27", "a1s2d3f4"],
["james123", "c5bt43f4"],
["DaveIsGreat", "wlervtb3r"]
]

balances = [
150000,
12000,
19000
]
ბალანსი ჩაამატეთ შესაბამის ინექსზე users ლისტში (მაგ. განახლებულ ლისტში მეორე ინდექსე მდგომ ელემენტს ასეთი სახე უნდა ჰქონდეს ["james123", "c5bt43f4", 12000])
"""
users = [
    ["Legend27", "a1s2d3f4"],
    ["james123", "c5bt43f4"],
    ["DaveIsGreat", "wlervtb3r"]
]

balances = [
    150000,
    12000,
    19000
]

for i in range(len(users)):
    users[i].append(balances[i])

print(users)

"""
შეავსეთ ლისტი იმ ასოებით, რომლებიც აკლია პირველიდან ბოლო ელემენტამდე

alphabet_part = ['c', 'h', 'e']

(ამ შემთხვევაში a-დან h-მდე უნდა შეივსოს მხოლოდ)
უკეთესი იქნება თუ კოდი სხვა ასოებზეც იმუშავებს
------
"""

#რა არის list slicing? (alphabet[:5]), აღწერეთ მისი მუშაობის პრინციპი
"""
list slicing არის Python-ის ფუნქცია, რომელიც საშუალებას გაძლევთ ამოიღოთ სიის ნაწილი ინდექსების დიაპაზონის მითითებით.
start, stop, range
[2:6]; [:4]; [5:]; [:]; [::2]; [::-1]
"""