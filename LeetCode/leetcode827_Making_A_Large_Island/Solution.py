class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        pass


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
    print(f"Test 5: {result5}")  # Expected: 5
