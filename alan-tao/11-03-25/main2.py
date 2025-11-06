[a, b] = map(int, input().split())

p = (a//pow(10, b-1)) % 10
ans = 0
cnt = 0

while (a > 0):
  if (cnt < b-1):
    ans += abs(a % 10 - p) * pow(10, cnt)
  elif (cnt >= b):
    ans += ((a%10 + p)%10) * pow(10, cnt)
  else:
    ans += a%10 * pow(10, cnt)
  cnt += 1
  a //= 10

print(int(ans))