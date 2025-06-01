from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        M = len(grid[0])
        N = len(grid)
        visited = [[False] * M for _ in range(N)]
        def bfs(x, y):
            q = deque([(x, y)])
            visited[x][y] = True

            while q:
                px, py = q.popleft()

                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = px + dx, py + dy
                    if not (0 <= nx < N and 0 <= ny < M): continue
                    if visited[nx][ny]: continue
                    if grid[nx][ny] == '0': continue


                    visited[nx][ny] = True
                    q.append((nx, ny))

        for i in range(N):
            for j in range(M):
                if not visited[i][j] and grid[i][j] == '1':
                    ans += 1
                    bfs(i, j)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))  # 1
    print(sol.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))  # 3
