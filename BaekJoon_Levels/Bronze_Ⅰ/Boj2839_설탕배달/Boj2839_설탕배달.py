

import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

answer = 0
while True:
    if N % 5 == 0:
        answer += N // 5
        print(answer)
        break
    else:
        N -= 3
        answer += 1

    if N < 0:
        print("-1")
        break