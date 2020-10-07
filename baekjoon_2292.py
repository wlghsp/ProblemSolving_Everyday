import sys
input = sys.stdin.readline


def sugar(N):
    for y in range((n//3)+1):
        for x in range((n//5)+1):
            if ((5*x + 3*y) == n):
                return x+y
    return -1


n = int(input())
print(sugar(n))
