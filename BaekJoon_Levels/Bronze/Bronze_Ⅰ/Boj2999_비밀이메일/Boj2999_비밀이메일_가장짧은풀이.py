import sys

input = lambda: sys.stdin.readline().rstrip()

s = input()
n = len(s)
for i in range(1, n + 1):
    j = n // i
    if i <= j and i * j == n:
        R = i
for i in range(R):
    print(s[i::R], end='')

s = input()
p, q = 1, len(s)
for i in range(2, len(s)):
    if i * i > len(s):
        break
    if len(s) % i == 0:
        p, q = i, len(s) // i;
print("".join([s[i * p + j] for j in range(p) for i in range(q)]))
