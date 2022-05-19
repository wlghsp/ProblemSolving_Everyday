from collections import deque


def solution(rows, columns, maze, r1, c1, r2, c2):
    answer = 0

    def is_valid_coord(y, x):
        return 0 <= y < N and 0 <= x < N

    dy = (0, 1, 0, -1)
    dx = (1, 0, -1, 0)

    N = rows ** 2
    M = columns ** 2

    board = [[0 for _ in range(columns)] for _ in range(rows)]
    for m in maze:
        a, b, c, d = m
        board[a - 1][b - 1] = 1
        board[c - 1][d - 1] = 1
    print(board)

    # while len(dq) > 0:
    #     y, x, d = dq.popleft()

    #     if y == N - 1 and x == M - 1:
    #         answer = d
    #         break

    #     for k in range(4):
    #         ny = y + dy[k]
    #         nx = x + dx[k]
    #         nd = d + 1
    #         if is_valid_coord(ny, nx) and board[ny][nx] == "1" and not chk[ny][nx]:
    #             chk[ny][nx] = True
    #             dq.append((ny, nx, nd))

    return answer


rows = 2
columns = 3
maze = [[1, 1, 2, 1], [2, 1, 2, 2], [2, 2, 2, 3], [1, 2, 1, 3], [2, 2, 1, 2]]
r1, c1, r2, c2 = 3, 1, 1, 9
print(solution(rows, columns, maze, r1, c1, r2, c2))  # 12
