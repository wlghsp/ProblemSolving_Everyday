


str = list(input())

nums = []

for s in str:
    if s.isdigit():
        nums.append(s)
print(int(''.join(nums)))