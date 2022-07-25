import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

k = 1
cnt = 0
while n != 0:
    if n >= k:
        n -= k
    else:
        k = 1
        n -= k
    k += 1
    cnt += 1
print(cnt)