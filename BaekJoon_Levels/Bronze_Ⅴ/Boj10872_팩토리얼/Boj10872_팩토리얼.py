import sys
input = lambda : sys.stdin.readline().rstrip()

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input())
print(factorial(n))