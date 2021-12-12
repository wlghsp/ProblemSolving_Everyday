"""
5
1 6
3 7
6 2
7 100
9 635

1
7
6
1
9

그냥 풀면 시간초과 뜬다. 
나머지 % 연산을 자주 할 수 있도록 머리를 굴려야 한다. 
어렵다 

"""
import sys

input = lambda: sys.stdin.readline().rstrip()
t = int(input())

tc = []
for _ in range(t):
    a1, b1 = map(int, input().split())
    tc.append([a1, b1])

for t in tc:
    t[0] = t[0] % 10

    if t[0] == 0:
        print(10)
    elif t[0] in [1, 5, 6]:
        print(t[0])
    elif t[0] in [4, 9]:
        t[1] = t[1] % 2
        if t[1] == 0:
            print(t[0] ** 2 % 10)
        else:
            print(t[0])
    else:  # 2, 3, 7, 8 일때
        if t[1] % 4 == 0:
            print(t[0] ** 4 % 10)
        else:
            print(t[0] ** (t[1] % 4) % 10)
