def z(n, x, y):
    if n == 0:
        return 0

    size = 2 ** (n - 1)

    if x < size and y < size:
        return z(n - 1, x, y)
    elif x < size and y >= size:
        return size * size + z(n - 1, x, y - size)
    elif x >= size and y < size:
        return 2 * size * size + z(n - 1, x - size, y)
    else:
        return 3 * size * size + z(n - 1, x - size, y - size)

N, r, c = map(int, input().split())
print(z(N, r, c))