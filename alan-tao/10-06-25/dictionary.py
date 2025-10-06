fruits = {}
while True:
  name = input("What is the name of the fruit? ")

  if name == "quit":
    break
  if name in fruits:
    print("You have " + str(fruits[name]) + " " + name + "s!")
  else:
    count = input("How many " + name + "s do you have? ")
    fruits[name] = count
    print("You now have " + count + " " + name + "s.")
  
  print()


print("Here is what you have:")
for name, count in fruits.items():
  print("You have " + count + " " + name + "s.")