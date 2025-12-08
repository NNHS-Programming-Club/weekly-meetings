f = open("heona-liu/12-08-25/day1/input.txt")

dial = 50
hitZero = 0

for i in f:
    direction = i[0]
    num = int(i[1:])

    if (direction == "L"): #to the left
        dial = (dial - num) % 100
        #print(dial)
    elif (direction == "R"): #to the right
        dial = (dial + num) % 100
        #print(dial)

    if (dial == 0): 
        hitZero+=1

print("Hits 0: " + str(hitZero))

#part 2 -  if the mod is less than original number then it must have passed
#take the int




    