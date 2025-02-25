import sys
from collections import defaultdict

input = lambda : sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    n = int(input())
    clothes_sort_count = defaultdict(int)
    for _ in range(n):
        a, b = input().split()
        clothes_sort_count[b] += 1
    ans = 1

    for v in clothes_sort_count.values():
        ans *= (v + 1)
    print(ans - 1)