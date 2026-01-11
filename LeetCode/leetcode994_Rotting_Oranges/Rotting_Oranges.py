class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        pass


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
