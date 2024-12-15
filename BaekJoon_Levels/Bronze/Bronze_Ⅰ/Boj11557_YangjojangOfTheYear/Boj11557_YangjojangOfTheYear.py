import sys
input = lambda : sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    N = int(input())
    univs = []
    for i in range(N):
        name, amount = input().split()
        univs.append((int(amount), name))
    univs.sort(key=lambda x: x[0])
    print(univs[-1][1])

