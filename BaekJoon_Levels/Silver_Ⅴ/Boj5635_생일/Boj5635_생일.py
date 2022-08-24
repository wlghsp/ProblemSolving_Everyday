

import sys
input = lambda : sys.stdin.readline().rstrip()


n = int(input())

list = []
for _ in range(n):
    student = input().split()
    list.append(student)

list.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(list[n-1][0])
print(list[0][0])
