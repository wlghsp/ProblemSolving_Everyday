

import sys
input = lambda : sys.stdin.readline()

N = int(input())

result = 0

for _ in range(N):
    result += int(input())

print(result -(N-1))