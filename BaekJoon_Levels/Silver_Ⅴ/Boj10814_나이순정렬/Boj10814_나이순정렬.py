

import sys

input = lambda : sys.stdin.readline().rstrip()



N = int(input())
list = []
for i in range(N):
    age, name = input().split()
    list.append((age, name))

list.sort(key=lambda x: int(x[0]))

for k, v in list:
    print(k, v)