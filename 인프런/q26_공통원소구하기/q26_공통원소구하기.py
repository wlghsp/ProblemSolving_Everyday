
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
a = [i for i in map(int, input().split())]
M = int(input())
b = [i for i in map(int, input().split())]

# 둘다 꼭 정렬을 해줘야 아래서 탐색할 때 잘 정렬될 수 있다.
a.sort()
b.sort()

p1, p2 = 0, 0
answer = []
while p1 < N and p2 < M:
    if a[p1] < b[p2]:
        p1 += 1
    elif a[p1] > b[p2]:
        p2 += 1
    elif a[p1] == b[p2]:
        answer.append(a[p1])
        p1 += 1
        p2 += 1

print(*answer)