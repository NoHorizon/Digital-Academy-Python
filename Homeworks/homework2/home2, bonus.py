"""
დაწერეთ კოდი შექმენით products ცვლადი, სადაც შეინახავთ 5 პროდუქტს (მოიფიქრეთ).
ლისტის ელემენტები უნდა იყოს ლისტი [ პროდუქტის დასახელება, ფასი ]
შემდეგ გამოიტანეთ თითოეული ელემენტის დასახელება და ფასი ცალ ცალკე ხაზზე (for ციკლი უნდა გამოიყენოთ)
"""

products = [['car', 12500], ['computer', 3500],
            ['toy', 80], ['pen', 2], ['tv', 1100]]

for product in products:
    print(f"{product[0]}: \n {product[1]}")


print("===== Metodi #2 =====")

for name, price in products:
    print(f"{name}:\n {price}")


#TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT