import sys
sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

numbers = list(map(int, input().split()))
numbers.sort()
d1 = numbers[2] - numbers[1]
d2 = numbers[1] - numbers[0]
if d1 == 1 and d2 == 1:
    print(0)
    print(0)
elif d1 == 2 and d2 <= 2 or d1 <= 2 and d2 == 2:
    print(1)
    print(1)
elif d1 == 2 or d2 == 2:
    print(1)
    if d1 > d2:
        print(int(d1 - 1))
    else:
        print(int(d2 - 1))
else:
    print(2)
    if d1 > d2:
        print(int(d1 - 1))
    else:
        print(int(d2 - 1))
