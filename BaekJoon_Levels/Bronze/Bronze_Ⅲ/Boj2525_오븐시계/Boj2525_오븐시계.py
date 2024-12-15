
import sys
input = lambda : sys.stdin.readline().rstrip()


'''
현재 시각 A B
요리하는데 필요한 시간 C 
'''
a, b = map(int, input().split())
c = int(input())

min = b + c

if min >= 60:
    up = min // 60
    a += up
    min -= 60 * up

if a >= 24:
    a -= 24

print(a, min)

