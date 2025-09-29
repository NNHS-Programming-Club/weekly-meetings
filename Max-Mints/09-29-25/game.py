import random

maxNum = int(input("What should the maximum number be?: "))
randNum= random.randint(1,maxNum)
rounds= int(input("How many rounds?: "))
guess= int(input("What number is your first guess?: "))

while guess != randNum:
    if guess > maxNum or guess <= 0:
        guess = int(input("Please enter a guess between 1-10: "))
    
    else:
        if guess > randNum:
            print("Your guess was too big.")
        else:
            print("Your guess was too small.")

        guess = int(input("Guess again: "))

if guess == randNum:
    print(f"You got it! The number was {randNum}") 