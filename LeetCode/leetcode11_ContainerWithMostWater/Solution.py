from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
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
    s = Solution()

    # Example 1: [1,8,6,2,5,4,8,3,7] -> 49
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Expected: 49

    # Example 2: [1,1] -> 1
    print(s.maxArea([1, 1]))  # Expected: 1
