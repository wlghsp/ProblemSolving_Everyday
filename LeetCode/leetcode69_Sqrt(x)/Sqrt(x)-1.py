import math


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l <= r:
            mid = l + (r - l) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num > x:
                r = mid - 1
            else:
                l = mid + 1

        return math.floor(r)



if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(4)) # 2
    print(sol.mySqrt(8)) # 2