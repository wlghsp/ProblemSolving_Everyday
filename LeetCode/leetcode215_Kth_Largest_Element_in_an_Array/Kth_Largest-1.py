import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = heapq.nlargest(k, nums)
        return res[-1]




if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5

