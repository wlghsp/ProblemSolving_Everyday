from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def dfs(picked, start, length):
            if len(picked) == length:
                res.append(picked[:])
                return
            for i in range(start, n):
                # 중복 숫자 가지치기 , 첫 번째 숫자는 오케이 그다음을 확인
                if i < start and nums[i] == nums[i - 1]: continue
                picked.append(nums[i])
                dfs(picked, i + 1, length)
                picked.pop()

        for l in range(n + 1):
            dfs([], 0, l)
        return res


if __name__ == "__main__":
    s = Solution()

    print(s.subsetsWithDup([1, 2, 2]))  # [[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(s.subsetsWithDup([0]))        # [[],[0]]
    print(s.subsetsWithDup([4,4,4,1,4]))        # [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
