

"""
N = AB로 나타낼 수 있을 때 

A와 B는 N의 약수이다. 

N은 A와 B의 배수이다. 


"""
import sys

input = lambda: sys.stdin.readline().rstrip()


MAX = 1000000

d = [1] * (MAX+1) # d[N] N의 약수의 합 , f(N)들
s = [0] * (MAX+1) # 1-N까지의 약수들의 합을 저장, g(N)e들들
for i in range(2, MAX+1):
    j = 1
    while i*j <= MAX:
        d[i*j] += i
        j += 1

for i in range(1, MAX+1):
    s[i] = s[i-1] + d[i]

t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    ans.append(s[n])

print('\n'.join(map(str, ans)) + '\n')