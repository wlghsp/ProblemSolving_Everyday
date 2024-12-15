import sys

input = lambda: sys.stdin.readline().rstrip()

r, c = map(int, input().split())
visit = [[False for _ in range(c + 1)] for _ in range(r + 1)]
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def simulation():
    curve = 0
    x, y, d = 1, 1, 0
    while True:
        visit[x][y] = True

        nx = x + dx[d]
        ny = y + dy[d]

        if nx >= 1 and ny >= 1 and nx <= r and ny <= c and not visit[nx][ny]:
            x = nx
            y = ny
        else:
            d = (d + 1) % 4 # 이 부분이 키포인트 시계방향으로 회전 시킴
            x += dx[d]
            y += dy[d]
            if visit[x][y]:
                break
            curve += 1

    print(curve)


simulation()
