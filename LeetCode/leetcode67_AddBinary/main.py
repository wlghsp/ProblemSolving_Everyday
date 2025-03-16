
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return "0"

        def to_decimal(num):
            result = 0
            for i in range(len(num)):
                result += (int(num[len(num) - i - 1]) * (2 ** i))
            return result

        def to_binary(num):
            result = ""
            while num != 0:
                result += str(num % 2)
                num //= 2
            return "".join(reversed(result))

        num_a = to_decimal(a)
        num_b = to_decimal(b)
        answer = num_a + num_b
        return to_binary(answer)

