
A, B = map(int, input().split())

divisors = set(i for i in range(1, 101) if 100 % i == 0)
# any(조건 for 요소 in iterable)
print("Yes" if any(100 % i == 0 for i in range(A, B + 1)) else "No")