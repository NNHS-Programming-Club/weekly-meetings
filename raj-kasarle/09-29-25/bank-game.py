import random

print("I am thinking of a number between 1 and 10.")

secret = random.randint(1, 10)
rounds = int(input("How many rounds?\n"))

guess = int(input((str(rounds) + " rounds. Guess the number.")))
tries = 0

while tries < rounds:
    tries +=1
    if guess == secret:
        print("You got my number!")
        break
    elif guess > secret:
        print("Lower.")
    elif guess < secret:
        print("Higher.")

print("The number was " + secret + ".")
print("Turns used: " + tries)