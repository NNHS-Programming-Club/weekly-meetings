# optimized simulation

N, T = map(int, input().split())

# read all deliveries
arr = []
for i in range(N):
  d, b = map(int, input().split())
  arr.append((d, b))

# this is so that it will calculate from 0 to T
arr.append((T+1, 0))

ans = 0
hay = 0
for i in range(N):
  # add hay
  hay += arr[i][1]

  # calculate number of days until next delivery
  dist = arr[i+1][0] - arr[i][0]

  if hay > dist:
    # there is enough hay until next delivery
    hay -= dist
    ans += dist
  else:
    # bessie is going to finish all hay before next delivery
    ans += hay
    hay = 0


print(ans)
