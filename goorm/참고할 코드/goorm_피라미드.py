import sys

input = sys.stdin.readline


n = int(input())


for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (1 + (i - 1) * 2))

# 등차수열 첫 째항 a, n번째항을 구하는 공식, 공차는 d
#  a + (n-1) * d
