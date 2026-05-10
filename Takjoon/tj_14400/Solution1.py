
import sys, os
sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

N = int(input())

locs = []
xs = []
ys = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    locs.append((x, y))

xs.sort()
ys.sort()
mx = xs[(N - 1) // 2]
my = ys[(N - 1) // 2]

# res = 0
# for x, y in locs:
#     res += abs(x - mx) + abs(y - my)

print(sum(abs(x - mx) + abs(y - my) for x, y in locs))


