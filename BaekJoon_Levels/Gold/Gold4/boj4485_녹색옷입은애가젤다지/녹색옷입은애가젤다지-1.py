import heapq
import sys

input = lambda : sys.stdin.readline().rstrip()

INF = int(1e9)
def dijkstra():
    distance = [[INF] * N for _ in range(N)]
    q = []
    heapq.heappush(q, (0, 0, rupees[0][0]))
    distance[0][0] = rupees[0][0]

    while q:
        x, y, dist = heapq.heappop(q)

        if dist > distance[x][y]: continue

        for dx, dy in [(1, 0),(0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N): continue

            cost = dist + rupees[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (nx, ny, distance[nx][ny]))
    return distance[N - 1][N - 1]
idx = 1
while True:
    N = int(input())
    if N == 0:
        break
    rupees = [list(map(int, input().split())) for _ in range(N)]
    res = dijkstra()
    print(f'Problem {idx}: {res}')
    idx += 1