import sys
input = sys.stdin.readline
""" 

걍 "비와이"가 출력되면 맞는 문제 
"""
n, k = map(int, input().split())

for _ in range(n):
    on, off = map(int, input().split())
    k += on - off

print(k)
print("비와이")
