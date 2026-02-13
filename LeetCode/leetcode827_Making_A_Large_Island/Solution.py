class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        record = {}
        label = 2

        def dfs(x, y, label):
            size = 1
            grid[x][y] = label
            
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m): continue
                if grid[nx][ny] != 1: continue

                size += dfs(nx, ny, label)
            
            return size
                

        # 1. 사전작업: 모든 섬 DFS 탐색
        # 각 섬에 고유 라벨 붙이고, {라벨: 크기} 딕셔너리에 저장
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    size = dfs(i, j, label)
                    record[label] = size
                    label += 1

        # 2. 0 탐색
        # 각 0 칸의 상하좌우를 보고, 인접한 서로 다른 라벨의 크기 합산 + 1(자기자신)
        max_size = -1
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    size = 0
                    label_set = set()
                    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if not (0 <= ni < n and 0 <= nj < m): continue
                        if grid[ni][nj] == 0: continue
                        label = grid[ni][nj]
                        if label in label_set: continue

                        size += record[label]
                        label_set.add(label)
                    max_size = max(max_size, size + 1)
        if max_size == -1:
            return m * n
        return max_size
        


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.largestIsland([[1, 0], [0, 1]])
    print(f"Test 1: {result1}")  # Expected: 3

    # Test case 2
    result2 = solution.largestIsland([[1, 1], [1, 0]])
    print(f"Test 2: {result2}")  # Expected: 4

    # Test case 3
    result3 = solution.largestIsland([[1, 1], [1, 1]])
    print(f"Test 3: {result3}")  # Expected: 4

    # Test case 4
    result4 = solution.largestIsland([[0, 0], [0, 0]])
    print(f"Test 4: {result4}")  # Expected: 1

    # Test case 5
    result5 = solution.largestIsland([
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ])
    print(f"Test 5: {result5}")  # Expected: 3
