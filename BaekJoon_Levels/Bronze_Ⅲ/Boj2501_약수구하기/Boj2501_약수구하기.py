import sys
input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
cnt = 0
found = False
for i in range(1, n+1):
    if n % i == 0:
       cnt += 1
    if cnt == k:
        print(i)
        found = True
        break

if not found:
    print("0")