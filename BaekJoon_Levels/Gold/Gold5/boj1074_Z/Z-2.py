
def z(x, y, n):
    if n == 0:
        return 0

    size = 2 ** (n - 1)

    if x < size and y < size:
        return z(x, y, n - 1)
    elif x < size and y >= size:
        return size * size + z(x, y - size, n - 1)
    elif x >= size and y < size:
        return 2 * size * size + z(x - size, y, n - 1)
    else:
        return 3 * size * size + z(x - size, y - size, n - 1)


N, r, c = map(int, input().split())
print(z(r, c, N))