

'''
Given two binary strings a and b, return their sum as a binary string.
'''


def addBinary1(a: str, b: str) -> str:
    a = int(a, 2)
    b = int(b, 2)
    return bin(a+b)[2:]


def addBinary2(a: str, b: str) -> str:
    carry = 0
    result = ''

    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())

        result += str(carry % 2)
        carry //= 2
    return result[::-1]

def addBinary(a: str, b: str) -> str:
    res = ""

    i, j, carry = len(a) - 1, len(b) - 1, 0
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += ord(a[i]) - ord('0')
        if j >= 0:
            sum += ord(b[j]) - ord('0')
        i, j = i - 1, j - 1
        carry = 1 if sum > 1 else 0
        res += str(sum % 2)
    if carry != 0:
        res += str(carry)
    return res[::-1]


a = "11"
b = "1"
print(addBinary(a, b))