#1

n = int(input())
output = "*"
for i in range (n):
    print(output)
    output += "*"

#2

for i in range (n):
    output = ""
    for j in range (n-i):
        output += "*"
    print(output)

#3

output = ""
for i in range (n):
    output += "*"
print(output)
for i in range (n-2):
    output = "*"
    for j in range (n-2):
        output += " "
    output += "*"
    print(output)
output = ""
for i in range (n):
    output += "*"
print(output)

#4

for i in range (1,n+1):
    output = ""
    for j in range(n-i):
        output += " "
    for j in range(i*2-1):
        output += "*"
    print(output)

#5

print("*")
for i in range (n-2):
    output = "*"
    for j in range (i):
        output += " "
    output += "*"
    print(output)

output = ""
for i in range (n):
    output += "*"
print(output)