import sys

input = lambda: sys.stdin.readline().rstrip()
s = input()
banned = "CAMBRIDGE"
result = ""
for i in s:
    if i not in banned:
        result += i
print(result)
