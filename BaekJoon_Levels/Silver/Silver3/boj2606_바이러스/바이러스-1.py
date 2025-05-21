
N = int(input())
graph = {i:[] for i in range(N + 1)}

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

def dfs(x):
    visited[x] = True
    count = 0 # 글로벌 변수를 사용하기 보다는 리턴값으로 넘기는 방식이 더 함수형이고 안정적
    for node in graph[x]:
        if visited[node]: continue

        count += 1
        count += dfs(node)

    return count

print(dfs(1))