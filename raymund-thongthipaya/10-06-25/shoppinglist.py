print("shopping list")

items = {}

while True:
    item = input("Item: ")
    if item == "":
        break
    
    if not item in items:
        quantity = int(input("Quantity: "))
        items[item] = quantity
    else:
        print("Item already in list, you need", items[item])