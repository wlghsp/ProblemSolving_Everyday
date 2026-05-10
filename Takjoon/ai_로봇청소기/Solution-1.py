

from collections import deque
import sys, os
sys.stdin = open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r')

def input(): return sys.stdin.readline().rstrip()

# N: 격자 크기, K: 로봇 청소기의 개수, L: 테스트 횟수
N, K, L = map(int, input().split()) 

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
# grid[r][c]: -1=물건, 0=깨끗, 양수=먼지량 

# direction = 0 오른쪽, 1 아래쪽, 2 왼쪽, 3 위쪽
cleaners = []
for _ in range(K):
    r, c = map(int, input().split())
    cleaners.append((r - 1, c - 1, 0))

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def out_of_grid(nr, nc):
    return not (0 <= nr < N and 0 <= nc < N)

def bfs_closest(sr, sc):
    q = deque()
    visited = set()

    # 1. 시작좌표 삽입
    q.append((sr, sc))
    visited.add((sr, sc))

    # 2. 큐 진행
    while q:
        r, c = q.popleft()
        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if out_of_grid(nr, nc): continue
            pass

def move_cleaners():
    """
     1. 청소기 이동 
     - 청소기로부터 가장 가까운 먼지 찾아서 이동 
     - 물건, 청소기 위치 이동 불가
     - 정렬 순서 : 거리, 행, 열
    """
    for i, (r , c, d) in enumerate(cleaners):
        pass


def clean():
    """
    2. 청소
     - 청소 가능: 4군데 본인 위치, 왼쪽, 위쪽, 오른쪽
     - 각 방향별로 청소 가능량 확인해서 정렬 하고 가장 큰 방향 청소
     - 격자별 최대 청소량 20
    """

def accumulate():
    for r in range(N):
        for c in range(N):
            if grid[r][c] > 0:
                grid[r][c] += 5

def spread_dust():
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                # 4방향 합산 // 10
                dust = 0
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc
                    if out_of_grid(nr, nc): continue
                    if grid[nr][nc] <= 0: continue

                    dust += grid[nr][nc]
                grid[r][c] += dust // 10



for _ in range(L):
    move_cleaners()
    clean()
    accumulate()
    print(sum(grid[r][c] for r in range(N) for c in range(N) if grid[r][c] > 0))