class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        div = 1
        while x >= 10 * div:
            div *= 10

        while x:
            right = x % 10
            left = x // div

            if left != right:
                return False

            x = (x % div) // 10
            div /= 100
        return True


    def isPalindrome1(self, x: int) -> bool:
        if x < 0:
            return False
        def reverseInt(n:int) -> int:
            res = 0
            while n > 0:
                remainder = n % 10 # 1의 자리 숫자 빼내기
                res = res * 10 + remainder # 새 숫자에 10 곱해 1의 자리 확보하고 빼낸 1의 자리 숫자를 더함
                n = n // 10 # 원래 숫자를 10으로 나눠 1의 자리 제거
            return res

        return x == reverseInt(x)
