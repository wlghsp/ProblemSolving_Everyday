N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 -1로 초기화 (아직 안 구한 상태)
dp = [[-1] * N for _ in range(N)]

# (x, y)에서 시작해서 얻을 수 있는 최대합
def dfs(x, y):
    # 마지막 행이면 더 내려갈 곳이 없으니까 자기 자신 반환
    if x == N - 1:
        return triangle[x][y]
    # 이미 구한 값이면 바로 반환
    if dp[x][y] != -1:
        return dp[x][y]

    # 아래, 아래 오른쪽 중 큰 것  + 현재 값
    dp[x][y] = triangle[x][y] + max(dfs(x + 1, y), dfs(x + 1, y + 1))

    return dp[x][y]


print(dfs(0, 0))