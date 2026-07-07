
import random

secret_number = random.randint(1, 100)

print("=== NUMBER GUESSING GAME (1 - 100) ===")

while True:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("The number is too small! Try again.\n")

    elif guess > secret_number:
        print("The number is too big! Try again.\n")

    else:
        print("🎉 Player Wins! Success!")
        print("Your guess is correct!\nThe number was", secret_number)
        break