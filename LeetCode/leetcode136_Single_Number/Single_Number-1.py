from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # xor 연산
        # 2진수 연산이 이루어져서 1이 되어 남은 숫자만 남음
        for n in nums:
            result ^= n
        return result

    # 다른 풀이
    # return next(k for k, v in Counter(nums).items() if v == 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,1])) # 1
    print(sol.singleNumber([4,1,2,1,2])) # 4
