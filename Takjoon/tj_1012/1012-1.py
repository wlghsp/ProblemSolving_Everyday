import sys, os

sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

T = int(input())

for _ in range(T):
    # M: 가로길이, N: 세로길이, K: 배추 갯수
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
    
    def dfs(x, y):
        field[x][y] = -1
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M): continue
            if field[nx][ny] != 1: continue
            
            dfs(nx, ny)
                    
    cnt = 0
    for x in range(N):
        for y in range(M):
            if field[x][y] == 1:
                cnt += 1
                dfs(x, y)
    
    print(cnt)
    
    