mydict = {}

while True:

    fruit = input("Fruit:")
    if fruit.lower() == "quit":
        print(mydict)
        break
    if fruit in mydict:
        print("Already in dictionnary")
    hm = int(input("How many fruit?:"))
    mydict[fruit] = hm


    

    