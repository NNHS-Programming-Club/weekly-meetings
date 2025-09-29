import random


lowrange = int(input("Enter lower threshold: "))
highrange = int(input("Enter higher threshold: "))
secret = random.randint(lowrange,highrange)
tries = 0
guess = int(input("Enter your guess: "))
tries += 1

while (guess != secret):
    if (guess > secret):
        guess = int(input("Number is too high. Guess again: "))
        tries += 1
    elif (guess < secret):
        guess = int(input("Number is too low. Guess again: "))
        tries += 1
    else:
        break

print(f"You got it! It took you {str(tries)} tries")