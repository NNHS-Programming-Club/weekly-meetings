pos = 50
ans = 0

with open("stephen-ruan/12-8-25/67input.txt", "r") as f:
    for line in f:
        line = line.strip()
        dir = line[0]
        dist = int(line[1:])
        step = -1 if dir == "L" else 1
        for _ in range(dist):
            pos = (pos + step) % 100
            if pos == 0:
                ans += 1

print(ans)
