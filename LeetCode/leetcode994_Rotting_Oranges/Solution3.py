from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh_count = 0
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        if fresh_count == 0:
            return 0
        
        mins = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m): continue
                    if grid[nx][ny] != 1: continue
                    
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    queue.append((nx, ny))
            mins += 1
        
        
        return mins - 1 if fresh_count == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Expected: 4
    print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Expected: -1
    print(sol.orangesRotting([[0,2]]))                    # Expected: 0
