
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def to_decimal(num):
            result = 0
            for idx, bit in enumerate(reversed(num)):
                if bit == '1':
                    result += 2 ** idx
            return result

        def to_binary(num):
            return bin(num)[2:]
        decimal_a = to_decimal(a)
        decimal_b = to_decimal(b)
        total = decimal_a + decimal_b
        return to_binary(total)
    def addBinary1(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == "__main__":
    a = "11"
    b = "1"
    sol = Solution()
    print(sol.addBinary1(a, b))