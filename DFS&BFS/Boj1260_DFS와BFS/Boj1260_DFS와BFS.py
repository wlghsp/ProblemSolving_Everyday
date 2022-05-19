
'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''''


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

