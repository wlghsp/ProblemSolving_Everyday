nums = []
n = int(input())
for _ in range(n):
    nums.append(int(input()))

# Insert sort
for i in range(1, len(nums)):
    while (i > 0) & (nums[i] < nums[i - 1]):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
        i -= 1

for num in nums:
    print(num)
