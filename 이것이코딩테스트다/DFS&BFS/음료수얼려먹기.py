

N, M = map(int, input().split())

# 2차원의 맵 정보 입력받기
graph = []
for i in range(N):
    graph.append(list(map(int, input())))


# DFS로 특정한 노드를 방문한 뒤에 연결되 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)

'''
4 5
00110
00011
11111
00000

'''