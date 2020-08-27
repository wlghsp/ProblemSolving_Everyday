# 20 30 10
# 20

# 30 30 10
# 30
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))
