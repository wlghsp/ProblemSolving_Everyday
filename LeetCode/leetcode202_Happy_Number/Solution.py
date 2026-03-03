class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        nums.add(n)
        while n != 1:
            n = self.nextNum(n)
            if n in nums:
                return False
            nums.add(n)
        return True
    
    def nextNum(self, n):
        result = 0
        while n != 0:
            ones = n % 10
            result += ones * ones
            n //= 10
        return result

if __name__ == "__main__":
    sol = Solution()

    print(sol.isHappy(19))   # Expected: True
    # 1^2 + 9^2 = 82
    # 8^2 + 2^2 = 68
    # 6^2 + 8^2 = 100
    # 1^2 + 0^2 + 0^2 = 1 → True

    print(sol.isHappy(2))    # Expected: False (무한 루프)
    print(sol.isHappy(1))    # Expected: True
