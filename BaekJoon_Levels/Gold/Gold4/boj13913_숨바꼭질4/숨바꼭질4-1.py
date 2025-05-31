from collections import deque

N, K = map(int, input().split())

prev = [0] * 100001

def bfs():
    visited = [False] * 100001
    q = deque([N])
    visited[N] = True

    while q:
        x = q.popleft()

        if x == K:
            print_answer()
            return

        for nx in [x - 1, x + 1, 2 * x]:
            if not (0 <= nx <= 100000): continue
            if visited[nx]: continue

            visited[nx] = True
            prev[nx] = x
            q.append(nx)

def print_answer():
    path = []
    curr = K
    while curr != N:
        path.append(curr)
        curr = prev[curr]
    path.append(N)
    path.reverse()
    print(len(path) - 1)
    print(*path, sep=' ')


bfs()
