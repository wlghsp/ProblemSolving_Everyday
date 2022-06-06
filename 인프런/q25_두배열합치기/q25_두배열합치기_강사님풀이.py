


import sys
input = lambda : sys.stdin.readline().rstrip()
N = int(input())
a = [i for i in map(int, input().split())]
M = int(input())
b = [i for i in map(int, input().split())]

# 투포인터 알고리즘
p1, p2 = 0, 0 # 둘다 0에서 시작
answer = []
while p1 < N and p2 < M:
    if a[p1] < b[p2]: # a의 원소가 b의 원소보다 작다면
        answer.append(a[p1]) # 더 작은 a의 원소를 배열에 넣어준다
        p1 += 1 # a의 포인터 증가
    else: # b의 원소가 a의 원소보다 작다면
        answer.append(b[p2]) # 더 작은 b의 원소를 배열에 넣어준다
        p2 += 1 # b의 포인터 증가
while p1 < N:
    answer.append(a[p1])
    p1 += 1
while p2 < M:
    answer.append(b[p2])
    p2 += 1

print(*answer)