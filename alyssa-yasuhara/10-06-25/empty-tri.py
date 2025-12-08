h = int(input("Enter height:"))

for i in range(0, h+1):
    if i == 1:print("*")
    elif i == h:print("*"*h)
    print("*", " "*(i-1), "*")