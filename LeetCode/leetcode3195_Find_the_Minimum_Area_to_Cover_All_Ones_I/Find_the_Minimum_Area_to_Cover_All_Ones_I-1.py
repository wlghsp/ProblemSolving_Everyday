from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # maxX, maxY, minX, minY
        maxX, maxY, minX, minY = 0, 0, float('inf'), float('inf')
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    maxX, maxY, minX, minY = max(x, maxX), max(y, maxY), min(x, minX), min(y, minY)

        return (maxX - minX + 1) * (maxY - minY + 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumArea([[0,1,0],[1,0,1]])) # 6
    print(sol.minimumArea([[1,0],[0,0]])) # 1