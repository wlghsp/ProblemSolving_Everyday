from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for n, freq in counter.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]


if __name__ == "__main__":
    sol = Solution()

    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(sol.topKFrequent([1], 1))                  # [1]
    print(sol.topKFrequent([4, 1, 1, 1, 2, 2, 3], 2))  # [1, 2]
