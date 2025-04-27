
class Solution:
    def isPalindrome(self, x: int) -> bool:
        def reverseInt(n: int) -> int:
            res = 0
            while n > 0: # 음수는 무조건 false 가 됨
                res = res * 10 + n % 10
                n //= 10
            return res

        return x == reverseInt(x)




if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121)) # True