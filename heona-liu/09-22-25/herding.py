listCow = list(map(int, input().split()))
listCow.sort()
cow1, cow2, cow3 = listCow[0], listCow[1], listCow[2]

minimum = 0
maximum = 0

if ((cow3 - cow2) == 1) and ((cow2 - cow1) == 1): #all numbers together => min = 0
    minimum = 0

elif (((cow3 - cow2)) == 2 or ((cow2 - cow1)) == 2): #check 2 numbers have a difference of 2 =>  min = 1
    minimum = 1

else:
    minimum = 2 # >2 numbers in between => min of 2 moves

#MAXIMUM

if ((cow3 - cow2) > (cow2 - cow1)):
    maximum = (cow3 - cow2) - 1 # -1 because you are looking for the numbers between the largest dist between 2 numbers
else:
    maximum = (cow2-cow1) - 1

print(maximum)