print(5 * "#", "7-8", 5 * "#")
print("")

sandwich_orders = ["tuna", "chicken", "turkey", "ham"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your", sandwich, "sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"made from {sandwich}")


print("")
print(5 * "#", "7-9", 5 * "#")
print("")

sandwich_orders = ["tuna", "pastrami", "chicken", "pastrami", "turkey", "pastrami", "ham"]
finished_sandwiches = []

print("Deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

for sandwich in sandwich_orders:
    print("I made your", sandwich, "sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)

print("")
print(5 * "#", "7-10", 5 * "#")
print("")

poll_results = {}
num_users = 2

for i in range(num_users):
    user_name = input(f"User {i+1}, please enter your name: ")
    dream_destination = input(f"{user_name}, which place you want to visit? ")

    poll_results[user_name] = dream_destination

print("\nPoll Results:")
for user_name, dream_destination in poll_results.items():
    print(f"{user_name} would like to visit {dream_destination}.")
