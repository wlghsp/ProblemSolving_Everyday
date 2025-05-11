class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = 1
        for i in range(2, n + 1):
            number = number * i

        cnt = 0
        s, r = divmod(number, 10)
        while r == 0:
            cnt += 1
            s, r = divmod(s, 10)
        return cnt

if __name__ == '__main__':
    sol = Solution()
    print(sol.trailingZeroes(3)) # 0
    print(sol.trailingZeroes(5)) # 1