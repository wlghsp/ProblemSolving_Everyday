import sys

input = lambda: sys.stdin.readline()[:-1]

def partition(row, col, size):
    global white
    global blue
    if size == 1 or is_all_same_color(row, col, size):
        if paper[row][col] == 0:
            white += 1
        else:
            blue += 1
        return

    new_size = size // 2

    partition(row, col, new_size)
    partition(row + new_size, col, new_size)
    partition(row, col + new_size, new_size)
    partition(row + new_size, col + new_size, new_size)


def is_all_same_color(row, col, size):
    color = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if paper[i][j] != color:
                return False

    return True


white = 0
blue = 0
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

partition(0, 0, N)

print(white)
print(blue)
