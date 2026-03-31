class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        l, r = 0, len(height) - 1
        while l < r:
            min_h = min(height[l], height[r])
            diff = r - l
            max_area = max(max_area, min_h * diff)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Test 1: {sol.maxArea(height)}")  # Expected: 49 (between index 1 and 8)

    # Test case 2
    height = [1, 1]
    print(f"Test 2: {sol.maxArea(height)}")  # Expected: 1

    # Test case 3
    height = [2, 3, 4, 5, 18, 17, 6]
    print(f"Test 3: {sol.maxArea(height)}")  # Expected: 17 (between index 4 and 5)

    # Test case 4
    height = [1, 2, 1]
    print(f"Test 4: {sol.maxArea(height)}")  # Expected: 2
