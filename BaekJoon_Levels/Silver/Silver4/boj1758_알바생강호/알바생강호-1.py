import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
tips = [int(input()) for _ in range(N)]
tips.sort(reverse=True)

res = 0
for i in range(N):
    tip = tips[i] - (i + 1 - 1)
    if tip > 0:
        res += tip
print(res)