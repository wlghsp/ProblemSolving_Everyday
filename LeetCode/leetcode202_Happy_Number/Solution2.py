class Solution:
    def getSquare(self, n):
        result = 0
        while n != 0:
            d = n % 10
            result += d * d
            n //= 10
        return result
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getSquare(n) # fast는 한발 앞서 시작
        while fast != 1 and slow != fast:
            slow = self.getSquare(slow) # 한 번
            fast = self.getSquare(self.getSquare(fast)) # 두 번
        return fast == 1

if __name__ == "__main__":
    s = Solution()

    print(s.isHappy(19))   # True  (1² + 9² = 82 → 6² + 8² = 100 → 1)
    print(s.isHappy(2))    # False
    print(s.isHappy(1))    # True
    print(s.isHappy(7))    # True
