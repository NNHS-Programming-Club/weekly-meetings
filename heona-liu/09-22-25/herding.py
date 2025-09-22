listCow = list(map(int, input().split()))
listCow.sort()
cow1, cow2, cow3 = listCow[0], listCow[1], listCow[2]

minimum = 0
maximum = 0

d1 = cow3 - cow2
d2 = cow2 - cow1

if (d1 == 1 and d2 == 1): #all numbers together => min = 0
    minimum = 0

elif (d1 == 2 or d2 == 2): #check 2 numbers have a difference of 2 =>  min = 1
    minimum = 1

else:
    minimum = 2 # >2 numbers in between => min of 2 moves

#MAXIMUM

if (d1 > d2):
    maximum = d1 - 1 # largest dist between 2 numbers
else:
    maximum = d2 - 1

print(minimum, maximum)