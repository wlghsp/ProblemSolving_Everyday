import math
import sys

input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

student = [[0] * 7 for _ in range(2)]

for _ in range(N):
    s, y = map(int, input().split())
    student[s][y] += 1

room = 0
for i in student:
    for j in i:
        room += math.ceil(j / K) # math.ceil함수는 올림 함수

print(room)