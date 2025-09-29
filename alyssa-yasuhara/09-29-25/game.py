import random
choose_num = int(input('enter a range:'))
x = random.randint(1, choose_num)
count = 0
while True:
    guess = int(input("guess a number from 1 to your range:"))
    count +=1
    if guess<x:print("too low")
    elif guess>x:print("too high")
    elif guess==x:
        print(f"you got it in {count} tries, and the number was {x}")
        break
