
import sys

input = lambda : sys.stdin.readline().rstrip()

s = set()

for _ in range(int(input())):
    name, el = input.split()
    if el == 'enter':
        s.add(name)
    else:
        if name in s:
            s.remove(name)

for name in sorted(s, reverse=True):
    print(name)