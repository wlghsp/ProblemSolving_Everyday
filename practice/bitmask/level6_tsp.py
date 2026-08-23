"""
Level 6 - TSP (외판원 순회), dp[mask][last]

비트마스킹 DP의 대표 종착지 문제입니다.
0번 도시에서 출발해 모든 도시를 한 번씩 방문하고 다시 0번으로 돌아오는
최소 비용을 구하세요.

dist[i][j] = i에서 j로 가는 비용 (dist[i][i] = 0)

이 레벨은 N <= 15 정도까지가 현실적인 상한선입니다 (dp[mask][last] 크기 = 2^N * N).
"""


def tsp_min_cost(dist: list[list[int]]) -> int:
    # 힌트:
    # dp[mask][last] = mask에 해당하는 도시들을 모두 방문했고,
    #                  마지막으로 last 도시에 있을 때의 최소 비용
    # 시작: dp[1][0] = 0 (0번 도시만 방문한 상태)
    # 전이: dp[mask | (1<<next)][next] = min(..., dp[mask][last] + dist[last][next])
    # 답: 모든 도시를 방문한 마스크에서 다시 0으로 돌아오는 비용까지 더한 최솟값
    pass


if __name__ == "__main__":
    # 4개 도시, 대칭 거리 행렬
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]
    # 잘 알려진 예제: 최적 경로 0-1-3-2-0 = 10+25+30+15 = 80
    assert tsp_min_cost(dist) == 80, f"got {tsp_min_cost(dist)}"

    print("Level 6 all tests passed!")
