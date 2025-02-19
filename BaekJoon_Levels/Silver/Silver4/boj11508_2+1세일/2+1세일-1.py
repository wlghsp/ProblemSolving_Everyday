import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
prices = [int(input()) for _ in range(N)]
ans = 0
i = 0
prices.sort(reverse=True)
while i < N:
    if i + 2 < N:
        ans += prices[i] + prices[i + 1]
        i += 3
    else:
        ans += prices[i]
        i += 1

print(ans)