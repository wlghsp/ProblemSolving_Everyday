N = int(input())
A = list(map(int, input().split()))
A_set = set(A)
found = False

for i in range(N):
    for j in range(i + 1, N):
        needed = 1000 - A[i] - A[j]

        if needed in A_set:
            cnt = (A[i] == needed) + (A[j] == needed)
            if A.count(needed) > cnt:
                found = True
                break
    if found:
        break

print("Yes" if found else "No")