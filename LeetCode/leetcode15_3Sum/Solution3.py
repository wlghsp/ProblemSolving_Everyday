from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(f"Test 1: {result1}")  # Expected: [[-1, -1, 2], [-1, 0, 1]]

    # Test case 2
    result2 = solution.threeSum([0, 1, 1])
    print(f"Test 2: {result2}")  # Expected: []

    # Test case 3
    result3 = solution.threeSum([0, 0, 0])
    print(f"Test 3: {result3}")  # Expected: [[0, 0, 0]]

    # Test case 4
    result4 = solution.threeSum([-2, 0, 1, 1, 2])
    print(f"Test 4: {result4}")  # Expected: [[-2, 0, 2], [-2, 1, 1]]
