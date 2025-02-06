import sys

input = lambda : sys.stdin.readline().rstrip()
N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
arr.sort()
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + arr[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L - 1])