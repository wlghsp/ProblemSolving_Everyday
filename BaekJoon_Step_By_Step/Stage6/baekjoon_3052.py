import sys
input = sys.stdin.readline

nums = []
for _ in range(10):
    nums.append(int(input()))
result = set()
for i, v in enumerate(nums):
    result.add(v % 42)

print(len(result))
