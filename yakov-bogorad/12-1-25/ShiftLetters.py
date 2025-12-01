print("Only enter lowcase a-z:")
string=str(input())
char_string=list(string)
numlist=[]
letterlist=[]

for i in range(len(char_string)):
    ascii = ord(char_string[i])
    if ascii == 122:
        ascii = ascii-25
    else:
        ascii = ascii+1

    numlist.append(ascii)
for j in range(len(numlist)):
    newchr = chr(numlist[j])
    letterlist.append(newchr)
result="".join(letterlist)
print(result)