x = input()
ans = []
for i in range(1000):
    ans.append(100000000000)
for i in range(len(x)):
    ans.pop(i)
    ans.insert(int(x[i]),i)
print(ans)