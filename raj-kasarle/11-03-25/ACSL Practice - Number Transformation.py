N, P = map(int, input().split())
listN = list(str(N))

def addP(n, i, p):
    return (int(n[i]) + int(n[p]))
def subtractP(n, i, p):
    return (int(n[i]) - int(n[p]))

for i in range(0, len(str(N))):
    if i < P:
        listN[i] = str(addP(listN, i, P) % 10)
    elif i > P:
        listN[i] = str(abs(subtractP(listN, i, P)))

newN = "".join(listN)
N = int(newN)
print(N)