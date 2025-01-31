N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]

min_population_diff = float('inf')
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if 0 <= x + d1 + d2 < N and 0 <= y - d1 and y + d2 < N:
                    # 1번 선거구 인구수
                    first_population = 0
                    for r in range(x + d1):
                        for c in range(y + 1):
                            first_population += city[r][c]
                    # 2번 선거구 인구수
                    second_population = 0
                    for r in range(x + d2 + 1):
                        for c in range(y + 1, N):
                            second_population += city[r][c]
                    # 3번 선거구 인구수
                    third_population = 0
                    for r in range(x + d1, N):
                        for c in range(y - d1 + d2 - 1):
                            third_population += city[r][c]
                    # 4번 선거구 인구수
                    fourth_population = 0
                    for r in range(x + d2 + 1, N):
                        for c in range(y - d1 + d2, N):
                            fourth_population += city[r][c]

                    # 5번 선거구 인구수
                    fifth_population = 0

                    # 최대 인구수
                    max_population = max(first_population, second_population, third_population, fourth_population, fifth_population)
                    # 최소 인구수
                    min_population = min(first_population, second_population, third_population, fourth_population, fifth_population)
                    # 최대 인구수 - 최소 인구수 차이 최솟값 비교
                    min_population_diff = min(min_population_diff, max_population - min_population)

print(min_population_diff)