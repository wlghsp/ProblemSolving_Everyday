import sys

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
total_population = sum(sum(row) for row in city)

min_population_diff = float('inf')

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 >= N: continue
                if y - d1 < 0 or y + d2 >= N: continue

                # 경계선 그리기
                boundary = [[False] * N for _ in range(N)]
                for i in range(d1 + 1): # 1, 4 번
                    boundary[x + i][y - i] = True
                    boundary[x + d2 + i][y + d2 - i] = True
                for i in range(d2 + 1): # 2, 3 번
                    boundary[x + i][y + i] = True
                    boundary[x + d1 + i][y - d1 + i] = True

                population = [0] * 5
                # 1번 선거구
                for r in range(x + d1):
                    for c in range(y + 1):
                        if boundary[r][c]: break
                        population[0] += city[r][c]
                # 2번 선거구
                for r in range(x + d2 + 1):
                    for c in range(N - 1, y, -1):
                        if boundary[r][c]: break
                        population[1] += city[r][c]
                # 3번 선거구
                for r in range(x + d1, N):
                    for c in range(y - d1 + d2):
                        if boundary[r][c]: break
                        population[2] += city[r][c]
                # 4번 선거구
                for r in range(x + d2 + 1, N):
                    for c in range(N - 1, y - d1 + d2 - 1, -1):
                        if boundary[r][c]: break
                        population[3] += city[r][c]
                # 5번 선거구
                population[4] = total_population - sum(population)

                min_population = min(population)
                max_population = max(population)

                min_population_diff = min(min_population_diff, max_population - min_population)

print(min_population_diff)



