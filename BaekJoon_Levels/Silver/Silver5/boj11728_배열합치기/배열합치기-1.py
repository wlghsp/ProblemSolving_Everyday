import sys

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
C = [0] * (N + M)

a, b, c = 0, 0, 0

while a < N and b < M:
    if A[a] > B[b]:
        C[c] = B[b]
        b += 1
    else:
        C[c] = A[a]
        a += 1

    c += 1

while a < N:
    C[c] = A[a]
    a += 1
    c += 1
while b < M:
    C[c] = B[b]
    b += 1
    c += 1

print(*C, sep=' ')