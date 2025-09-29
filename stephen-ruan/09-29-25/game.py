import random
secret = random.randint(1,100)
rounds = int(input("How many rounds?"))
tries = 0
while tries < rounds:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    if guess > secret:
        print("Too high!")
    tries += 1
    if guess == secret:
        print("The number was: " + str(secret) + ", so you win!")
        print("You took " + str(tries) + " tries.")
        break
if tries >= rounds:
    print("You took too many tries, and lost :(")
    