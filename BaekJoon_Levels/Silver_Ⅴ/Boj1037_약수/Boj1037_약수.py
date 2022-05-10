


import sys

input = lambda : sys.stdin.readline().rstrip()

# 약수의 갯수
k = int(input())

# 진짜 약수들
nums = list(map(int, input().split()))

#  최솟값과 최댓값을 구하고 이를 곱하면 N을 구할 수 있다.
print(max(nums) * min(nums))
