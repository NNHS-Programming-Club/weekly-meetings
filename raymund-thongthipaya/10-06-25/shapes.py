rows = 5
shape = "o"

print("SHAPE 1")

for i in range(rows):
    print(shape * (i + 1))

print("\nSHAPE 2")

for i in range(rows):
    print(shape * (rows - i))

print("\nSHAPE 3")

print(shape * rows) # top

# middle
for i in range(rows - 2):
    print(shape, end="")
    print(" " * (rows - 2), end="")
    print(shape)

print(shape * rows) # bottom

print("\nSHAPE 4") # bruh this one was difficult
for i in range(rows):
    print(" " * (rows - (i * 1) - 1), end="")
    print(shape * (i * 2 + 1), end="")
    print(" " * (rows - i - 1))

print("\nSHAPE 5")
for i in range(rows - 1):
    print(shape, end="")
    print(" " * (i - 1), end="")

    if i >= 1:
        print(shape)
    else:
        print("")

# base
print(shape * rows)

