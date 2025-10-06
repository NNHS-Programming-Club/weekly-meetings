c = int(input("Enter the number of stars in last row:"))
x = 1

if c < 2:
    print("Please input a higher number.")
for i in range (0, c):
    # space = int((c-x)/2)
    space = c-1-i
    print(" "*space, "*"*x, " "*space)
    x +=2