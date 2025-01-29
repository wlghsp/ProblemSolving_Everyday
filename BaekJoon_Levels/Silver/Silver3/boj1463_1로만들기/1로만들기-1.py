import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)
# dp[i] : 숫자 i를 1로 만들기 위한 최소 연산 횟수
# 숫자 i에서 1로 가는게 아닌 1에서 i까지 올라가면서 최적해를 구하는 방식

for i in range(2, N + 1):
    # i 에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        # i가 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        # i가 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])