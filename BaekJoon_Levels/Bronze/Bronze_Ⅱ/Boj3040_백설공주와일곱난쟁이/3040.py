
def print_dwarves(nums, x, y):
    for i in range(len(nums)):
        if i != x and i != y:
            print(nums[i])

nums = []
for _ in range(9):
    nums.append(int(input()))

total = sum(nums)

for i in range(9):
    for j in range(i + 1, 9):
        if total - nums[i] - nums[j] == 100:
            print_dwarves(nums, i, j)
            break