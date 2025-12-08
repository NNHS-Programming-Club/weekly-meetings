#Inputs
p = int(input("P: "))
number = str(input("Input: "))

#Variables
number_arr = list(number)
p_val = int(number_arr[-p])
array_bef = number_arr[:p_val]
array_aft = number_arr[-p:]


print(array_bef, array_aft, p, p_val)

new_number = []

#digits on left (ADD)
#print(array_bef[0])

while (len(array_bef)>1):
    sum = int(array_bef[0])+p_val
    
    if (sum>=10):
        digit = sum%10
        new_number.append(digit)
        print(new_number)
        array_bef = array_bef[1:]
    else:
        new_number.append(sum)
        print(new_number)
        array_bef = array_bef[1:]

# append middle digit
new_number.append(p_val)

# digits on right (SUB)
while (len(array_aft)>1):
    sum = p_val-int(array_aft[0])
    
    if (sum<0):
        digit = sum*-1
        new_number.append(digit)
        print("AFT _ " + str(new_number))
        array_aft = array_aft[1:]
    else:
        new_number.append(sum)
        print("AFT ____ " + str(new_number))
        array_aft = array_aft[1:]

new_number = (str(i) for i in new_number)
new_number = "".join(new_number)
print(new_number)

