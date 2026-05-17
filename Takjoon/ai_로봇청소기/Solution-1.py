from collections import deque
import sys, os
sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

def input(): return sys.stdin.readline().rstrip()

# N: 격자 크기, K: 로봇 청소기의 개수, L: 테스트 횟수
N, K, L = map(int, input().split()) 

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
cleaners = []
for _ in range(K):
    x, y = map(int, input().split())
    cleaners.append((x - 1, y - 1))

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
areas = [
    [(0, 0), (-1, 0), (1, 0), (0, 1)], # 오른쪽
    [(0, 0), (0, -1), (1, 0), (0, 1)], # 아래쪽
    [(0, 0), (0, -1), (1, 0), (-1, 0)], # 왼쪽
    [(0, 0), (-1, 0), (0, -1), (0, 1)]  # 위쪽
]


def out_of_grid(nr, nc):
    return not (0 <= nr < N and 0 <= nc < N)

# 이동로직은 코테풀님 코드 참고
def bfs_closest(sr, sc):
    q = deque()
    visited = set()

    q.append((0, sr, sc))
    visited.add((sr, sc))

    for x, y in cleaners:
        visited.add((x, y))
        
    dusts = []

    while q:
        q_next = deque()
         # 1. 시작 위치 먼지 확인  
        while q:
            depth, r, c = q.popleft()
            
            if grid[r][c] > 0: # 시작위치가 먼지
                dusts.append((r, c))
            # 시작위치가 먼지가 아닌 경우
            q_next.append((depth, r, c))

        if dusts: # 먼지를 이미 찾아다면 break
            break        
        
        # 2. 시작위치에서 먼지를 못 찾아서 다음 위치로 이동
        while q_next:
            depth, r, c = q_next.popleft()
            for dr, dc in dir:
                nr, nc = r + dr, c + dc
                if out_of_grid(nr, nc): continue
                if (nr, nc) in visited: continue
                if grid[nr][nc] == -1: continue # 물건 있으면 못 감
                
                q.append((depth + 1, nr, nc)) # 다음 큐 반복에서 먼지 여부 확인함
                visited.add((nr, nc))

    if not dusts:
        return (sr, sc)
    
    dusts.sort()
    return dusts[0]

def move_cleaners():
    for i, (r, c) in enumerate(cleaners):
        nr, nc = bfs_closest(r, c)
        cleaners[i] = (nr, nc)

def clean():
    for r, c in cleaners:
        candidates = []
        for i in range(4):
            dust = 0
            for dr, dc in areas[i]:
                nr, nc = r + dr, c + dc
                if out_of_grid(nr, nc): continue
                if grid[nr][nc] <= 0: continue

                dust += min(20, grid[nr][nc])

            candidates.append((dust * -1, i))

        candidates.sort()
        _, max_d = candidates[0]
        for dr, dc in areas[max_d]:
            nr, nc = r + dr, c + dc
            if out_of_grid(nr, nc): continue
            if grid[nr][nc] > 0:
                grid[nr][nc] -= 20
                if grid[nr][nc] < 0:
                    grid[nr][nc] = 0

def accumulate():
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:
                grid[r][c] += 5

def spread_dust():
    new_grid = [row[:] for row in grid]

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                dust = 0
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if out_of_grid(nr, nc): continue
                    if grid[nr][nc] <= 0: continue
                    
                    dust += grid[nr][nc]
                new_grid[r][c] = dust // 10
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                grid[r][c] = new_grid[r][c]

for _ in range(L):
    move_cleaners()
    clean()
    accumulate()
    spread_dust()
    print(sum(grid[r][c] for r in range(N) for c in range(N) if grid[r][c] > 0))