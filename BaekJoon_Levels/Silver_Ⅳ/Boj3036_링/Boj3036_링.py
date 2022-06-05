
''''
기약분수: 분모와 분자를 최대공약수로 약분하여 1 이외의 공약수를 갖지 않도록 만든 분수

유클리드호제법으로 최대공약수를 구하고 분자와 분모를 최대공약수로 나눠주면 됨
'''

import sys

input = lambda: sys.stdin.readline().rstrip()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

N = int(input())

arr = [i for i in map(int, input().split())]

bunmo = arr[0]

for i in range(1, len(arr)):
    gcd_result = gcd(arr[i], bunmo)
    print(f"{bunmo//gcd_result}/{arr[i]//gcd_result}")


