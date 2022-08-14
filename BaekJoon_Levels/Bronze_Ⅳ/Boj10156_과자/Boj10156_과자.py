import sys
input = lambda : sys.stdin.readline().rstrip()

'''
k 과자 한개의 가격
n 사려고 하는 과자의 개수
m 현재 가진 돈의 액수
'''
k, n, m = map(int, input().split())

total = k * n
result = total - m
if result < 0:
    print(0)
else:
    print(result)