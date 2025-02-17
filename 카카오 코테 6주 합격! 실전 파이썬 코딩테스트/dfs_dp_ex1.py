N, M = 5, 5

dp = [[-1] * M for _ in range(N)] # -1이면 아직 계산 안 한 상태

def dfs(x, y):
    # 도착점에 도달했으면 경우의 수 1 리턴
    if x == N - 1 and y == N - 1:
        return 1

    # 이미 (x, y)에서 출발한 경우의 수를 구해놨으면 그거 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    # 아직 안 구해봤으면 직접 구해보자
    dp[x][y] = 0 # 일단 0으로 초기화 해두고 시작

    # 아래로 이동
    if x + 1 < N:
        dp[x][y] += dfs(x + 1, y)

    # 오른쪽으로 이동
    if y + 1 < M:
        dp[x][y] += dfs(x, y + 1)

    return dp[x][y]
print(dfs(0, 0))