
# 답안 보고 했음.. 이중포문 넘 어려워 ... ㅜㅜ

import sys

input = sys.stdin.readline

n = int(input())

for i in range(1, n + 1):
    for x in range(0, n):
        print(str(i + n * x), end=" ")
    print()
