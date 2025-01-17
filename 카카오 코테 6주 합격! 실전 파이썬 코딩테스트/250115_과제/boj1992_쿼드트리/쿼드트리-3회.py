
N = int(input())
img = [list(input()) for _ in range(N)]

result = ""

def is_all_same(x, y, size):
    color = img[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if color != img[i][j]:
                return False

    return True

def partition(x, y, size):
    global result
    if is_all_same(x, y, size):
        result += img[x][y]
        return

    result += "("

    new_size = size // 2
    partition(x, y, new_size)
    partition(x, y + new_size, new_size)
    partition(x + new_size, y, new_size)
    partition(x + new_size, y + new_size, new_size)

    result += ")"


partition(0, 0, N)


print(result)