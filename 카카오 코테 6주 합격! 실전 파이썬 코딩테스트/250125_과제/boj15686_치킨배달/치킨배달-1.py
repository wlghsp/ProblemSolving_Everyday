import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
city = [list(input().split()) for _ in range(N)]
houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            houses.append([i, j])
        elif city[i][j] == '2':
            chickens.append([i, j])

min_chicken_distance = float('inf')

combs = combinations(chickens, M)

for comb in combs:
    city_chicken_distance = 0
    for hx, hy in houses:
        chicken_distance = float('inf')
        for cx, cy in comb:
            chicken_distance = min(chicken_distance, abs(hx - cx) + abs(hy - cy))
        city_chicken_distance += chicken_distance
    min_chicken_distance = min(min_chicken_distance, city_chicken_distance)

print(min_chicken_distance)