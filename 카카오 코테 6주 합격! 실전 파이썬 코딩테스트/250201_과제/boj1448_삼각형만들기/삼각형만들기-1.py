import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
straws = [int(input()) for _ in range(N)]

straws.sort()
can_make = False

result = 0
for i in range(len(straws) - 2):
    if straws[i + 2] < (straws[i] + straws[i + 1]):
        can_make = True
        result = max(result, straws[i] + straws[i + 1] + straws[i + 2])
print(result if can_make else -1)