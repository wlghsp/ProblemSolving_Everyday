N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def dfs(x, y, prev_dir, cnt):
    if cnt > K:
        return 0

    if x == N - 1 and y == N - 1:
        return 1

    total = 0
    for i, (dx, dy) in enumerate([(0, 1), (1, 0)]):  # 0: 오른쪽, 1: 아래
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N): continue
        if grid[nx][ny] == 1: continue

        total += dfs(nx, ny, i, cnt if prev_dir == -1 or prev_dir == i else cnt + 1)
    return total

# 진짜로 (0,0)부터 시작, prev_dir 없음, 방향 전환 0회
print(dfs(0, 0, -1, 0))

"""
3 1
0 0 0
0 0 0
0 0 0

2
"""