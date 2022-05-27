
''''
1. 뱀은 처음에 맨 위, 맨 좌측에 위치하고 길이는 1이다. 뱀의 처음 이동방향은 오른쪽이다. 
2. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다. 
3. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다. 
4. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
'''''


import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def direction_change(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < N


N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

direction = 1
time = 1
y, x = 0, 0
snake = deque([[y, x]])
board[y][x] = 2

while True:
    y, x = y + dy[direction], x + dx[direction]
    if is_valid_coord(y, x) and board[y][x] != 2:
        if not board[y][x] == 1:
            delY, delX = snake.popleft()
            board[delY][delX] = 0
        board[y][x] = 2
        snake.append([y, x])
        if time in times.keys():
            direction = direction_change(direction, times[time])
        time += 1
    else:
        break

print(time)