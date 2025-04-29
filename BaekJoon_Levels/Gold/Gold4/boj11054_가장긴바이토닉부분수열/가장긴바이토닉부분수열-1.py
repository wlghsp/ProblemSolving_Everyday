N = int(input())
arr = list(map(int, input().split()))
dp1 = [1] * (N + 1)
dp2 = [1] * (N + 1)

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if arr[i] > arr[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
res = 0
for i in range(N):
    res = max(res, dp1[i] + dp2[i] - 1)

print(res)
