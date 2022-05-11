


import sys

input = lambda : sys.stdin.readline().rstrip()


def GCD(a, b):
    return GCD(b, a%b) if b != 0 else a

def LCM(a, b):
    return (a*b) // GCD(a,b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    print(LCM(a,b))

