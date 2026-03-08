from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for a in arr:
            freq[a] = freq.get(a, 0) + 1
        sorted_freq = sorted(freq.items(), key=lambda v : v[1])
        for key,cnt in sorted_freq:
            if cnt <= k:
                k -= cnt
                del freq[key]
        return len(freq)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findLeastNumOfUniqueInts([5,5,4], 1))           # 1
    print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))   # 2
    print(sol.findLeastNumOfUniqueInts([2,4,1,8,3,5,1,3], 3)) # 3
