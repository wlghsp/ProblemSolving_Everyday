import sys

input = lambda: sys.stdin.readline().rstrip()

r, c, zr, zc = map(int, input().split())


for i in range(r):
    article = input()
    res = ''
    for c in article:
        res += c * zc
    for _ in range(zr):
        print(res)
