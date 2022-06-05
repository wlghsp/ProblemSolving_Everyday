
import sys
input = lambda : sys.stdin.readline().rstrip()


T = int(input())

# 중복이 안되는 경우의 수를 구해야 한다.
for i in range(T):
    map = {}
    answer = 1
    n = int(input())
    for j in range(n):
        a, b = input().split()
        if not b in map:
            map[b] = 1
        else:
            map[b] += 1
    for k in map.keys():
        answer *= (map[k] + 1) # 선택 안 한 경우 + 1
    print(answer-1) # 전부 입지 않은 상태 빼기