import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
a = input()
b = input()


def solve(a, b):
    dict_a = defaultdict(int)

    for c in a:
        dict_a[c] += 1

    for t in b:
        # get은 에러를 일으키지 않음
        if not dict_a.get(t) or dict_a.get(t) == 0:
            return "NO"
        # 비교하고 나면 t의 갯수를 하나 줄여줘야 한다.
        dict_a[t] -= 1

    return "YES"


print(solve(a, b))
