shape1 = int(input("Let's make a triangle.\nHow tall should it be?\n"))
for i in range(0, shape1):
    print("*"*(i+1))

shape2 = int(input("Let's make another one.\nHow tall should it be?\n"))
for i in range(0, shape2):
    print("*"*(shape2-i))