import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())

ans = 0
for i in range(N, 3, -1):
    remove_i = str(i).replace("7","").replace("4", "")
    if not remove_i:
        ans = i
        break
print(ans)