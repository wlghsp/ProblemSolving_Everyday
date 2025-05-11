from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        i = 0
        while i < len(digits):
            number = number * 10 + digits[i]
            i += 1

        number += 1

        return list(map(int, str(number)))


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1,2,3])) # [1,2,4]


