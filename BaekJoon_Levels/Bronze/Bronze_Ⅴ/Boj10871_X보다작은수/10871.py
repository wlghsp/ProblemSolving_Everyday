

N, X = map(int, input().split())
arr = list(map(int, input().split()))

for n in arr:
    if X > n:
        print(n, end=' ')

