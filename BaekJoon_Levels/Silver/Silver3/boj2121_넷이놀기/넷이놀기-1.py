
N = int(input())
A, B = map(int, input().split())
dots = []
dots_set = set()
for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))
    dots_set.add((x, y))
ans = 0
for x, y in dots:
    if all([(pt in dots_set) for pt in [(x + A, y), (x, y + B), (x + A, y + B)]]):
        ans += 1
print(ans)