
N = int(input())

nums = list(map(int, input().split()))

print(nums[0], end=' ')
for i in range(1, len(nums)):
    if nums[i-1] < nums[i]:
        print(nums[i], end=' ')

