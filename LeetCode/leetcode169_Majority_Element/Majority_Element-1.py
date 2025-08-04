from typing import List, Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        huddle = len(nums) / 2
        counter = Counter(nums)
        return next(k for k, v in counter.items() if v >= huddle)


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3])) # 3
    print(sol.majorityElement([2,2,1,1,1,2,2])) # 2
