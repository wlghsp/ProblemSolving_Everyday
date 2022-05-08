
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()


def dfs(v):
    chk[v] = True
    print(v, end=' ') # 방문한 노드 출력

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N+1):
        if matrix[v][i] == 1 and not chk[i]:
            dfs(i)

def bfs(v):
    dq = deque()
    dq.append(v)
    chk[v] = True

    while len(dq) > 0:
        v = dq.popleft()
        print(v, end=' ')
        for i in range(1, N+1):
            if matrix[v][i] == 1 and not chk[i]:
                chk[i] = True
                dq.append(i)



N, M, V = map(int, input().split())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]


# 방문한 곳 체크를 위한 배열 선언
chk = [False] * (N + 1)

# 입력 받는 두 값에 대해 영행렬에 1 삽입
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

dfs(V)
chk = [False] * (N + 1)
print()
bfs(V)

