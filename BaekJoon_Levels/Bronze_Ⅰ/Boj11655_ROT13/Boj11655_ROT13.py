import sys

input = lambda: sys.stdin.readline().rstrip()
from string import ascii_lowercase, ascii_uppercase
alpha_lower = list(ascii_lowercase)
alpha_upper = list(ascii_uppercase)

sen = input()
result = ""
for c in sen:
    if c.isalpha():
        if c.isupper():
            result += alpha_upper[(alpha_upper.index(c) + 13) % 26]
        else:
            result += alpha_lower[(alpha_lower.index(c) + 13) % 26]
    else:
        result += c

print(result)