# challenge 1
shape1 = int(input("Let's make a isosceles right triangle.\nHow tall should it be?\n"))
for i in range(0, shape1):
    print("*"*(i+1))

# challenge 2
shape2 = int(input("Let's make another one, but upside down.\nHow tall should it be?\n"))
for i in range(0, shape2):
    print("*"*(shape2-i))

# challenge 3
shape3 = int(input("Let's try a square outline.\nSide length?\n"))
for i in range(0, shape3):
    if (i == 0 or i == shape3-1):
        print("*"*shape3)
    else:
        print("*", end="")
        print(" "*(shape3-2), end="")
        print("*", end="\n")

# challenge 4
shape4 = int(input("How about a new icosceles triangle?\nBase width?\n"))
for i in range (0, -(shape4//-2)):
    print(" "*(-(shape4//-2)-(i+1)), end="")
    if (shape4%2 == 1):
        print("*"*((i+1)*2-1))
    else:
        print("*"*((i+1)*2))

# challenge 5
shape5 = int(input("Let's try making a right triangle again, this time with no fill; just the outline.\nHow tall should it be?\n"))
for i in range(0, shape5):
    if (i+1 == shape5 or i+1 == 1):
        print("*"*(i+1))
    else:
        print("*", end="")
        print(" "*(i-1), end="")
        print("*", end="\n")