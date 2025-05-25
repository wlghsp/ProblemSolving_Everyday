import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []
        answer = []
        for j in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
        while heap and len(answer) < k:
            total, i, j = heapq.heappop(heap)
            answer.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return answer

if __name__ == "__main__":
    sol = Solution()
    print(sol.kSmallestPairs([1,7,11], [2, 4, 6], 3)) # [[1,2],[1,4],[1,6]]
