import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
a = [i for i in map(int, input().split())]

answer = 0
total = 0
for i in range(K):
    total += a[i] # 미리 K개를 더해 놓는다.
answer = total
# 슬라이딩 윈도우 K 크기만큼의 윈도우를 계속 이동시킨다.
for i in range(K, len(a)):
    total += a[i] - a[i - K] # 인덱스를 하나 이동하고 K크기에서 벗어난 원소는 빼준다
    answer = max(answer, total) # 바뀐 매출액이 최댓값인지 계속 확인한다.

print(answer)

