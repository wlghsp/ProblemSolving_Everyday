import sys

input = sys.stdin.readline

sumOfSeconds = 0

for _ in range(4):
    sumOfSeconds += int(input())

print(sumOfSeconds // 60)
print(sumOfSeconds % 60)
