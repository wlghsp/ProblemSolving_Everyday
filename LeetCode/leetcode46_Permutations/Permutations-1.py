from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answers = []

        def dfs(picked, length):
            if length == n:
                answers.append(picked[:])
                return
            for i in range(n):
                if nums[i] in picked:
                    continue
                picked.append(nums[i])
                dfs(picked, length + 1)
                picked.pop()

        dfs([], 0)
        return answers

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(sol.permute([0, 1])) # [[0,1],[1,0]]