


import sys

input = lambda : sys.stdin.readline().rstrip()


N, M = map(int, input().split())

set1 = set()
set2 = set()

for i in range(N):
    set1.add(input())
for i in range(M):
    set2.add(input())

set3 = sorted(set1 & set2)

print(len(set3))
for i in set3:
    print(i)