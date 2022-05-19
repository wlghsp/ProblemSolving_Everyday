"""
최근 캔디팡이라는 스마트폰 게임이 인기를 끌고 있다. 
캔디팡은 7 * 7 모양의 격자 판에 같은 색깔이 연속 3개 이상인 부분을 찾아 터치하면 터지면서 점수를 얻는 게임이다. 
이때 연속된 부분은 상, 하, 좌, 우만 판단한다.
위 캔디팡 화면에서 터치하면 터지는 영역은 총 4군데 존재한다.
캔디팡 격자 정보가 주어졌을 때 터치하면 터지는 영역의 개수를 출력하는 프로그램을 작성하시오.(위 예시 참고)

입력
캔디팡 격자판(7 * 7)의 색깔 정보(1~5)가 입력된다.
※ 색깔정보
빨강 = 1 , 노랑 = 2 , 파랑 = 3 , 초록 = 4 , 보라 = 5

출력
터치하면 터지는 영역의 개수를 출력한다.

입력 예시   
2 1 5 1 1 3 4
2 1 5 1 3 5 3
2 3 4 5 2 2 4
4 4 3 2 3 1 3
4 3 5 3 1 4 3
5 4 4 3 3 5 5
2 1 3 5 1 1 2

출력 예시
4

도움말
위 예시에서 색깔이 연속 3개 이상인 부분은 4영역이 존재한다.

"""
import sys

input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def bfs(x, y, board, check):
    queue = deque()
    queue.append([x, y])
    check[x][y] = 1

    color = board[x][y]

    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx and nx < 7 and 0 <= ny and ny < 7:
                # 같은 색상이면서 아직 탐색이 되지 않으면 탐색
                if board[nx][ny] == color and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    queue.append([nx, ny])
                    count += 1

    if count >= 3:
        return 1
    else:
        return 0


# 1. board입력
board = [list(map(int, input().split())) for _ in range(7)]


# 2. 탐색 체크
check = [[0 for _ in range(7)] for _ in range(7)]

# 3. 탐색 방향
global dx, dy  # global 키워드 사용하여 위의 함수 내부에서도 사용
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
