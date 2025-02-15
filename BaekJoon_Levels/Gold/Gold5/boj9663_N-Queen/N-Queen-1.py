N = int(input())
queen_positions = [0] * N # 각 행(row)의 퀸이 놓인 열(column) 위치 기록
cnt = 0 # 가능한 경우의 수

def is_position_safe(current_row):
    for previous_row in range(current_row):
        # 같은 행에 퀸이 존재하는지 확인
        if queen_positions[previous_row] == queen_positions[current_row]:
            return False

        # 대각선에 퀸이 있는지 확인 (행 차이 == 열 차이)
        if abs(previous_row - current_row) == abs(queen_positions[previous_row] - queen_positions[current_row]):
            return False

    return True

def position_queens(row):
    global cnt
    # 모든 행(row)에 퀸을 다 배치했다면 경우의 수 + 1
    if row == N:
        cnt += 1
        return

    # 현재 행(row)에 대해 각 열(column)에 퀸을 놓는 모든 경우 시도
    for col in range(N):
        queen_positions[row] = col # 현재 행(row)에 col(열)에 퀸 배치

        # 현재 위치에 퀸을 놓는게 안전하면 다음 행으로 이동
        if is_position_safe(row):
            position_queens(row + 1)

position_queens(0)
print(cnt)