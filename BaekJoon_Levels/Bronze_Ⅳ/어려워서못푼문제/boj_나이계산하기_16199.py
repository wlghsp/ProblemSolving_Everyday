"""
2003 3 5
2003 4 5

0
1
0

만 나이
세는 나이
연 나이

"""
import sys

input = lambda: sys.stdin.readline().rstrip()

by, bm, bd = map(int, input().split())
cy, cm, cd = map(int, input().split())


man_age = cy - by
if cm < bm:
    man_age -= 1

if cm == bm:
    if cd < bd:
        man_age -= 1

counting_age = cy - by + 1

year_age = cy - by

print(man_age)
print(counting_age)
print(year_age)


