
N = int(input())
X = []
Y = []
locs = []
for _ in range(N):
    x, y = map(int, input().split())
    locs.append((x, y))
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()

a = X[N // 2]
b = Y[N // 2]
res = 0
for x, y in locs:
    res += abs(x - a) + abs(y - b)

print(res)
