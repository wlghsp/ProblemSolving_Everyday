"""
-10
20
5
10
3

120

35
92
31
50
11

627


고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.


"""
import sys

input = lambda: sys.stdin.readline().rstrip()

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

result = 0
if a < 0:
    result = abs(a) * c + d + b * e
elif a >= 1:
    result = (b - a) * e

print(result)
