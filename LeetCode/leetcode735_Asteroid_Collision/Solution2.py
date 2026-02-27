from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Example 1: asteroids = [5, 10, -5]
    # Expected: [5, 10]
    print(sol.asteroidCollision([5, 10, -5]))

    # Example 2: asteroids = [8, -8]
    # Expected: []
    print(sol.asteroidCollision([8, -8]))

    # Example 3: asteroids = [10, 2, -5]
    # Expected: [10]
    print(sol.asteroidCollision([10, 2, -5]))

    # Example 4: asteroids = [-2, -1, 1, 2]
    # Expected: [-2, -1, 1, 2]
    print(sol.asteroidCollision([-2, -1, 1, 2]))
