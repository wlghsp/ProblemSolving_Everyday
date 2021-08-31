"""




"""
import sys
import math

input = lambda: sys.stdin.readline().rstrip()

m, n = map(int, input().split())


def isPrimenum(k):
    if k <=1:
        return
    for i in range(2, int(math.sqrt(k) + 1)):
        if k % i == 0:
            return False
    return True


for i in range(m, n + 1):
    if isPrimenum(i):
        print(i)        
