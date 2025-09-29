# simulation

N, T = map(int, input().split())

# read all deliveries
arr = {}
for i in range(N):
  d, b = map(int, input().split())
  arr[d] = b

hay = 0
ans = 0

# start simulation
for i in range(1, T+1):
  if i in arr:
    # there is a delivery
    hay += arr[i]
  
  if hay > 0:
    # bessie can eat a haybale
    ans += 1
    hay -= 1

print(ans)