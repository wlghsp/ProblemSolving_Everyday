"""
첫 구름은 (N, 1), (N, 2), (N - 1, 1), (N - 1, 2)

구름 이동하기
d 방향으로 s만큼 이동
구름 이동 후
1. 구름 범위 모두 물의 양 1 증가
2. 대각선 4방향 확인 물의 양 > 0 바구니 수 만큼 증가, 경계 넘어가는 칸 무시,
3. 구름이 있었던 칸 제외 나머지 칸에서 물의 양 2 이상인 칸 구름 생성 및 해당 칸 물의 양 -2

"""
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
            if grid[nx][ny] <= 0: continue
            cnt += 1
        return cnt
    def make_clouds(visited):
        for i in range(N):
            for j in range(N):
                if visited[i][j]: continue
                if grid[i][j] < 2: continue

                grid[i][j] -= 2
                clouds.append((i, j))

    for d, s in moves:
        d = d - 1
        visited = [[False] * N for _ in range(N)]
        for cx, cy in clouds:
            nx, ny = cx + (dir[d][0] * s % N), cy + (dir[d][1] * s % N)
            nx += (N if nx < 0 else 0)
            nx -= (N if nx >= N else 0)
            ny += (N if ny < 0 else 0)
            ny -= (N if ny >= N else 0)

            # 1. 구름 사라지고 1 증가
            grid[nx][ny] += 1
            # 2. 대각선 물 바구니 갯수 확인 후 물의 양 증가
            grid[nx][ny] += cnt_diagonal_basket(nx, ny)
            visited[nx][ny] = True
        clouds.clear()
        make_clouds(visited)
    return sum(sum(row) for row in grid)

print(solve())