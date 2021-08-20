""" 
7 3 2 750
3000

60 10 300 1000
1500000
n 여름의 일 수
t 스타후르츠가 자라는데 걸리는 일 수
c 후르츠 심을 수 있는 칸의 수
p 스타후르츠 개당 가격
"""
import sys

input = sys.stdin.readline

n, t, c, p = map(int, input().split())
print((n - 1) // t * c * p)

# countFruits = 0
# for _ in range((n - 1) // t):
#     countFruits += c

# print(countFruits * p)

