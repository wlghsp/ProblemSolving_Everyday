import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

## dfs 풀이

V = int(input())
tree = [[] for _ in range(V + 1)]
# 2차원 리스트에 트리 저장 (연결 그래프)
for _ in range(V):
    line = list(map(int, input().split()))
    cnt_node = line[0]
    idx = 1
    while line[idx] != -1:
        adj_node, adj_cost = line[idx], line[idx + 1]
        tree[cnt_node].append((adj_node, adj_cost))
        idx += 2

visited = [-1] * (V + 1)
visited[1] = 0

# 리턴값 없음. visited에 모든 노드까지의 거리 저장
def dfs(node, dist):
    for v, d in tree[node]:
        cal_dist = dist + d
        if visited[v] == -1:
            visited[v] = cal_dist
            dfs(v, cal_dist)
    return

dfs(1, 0)
tmp = [0, 0]
# 최대 거리에 있는 노드 찾기
for i in range(1, len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

visited = [-1] * (V + 1)
visited[tmp[0]] = 0
dfs(tmp[0], 0)

print(max(visited))