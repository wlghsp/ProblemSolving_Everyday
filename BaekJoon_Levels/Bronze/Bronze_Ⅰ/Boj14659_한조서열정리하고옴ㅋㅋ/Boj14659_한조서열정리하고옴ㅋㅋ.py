import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

arr = list(map(int, input().split()))

maxVal = 0
ans = 0
cnt = 0
for w in arr:
    if w > maxVal:
        maxVal = w
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)
print(ans)