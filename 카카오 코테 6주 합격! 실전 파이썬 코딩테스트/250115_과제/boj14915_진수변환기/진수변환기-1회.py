
m, n = map(int, input().split())

original_m = m

result = ""
alpha = "0123456789ABCDEF"

while m != 0:
    result += str(m % n) if n <= 10 else alpha[m % n]
    m //= n

print(''.join(reversed(result)) if original_m > 0 else 0)