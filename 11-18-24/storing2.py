# open the input file
file = open('input.txt', 'r')

# read N and M
line = file.readline().split()
N = int(line[0])
M = int(line[1])

# initialize arr
arr = []
for i in range(N):
  arr.append([])
  for j in range(N):
    arr[i].append(False)

# read the edges
for i in range(M):
  line = file.readline().split()
  a = int(line[0])
  b = int(line[1])

  # it is an undirected graph
  arr[a][b] = True
  arr[b][a] = True

print(arr)