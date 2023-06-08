arr = [0, 0 , 0, 0, 0, 2, 0, 0, 0, 1, 0, 0]

print(f"2 dan 1 mde aris {arr.index(1) - arr.index(2) - 1} noli")


products = [
    {
        'title': 'Laptop',
        'price': 3499,
        'brand': 'Asus',
    },
    {
        'title': 'Laptop',
        'price': 5499,
        'brand': 'Legion',
    },
    {
        'title': 'Laptop',
        'price': 7499,
        'brand': 'Alienware',
    },
]

highest = products[0]['price']

for product in products:
    if product['price'] > highest:
        highest = product['price']

print(highest)