from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def permute(picked, visited):
            if len(picked) == n:
                res.append(picked[:])
                return 
            for i in range(n):
                if visited[i]: continue
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue

                picked.append(nums[i])
                visited[i] = True

                permute(picked, visited)

                picked.pop()
                visited[i] = False

        permute([], [False] * n)

        return res

if __name__ == "__main__":
    s = Solution()

    print(s.permuteUnique([1, 1, 2]))  # [[1,1,2],[1,2,1],[2,1,1]]
    print(s.permuteUnique([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(s.permuteUnique([1]))        # [[1]]
