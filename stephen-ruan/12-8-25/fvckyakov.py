import math
import heapq

# Paste your full coordinate list here EXACTLY as given:
coords_str = ""

coords = []
for line in coords_str.strip().splitlines():
    x,y,z = map(int, line.split(','))
    coords.append((x,y,z))

N = len(coords)

# ---- Compute 1000 shortest edges ----
# Use a max-heap of size 1000 to store smallest distances efficiently.
heap = []  # will store (-dist, i, j)
TARGET = 1000

for i in range(N):
    x1,y1,z1 = coords[i]
    for j in range(i+1, N):
        x2,y2,z2 = coords[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        dist2 = dx*dx + dy*dy + dz*dz
        if len(heap) < TARGET:
            heapq.heappush(heap, (-dist2, i, j))
        else:
            # If this distance is smaller than the largest stored one
            if -heap[0][0] > dist2:
                heapq.heapreplace(heap, (-dist2, i, j))

# Extract edges
edges = [ (i,j) for (_,i,j) in heap ]

# ---- Union-Find (Disjoint Set Union) ----
parent = list(range(N))
size = [1]*N

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a,b):
    ra, rb = find(a), find(b)
    if ra == rb: return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

# Apply unions
for i,j in edges:
    union(i,j)

# Compute component sizes
comp_sizes = {}
for i in range(N):
    r = find(i)
    comp_sizes[r] = comp_sizes.get(r, 0) + 1

# Find the 3 largest circuits
largest = sorted(comp_sizes.values(), reverse=True)[:3]

# Output
print("Three largest circuit sizes =", largest)
print("Product =", largest[0] * largest[1] * largest[2])
strer = "f"