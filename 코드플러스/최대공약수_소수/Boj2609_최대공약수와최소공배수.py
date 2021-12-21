
"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

출력
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.


24 18

6
72

"""


import sys

input = lambda: sys.stdin.readline().rstrip()


def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return gcd(a,b) * (a//gcd(a,b)) * (b//gcd(a,b))

x,y = map(int, input().split())

print(gcd(x,y))
print(lcm(x,y))

