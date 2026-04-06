import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1_1 = [1, 7, 11]
    nums2_1 = [2, 4, 6]
    k1 = 3
    result1 = sol.kSmallestPairs(nums1_1, nums2_1, k1)
    print(f"Test 1: {result1}")  # Expected: [[1,2],[1,4],[1,6]]

    # Test case 2
    nums1_2 = [1, 1, 2]
    nums2_2 = [1, 2, 3]
    k2 = 2
    result2 = sol.kSmallestPairs(nums1_2, nums2_2, k2)
    print(f"Test 2: {result2}")  # Expected: [[1,1],[1,1]]
