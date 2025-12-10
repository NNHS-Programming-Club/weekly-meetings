f = open('input.txt')
dial = 50
point = 0
rotations =0

for line in f:
    #print(line.strip())
    direction = line[0]
    num = line[1:].strip()
    rotations = int(num) // 100
    
    if direction == 'R':
        dist_from_100 = abs(100-dial)
        num = int(num) % 100 #gets remainder after all rotations
        
        if (num >= dist_from_100 and dial != 0):
            point += 1 
        dial += int(num) % 100
        
    if direction == 'L':
        dist_from_0 = abs(0-dial)
        num = int(num) % 100 #gets remainder after all rotations
        
        if (num >= dist_from_0 and dial != 0):
            point += 1
            
        dial -= int(num) % 100
    dial = dial % 100
    point += rotations

print("Zeros: " + str(point))
    