import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(x, y, board, check):
    queue = deque()
    queue.append([x,y])
    check[x][y] = 1


    color = board[x][y]

    count = 1
     

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx > 0 and nx < 7 and ny > 0 and ny < 7:
                if board[nx][ny] == color and check[nx][ny] == 0:
                    count += 1

    return 1 if count >= 3 else 0 # 1은 True, 0 은 false 




# 1. board 입력
board = [list(map(int, input().split())) for _ in range(7)]

# 2. 탐색 체크 
check = [[ 0 for _ in range(7)] for _ in range(7)]

# 3. 탐색방향  동 서 남 북
global dx, dy
dx = [0, 0, 1, -1] 
dy = [1, -1, 0, 0]


# 4. 탐색 시작
count = 0


for i in range(7):
    for j in range(7):
        if check[i][j] == 0:
            if bfs(i, j, board, check):
                count += 1

print(count)