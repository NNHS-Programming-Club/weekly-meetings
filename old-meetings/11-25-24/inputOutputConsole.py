# read N
N = int(input())

# read next line and split by space
arr = input().split()
ans = 0

# convert string to int
for i in range(N):
  arr[i] = int(arr[i])
  ans += arr[i]

# write output
print(str(ans) + "\n")
