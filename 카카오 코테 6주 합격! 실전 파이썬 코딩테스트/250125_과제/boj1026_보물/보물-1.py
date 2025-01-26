N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
used = [False] * len(B)

result = 0

for a in A:
    max_val = -1
    max_idx = -1
    for i in range(len(B)):
        if not used[i] and B[i] > max_val:
            max_val = B[i]
            max_idx = i
    result += a * max_val
    used[max_idx] = True


print(result)