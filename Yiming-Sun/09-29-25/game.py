import random
secret = random.randint(1, 10)
rounds = int(input("how many rounds? "))
num = 1
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