shape1 = int(input("Let's make a triangle.\nHow tall should it be?\n"))
for i in range(0, shape1):
    print("*"*(i+1))

shape2 = int(input("Let's make another one.\nHow tall should it be?\n"))
for i in range(0, shape2):
    print("*"*(shape2-i))

shape3 = int(input("Let's try a square outline.\nSide length?\n"))
for i in range(0, shape3):
    if i == 0 or i == shape3-1:
        print("*"*shape3)
    else:
        print("*", end="")
        print(" "*(shape3-2), end="")
        print("*", end="\n")