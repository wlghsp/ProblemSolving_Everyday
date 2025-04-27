

N, X = map(int, input().split())
# A = list(map(int, input().split())) # list 이면 O(N)
A = set(map(int, input().split())) # set 이면 O(1)

print("Yes" if X in A else "No")