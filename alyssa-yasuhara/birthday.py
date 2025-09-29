import random
secret = random.randint(1, 10)
count = 0

while True:
    x = int(input("Guess a number from 1-10:"))
    count += 1
    if x < secret:print("too low")

    elif x > secret:print("too high")

    elif x == secret:
        print(f"you did it in {count} tries")
        break
