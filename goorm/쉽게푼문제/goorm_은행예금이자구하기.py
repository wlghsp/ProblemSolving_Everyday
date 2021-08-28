"""
100000 5.5 5

130696.00

5550000 2.3 2

5808235.95
"""
import sys

input = lambda: sys.stdin.readline().rstrip()
nums = list(input().split())
principal = int(nums[0])
interest = float(nums[1])
duration = int(nums[2])

# 복리공식 : 원리금: 원금 * (1 + 이자율)**기간, 복리횟수가 1인 경우임.
# 복리횟수가 1회 이상인 경우 -> 원리금: 원금 * (1 + 이자율/1년 복리횟수)**기간
result = principal * ((1 + interest / 100) ** duration)

print("%.2f" % result)
