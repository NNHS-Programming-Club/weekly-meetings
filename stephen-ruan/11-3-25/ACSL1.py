[a, b] = input().split()
b = int(b)
N = len(a)
p = a[N-b]

res = ['0'] * N
res[N-b] = p

for i in range(N-b):
  res[i] = str((int(a[i]) + int(p)) % 10)
for i in range(N-b+1, N):
  res[i] = str(abs(int(a[i]) - int(p)))

print("".join(res))