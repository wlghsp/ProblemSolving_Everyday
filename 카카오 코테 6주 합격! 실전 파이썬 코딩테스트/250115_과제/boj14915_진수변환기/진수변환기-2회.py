
m, n = map(int, input().split())

if m == 0:
    print(0)
else:
    alpha = "0123456789ABCDEF"

    def to_different_number(number, n):
        result = ""
        while number != 0:
            result += str(number % n if n < 10 else alpha[number % n])
            number //= n

        return "".join(reversed(result))


    print(to_different_number(m, n))