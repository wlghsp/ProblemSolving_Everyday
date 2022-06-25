import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

def solution(a, b):
    answer = 0
    am = defaultdict(int)
    bm = defaultdict(int)
    for x in b:
        bm[x] += 1
    L = len(b) - 1
    for i in range(L):
        am[a[i]] += 1
    lt = 0
    for rt in range(L, len(a)):
        am[a[rt]] += 1
        if am == bm: answer += 1
        am[a[lt]] -= 1
        if am[a[lt]] == 0:
            del am[a[lt]]
        lt += 1
    return answer


s = input()
t = input()

print(solution(s, t))