
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def to_decimal(num):
            result = 0
            num = int(num)
            idx = 0
            while num != 0:
                result += 2 ** idx if num % 10 == 1 else 0
                num //= 10
                idx += 1
            return result

        def to_binary(num):
            if num == 0:
                return "0"

            result = []
            while num != 0:
                result.append(0 if num % 2 == 0 else 1)
                num //= 2
            result.reverse()
            return "".join(map(str, result))
        decimal_a = to_decimal(a)
        decimal_b = to_decimal(b)
        total = decimal_a + decimal_b
        return to_binary(total)

if __name__ == "__main__":
    a = "0"
    b = "0"
    sol = Solution()
    print(sol.addBinary(a, b))