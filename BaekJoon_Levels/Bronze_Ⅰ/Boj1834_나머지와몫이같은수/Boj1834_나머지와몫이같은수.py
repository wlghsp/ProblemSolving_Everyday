import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())

num = 0
for i in range(N+1, N**2,N+1):
    num += i
print(num)