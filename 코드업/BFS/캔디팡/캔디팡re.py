"""
2 1 5 1 1 3 4
2 1 5 1 3 5 3
2 3 4 5 2 2 4
4 4 3 2 3 1 3
4 3 5 3 1 4 3
5 4 4 3 3 5 5
2 1 3 5 1 1 2

4

"""

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

            if nx >= 0 and nx < 7 and ny >= 0 and ny < 7:
                if board[nx][ny] == color and check[nx][ny] == 0:
                    check[nx][ny] = 1 # 방문체크로 1을 삽입
                    queue.append([nx, ny]) # 
                    count += 1

    #  연속 3개 이상인 부분이 있을 경우 리턴 1 = True 없으면 0 = false  

    return 1 if count >= 3 else 0 




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
                count += 1 # 1을 받아 참일 경우 

print(count)