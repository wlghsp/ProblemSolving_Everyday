from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        i = j = 0
        N = len(nums)
        while i < N and j < N:
            ranges = [str(nums[i])]
            j = i + 1
            while j < len(nums) and nums[j - 1] + 1 == nums[j]:
                ranges.append(str(nums[j]))
                j += 1
            i = j
            if ranges and len(ranges) >= 2:
                answer.append(ranges[0] + "->" + ranges[-1])
            elif ranges and len(ranges) == 1:
                answer.append(ranges[0])


        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
