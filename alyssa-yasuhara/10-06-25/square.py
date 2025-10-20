r = int(input("Enter number of rows:"))
c = int(input("Enter number of columns:"))

for i in range(0, r):
    if i == 0 or i == r-1:
        print("*"*(r+2))
    else:
        print("*", " "*(r-2), "*")
