dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diagonal = [(-1, -1), (-1, 1), (1, 1), (1, -1)]


def solve():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    moves = [list(map(int, input().split())) for _ in range(M)]
    clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]

    def cnt_diagonal_basket(x, y):
        cnt = 0
        for dx, dy in diagonal:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue
            if grid[nx][ny] >= 1:
                cnt += 1
        return cnt

    def make_clouds(visited):
        for i in range(N):
            for j in range(N):
                if visited[i][j]: continue
                if grid[i][j] < 2: continue

                grid[i][j] -= 2
                clouds.append((i, j))

    def get_nx_ny(cx, cy, d, s):
        for _ in range(s):
            cx += dir[d][0]
            cy += dir[d][1]

            if cx == -1:
                cx = N - 1
            if cy == -1:
                cy = N - 1
            if cx == N:
                cx = 0
            if cy == N:
                cy = 0

        return cx, cy

    for d, s in moves:
        d = d - 1
        visited = [[False] * N for _ in range(N)]
        # 1. 구름 사라지고 1 증가
        for cx, cy in clouds:
            nx, ny = get_nx_ny(cx, cy, d, s)
            grid[nx][ny] += 1
            visited[nx][ny] = True

        # 2. 대각선 물 바구니 갯수 확인 후 물의 양 증가
        for cx, cy in clouds:
            nx, ny = get_nx_ny(cx, cy, d, s)
            grid[nx][ny] += cnt_diagonal_basket(nx, ny)

        clouds.clear()
        make_clouds(visited)
    return sum(sum(row) for row in grid)


print(solve())
