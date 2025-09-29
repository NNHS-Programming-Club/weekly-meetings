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

        if abs(guess - value) >= 500:
            print("ur way off")
        elif abs(guess - value) < 100 and abs(guess - value) >= 50:
            print("ur kinda close")
        elif abs(guess - value) < 50 and abs(guess - value) > 10:
            print("ur close")
        elif abs(guess - value) <= 10:
            print("ur very close")

    if guess > value:
        print("go lower")

        if abs(guess - value) >= 500:
            print("ur way off")
        elif abs(guess - value) < 100 and abs(guess - value) >= 50:
            print("ur kinda close")
        elif abs(guess - value) < 50:
            print("ur close")
        elif abs(guess - value) <= 10:
            print("ur very close")