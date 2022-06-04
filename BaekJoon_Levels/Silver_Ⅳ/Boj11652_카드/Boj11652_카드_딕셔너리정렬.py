


import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

map = {}

for _ in range(N):
    num = int(input())
    if num not in map:
        map[num] = 1
    else:
        map[num] += 1

# 값은 내림차순, 키는 오름차순
sortedMap = sorted(map.items(), key=lambda x: (-x[1], x[0]))
print(sortedMap[0][0])
