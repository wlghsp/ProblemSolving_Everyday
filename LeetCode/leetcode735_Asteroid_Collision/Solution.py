class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        pass


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.asteroidCollision([5, 10, -5])
    print(f"Test 1: {result1}")  # Expected: [5, 10]

    # Test case 2
    result2 = solution.asteroidCollision([8, -8])
    print(f"Test 2: {result2}")  # Expected: []

    # Test case 3
    result3 = solution.asteroidCollision([10, 2, -5])
    print(f"Test 3: {result3}")  # Expected: [10]

    # Test case 4
    result4 = solution.asteroidCollision([-2, -1, 1, 2])
    print(f"Test 4: {result4}")  # Expected: [-2, -1, 1, 2]

    # Test case 5
    result5 = solution.asteroidCollision([1, -2, -2, -2])
    print(f"Test 5: {result5}")  # Expected: [-2, -2, -2]
