
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

result = 0
num = input()
for i in range(len(num)):
    result += int(num[i])
print(result)