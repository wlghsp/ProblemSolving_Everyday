import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]



if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = sol.topKFrequent(nums1, k1)
    print(f"Test 1: {result1}")  # Expected: [1, 2]

    # Test case 2
    nums2 = [4, 1, 1, 1, 2, 2, 3]
    k2 = 2
    result2 = sol.topKFrequent(nums2, k2)
    print(f"Test 2: {result2}")  # Expected: [1, 2]
