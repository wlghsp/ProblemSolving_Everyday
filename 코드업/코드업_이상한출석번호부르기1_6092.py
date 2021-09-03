n = int(input())
input_nums = list(map(int, input().split()))

all_nums = [0 for _ in range(1, 24)]


for i in input_nums:
    all_nums[i - 1] += 1

print(*all_nums)
