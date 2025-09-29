import random

print("guessing game :)")

value = random.randint(0, 1000)

while True:
    guess = int(input("guess: "))

    if guess == value:
        print("yay")
        break

    if guess < value:
        print("go higher")

    if guess > value:
        print("go lower")