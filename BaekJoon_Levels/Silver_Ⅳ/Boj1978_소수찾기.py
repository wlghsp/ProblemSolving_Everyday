


import sys

input = lambda : sys.stdin.readline().rstrip()


def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False

    return True


N = int(input())

cnt = 0
for i in map(int, input().split()):
    if isPrime(i): cnt+=1

print(cnt)