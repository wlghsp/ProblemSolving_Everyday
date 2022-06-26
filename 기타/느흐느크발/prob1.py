'''
6 2
5 2 4 1 3 6
A
B
'''

import sys

si = sys.stdin.readline
N, Q = map(int, si().split())
arr = list(map(int, si().split()))


def A(arr: list) -> list:
    return arr[N // 2:] + arr[:N // 2]


def B(arr: list) -> list:
    ret = []
    for x, y in zip(arr[:N // 2], arr[N // 2:]):
        ret.extend([x, y])
    return ret


for _ in range(Q):
    query = si().strip()
    if query == 'A':
        arr = A(arr)
    else:
        arr = B(arr)
print(*arr)
