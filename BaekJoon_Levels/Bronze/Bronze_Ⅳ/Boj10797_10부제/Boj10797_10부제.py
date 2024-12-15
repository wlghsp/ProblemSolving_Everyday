import sys
input = lambda : sys.stdin.readline().rstrip()
num = input()
arr = list(input().split())
cnt = 0
for a in arr:
    if a == num:
        cnt += 1

print(cnt)
