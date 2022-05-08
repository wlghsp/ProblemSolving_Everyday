
import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

# 문제에 수의 중복이 없다고 하여 boolean으로 체크하여 입력되면 True로 바꿔줌
"""
  range : -1000 ~ 1000
  0 은 index[1000] 을 의미
"""
arr = [False] * 2001


for i in range(N):
    arr[int(input()) + 1000] = True


for i in range(2001):
    if arr[i]:
        print(i- 1000)
