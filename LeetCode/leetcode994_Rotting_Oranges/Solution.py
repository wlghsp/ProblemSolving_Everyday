from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh_oranges = 0
        mins = 0
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1 

        if fresh_oranges == 0:
            return 0

        while q:
            # Python: range(len(q))는 호출 시점에 고정됨 → 루프 중 q에 append해도 반복 횟수 안 변함
            # Java: for(i < queue.size())는 매 반복마다 size() 재평가 → int size = queue.size()로 미리 저장 필요
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m): continue
                    if grid[nx][ny] != 1: continue

                    grid[nx][ny] = 2
                    fresh_oranges -= 1
                    q.append((nx, ny))
        
            mins += 1
        
            
        # 익지 않은 오렌지 있으면 -1
        return mins - 1 if fresh_oranges == 0 else -1
        


if __name__ == "__main__":
    sol = Solution()

    # Test 1: Basic case
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(sol.orangesRotting(grid1))  # Expected: 4

    # Test 2: Already no fresh oranges
    grid2 = [[0, 2]]
    print(sol.orangesRotting(grid2))  # Expected: 0

    # Test 3: Impossible case
    grid3 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(sol.orangesRotting(grid3))  # Expected: -1

    # Test 4: Empty grid
    grid4 = [[0]]
    print(sol.orangesRotting(grid4))  # Expected: 0

    # Test 5: All rotten
    grid5 = [[2, 2], [2, 2]]
    print(sol.orangesRotting(grid5))  # Expected: 0
