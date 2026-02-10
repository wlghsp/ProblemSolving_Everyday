from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = dict()
        for i in range(len(nums)):
            if nums[i] in map:
                idx = map[nums[i]]
                if i - idx <= k:
                    return True
            map[nums[i]] = i

        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    result1 = solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(f"Test 1: {result1}")  # Expected: True

    # Test case 2
    result2 = solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(f"Test 2: {result2}")  # Expected: True

    # Test case 3
    result3 = solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(f"Test 3: {result3}")  # Expected: False

    # Test case 4
    result4 = solution.containsNearbyDuplicate([1], 1)
    print(f"Test 4: {result4}")  # Expected: False
