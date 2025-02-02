import sys

input = sys.stdin.readline
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

                border = [[False] * N for _ in range(N)]
                # 경계선 그리기
                for i in range(d1 + 1): # 1번과 4번
                    border[x + i][y - i] = True
                    border[x + d2 + i][y + d2 - i] = True
                for i in range(d2 + 1): # 2번과 3번
                    border[x + i][y + i] = True
                    border[x + d1 + i][y - d1 + i] = True

                # 지도의 경계에서 안쪽 경계로 탐색해야 정확히 구역 체크 가능
                # 안쪽에서 시작하면 경계 내부 인구가 포함될 수 있음
                # 1번 선거구
                first_population = 0
                for r in range(x + d1):
                    for c in range(y + 1):
                        if border[r][c]: break
                        first_population += city[r][c]

                # 2번 선거구
                second_population = 0
                for r in range(x + d2 + 1):
                    for c in range(N - 1, y, -1):
                        if border[r][c]: break
                        second_population += city[r][c]

                # 3번 선거구
                third_population = 0
                for r in range(x + d1, N):
                    for c in range(y - d1 + d2):
                        if border[r][c]: break
                        third_population += city[r][c]

                # 4번 선거구
                fourth_population = 0
                for r in range(x + d2 + 1, N):
                    for c in range(N - 1, y - d1 + d2 - 1, -1):
                        if border[r][c]: break
                        fourth_population += city[r][c]

                # 5번 선거구 인구수
                fifth_population = total_population - first_population - second_population - third_population - fourth_population

                # 최대 인구수
                max_population = max(first_population, second_population, third_population, fourth_population, fifth_population)
                # 최소 인구수
                min_population = min(first_population, second_population, third_population, fourth_population, fifth_population)
                # 최대 인구수 - 최소 인구수 차이 최솟값 비교
                min_population_diff = min(min_population_diff, max_population - min_population)

print(min_population_diff)