from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in nums:
            map[n] = map.get(n, 0) + 1

        sorted_map = sorted(map.items(), key=lambda x:(-x[1], x[0]))

        return [sorted_map[i][0] for i in range(k)]




