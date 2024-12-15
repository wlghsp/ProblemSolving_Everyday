import sys, math

input = lambda: sys.stdin.readline().rstrip()

'''
유클리드 기하학 원 넓이 : pi* r^2
택시 기하학 원의 넓이 2 * r^2
'''
r = int(input())

print(f'{math.pi * (r * r):.6f}')
print(f'{2 * (r*r):.6f}')