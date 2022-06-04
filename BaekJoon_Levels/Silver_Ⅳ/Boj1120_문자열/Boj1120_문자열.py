
'''
추가되는 것을 고민할 것이 아니다 추가되는 것은 무조건 차이가 없게 추가할 수 있기 때문이다.

원래 있던 A와 B를 비교하면서
차이가 가장 작은 경우를 찾으면 그 경우가 A와 B의 차이를 최소화하는 경우임

'''

import sys
input = lambda : sys.stdin.readline().rstrip()


a, b = input().split()


result = []
for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]: # 이렇게 탐색하는 것도 외워두자
            cnt += 1
    result.append(cnt)

print(min(result))