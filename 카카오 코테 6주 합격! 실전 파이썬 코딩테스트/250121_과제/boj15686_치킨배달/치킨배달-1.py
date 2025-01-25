from itertools import combinations

N, M = map(int, input().split())
city = [list(input().split()) for _ in range(N)]
houses = []
chickens = []
min_city_chicken_distance = float('inf')

# 1. 치킨집과 집의 좌표 구하기
for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            houses.append((i, j))
        elif city[i][j] == '2':
            chickens.append((i, j))

# 2. 치킨집 M개를 고르는 조합 구하기 (중복이 없고 순서를 고려하지 않으므로 조합)
chicken_combs = combinations(chickens, M)

# 3. 각 조합 마다 도시의 치킨 거리를 각각 구해서 최솟값을 찾는다.
for chicken_comb in chicken_combs:
    # 치킨집 M개 조합 마다 도시의 치킨 거리를 구하고
    city_chicken_distance = 0
    for hx, hy in houses:
        # 각 집의 치킨 거리를 구한다.
        chicken_distance = float('inf')
        for cx, cy in chicken_comb:
            chicken_distance = min(chicken_distance, abs(cx - hx) + abs(cy - hy))
        city_chicken_distance += chicken_distance
    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

print(min_city_chicken_distance)