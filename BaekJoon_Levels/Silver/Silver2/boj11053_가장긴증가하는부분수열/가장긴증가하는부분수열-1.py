N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N # 최소 자기 자신 하나로만 구성 1로 초기화
for i in range(N):
    for j in range(i): # i보다 앞에 있는 원소 탐색
        if arr[j] < arr[i]: # 증가하는 수열 조건
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))