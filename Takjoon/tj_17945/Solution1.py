

a, b = map(int, input().split())
res = []
for x in range(-1000, 1001, 1):
    c = (x * x) + 2 * a * x + b
    if c == 0:
        res.append(x)
print(*res)