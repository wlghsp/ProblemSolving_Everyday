N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Please write your code here.
dp = [[0] * 3 for _ in range(N)]
dp[0][0] = A[0]
dp[0][1] = B[0]
dp[0][2] = C[0]

for i in range(1, N):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + A[i]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + B[i]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + C[i]

print(max(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))


"""
4
1 10 3 5
8 3 7 1
2 1 2 9

34
"""