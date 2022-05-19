
"""
10∗10 크기의 그림이 있다. 이 그림에 그림판 색 채우기 기능을 구현하시오.
(단, 원점은 왼쪽 위 끝이고, x 값은 오른쪽, y값은 아래로 갈수록 증가한다.)

입력
10∗10크기의 그림과 색칠할 좌표의 x,y값이 차례로 입력된다.
_ 는 색칠되지 않은 부분이고 * 는 색칠된 부분이다.


출력
색 채우기를 한 결과를 출력한다.

__________
_____****_
_____*__*_
__*******_
__*__*_**_
__*__****_
__*____*__
__*____*__
__******__
__________
6 2

__________
_____****_
_____****_
__*******_
__*__*_**_
__*__****_
__*____*__
__*____*__
__******__
__________

"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    board[x][y] = '*'
    check[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < 10 and ny >= 0 and ny < 10:
                if board[nx][ny] == '_' and check[nx][ny] == 0: # 색칠이 아직 안되었고, 방문한적이 없다면 
                    check[nx][ny] = 1
                    board[nx][ny] = '*'
                    queue.append([nx, ny])



# 1. board 입력 
board = [list(map(str, input())) for _ in range(10)]

# 2. 시작 점 
y, x = map(int, input().split())

# 3. 방문 체크 
check = [ [0 for _ in range(10)] for _ in range(10)]

# 4. 탐색방향 동 서 남 북
# global dx, dy
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# 5. 시작점이 색칠되지 않은 경우 
if board[x][y] == '_':
    bfs(x, y)

# 6. 색칠결과 출력 
for i in range(10):
    print(''.join(board[i]))






