import sys

input = lambda: sys.stdin.readline().rstrip()

r, c, zr, zc = map(int, input().split())

new = []
res = ''

for i in range(r):
    article = input()
    for k in range(zr):
        for j in range(c):
            res += article[j] * zc
        new.append(res)
        res = ''
for i in new:
    print(i)
