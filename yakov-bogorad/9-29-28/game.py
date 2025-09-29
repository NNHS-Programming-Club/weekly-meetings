import random

secret = random.randint(1, 10)
rounds = 10
x = 1.5

while x != secret :
    x = int(input())
    if x > secret:
        print("too high")
    if x < secret:
        print("too low")
    rounds = rounds - 1
    if rounds < 1:
        print("you lost")

print("you won!")