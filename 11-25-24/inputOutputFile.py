# open input and output
fin = open("input.txt", "r")
fout = open("output.txt", "w")

# read N
N = int(fin.readline())

# read next line and split by space
arr = fin.readline().split()
ans = 0

# convert string to int
for i in range(N):
  arr[i] = int(arr[i])
  ans += arr[i]

# write output
fout.write(str(ans) + "\n")

# close files
fin.close()
fout.close()