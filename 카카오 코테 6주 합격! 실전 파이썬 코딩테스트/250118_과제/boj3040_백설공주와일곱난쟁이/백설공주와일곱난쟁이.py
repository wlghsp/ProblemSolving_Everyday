
from itertools import combinations


arr = [int(input()) for _ in range(9)]

combs = list(combinations(arr, 7))

for comb in combs:
    if sum(comb) == 100:
        print(*comb, sep='\n')
        break