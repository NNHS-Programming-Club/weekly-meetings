
quantity = 0

fruit_list = {}

quit = False
while True:

    fruit = str(input("Which Fruit/Quit? "))
    if fruit in fruit_list:
        # in list
        print(f"{fruit_list[fruit]}")
    elif fruit == "quit":
        print(fruit_list)
        break

    else:
        fruit_list[fruit] = 0
        quantity = int(input("How many fruit?: "))
        fruit_list[fruit] = quantity

    