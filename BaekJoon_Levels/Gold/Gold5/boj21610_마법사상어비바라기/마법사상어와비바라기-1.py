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
        clouds.clear()
        for i in range(N):
            for j in range(N):
                if visited[i][j]: continue
                if grid[i][j] < 2: continue

                grid[i][j] -= 2
                clouds.append((i, j))

    def get_nx_ny(cx, cy, d, s):
        return (cx + dir[d][0] * s) % N, (cy + dir[d][1] * s) % N

    for d, s in moves:
        d = d - 1
        visited = [[False] * N for _ in range(N)]

        # 1. 구름 이동 및 비 내리기
        new_positions = []
        for cx, cy in clouds:
            nx, ny = get_nx_ny(cx, cy, d, s)
            grid[nx][ny] += 1
            visited[nx][ny] = True
            new_positions.append((nx, ny))

        # 2. 대각선 물 바구니 갯수 확인 후 물의 양 증가
        for nx, ny in new_positions:
            grid[nx][ny] += cnt_diagonal_basket(nx, ny)

        make_clouds(visited)

    return sum(sum(row) for row in grid)


print(solve())
