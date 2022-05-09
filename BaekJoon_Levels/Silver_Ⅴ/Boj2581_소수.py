import math
import sys

input = lambda : sys.stdin.readline().rstrip()

def isPrime(num):
    if num ==1 or num == 0:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

M = int(input())
N = int(input())

nums = []
for i in range(M, N+1):
    if isPrime(i):
        nums.append(i)
if len(nums) > 0:
    print(sum(nums))
    print(min(nums))
else:
    print(-1)