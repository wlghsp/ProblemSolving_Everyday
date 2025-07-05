from collections import defaultdict
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        freq = sorted(freq.items(), key=lambda x: (-x[0]))

        for k, v in freq:
            if k == v:
                return k
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findLucky([2,2,3,4])) # 2
