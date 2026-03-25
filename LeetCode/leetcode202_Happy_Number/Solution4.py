class Solution:
    def getSquare(self, n):
        res = 0
        while n:
            d = n % 10
            res += d * d
            n //= 10
        return res
    
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getSquare(n)
        while fast != 1 and slow != fast:
            slow = self.getSquare(slow)
            fast = self.getSquare(self.getSquare(fast))
        return fast == 1



if __name__ == "__main__":
    sol = Solution()

    print(sol.isHappy(19))  # True  (1² + 9² = 82 → 8²+2²=68 → ... → 1)
    print(sol.isHappy(2))   # False
    print(sol.isHappy(1))   # True
