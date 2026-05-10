

N = int(input())
locs = list(map(int, input().split()))

locs.sort()

res = locs[(N - 1) // 2]
print(res)