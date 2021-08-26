nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))

# Bubble sort
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

for num in nums:
    print(num)
