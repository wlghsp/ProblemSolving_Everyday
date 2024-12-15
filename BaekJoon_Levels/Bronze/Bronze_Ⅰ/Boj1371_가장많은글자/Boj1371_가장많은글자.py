import sys

# 입력 테스트를 한 번에 다 받음
s = sys.stdin.read()
li = [0] * 26

for c in s:
    if c.islower():
        li[ord(c) - 97] += 1

for i in range(26):
    if li[i] == max(li):
        print(chr(97+i), end="")