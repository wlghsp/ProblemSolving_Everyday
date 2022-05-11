
N = int(input())

board = []

for i in range(N):
    board.append(list(map(int, input().split())))


# 최대합 구하기
# 1. 각 행의 합, 각 열의 합마다 최대값 비교
answer = float("-inf") # 음의 무한대, 양의 무한대 = float("inf)
sumOfRow, sumOfCol = 0, 0

for i in range(N):
    sumOfRow = sumOfCol = 0
    for j in range(N):
        sumOfRow += board[i][j] # 행의 합
        sumOfCol += board[j][i] # 열의 합
    answer = max(answer, sumOfRow)
    answer = max(answer, sumOfCol)


sumOfRow = sumOfCol = 0

# 2. 대각선의 합 구하고 비교하기
for i in range(N):
    sumOfRow += board[i][i]  # 왼쪽 위에서 오른쪽 아래 대각선
    sumOfCol += board[i][N - i - 1] # 오른쪽 위에서 왼쪽 아래 방향 대각선

answer = max(answer, sumOfRow)
answer = max(answer, sumOfCol)

print(answer)