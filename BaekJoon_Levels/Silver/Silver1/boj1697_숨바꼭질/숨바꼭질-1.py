from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = True

    while q:
        px, time = q.popleft()
        if px == K:
            # BFS는 먼저 도착한 경로가 항상 최소 시간 이므로 찾으면 바로 종료
            print(time)
            return

        for next_loc in [px -1, px + 1, 2 * px]:
            if next_loc < 0 or next_loc > 100000: continue
            if visited[next_loc]: continue

            visited[next_loc] = True
            q.append((next_loc, time + 1))

bfs(N)

