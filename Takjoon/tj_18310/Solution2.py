


N = int(input())
locs = list(map(int,input().split()))

locs.sort()

print(locs[(N - 1) // 2])