
import sys
input = lambda : sys.stdin.readline().rstrip()
a, b = map(int, input().split())

n = ((b-a)+1)
print(n*(a+b)//2)
