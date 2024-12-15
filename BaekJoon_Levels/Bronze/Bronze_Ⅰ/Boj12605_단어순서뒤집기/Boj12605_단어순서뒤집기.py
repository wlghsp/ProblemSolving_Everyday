import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
idx = 1
for _ in range(N):
    sen = list(input().split())
    sen.reverse()

    print(f"Case #{idx}: ", end="")
    idx += 1
    print(*sen)
