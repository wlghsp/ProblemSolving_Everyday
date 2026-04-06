import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heapq.heappop(heap) 

if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"Test 1: {sol.findKthLargest(nums1, k1)}")  # Expected: 5

    # Test case 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"Test 2: {sol.findKthLargest(nums2, k2)}")  # Expected: 4
