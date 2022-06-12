
import sys
input = lambda :sys.stdin.readline().rstrip()
from collections import Counter
N = int(input())

for _ in range(N):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    a_count = Counter(a)
    b_count = Counter(b)

    idx = 4
    while idx > 0:
        if a_count[idx] > b_count[idx]:
            print("A")
            break
        elif b_count[idx] > a_count[idx]:
            print("B")
            break
        else:
            idx -= 1
    if idx == 0:
        print("D")


