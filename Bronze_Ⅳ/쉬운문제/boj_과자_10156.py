"""
입력
과자 한 개의 가격 k
사려고하는 과자의 개수 n
현재 동수가 가진 돈 m 

출력
동수가 부모님께 받아야 하는 돈의 액수
"""

import sys

input = lambda: sys.stdin.readline().rstrip()

k, n, m = map(int, input().split())
money_needed = k * n

if money_needed <= m:
    result = 0
else:
    result = money_needed - m

print(result)
