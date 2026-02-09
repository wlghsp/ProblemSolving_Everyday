from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        pass


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = solution.findDiagonalOrder(mat1)
    print(f"Test 1: {result1}")  # Expected: [1,2,4,7,5,3,6,8,9]

    # Test case 2
    mat2 = [[1, 2], [3, 4]]
    result2 = solution.findDiagonalOrder(mat2)
    print(f"Test 2: {result2}")  # Expected: [1,2,3,4]

    # Test case 3
    mat3 = [[1]]
    result3 = solution.findDiagonalOrder(mat3)
    print(f"Test 3: {result3}")  # Expected: [1]
