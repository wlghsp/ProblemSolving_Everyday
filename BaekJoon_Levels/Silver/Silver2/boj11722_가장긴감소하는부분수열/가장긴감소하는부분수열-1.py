N = int(input())
arr = [0] * N
nums = list(map(int, input().split()))
for i in range(N):
    arr[i] = nums[i]
dp = [1] * N

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))