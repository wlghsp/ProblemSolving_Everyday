import sys, os
sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')
def input(): return sys.stdin.readline().rstrip()

N = int(input())
xs = []
ys = []
res = [0]
locs = []
for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    locs.append((x, y))
    
def get_cost(mx, my, k):
    dists = []
    for x, y in locs:
        dists.append(abs(mx - x) + abs(my - y))
    dists.sort()
    return sum(dists[:k])


for k in range(2, N + 1):
    min_cost = float('inf')
    for cx in xs:
        for cy in ys:
            cost = get_cost(cx, cy, k)
            min_cost = min(min_cost, cost)
    res.append(min_cost)        

print(*res)
