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

    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))   # 5
    print(sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
