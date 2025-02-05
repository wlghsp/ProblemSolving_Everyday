N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            # 기존 j까지 증가수열 길이에서 1을 더한 것과 비교
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))