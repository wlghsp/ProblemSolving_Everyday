from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 1. 전치
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 2. reverse
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    sol = Solution()
    sol.rotate([[1,2,3],[4,5,6],[7,8,9]])