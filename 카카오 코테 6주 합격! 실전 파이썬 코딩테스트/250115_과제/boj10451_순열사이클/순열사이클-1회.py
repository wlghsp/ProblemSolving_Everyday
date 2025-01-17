T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (N + 1)
    def dfs(v):
        visited[v] = True
        next_node = arr[v - 1]
        if not visited[next_node]:
            dfs(next_node)

    cycle_cnt = 0

    for i in range(1, N + 1):
        if not visited[i]:
            cycle_cnt += 1
            dfs(i)

    print(cycle_cnt)