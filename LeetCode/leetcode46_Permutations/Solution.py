from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def dfs(picked, visited):
            if len(picked) == n:
                res.append(picked[:])
                return
            for i in range(n):
                if visited[i]: continue
                picked.append(nums[i])
                visited[i] = True

                dfs(picked, visited)

                picked.pop()
                visited[i] = False
        dfs([], [False] * n)

        return res


if __name__ == "__main__":
    sol = Solution()

    print(sol.permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(sol.permute([0, 1]))     # [[0,1],[1,0]]
    print(sol.permute([1]))        # [[1]]
