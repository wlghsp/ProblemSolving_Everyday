import sys

input = sys.stdin.readline


n = int(input())
result = 0
mod = 1000000007
# 자연수 세제곱의 합 구하는 공식인데 이를 두번 mod로 나누어 수가 커지는 경우에 대비
result = (n * (n + 1) // 2) % mod
result = result * result % mod


print(result)
