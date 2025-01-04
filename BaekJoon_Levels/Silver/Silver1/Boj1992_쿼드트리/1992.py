import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
img = [list(input()) for _ in range(N)]
result = ""

def partition(img, row, col, size):
    global result
    if is_all_same(img, row, col, size):
        result += img[row][col]
        return

    result += "("

    new_size = size // 2
    partition(img, row, col, new_size)
    partition(img, row, col + new_size, new_size)
    partition(img, row + new_size, col, new_size)
    partition(img, row + new_size, col + new_size, new_size)

    result += ")"

def is_all_same(img, row, col, size):
    color = img[row][col]
    for i in range(row, row+size):
        for j in range(col, col+size):
            if color != img[i][j]:
                return False

    return True

partition(img, 0, 0, N)

print(result)
