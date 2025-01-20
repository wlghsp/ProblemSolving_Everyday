

from itertools import combinations

nums = [int(input()) for _ in range(9)]

combs = combinations(nums, 7)

for comb in combs:
    if sum(comb) == 100:
        print(*comb, sep='\n')
        break