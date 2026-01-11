from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0

        # 초기 상태: 썩은 오렌지와 신선한 오렌지 카운트
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # 신선한 오렌지가 없으면 0 반환
        if fresh_count == 0:
            return 0
        
        while queue:
            # 현재 분의 모든 썩은 오렌지 처리
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # 4방향 확인
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols): continue
                    if grid[nr][nc] != 1: continue

                    # 오렌지 썩힘
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))

            minutes += 1

        # 마지막 1분은 새로 썩을 오렌지가 없으므로 -1
        return minutes - 1 if fresh_count == 0 else -1


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    print(sol.orangesRotting(grid1))  # 4

    # Example 2
    grid2 = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    print(sol.orangesRotting(grid2))  # -1

    # Example 3
    grid3 = [[0, 2]]
    print(sol.orangesRotting(grid3))  # 0

    # Example 4: 모든 오렌지가 이미 썩음
    grid4 = [[2, 2], [2, 2]]
    print(sol.orangesRotting(grid4))  # 0

    # Example 5: 신선한 오렌지 없음
    grid5 = [[0, 0], [0, 0]]
    print(sol.orangesRotting(grid5))  # 0
