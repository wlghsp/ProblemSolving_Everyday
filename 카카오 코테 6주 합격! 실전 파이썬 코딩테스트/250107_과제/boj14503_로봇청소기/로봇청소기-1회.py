import sys

# N,M 방의 크기
N, M = map(int, input().split())
# r, c 로봇 청소기가 있는 좌표, d 로봇 청소기가 바라보는 방향
# d 0: 북, 1: 동, 2: 남, 3: 서
r, c, d = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
# 0 청소되지 않는 공간 1은 벽이 있는 것, 로봇청소기가 있는 공간은 빈 공간
# 청소하는 영역의 갯수 구하기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1
matrix[r][c] = -1

def is_valid_move(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def clean(x, y, direction):
    global cnt
    matrix[x][y] = -1

    # 4방향 빈칸 찾기
    for i in range(4):
        direction = (direction + 3) % 4 # 반시계 방향 90도 회전
        nx, ny = x + dx[direction], y + dy[direction]
        if is_valid_move(nx, ny) and matrix[nx][ny] == 0:
            cnt += 1
            clean(nx, ny, direction)
            return

    # 빈칸을 못 찾은 상태에서 한칸 후진 하기
    back = (direction + 2) % 4 # 후진할 뿐 방향은 바꾸지 않음
    nx, ny = x + dx[back], y + dy[back]
    if is_valid_move(nx, ny) and matrix[nx][ny] != 1:
        clean(nx, ny, direction)

clean(r, c, d)

print(cnt)