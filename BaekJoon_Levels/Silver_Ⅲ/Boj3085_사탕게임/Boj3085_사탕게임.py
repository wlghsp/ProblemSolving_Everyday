
import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())

board = [list(input()) for _ in range(N)]

ans = 1

def search(): # 행과 열을 체크하는 메서드
    global ans
    # 행 체크
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

    # 열 체크
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1

for i in range(N):
    for j in range(N):
        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 행 바꾸기
            search()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j] # 원상 복구
        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j] # 열 바꾸기
            search()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 원상 복구

print(ans)