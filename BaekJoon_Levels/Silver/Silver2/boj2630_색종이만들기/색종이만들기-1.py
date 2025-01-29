N = int(input())
board = [list(input().split()) for _ in range(N)]
white = 0
blue = 0

def is_all_same(x, y, size):
    color = board[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != board[i][j]:
                return False
    return True

def partition(x, y, size):
    global white
    global blue
    if is_all_same(x, y, size):
        if board[x][y] == '0': # 하얀색
            white += 1
        elif board[x][y] == '1': # 파란색
            blue += 1
        return

    new_size = size // 2
    partition(x, y, new_size)
    partition(x + new_size, y, new_size)
    partition(x, y + new_size, new_size)
    partition(x + new_size, y + new_size, new_size)


partition(0, 0, N)

print(white)
print(blue)