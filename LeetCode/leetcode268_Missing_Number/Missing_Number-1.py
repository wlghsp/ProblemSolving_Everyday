from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        0 이상 n 이하 : [0, n] 구간
        """
        # 총합을 구하고 총합에서 현재 nums 배열의 합을 빼면 없는 숫자가 나옴
        # 가우스 덧셈 공식 1부터 n까지의 합 = n * (n + 1) / 2
        n = len(nums)
        total_sum = n * (n + 1) // 2
        return total_sum - sum(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.missingNumber([3,0,1])) # 2
