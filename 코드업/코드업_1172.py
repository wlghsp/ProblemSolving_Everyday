import sys

input = lambda: sys.stdin.readline().rstrip()


nums = list(map(int, input().split()))


nums.sort()

print(*nums)
