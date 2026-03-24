from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def comb(nums, start):
            if len(nums) == k:
                result.append(nums[:])
                return
            for i in range(start, n - (k - len(nums)) + 2):
                nums.append(i)
                comb(nums, i + 1)
                nums.pop()

        comb([], 1)
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: n=4, k=2 → [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    print(sol.combine(4, 2))

    # Test 2: n=1, k=1 → [[1]]
    print(sol.combine(1, 1))
