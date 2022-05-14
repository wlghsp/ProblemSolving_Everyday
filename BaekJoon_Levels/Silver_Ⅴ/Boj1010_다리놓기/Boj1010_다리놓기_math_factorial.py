

import sys, math
input = lambda : sys.stdin.readline().rstrip()


# nCr = n! / r!(n-r)!

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(bridge)