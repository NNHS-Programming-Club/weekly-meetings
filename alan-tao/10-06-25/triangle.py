rows = int(input("How many rows? "))

def repeat(char, times):
    x = ""
    for i in range(times):
        x += char
    return x

# 1
for i in range(rows):
    print(repeat("*", i+1))

# 2
for i in range(rows):
    print(repeat("*", rows-i))


# 3
print(repeat("*", rows))
for i in range(rows-2):
    print("*" + repeat(" ", rows-2) + "*")

print(repeat("*", rows))

# 4
lineLen = rows*2-1

for i in range(rows):
    print(repeat(" ", rows-i-1) + repeat("*", i*2+1) + repeat(" ", rows-i-1))


# 5
print("*")
for i in range(rows-2):
    print("*" + repeat(" ", i) + "*")
print(repeat("*", rows))