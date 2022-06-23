import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()
a = input()
b = input()
def make_dict(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d

def solve(a, b):
    dict_a = make_dict(a)
    dict_b = make_dict(b)

    for k in dict_a.keys():
        if dict_b[k] != dict_a[k]:
            return "NO"
    return "YES"

print(solve(a, b))
