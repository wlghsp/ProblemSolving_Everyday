
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            bit_sum = 0

            for num in nums:
                bit_sum += (num >> i) & 1
            result |= (bit_sum % 3) << i

        if result >= 2 ** 31:
            result -= 2 ** 32

        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,3,2])) # 3
    print(sol.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2])) # -4