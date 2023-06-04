print("=== 5-8 ===")

usernames = ['david', 'luka', 'giorgi', 'admin', 'nino']

for user in usernames:
    if user == 'admin':
        print(f"Hello {user.upper()}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

print("=== 5-9 ===")

users = []  # Empty list of users

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("=== 5-10 ===")

current_users = ['david', 'LUKA', 'giorgi', 'beqa', 'nino']

new_users = ['goga', 'rati', 'David', 'luka', 'Lali']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The current usernames {user} already exist, please enter new username.")
    else:
        print(f"The username {user} is available")

print("=== 5-11 ===")

num_list = list(range(1,10))

for num in num_list:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")