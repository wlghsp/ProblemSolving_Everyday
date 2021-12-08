
"""
피보나치 수열이란 앞의 두 수를 더하여 나오는 수열이다.
첫 번째 수와 두 번째 수는 모두 1이고, 세 번째 수부터는 이전의 두 수를 더하여 나타낸다. 피보나치 수열을 나열해 보면 다음과 같다.

1, 1, 2, 3, 5, 8, 13 …

자연수 N을 입력받아 N번째 피보나치 수를 출력하는 프로그램을 작성하시오.


입력
자연수 N이 입력된다. (N은 20보다 같거나 작다.)

출력
N번째 피보나치 수를 출력한다.

입력 예시
7

출력 예시
13

"""


import sys
input = lambda : sys.stdin.readline().rstrip()


# 재귀
def fib(n):
    if n <=2:
        return 1
    return fib(n-1) + fib(n-2)


# dp 재귀 함수 활용  top-down
def fib_dp(n):
    if n == 0:
        return 0
    if n ==1 or n == 2:
        return 1

    if dp[n] != 0:
        return dp[n]

    dp[n] = fib_dp(n-1) + fib_dp(n-2)

    return dp[n]


dp = [0] * 30 # 0으로 초기화 하기
num = int(input())

dp[1] = dp[2] = 1

# dp  재귀 호출
print(fib_dp(num))

# dp 반복문 bottom-up
for i in range(3, num+1):
    dp[i] = dp[i-1] + dp[i-2]

# print(dp[num])

