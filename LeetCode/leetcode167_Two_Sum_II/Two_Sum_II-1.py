from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else:
                left += 1

        return [0, 0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9)) # [1,2]