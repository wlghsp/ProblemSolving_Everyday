

m, n = map(int, input().split())

if m == 0:
    print(m)
else:
    result = ""
    alpha = "0123456789ABCDEF"
    while m != 0:
        number = m % n
        result += str(number) if number < 10 else alpha[number]
        m //= n

    print("".join(reversed(result)))