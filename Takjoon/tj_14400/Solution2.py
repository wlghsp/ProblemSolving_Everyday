
N = int(input())
xs = []
ys = []
locs = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    locs.append((x, y))

xs.sort()
ys.sort()
mx = xs[(N - 1) // 2]
my = ys[(N - 1) // 2]

print(sum(abs(x - mx) + abs(y - my) for x, y in locs))