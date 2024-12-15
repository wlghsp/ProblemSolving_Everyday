import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
result = 0
maxVal = max(arr)
total = sum(arr)

print(100 * total / maxVal / N)
