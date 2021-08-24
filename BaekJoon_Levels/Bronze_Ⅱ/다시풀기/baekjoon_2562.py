import sys
input = sys.stdin.readline


nums = []

for _ in range(9):
    a = int(input())
    if a < 100:
        nums.append(a)
    else:
        break
biggest = max(nums)
print(biggest)
print(nums.index(biggest)+1)
