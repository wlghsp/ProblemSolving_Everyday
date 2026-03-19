class Solution:

    def getSquares(self, n):
        result = 0
        while n != 0:
            d = n % 10
            result += d * d
            n //= 10
        return result
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getSquares(n)
        while fast != 1 and slow != fast:
            slow = self.getSquares(slow)        
            fast = self.getSquares(self.getSquares(fast))
        return fast == 1        


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))   # True
    print(s.isHappy(2))    # False
    print(s.isHappy(1))    # True
