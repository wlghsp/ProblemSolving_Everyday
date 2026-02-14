from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
     

        level = 0
        while True:
            q = deque()
            # 1. 익은 오렌지인데 주변에 안 익은 오렌지가 있다면 담기
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 2:
                        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                            nx, ny = i + dx, j + dy
                            if not (0 <= nx < n and 0 <= ny < m): continue
                            if grid[nx][ny] == 1:
                                q.append((i, j))

            if not q: break

            while q:
                x, y = q.pop()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m): continue
                    if grid[nx][ny] != 1: continue

                    grid[nx][ny] = 2
            
            level += 1
        
            
        # 익지 않은 오렌지 있으면 -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return level
        



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
