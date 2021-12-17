


"""

5457
3
6 7 8

6

100
5
0 1 2 3 4

0

"""
# https://seol-limit.tistory.com/48
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
m = int(input())

broken = [False]  * 10

if m > 0:
    a = list(map(int, input().split()))
else:
    a = []

for x in a:
    broken[x] = True # 고장난 번호 

def possible(c):
    if c == 0:
        return 0 if broken[0] else 1
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l


ans = abs(n - 100)
for i in range(0, 1000000+1):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c - n)
        if ans > l + press:
            ans = l + press

print(ans)