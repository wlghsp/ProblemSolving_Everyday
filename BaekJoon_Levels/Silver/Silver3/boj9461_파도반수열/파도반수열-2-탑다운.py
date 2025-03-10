
T = int(input())
dp = [-1] * 101
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2

def recur(num):
    if dp[num] != -1:
        return dp[num]

    dp[num] = recur(num - 1) + recur(num - 5)

    return dp[num]

for _ in range(T):
    print(recur(int(input())))