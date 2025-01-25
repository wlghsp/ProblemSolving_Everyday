

from itertools import combinations

numbers = [int(input()) for _ in range(9)]

combs = combinations(numbers, 7)

for comb in combs:
    if sum(comb) == 100:
        print(*comb, sep='\n')
        break