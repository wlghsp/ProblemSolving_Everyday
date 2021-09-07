import sys

input = lambda: sys.stdin.readline().rstrip()


alphabets = list(input())
result = ""
for s in alphabets:
    if s.isupper():
        result += s.lower()
    elif s.islower():
        result += s.upper()
    else:
        result += s

print(result)
