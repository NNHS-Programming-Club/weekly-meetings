import random

secret = random.randint(1, 10)

turns = 0
while True:
    guess = int(input("What is your guess? "))
    turns += 1
    if (guess > secret):
        print("Too Big")
    elif (guess < secret):
        print("Too Small")
    else:
        print("You got it!")
        print("It took you " + str(turns) + " turns.")
        break

