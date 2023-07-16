import sys
input =lambda : sys.stdin.readline().rstrip()
n = int(input())


ans = 0
for a in range(2, n - 1, 2):
    for b in range(1, n - 1):
        for c in range(1, n - 1):
            if a + b + c != n:
                continue
            if c < b + 2:
                continue
            ans = ans + 1
print(ans)


