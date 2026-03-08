from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    print(sol.findLeastNumOfUniqueInts([5,5,4], 1))           # 1
    print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))   # 2
    print(sol.findLeastNumOfUniqueInts([2,4,1,8,3,5,1,3], 3)) # 3
