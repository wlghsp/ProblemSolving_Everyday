from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set: # 수열의 시작점이라면
                length = 1
                current  = num
                while current + 1 in num_set:
                    current += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2])) # 4