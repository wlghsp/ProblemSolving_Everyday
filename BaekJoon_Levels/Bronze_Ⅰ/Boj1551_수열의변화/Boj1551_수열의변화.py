import sys
input = lambda : sys.stdin.readline().rstrip()
N, K = map(int, input().split())

A = list(map(int, input().split(",")))
B = [0] * (len(A) - 1)
for _ in range(K):
    for i in range(len(A) - 1):
        B[i] = A[i+1] - A[i]
    A = B
    B = [0] * (len(A) - 1)

print(','.join(map(str, A)))