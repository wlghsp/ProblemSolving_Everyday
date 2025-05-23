T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (N + 1)

    def dfs(x):
        visited[x] = True
        next_node = arr[x - 1]
        if not visited[next_node]:
            dfs(next_node)

    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            cnt += 1
            dfs(i)

    print(cnt)