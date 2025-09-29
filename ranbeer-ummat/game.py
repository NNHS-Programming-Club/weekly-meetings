import random
range_num = int(input("Enter a range for the game:"))
secret = random.randint(1,range_num)
attempts = 0

print("Guess the number less than 10!")

while True:
    guess = int(input("Your guess: "))
    attempts +=1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! The number was {secret}, you took {attempts} tries.")
        break
