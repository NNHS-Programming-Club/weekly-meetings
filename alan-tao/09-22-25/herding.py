import sys
sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")

x = list(map(int, input().split()))
x.sort()
d1 = x[1] - x[0]
d2 = x[2] - x[1]
# d3 = x[2] - x[0]
if (d1 == 1 and d2 == 1):
    print(0)
elif (d1 == 2 or d2 == 2):
    print(1)
else:
    print(2)

print(max(d2, d1)-1)
