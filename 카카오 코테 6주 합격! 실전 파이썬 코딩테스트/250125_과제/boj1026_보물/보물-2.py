
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()

used = [False] * (N + 1)
min_sum = 0
for i in range(N):
    max_val = -1
    max_idx = -1
    for j in range(N):
        if not used[j] and B[j] > max_val:
            max_val = B[j]
            max_idx = j
    min_sum += A[i] * B[max_idx]
    used[max_idx] = True

print(min_sum)
