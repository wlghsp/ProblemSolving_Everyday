
N = int(input())
img = [list(input()) for _ in range(N)]

result = ""

def is_all_same(row, col, size):
    color = img[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if img[i][j] != color:
                return False

    return True

def partition(row, col, size):
    global result
    if is_all_same(row, col, size):
        result += img[row][col]
        return

    result += "("

    new_size = size // 2
    partition(row, col, new_size)
    partition(row, col + new_size, new_size)
    partition(row + new_size, col, new_size)
    partition(row + new_size, col + new_size, new_size)

    result += ")"


partition( 0, 0, N)

print(result)