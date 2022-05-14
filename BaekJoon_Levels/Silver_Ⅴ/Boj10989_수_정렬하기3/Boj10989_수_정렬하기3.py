

# pypy3는 메모리초과, python3로 돌려야 함.
import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

# 카운팅 소트

arr = [0] * 10001

for i in range(N):
    arr[int(input())] += 1

for i in range(10001):
    while arr[i] > 0:
        print(i)
        arr[i] -= 1


# for i in range(10001):
#     if arr[i] != 0:
#         for j in range(arr[i]):
#             print(i)