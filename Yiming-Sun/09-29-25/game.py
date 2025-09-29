import random
secret, rounds, num = random.randint(1, 10), int(input("how many rounds? ")), 1
while num <= rounds:
    answer = int(input("guess the number: "))
    if answer > secret:
        print("too high")
    elif answer < secret:
        print("too low")
    else:
        print("you get it")
        break
    num += 1
if num > rounds:
    print(f"The number was {secret}")