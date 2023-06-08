import time

secret_number = int(time.time()) % 99 + 1


while True:
    user_guess = int(input("Guess the number (between 1 and 99): "))

    if user_guess < secret_number:
        print("Guess is LOW!")
    elif user_guess > secret_number:
        print("Guess is HiGH!")
    else:
        print("You guessed the number!")
        break
