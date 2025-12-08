f = open("/workspaces/weekly-meetings/yakov-bogorad/day-1/1.in")

lines = []
for line in f:
    print(line)

x = 50

for line in f:
    if line[0] == "R":
        x = x+(int(line[1:]))
    if line[0] == "L":
       x = x+(-1*int(line[1:]))
print(x)

