from collections import deque

N = int(input())
arr = list(map(int, input().split()))
jumps = [-1] * N
jumps[0] = 0
q = deque([0])

while q:
    popped = q.popleft()

    for i in range(popped, popped + arr[popped] + 1):
        if i > (N - 1): continue
        if jumps[i] != -1: continue

        jumps[i] = jumps[popped] + 1
        q.append(i)

print(jumps[N - 1])