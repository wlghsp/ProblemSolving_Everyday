import sys
input = lambda : sys.stdin.readline().rstrip()


n = int(input())

result = 5

for i in range(2, n+1):
    result += (3 * i) + 1

print(result % 45678)

