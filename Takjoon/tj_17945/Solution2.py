

a, b = map(int, input().split())
ans = []

for x in range(-1000, 1001):
    res = (x * x) + 2 * a * x + b
    if res == 0:
        ans.append(x) 

print(*ans)